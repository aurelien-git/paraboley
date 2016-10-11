# Maintainer (Parabola) : Aurélien DESBRIÈRES <aurelien@hackers.camp>

pkgname=paraboley
pkgver=0.1
pkgrel=1
pkgdesc="Python script to display system infomation alongside the Parabola GNU / Linux-libre logo."
arch=('any')
url="http://aurelien-git.github.com/paraboley"
license=('GPL')
depends=('python')
makedepends=('git' 'python-distribute')
optdepends=(
'python-mpd-git: python libary for mpd interaction',
'python-logbook-git: for logging'
'imagemagick: for default screenshot command'
)
conflicts=()
provides=('paraboley')
source="git://github.com/aurelien-git/paraboley.git"

pkgver() {
	cd ${pkgname}
	git describe --always | sed 's|-|.|g'
}

package() {
	cd "$srcdir/$pkgname"
	python setup.py install --root=${pkgdir}
	install -D -m644 COPYING ${pkgdir}/usr/share/licenses/paraboley/COPYING
}
