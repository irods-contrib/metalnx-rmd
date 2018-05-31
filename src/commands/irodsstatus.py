import re
from .base import RMDCommand
from json import dumps

class IrodsstatusRMDCommand(RMDCommand):

    def __init__(self):
        """
        Initiates the RMDCommand class object with the df command
        :return: new instance of DiskRMDCommand
        """
        super(IrodsstatusRMDCommand, self).__init__('ps', ['-ef'])

    def outputReport(self):
        """
        Generates JSON output for the iRods server status
        :return: JSON string
        """
        output, _ = self._run()
        r = re.search(r'irods\s+(\d+).*:\d{2}\s(.*irodsServer)', output)

        response = dict()
        if r is None:
            response['status'] = 'down'
            response['message'] = 'No servers running'
        else:
            process_id, server_bin = r.groups()[0], r.groups()[1]
            response['status'] = 'up'
            response['process_id'] = process_id
            response['server_bin'] = server_bin

        return dumps(response)
