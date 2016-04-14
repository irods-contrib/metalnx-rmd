from .base import RMDCommand
from json import dumps

class CpuRMDCommand(RMDCommand):
    def __init__(self):
        super(CpuRMDCommand, self).__init__('cat', ['/proc/cpuinfo'])

    def outputReport(self):
        output, err = self._run()

        # Preprocessing lines...
        lines = output.split('\n')

        cpuResponse = dict()
        for line in lines:
            line = line.replace('\t', ' ')
            lineParts = filter(len, line.split(':'))
            if len(lineParts) > 1:
                cpuResponse[lineParts[0].strip()] = lineParts[1].strip()

        return dumps(cpuResponse)