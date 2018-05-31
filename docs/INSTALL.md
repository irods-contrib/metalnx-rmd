<font color="#3892CF"> EMC METALNX
===================================

<font color="#3892CF"> Metalnx RMD Installation Guide
=========================================

<font color="#A6A6A6"> <font size=+2> Revision 1.0

6/2016 </font>

----------------------------------

<font color="#000000">
Copyright © 2015-16 EMC Corporation.

This software is provided under the Software license provided in the <a href="LICENSE"> LICENSE </a> file.

The information in this file is provided “as is.” EMC Corporation makes no representations or warranties of any kind with respect to the information in this publication, and specifically disclaims implied warranties of merchantability or fitness for a particular purpose.

--------------------------------

<font color="#0066CC"> <font size=+2> __TABLE OF CONTENTS__ </font>

<font color="#000000"> <a name="TOC"></a>

<font size=+1>

1. [Introduction](#introduction)
2. [Overview](#metalnx_RMD_overview)
3. [Metalnx RMD Installation](#metalnx_RMD_installation)
4. [Metalnx RMD Commands](#metalnx_RMD_commands)

</font>

----------------------------------

<br>
<font color="#0066CC"> <font size=+2> __INTRODUCTION__ </font> <a name="introduction"></a>

<font color="#000000">
The [Metalnx Web][metalnx_web_github_repo] interface contains a dashboard that provides real-time information about the machines on the grid. For the UI to retrieve all this information, it uses the RMD (Remote Monitoring Daemon) which should be installed on each server in the iRODS grid.

RMD is a lightweight webserver that accepts limited HTTP requests and responds with JSON data. There are a few pre-defined requests to which RMD is programmed to respond to. It runs as a Linux-service with the server name:  **rmd**.

RMD requires Python (version 2.6 or later) be installed on the ICAT and each iRODS resource server.  Please, note that iRODS should be setup on the server prior to RMD installation.

Metalnx will run without the RMD package. However, RMD is necessary to allow for complete dashboard and server detail page functions in Metalnx. With this package installed disk, memory, and CPU usage data of each server will be available.

__Assumptions__

In this installation guide, to fully install Metalnx, we will:

- Show how to install the _Metalnx Remote Monitor Daemon (RMD)_ packages on the ICAT and resource servers.  Metalnx uses these packages to monitor and report the active status of the iRODS grid.

Metalnx RMD has been tested on the following Linux distributions as indicated:

- CentOS 7 – all functional testing performed.
- CentOS 6 – verified Metalnx will install and start.
- Ubuntu 14 – verified Metalnx will install and start.

<br>
<font color="#0066CC"> <font size=+2> __Metalnx RMD Overview__ </font></font> <a name="metalnx_RMD_overview"></a>

<font color="#000000">

Metalnx RMD is a small, lightweight daemon which is installed (via .rpm or .deb package) on each iCAT and resource server in the grid.  Metalnx RMD provides, on demand, basic availability information of each server in the iRODS grid which allows Metalnx to report on the overall health of the grid.

![alt text] [2]
[2]: IMAGES/Install_figure_2.png "Figure 2 - An Example iRODS Grid with Metalnx Installed"

Metalnx Remote Monitor Daemon (RMD) is installed on the ICAT server and each iRODS resource server.  RMD runs as the user iRODS and listens for a request on a port of the customer’s choosing via a configuration file (port 8000 is the default).  When a Metalnx user views the dashboard page it issues update requests to the RMD daemon in the grid which will report memory, disk, and iRODS application status via JSON packets back to Metalnx.

The Metalnx application parses the information to build the dashboard and drill down pages.  (<strong> Note: </strong> Metalnx RMD is not required for the application to work, but without it the Dashboard page will have incomplete information and show each iRODS server without RMD to be in a <em> Warning </em> state.) </li>

[[Back to: Table of Contents](#TOC)]

----------
<br>
<font color="#0066CC"> <font size=+2> __METALNX RMD INSTALLATION__ </font> <a name="metalnx_RMD_installation"></a>

<font color="#000000">

### Installation Process Overview ###

- Verify the minimum system requirements for RMD are met.  This may include installing Python.
- Install the appropriate version of the Metalnx remote monitor daemon (RMD) on the ICAT server and each iRODS resource server.
- Configure RMD on each server if the default configuration does not meet the requirements of your environment.

### System Requirements ###

Figure 3 shows the relationship between iRODS and Metalnx components.

![alt text] [3]
[3]: IMAGES/Install_figure_3.png "Figure 3 - Relationship between iRODS/Metalnx components"

##### Python #####

Python 2.6 or later version is required to run the RMD service and must be installed on the ICAT and each iRODS Resource server that will run RMD.

For information on how to install Python, refer to:  [https://www.python.org/](https://www.python.org)

<a name="metalnx_RMD_installation"></a>
### Metalnx RMD Installation ###

RMD can be built as distribution-specific installation packages using the build instructions.

Install the RMD package on CentOS as root via the command:

 	# rpm -ivh emc-metalnx-rmd-1.0-1.noarch.rpm

Install the RMD package on a Debian distribution as root via the command:

	 # dpkg -i emc-metalnx-rmd-1.0-1.deb

##### Controlling Metalnx RMD #####

By default, the RMD runs on port 8000. This property is editable in the configuration file of the daemon, located at <span style="font-family: Courier New;">  /etc/rmd/rmd.conf: </span>

     [daemon]
     ip=0.0.0.0
     port=8000

     [irods]
     server_logs_dir=/var/lib/irods/iRODS/server/log
     log_lines_to_show=20

The lines in this file correspond as follows:

- `ip:` The IP address should not be changed. The value <span style="font-family: Courier New'"> 0.0.0.0 </span> is set for the machine to be visible by outside requests.
- `port:` the port on where RMD should listen to requests. This can be changed to meet any firewall or security needs of your environment.
-  `server_logs_dir:` the directory where iRODS server logs are kept.
-  `log_lines_to_show:` the number of lines to get from the end of the iRODS server log to show in the Metalnx UI on the server details page. This is set initially to the last 20 lines

**NOTE:** If you change the port number for RMD in the file <span style="font-family: Courier New;">  /etc/rmd/rmd.conf </span> you must ALSO change the port number that Metalnx knows to communicate with RMD at.  This must be done after Metalnx is installed.  We describe how to do this in the **[Setup Metalnx](#setup_metalnx)** section.

[[Back to: Table of Contents](#TOC)]

<br>
<a name="metalnx_RMD_commands"></a>
<font color="#0066CC"> <font size=+2> __METALNX RMD COMMANDS__ </font> <a name="metalnx_RMD_commands"></a>

Metalnx RMD responds to the following commands sent to is over the listen port.


<table>
	<tr>
		<td><h4>Request</td><td><h4>Result</td>
	<tr>
		<td><span style="font-family: Courier New;"> / </span></td>
		<td> Returns all the other commands in a single JSON-like object. For development purposes, this call should be avoided due to its long response time. </td>
	<tr>
		<td><span style="font-family: Courier New;"> /cpu </span></td>
		<td> CPU related information. </td>
	<tr>
		<td><span style="font-family: Courier New;">/cpustat</span></td>
		<td> CPU usage statistics. </td>
	<tr>
		<td><span style="font-family: Courier New;">/disk </span></td>
		<td> Disk and partition information of the system. </td>
	<tr>
		<td> <span style="font-family: Courier New;">/irodslogs </span></td>
		<td> The last pre-defined number of lines of the iRODS server log. This number is set in the RMD configuration file. (see Controlling section above) </td>
	<tr>
		<td> <span style="font-family: Courier New;">/irodsstatus </span></td>
		<td> Status of the iRODS process. </td>
	<tr>
		<td><span style="font-family: Courier New;">/memory </span></td>
		<td> Memory-related data. </td>
	<tr>
		<td> <span style="font-family: Courier New;">/mounts </span></td>
		<td> Lists all the file systems mounted on the current machine. </td>
	<tr>
		<td> <span style="font-family: Courier New;">/serverstatus </span></td>
		<td> System-wide status, taking into consideration all the others specific status listed above. </td>
	<tr>
		<td> <span style="font-family: Courier New;">/version </span></td>
		<td> Returns a JSON-like object containing the version and release numbers for the current instance of RMD. </td>
</table>

##### Confirm RMD Acccess #####

Once RMD is installed and configured, a quick test can be done to ensure that RMD is correctly working.

Open a browser window and access: `http://<IP_OF_THE_RMD_MACHINE>:<PORT>/disk`
It should list all the disk-related information of your machine in JSON format.  For example:

    http://192.168.1.157:8000/disk

##### RMD Troubleshooting #####

If a firewall is set up on the iRODS server, make sure that the port where RMD listens is opened. On IPTables it can be done by adding the following line to the `iptables.conf` file for port 8000 and reloading iptables:

 	-A INPUT -m state --state NEW -m tcp -p tcp --dport 8000 -j ACCEPT

If the RMD process get stuck, remove the PID file located at `/var/run/rmd.pid` and kill the process.

[[Back to: Table of Contents](#TOC)]

[metalnx_web_github_repo]: https://github.com/sgworth/metalnx-web







