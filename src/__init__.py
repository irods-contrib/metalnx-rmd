import ConfigParser

# Getting the properties
config = ConfigParser.ConfigParser()
config.read('/etc/rmd/rmd.conf')

# DAEMON SECTION
IP_ADDRESS = config.get('daemon', 'ip')
PORT = int(config.get('daemon', 'port'))

# iRODS SECTION
SERVER_LOGS_DIR = config.get('irods', 'server_logs_dir')
LOG_LINES = int(config.get('irods', 'log_lines_to_show'))

# Daemon logging settings
DAEMON_LOG_FILE = config.get('daemon', 'log_file')

VERSION = '__VERSION__'
RELEASE_NUMBER = '__DEV__'