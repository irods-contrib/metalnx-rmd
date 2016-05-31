 #!/bin/bash

TMP_DIR=/tmp/emc-tmp
PROJECT="emc-metalnx-rmd"
VERSION="$1-$2"

rm -rf $TMP_DIR
mkdir -p $TMP_DIR
cd $TMP_DIR

cp -r $WORKSPACE/* $TMP_DIR/
cp -r $WORKSPACE/packaging/deb/DEBIAN $TMP_DIR/

mkdir -p $TMP_DIR/$PROJECT-$VERSION/etc/init.d
mkdir -p $TMP_DIR/$PROJECT-$VERSION/etc/rmd
mkdir -p $TMP_DIR/$PROJECT-$VERSION/usr/local/rmd

mv $TMP_DIR/config/rmd.conf $TMP_DIR/$PROJECT-$VERSION/etc/rmd/
mv $TMP_DIR/main.py $TMP_DIR/$PROJECT-$VERSION/usr/local/rmd/
mv $TMP_DIR/src $TMP_DIR/$PROJECT-$VERSION/usr/local/rmd/
mv $TMP_DIR/rmd.debian $TMP_DIR/$PROJECT-$VERSION/etc/init.d/rmd

mv $TMP_DIR/DEBIAN $TMP_DIR/$PROJECT-$VERSION/
chmod -R 755 $TMP_DIR/$PROJECT-$VERSION/DEBIAN
chmod 755 $TMP_DIR/$PROJECT-$VERSION/DEBIAN/postinst
chmod 755 $TMP_DIR/$PROJECT-$VERSION/DEBIAN/prerm

sed -i "s/{{VERSION-NUMBER}}/$1/" $TMP_DIR/$PROJECT-$VERSION/DEBIAN/control
sed -i "s/{{BUILD-NUMBER}}/$2/" $TMP_DIR/$PROJECT-$VERSION/DEBIAN/control
sed -i "s/__VERSION__/$1/" $TMP_DIR/$PROJECT-$VERSION/usr/local/rmd/src/__init__.py
sed -i "s/__DEV__/$2/" $TMP_DIR/$PROJECT-$VERSION/usr/local/rmd/src/__init__.py

dpkg-deb --build $TMP_DIR/$PROJECT-$VERSION
 
