from subprocess import Popen, PIPE

class RMDCommand(object):
    def __init__(self, command='ls', args=None):
        """
        Initializes the Command obejct with the command name and
        list of arguments.
        :param command: string representing the command
        :param args: list of arguments for command
        """
        self._command = command
        self._args = args

    def _assembleCommand(self):
        """
        Auxiliary function that builds the list inputted on the
        Popen object.
        :return: list of command with its arguments
        """
        cmd = list()
        cmd.append(self._command)
        if self._args is not None:
            for arg in self._args:
                cmd.append(arg)
        return cmd

    def _run(self, input=None):
        """
        Executes command and returns the output lines
        :param input: input on stdin
        :return: output, errors
        """
        p = Popen(self._assembleCommand(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
        if input is None:
            return p.communicate()
        return p.communicate(input)

    def outputReport(self, input=None):
        return self._run(input)