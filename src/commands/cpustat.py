from base import RMDCommand
from json import dumps

class CpustatRMDCommand(RMDCommand):
    def __init__(self):
        """
        Executing the 'top' command to get CPU stat.
        """
        super(CpustatRMDCommand, self).__init__('top', ['-bn1'])

    def outputReport(self, input=None):
        output, err = self._run()
        output = output.split('\n')[:4]

        response = dict()
        for line in output:
            if 'Cpu' in line:
                line_parts = line.split(':')
                cpu_name = line_parts[0]

                cpu_stat = dict()

                details_parts = line_parts[1].split(',')
                for details in details_parts:
                    detail_name = details[-2:]
                    details = details[:-2].strip()
                    cpu_stat[detail_name] = details

                response[cpu_name] = cpu_stat
        return dumps(response)