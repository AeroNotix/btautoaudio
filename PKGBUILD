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
md5sums=('c79ee84cbefc43c447a80997a7ee9ac8'
         '7d3f0aa1390cabf7cfb8663d890858f6'
         '42b9613f9baeb44b52aa04e669f8a04e'
         'be5e732707ddc4b86a94da2bcb43a2ae')

package() {
  install -D create_a2dp_sinks.py "$pkgdir/usr/bin/create_a2dp_sinks.py" || return 1
  install -D create_a2dp_sinks.service "$pkgdir/usr/lib/systemd/system/create_a2dp_sinks.service" || return 1
  install -D sync_interfaces.py "$pkgdir/usr/bin/sync_interfaces.py" || return 1
  install -D sync_interfaces.service "$pkgdir/usr/lib/systemd/system/sync_interfaces.service" || return 1
}
