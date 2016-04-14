from base import RMDCommand
from disk import DiskRMDCommand
from memory import MemoryRMDCommand
from irodsstatus import IrodsstatusRMDCommand

from json import loads, dumps

NORMAL_STATE = (1, 'normal')
WARNING_STATE = (2, 'warning')
ERROR_STATE = (4, 'error')
STATE_LIST = [NORMAL_STATE, WARNING_STATE, ERROR_STATE]

class ServerstatusRMDCommand(RMDCommand):
    """
    RMD Command that returns the general status of the server
    """

    def __getDiskStatus(self):
        """
        Get disk status
        """
        diskCommand = DiskRMDCommand()
        report = diskCommand.outputReport()

        disk_status = NORMAL_STATE[0]

        json_report = loads(report)
        partitions = json_report.keys()

        # For each one of the partitions
        for partition in partitions:
            disk_usage = int(json_report[partition]['use_percentage'][:-1])
            if disk_usage > 95:
                disk_status |= ERROR_STATE[0]
                disk_status &= ERROR_STATE[0]
            elif disk_usage > 80:
                disk_status |= WARNING_STATE[0]
                disk_status &= WARNING_STATE[0]

        return disk_status

    def __getMemoryStatus(self):
        """
        Get memory status
        """
        memoryCommand = MemoryRMDCommand()
        report = memoryCommand.outputReport()

        memory_status = NORMAL_STATE[0]
        json_report = loads(report)

        memories = json_report.keys()

        # For each one of the memories
        for memory in memories:
            used = int(json_report[memory]['used'])
            total = int(json_report[memory]['total'])
            memory_usage = float(used) / total
            if memory_usage > 95:
                memory_status |= ERROR_STATE[0]
                memory_status &= ERROR_STATE[0]
            elif memory_usage > 80:
                memory_status |= WARNING_STATE[0]
                memory_status &= WARNING_STATE[0]

        return memory_status

    def __getIrodsServerStatus(self):
        """
        Get iRODS service status
        """
        irodsStatusCommand = IrodsstatusRMDCommand()
        report = irodsStatusCommand.outputReport()
        json_report = loads(report)

        if json_report['status'] == 'up':
            return NORMAL_STATE[0]
        else:
            return ERROR_STATE[0]

    def __getStringStatus(self, statusCode):
        """
        Auxiliary function that returns the string status based on the code passed
        :return:
        """
        for state in STATE_LIST:
            if state[0] == statusCode:
                return state[1]

    def outputReport(self, input=None):

        disk_status = self.__getDiskStatus()
        memory_status = self.__getMemoryStatus()
        irods_status = self.__getIrodsServerStatus()

        # Creating response dictionary
        response = dict()
        response['disk'] = self.__getStringStatus(disk_status)
        response['memory'] = self.__getStringStatus(memory_status)
        response['irods_server'] = self.__getStringStatus(irods_status)

        # List of returned status
        status_list = list()
        status_list.append(disk_status)
        status_list.append(memory_status)
        status_list.append(irods_status)

        # Deciding which is the general server status
        server_status = NORMAL_STATE[0]
        for status in status_list:
            if status == ERROR_STATE[0]:
                server_status |= ERROR_STATE[0]
                server_status &= ERROR_STATE[0]
            elif status == WARNING_STATE[0]:
                server_status |= WARNING_STATE[0]
                server_status &= WARNING_STATE[0]

        # Appending server status to the response dict
        response['server'] = self.__getStringStatus(server_status)

        return dumps(response)
