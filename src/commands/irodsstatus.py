import os
from .base import RMDCommand
from json import dumps

class IrodsstatusRMDCommand(RMDCommand):

    def __init__(self):
        """
        Initiates the RMDCommand class object with the df command
        :return: new instance of DiskRMDCommand
        """
        super(IrodsstatusRMDCommand, self).__init__('service', ['irods', 'status'])

    def outputReport(self):
        """
        Generates JSON output for the iRods server status
        :return: JSON string
        """
        output, err = self._run()
        lines = output.split('\n')
        server_line = lines[1]

        response = dict()
        if 'No servers running' in server_line:
            response['status'] = 'down'
            response['message'] = 'No servers running'
        else:
            process_id = server_line.strip().split(' ')[1]
            response['status'] = 'up'
            response['process_id'] = process_id

        return dumps(response)