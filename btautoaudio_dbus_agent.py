#!/usr/bin/python2

from __future__ import absolute_import, unicode_literals

import sys
import dbus
import dbus.service
import dbus.mainloop.glib

try:
  from gi.repository import GObject
except ImportError:
  import gobject as GObject


BUS_NAME = 'org.bluez'
AGENT_INTERFACE = 'org.bluez.Agent1'
AGENT_PATH = "/btautoaudio/agent"


def set_trusted(path):
	props = dbus.Interface(bus.get_object("org.bluez", path),
					"org.freedesktop.DBus.Properties")
	props.Set("org.bluez.Device1", "Trusted", True)



class BTAutoAudioAgent(dbus.service.Object):
    @dbus.service.method(AGENT_INTERFACE, in_signature="os", out_signature="")
    def AuthorizeService(self, device, uuid):
        print "AuthorizeService"
        return

    @dbus.service.method(AGENT_INTERFACE, in_signature="o", out_signature="s")
    def RequestPinCode(self, device):
        print "RequestPinCode"
	set_trusted(device)
        return "0000"

    @dbus.service.method(AGENT_INTERFACE, in_signature="o", out_signature="u")
    def RequestPasskey(self, device):
        print "requestpasskey"
	set_trusted(device)
	return dbus.UInt32("0000")

    @dbus.service.method(AGENT_INTERFACE, in_signature="ou", out_signature="")
    def RequestConfirmation(self, device, passkey):
        print device, passkey
        print "RequestConfirmation"
        set_trusted(device)
        return

    @dbus.service.method(AGENT_INTERFACE, in_signature="o", out_signature="")
    def RequestAuthorization(self, device):
        print "RequestAuthorization"
	return

    @dbus.service.method(AGENT_INTERFACE, in_signature="", out_signature="")
    def Cancel(self):
        print "cancel"
        return


if __name__ == '__main__':
	dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

	bus = dbus.SystemBus()
	agent = BTAutoAudioAgent(bus, AGENT_PATH)
	mainloop = GObject.MainLoop()
	capability = "KeyboardDisplay"
	obj = bus.get_object(BUS_NAME, "/org/bluez");
	manager = dbus.Interface(obj, "org.bluez.AgentManager1")
	manager.RegisterAgent(AGENT_PATH, capability)

	print("Agent registered")

	manager.RequestDefaultAgent(AGENT_PATH)

	mainloop.run()
