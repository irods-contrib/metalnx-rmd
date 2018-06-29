<font color="#3892CF"> METALNX RMD PACKAGE GUIDE </font>
================================================

<font color="#3892CF"> Build From Source Instructions
=====================================================

<font color="#A6A6A6"> <font size=+2> Revision 2.0

6/2018 </font>
 
----------------------------------

<font color="#000000">
Copyright © 2015-17 Dell EMC <br>
Copyright © 2015-17 The University of North Carolina at Chapel Hill

This software is provided under the Software license provided in the [LICENSE](LICENSE) file.

--------------------------------

<br>
<font color="#0066CC"> <font size=+2> __INTRODUCTION__ </font>

<font color="#000000"> <a name="Introduction"></a>

This tutorial explains how to package Metalnx RMD from scratch.

## Version
2.0

## Building RMD RPM and DEB packages

Before building RMD packages, make sure you have the metalnx-rmd source code downloaded in your environment and **cd** to its source tree root. You will see a folder called `packaging`. This folder contains all scripts and configuration files necessary to create both RPM and DEB packages.

Metalnx RMD provides a script for RPM package creation and another script for DEB package creation. Both scripts take two input parameters. The first parameter specifies which version of Metalnx the RPM package refers, currently it should be 1.0. The second parameter specifies the number of the current build. If you are building Metalnx for the first time, it should be 1.  You can increment this second (pass) number with each build you make for tracking purposes.

### RPM

Under `metalnx-rmd/packaging/rpm` is the file `emc-metalnx-rmd.spec` file which tells rpm-build how to build the Metalnx RMD RPM package and a file list for all the binaries that get included in the package.

To create the package use the script `create_rpm_package.sh` located at `metalnx-rmd/packaging/scripts`. This script was uses a environment variable, WORKSPACE, to track where the top level directory for the build is.  This variable must be set prior to using this script.  An example on how to create a RPM package using this script is:

    $ WORKSPACE=$(pwd) ./packaging/scripts/create_rpm_package.sh 2.0 0

When the script is finished you will have an `.rpm` packaged named `emc-metalnx-rmd-2.0-0.noarch.rpm`  ready for deployment.  This will will be located at `~/rpmbuild/noarch`.

### DEB

Under `metalnx-rmd/packaging/deb/DEBIAN` is a `control` file. This file is used to create the Metalnx RMD DEB package. The DEB creation script is `create_deb_package.sh` located at `metalnx-rmd/packaging/scripts`. This script uses a environment variable, WORKSPACE, to track where the top level directory for the build is.  This variable must be set prior to using this script.  An example on how to create a DEB package using this script is:

    $ WORKSPACE=$(pwd) ./packaging/scripts/create_deb_package.sh 2.0 0

After the script is done, you will have a file named `emc-metalnx-rmd-2.0-0.deb`  ready for deployment.  This will will be located at `/tmp/emc-tmp/emc-metalnx-rmd-2.0-0.deb`.

### Troubleshooting

If you are facing problems in executing either the `create_rpm_package.sh` or the `create_deb_package.sh` scripts, make sure your current Linux user has execution permissions on these files.

The execution permission on these files can be set as follows:

    $ chmod u+x ./packaging/rpm/create_rpm_package.sh

or

    $ chmod u+x ./packaging/deb/create_deb_package.sh

