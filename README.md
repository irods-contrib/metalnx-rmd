![Metalnx Logo](docs/IMAGES/mlx_logo_blue.png)

Metalnx RMD is a web application designed to work alongside the iRODS ([integrated Rule-Oriented Data System][irods]) and [Metalnx Web][metalnx-web]. It gets information about health status and resource usage from data grid servers and send them back to the administrator UI on Metalnx.

## Latest Version
2.0

Note: The revision number has been updated to match the revision release of the Metalnx application [Metalnx Web](https://github.com/irods-contrib/metalnx-web).  The functionality is the same as in Revision 1.0

## Core Features

- Data grid health status
- Status per resource
- Memory usage information per resource
- iRODS server logs
- Hardware information

## Documentation

Metalnx has documentation to help with building and using the tool. Please, check the following links for further information.

### Metalnx RMD RPM and DEB packages

Metalnx RMD must be built as **RPM** and/ or **DEB** packages depending on the flavor of Linux you are running your iRODS servers on. Information on how to build these packages in included in the [BUILD](docs/BUILD.md) document.

### Installing Metalnx RMD

The full documentation on how to install Metalnx RMD using `.rpm` and `.deb` packages is available in the [INSTALL](docs/INSTALL.md) document.

## License

Copyright © 2015-17 Dell EMC <br>
Copyright © 2018 The University of North Carolina at Chapel Hill

This software is provided under the Software license provided in the [LICENSE](LICENSE) file.

[irods]: http://www.irods.org
[metalnx-web]: https://github.com/irods-contrib/metalnx-web
