"""
RMD plugin for memory information
"""
from .base import RMDCommand
from json import dumps

class MemoryRMDCommand(RMDCommand):
    def __init__(self):
        """
        Initiates the RMDCommand class object with the 'free -mt' command
        :return: new instance of DiskRMDCommand
        """
        super(MemoryRMDCommand, self).__init__('free', ['-mt'])

    def outputReport(self):
        """
        Generates JSON output for memory information
        :return: JSON string
        """
        output, err = self._run()

        # Preprocessing lines...
        lines = output.split('\n')

        # Getting the 'Memory' line
        memLine = lines[1]
        memValues = memLine.split(':')[1].split(' ')
        memValues = filter(len, memValues)

        # Creating dictionary for the Memory line
        mem = dict()
        mem['total'] = int(memValues[0])
        mem['used'] = int(memValues[1])
        mem['free'] = int(memValues[2])
        mem['shared'] = int(memValues[3])
        mem['buffers'] = int(memValues[4])
        mem['cached'] = int(memValues[5])

        # Processing swap line
        swapLine = None
        for line in lines:
            if 'Swap' in line:
                swapLine = line

        swapValues = swapLine.split(':')[1].split(' ')
        swapValues = filter(len, swapValues)
        swapResult = dict()
        swapResult['total'] = int(swapValues[0])
        swapResult['used'] = int(swapValues[1])
        swapResult['free'] = int(swapValues[2])

        # Building final dictionary
        memResult = dict()
        memResult["mem"] = mem
        memResult["swap"] = swapResult

        return dumps(memResult)