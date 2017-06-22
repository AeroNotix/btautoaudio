# Maintainer:  <aaron.l.france@gmail.com>
pkgname=btautoaudio
pkgver=1
pkgrel=1
pkgdesc=""
arch=('any')
url=""
license=('BSD')
depends=('python2')
provides=('create_a2dp_sinks.py', 'sync_interfaces.py', )
install=
changelog=
source=(create_a2dp_sinks.py create_a2dp_sinks.service sync_interfaces.py sync_interfaces.service)
md5sums=('0c27e7e36ef6e87b5e7023837c031bf2'
         '0a514da6431f5bff0add3d51584fe559'
         'b04583dc78ed09f4212c5b326d4d88a6'
         '717e70e69b61ed9747a52d5012d7a124')

package() {
  install -D create_a2dp_sinks.py "$pkgdir/usr/bin/create_a2dp_sinks.py" || return 1
  install -D create_a2dp_sinks.service "$pkgdir/usr/lib/systemd/system/create_a2dp_sinks.service" || return 1
  install -D sync_interfaces.py "$pkgdir/usr/bin/sync_interfaces.py" || return 1
  install -D sync_interfaces.service "$pkgdir/usr/lib/systemd/system/sync_interfaces.service" || return 1
}
