#!/usr/bin/python2

import gobject
import dbus
import dbus.mainloop.glib
import os


def extract_br_add_as_mac(path):
    return ":".join(path.split('/')[-1].split('_')[1:])

def interfaces_added(path, interfaces):
    try:
        bt_mac = extract_br_add_as_mac(path)
        os.system('echo "default-agent\n pair %s\n quit" | bluetoothctl' % bt_mac)
        os.system('echo "default-agent\n connect %s\n quit" | bluetoothctl' % bt_mac)
        os.system('echo "default-agent\n trust %s\n quit" | bluetoothctl' % bt_mac)
    except Exception as e:
        print e


if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    bus = dbus.SystemBus()

    bus.add_signal_receiver(
        interfaces_added,
        bus_name="org.bluez",
        dbus_interface="org.freedesktop.DBus.ObjectManager",
        signal_name="InterfacesAdded"
    )

    mainloop = gobject.MainLoop()
    mainloop.run()
