import sys
import dbus
import dbus.service
import dbus.mainloop.glib

try:
  from gi.repository import GObject
except ImportError:
  import gobject as GObject


BUS_NAME = 'org.PulseAudio1'
AGENT_INTERFACE = 'org.pulseaudio.Core1'
AGENT_PATH = '/btautoaudio/pulseagent'


class PulseAudioSyncAgent(dbus.service.Object):

    @dbus.service.method(AGENT_INTERFACE, in_signature='o')
    def NewSource(self, source):
        print source



dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

bus = dbus.SessionBus()
agent = PulseAudioSyncAgent(bus, AGENT_PATH)
mainloop = GObject.MainLoop()
capability = "KeyboardDisplay"
obj = bus.get_object(BUS_NAME, "/org/pulseaudio/core1");
manager = dbus.Interface(obj, "org.pulseaudio.Core1")
manager.RegisterAgent(AGENT_PATH, capability)

print("Agent registered")

manager.RequestDefaultAgent(AGENT_PATH)

mainloop.run()
