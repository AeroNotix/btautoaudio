btautoaudio
===========

Small collection of scripts to automate pairing and creating the
correct source/sink pairs on a raspberry pi (hence the hardcoded sink
in create_a2dp_sinks.py).

Setup
=====

ArchLinux
---------

```shell
$ sudo pacman -S bluez bluetooth
$ git clone git@github.com/AeroNotix/btautoaudio.git
$ cd btautoaudio
$ makepkg -sf
$ sudo pacman -U btautoaudio-1-1-any.pkg.tar.xz
$ cp *.service ~/.config/systemd/user/
$ systemctl --user enable --now pulseaudio
$ systemctl --user enable --now create_a2dp_sinks
$ systemctl --user enable --now sync_interfaces
$ sudo systemctl enable --now bluetooth
$ pactl unload-module module-bluetooth-policy
$ # edit pulseaudio's configuration to add a2dp_source=false
$ # to module-bluetooth-policy
```
