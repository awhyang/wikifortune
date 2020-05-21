#Maintainer: mstdve@protonmail.com
pkgname=wikifortune
pkgver=0.1
pkgrel=1
pkgdesc="Displays a wikipedia snippet"
arch=('any')
url="https://github.com/awhyang/wikifortune"
license=('GPL')
depends=('python')
makedepends=('coreutils' 'make')
source=(https://github.com/awhyang/wikifortune)

build() {
  cd "wikifortune-pkgver"
  make
}

package() {
  cd "wikifortune-$pkgver"
  make install DESTDIR="${pkgdir}"
}
