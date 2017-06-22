#!/usr/bin/python2

import time
import gobject
import dbus
import dbus.mainloop.glib
import os
import shlex
import subprocess


relevant_ifaces = [ "org.bluez.Device1" ]
expected_sink = 'alsa_output.platform-soc_audio.analog-stereo'


def extract_bt_addr(path):
    return "_".join(path.split('/')[-1].split('_')[1:])


def add_bluetooth_audio_source(path, retry_timeout=1, retries=0, give_up=3):
    if retries == give_up:
        return
    cmd = 'pactl load-module module-loopback source_dont_move=yes source=bluez_source.%s.a2dp_source sink=%s'
    bt_addr = extract_bt_addr(path)
    if os.system(cmd % (bt_addr, expected_sink)) != 0:
        print "Failed to add loopback for %s. Waiting: %ds" % (bt_addr, retry_timeout)
        time.sleep(retry_timeout)
        add_bluetooth_audio_source(path, retry_timeout=retry_timeout*2, retries=retries+1)


def remove_bluetooth_audio_source(path):
    # it seems that pulseaudio automatically removes loopbacks when
    # their audio sources have been removed. Will finesse this if
    # needed.
    pass


def property_changed(interface, changed, invalidated, path=None):
    """Monitor dbus events and capture when a client connects via Bluetooth.

    Once connected, simply emit a shell command to create the loopback
    interface linking the onboard sound card.
    """
    if not interface in relevant_ifaces:
        return

    device_connected = changed.get('Connected')
    if device_connected == 1:
        add_bluetooth_audio_source(path)
    elif device_connected == 0:
        remove_bluetooth_audio_source(path)

if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    bus = dbus.SystemBus()

    bus.add_signal_receiver(
        property_changed,
        bus_name="org.bluez",
        dbus_interface="org.freedesktop.DBus.Properties",
        signal_name="PropertiesChanged",
        path_keyword="path"
    )

    mainloop = gobject.MainLoop()
    mainloop.run()
