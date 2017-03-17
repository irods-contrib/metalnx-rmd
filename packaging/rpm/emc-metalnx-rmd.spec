Name:       emc-metalnx-rmd
Version:	VERSION
Release:    DEV
Summary:    MetaLnx Remote Monitoring Tool

Group:      System Environment
License:    MIT
URL:        http://www.dellemc.com
Source0:    emc-metalnx-rmd-VERSION-DEV.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
This is a deamon to allow the MetaLnx UI to communicate with this machine
and get metrics.

%prep
%setup -q

%install
mkdir -p "${RPM_BUILD_ROOT}"
cp -R * "${RPM_BUILD_ROOT}"
exit 0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%dir /etc/rmd
%dir /opt/rmd
%defattr(-,root,root,-)
/etc/init.d/rmd
/etc/rmd/rmd.conf
/opt/rmd/main.py
/opt/rmd/src/__init__.py
/opt/rmd/src/daemon.py
/opt/rmd/src/handler.py
/opt/rmd/src/utils.py
/opt/rmd/src/commands/__init__.py
/opt/rmd/src/commands/all.py
/opt/rmd/src/commands/base.py
/opt/rmd/src/commands/cpu.py
/opt/rmd/src/commands/cpustat.py
/opt/rmd/src/commands/disk.py
/opt/rmd/src/commands/irodslogs.py
/opt/rmd/src/commands/irodsstatus.py
/opt/rmd/src/commands/memory.py
/opt/rmd/src/commands/mounts.py
/opt/rmd/src/commands/serverstatus.py
/opt/rmd/src/commands/version.py

%post
chmod 755 /etc/init.d/rmd
mkdir -p /var/run/rmd
touch /var/log/rmd.log
chkconfig rmd on
service rmd start
