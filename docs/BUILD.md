<font color="#3892CF"> EMC METALNX RMD PACKAGE GUIDE
====================================================

<font color="#3892CF"> Build From Source Instructions
=====================================================

<font color="#A6A6A6"> <font size=+2> Revision 1.0

6/2016 </font>

----------------------------------

<font color="#000000">
Copyright © 2015-16 EMC Corporation.

This software is provided under [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0).

The information in this file is provided “as is.” EMC Corporation makes no representations or warranties of any kind with respect to the information in this publication, and specifically disclaims implied warranties of merchantability or fitness for a particular purpose.

--------------------------------

<br>
<font color="#0066CC"> <font size=+2> __INTRODUCTION__ </font>

<font color="#000000"> <a name="Introduction"></a>

This tutorial explains how to package Metalnx RMD from scratch.

## Version
1.0

## Building RMD RPM and DEB packages

Before building RMD packages, make sure you have the metalnx-rmd source code downloaded in your environment and **cd** to its source tree root. You will see a folder called `packaging`. This folder contains all scripts and configuration files necessary to create both RPM and DEB packages.

Metalnx RMD provides a script for RPM package creation and another script for DEB package creation. Both scripts take two input parameters. The first parameter specifies which version of Metalnx the RPM package refers, currently it should be 1.0. The second parameter specifies the number of the current build. If you are building Metalnx for the first time, it should be 1.  You can increment this second (pass) number with each build you make for tracking purposes.

### RPM

Under `metalnx-rmd/packaging/rpm` is the file `emc-metalnx-rmd.spec` file which tells rpm-build how to build the Metalnx RMD RPM package and a file list for all the binaries that get included in the package.

To create the package use the script `create_rpm_package.sh` located at `metalnx-rmd/packaging/scripts`. This script was uses a environment variable, WORKSPACE, to track where the top level directory for the build is.  This variable must be set prior to using this script.  An example on how to create a RPM package using this script is:

    $ WORKSPACE=$(pwd) ./packaging/scripts/create_rpm_package.sh 1.0 1

When the script is finished you will have an `.rpm` packaged named `emc-metalnx-rmd-1.0-1.noarch.rpm`  ready for deployment.  This will will be located at `~/rpmbuild/noarch`.

### DEB

Under `metalnx-rmd/packaging/deb/DEBIAN` is a `control` file. This file is used to create the Metalnx RMD DEB package. The DEB creation script is `create_deb_package.sh` located at `metalnx-rmd/packaging/scripts`. This script uses a environment variable, WORKSPACE, to track where the top level directory for the build is.  This variable must be set prior to using this script.  An example on how to create a DEB package using this script is:

    $ WORKSPACE=$(pwd) ./packaging/scripts/create_rpm_package.sh 1.0 1

After the script is done, you will have a file named `emc-metalnx-rmd-1.0-1.deb`  ready for deployment.  This will will be located at `/tmp/emc-tmp/emc-metalnx-rmd-1.0-1.deb`.

### Troubleshooting

If you are facing problems in executing either the `create_rpm_package.sh` or the `create_deb_package.sh` scripts, make sure your current Linux user has execution permissions on these files.

The execution permission on these files can be set as follows:

    $ chmod u+x ./packaging/rpm/create_rpm_package.sh

or

    $ chmod u+x ./packaging/deb/create_deb_package.sh

