# Maintainer:  <aaron.l.france@gmail.com>
pkgname=btautoaudio
pkgver=1
pkgrel=1
pkgdesc=""
arch=('any')
url=""
license=('BSD')
depends=('python2')
provides=('create_a2dp_sinks.py', 'btautoaudio_dbus_agent.py')
install=
changelog=
source=(create_a2dp_sinks.py create_a2dp_sinks.service btautoaudio_dbus_agent.py btautoaudio_dbus_agent.service)
md5sums=('9fa6fee7e110c7b74460a7d1474bacd5'
         '0a514da6431f5bff0add3d51584fe559'
         'b74a74025f39c8368010f02578a12bab'
         '8a95defc4e174f0cc66b75ea1bd33a17')

package() {
  install -D create_a2dp_sinks.py "$pkgdir/usr/bin/create_a2dp_sinks.py" || return 1
  install -D create_a2dp_sinks.service "$pkgdir/usr/lib/systemd/user/create_a2dp_sinks.service" || return 1
  install -D btautoaudio_dbus_agent.py "$pkgdir/usr/bin/btautoaudio_dbus_agent.py" || return 1
  install -D btautoaudio_dbus_agent.service "$pkgdir/usr/lib/systemd/user/btautoaudio_dbus_agent.service" || return 1
}
