"""
RMD plugin for version
"""
from .. import VERSION, RELEASE_NUMBER
from .base import RMDCommand
from json import dumps

class VersionRMDCommand(RMDCommand):

    def outputReport(self):
        """
        Generates JSON output for version information
        :return: JSON string
        """
        dict_response = dict()
        dict_response['version'] = VERSION
        dict_response['release'] = RELEASE_NUMBER
        return dumps(dict_response)