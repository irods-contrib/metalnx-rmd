"""
RMD plugin for disk information
"""
from .base import RMDCommand
from json import dumps

class DiskRMDCommand(RMDCommand):
    def __init__(self):
        """
        Initiates the RMDCommand class object with the df command
        :return: new instance of DiskRMDCommand
        """
        super(DiskRMDCommand, self).__init__('df', ['-P'])

    def outputReport(self):
        """
        Generates JSON output for disk information
        :return: JSON string
        """
        output, err = self._run()

        lines = output.split('\n')
        lines = lines[1:]

        dictResponse = dict()
        for line in lines:
            lineParts = filter(len, line.split(' '))
            if len(lineParts) < 6:
                continue
            dictResponse[lineParts[0]] = dict()
            dictResponse[lineParts[0]]['blocks'] = lineParts[1]
            dictResponse[lineParts[0]]['used'] = lineParts[2]
            dictResponse[lineParts[0]]['available'] = lineParts[3]
            dictResponse[lineParts[0]]['use_percentage'] = lineParts[4]
            dictResponse[lineParts[0]]['mounted_on'] = lineParts[5]

        return dumps(dictResponse)