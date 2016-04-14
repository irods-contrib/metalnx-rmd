import os
from .base import RMDCommand
from json import dumps

from src import SERVER_LOGS_DIR, LOG_LINES

class IrodslogsRMDCommand(RMDCommand):

    def outputReport(self):

		if os.path.isdir(SERVER_LOGS_DIR):
	
			# Getting the correct file to show
			logfiles = sorted([ f for f in os.listdir(SERVER_LOGS_DIR) if f.startswith('rodsLog')])
			log_to_show = logfiles[-1]
			log_file = open(os.path.join(SERVER_LOGS_DIR, log_to_show))

			# Getting the last lines
			lines = filter(len, self._tail(log_file, LOG_LINES))

			# Closing file
			log_file.close()

			# Building dictionary and returning to the view
			return dumps({'lines': lines})
		return dumps({'error': 'iRODS is not installed on the machine'})

    def _tail(self, f, lines=20):
        """
        Auxiliary function that returns last lines of a file
        :param f: file
        :param lines: number of lines to show
        :return: list with lines
        """
        BLOCK_SIZE = 1024
        f.seek(0, 2)
        block_end_byte = f.tell()
        lines_to_go = lines
        block_number = -1
        blocks = []
        while lines_to_go > 0 and block_end_byte > 0:
            if block_end_byte - BLOCK_SIZE > 0:
                f.seek(block_number*BLOCK_SIZE, 2)
                blocks.append(f.read(BLOCK_SIZE))
            else:
                f.seek(0, 0)
                blocks.append(f.read(block_end_byte))
            lines_found = blocks[-1].count('\n')
            lines_to_go -= lines_found
            block_end_byte -= BLOCK_SIZE
            block_number -= 1
        all_read_text = ''.join(reversed(blocks))
        return all_read_text.splitlines()[-lines:]