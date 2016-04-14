#!/bin/sh

PROJECT_NAME=emc-metalnx-rmd
PROJECT_VERSION="$1"
PROJECT_RELEASE="$2"
RPMBUILD_DIR=~/rpmbuild

if [ -d $RPMBUILD_DIR ]; then
    rm -rf $RPMBUILD_DIR
fi

rpmdev-setuptree > /dev/null
if [ $? -ne 0 ]; then
	echo "rpmdev-setuptree is not installed on your system. Creating the RPM BUILD tree structure manually."
	mkdir -p $RPMBUILD_DIR/SOURCES/
	mkdir -p $RPMBUILD_DIR/RPMS/
	mkdir -p $RPMBUILD_DIR/SPECS/
fi

cp $WORKSPACE/packaging/rpm/emc-metalnx-rmd.spec $RPMBUILD_DIR/SPECS/emc-metalnx-rmd.spec

echo "Creating temporary directory for source..."
rm -rf /tmp/$PROJECT_NAME-$PROJECT_VERSION
mkdir -p /tmp/$PROJECT_NAME-$PROJECT_VERSION/rmd
cd /tmp/$PROJECT_NAME-$PROJECT_VERSION/rmd
cp -r $WORKSPACE/ .

echo "Creating RPMBUILD directory tree structure..."
cd ~/rpmbuild/SOURCES
mkdir $PROJECT_NAME-$PROJECT_VERSION
cd $PROJECT_NAME-$PROJECT_VERSION

echo "Creating dir structure for files on OS..."
mkdir -p etc/init.d
mkdir -p etc/rmd
mkdir -p opt/rmd/src/commands

echo "Copying files to SOURCES directory..."
cp /tmp/$PROJECT_NAME-$PROJECT_VERSION/rmd/main.py opt/rmd/
cp -R /tmp/$PROJECT_NAME-$PROJECT_VERSION/rmd/src opt/rmd/
cp /tmp/$PROJECT_NAME-$PROJECT_VERSION/rmd/config/rmd.conf etc/rmd/
cp /tmp/$PROJECT_NAME-$PROJECT_VERSION/rmd/rmd.centos etc/init.d/rmd

sed -i "s/VERSION/$1/" opt/rmd/src/__init__.py
sed -i "s/DEV/$2/" opt/rmd/src/__init__.py

echo "Creating tarball of the sources..."
cd $RPMBUILD_DIR/SOURCES
tar -cvzf $PROJECT_NAME-$PROJECT_VERSION-$PROJECT_RELEASE.tar.gz $PROJECT_NAME-$PROJECT_VERSION

sed -i "s/VERSION/$1/g" $RPMBUILD_DIR/SPECS/$PROJECT_NAME.spec
sed -i "s/DEV/$2/g" $RPMBUILD_DIR/SPECS/$PROJECT_NAME.spec

echo "Building package..."
cd ~
rpmbuild -v -bb $RPMBUILD_DIR/SPECS/$PROJECT_NAME.spec

echo "Done."
