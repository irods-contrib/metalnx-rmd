"""
RMD plugin for mounts information
"""
from .base import RMDCommand
from json import dumps

class MountsRMDCommand(RMDCommand):
    def __init__(self):
        """
        Initiates the RMDCommand class object with the 'mounts -l' command
        :return: new instance of MountsRMDCommand
        """
        super(MountsRMDCommand, self).__init__('mount', ['-l'])

    def outputReport(self):
        """
        Generates JSON output for mounts information
        :return: JSON string
        """
        output, err = self._run()

        # Preprocessing lines...
        lines = output.split('\n')

        response = []

        for line in lines:
            line_parts = line.split(' ')
            
            if len(line_parts) < 4:
                continue
            
            mount = {}
            mount['type'] = line_parts[4]
            mount['local_path'] = line_parts[2]

            if line_parts[4] == 'nfs':
                mount['remote_ip'] = line_parts[0].split(':')[0]
                mount['remote_path'] = line_parts[0].split(':')[1]
            else:
                mount['resource'] = line_parts[0]

            response.append(mount)

        return dumps(response)