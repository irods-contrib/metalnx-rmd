from .base import RMDCommand
from json import dumps, loads
from cpu import CpuRMDCommand
from cpustat import CpustatRMDCommand
from disk import DiskRMDCommand
from irodslogs import IrodslogsRMDCommand
from irodsstatus import IrodsstatusRMDCommand
from memory import MemoryRMDCommand
from mounts import MountsRMDCommand
from serverstatus import ServerstatusRMDCommand
from version import VersionRMDCommand

class AllRMDCommand(RMDCommand):

    def outputReport(self):
        cpu_results = CpuRMDCommand().outputReport()
        cpustat_results = CpustatRMDCommand().outputReport()
        disk_results = DiskRMDCommand().outputReport()
        irodslogs_results = IrodslogsRMDCommand().outputReport()
        irodsstatus_results = IrodsstatusRMDCommand().outputReport()
        memory_results = MemoryRMDCommand().outputReport()
        mounts_results = MountsRMDCommand().outputReport()
        serverstatus_results = ServerstatusRMDCommand().outputReport()
        version_results = VersionRMDCommand().outputReport()

        response = dict()
        response['cpu'] = loads(cpu_results)
        response['cpustat'] = loads(cpustat_results)
        response['disk'] = loads(disk_results)
        response['irodslogs'] = loads(irodslogs_results)
        response['irodsstatus'] = loads(irodsstatus_results)
        response['memory'] = loads(memory_results)
        response['mounts'] = loads(mounts_results)
        response['serverstatus'] = loads(serverstatus_results)
        response['version'] = loads(version_results)

        return dumps(response)