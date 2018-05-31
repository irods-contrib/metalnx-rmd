"""
    Remote Monitor Daemon HTTP handler
"""
import BaseHTTPServer
from utils import getClass

__version__ = "0.1"

class RMDHttpHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):

        userRequestPath = self.path.replace('/', '')

        # Handling JSONP requests
        if '?' in userRequestPath:
            urlParts = userRequestPath.split('?')
            request_url = urlParts[0]
            callback_function = urlParts[1].split('&')[0].split('=')[1]
        else:
            request_url = userRequestPath
            callback_function = None

        # Getting module name
        module_name = 'all'
        if request_url != '':
            module_name = request_url

        # Getting class name
        if request_url != '':
            commandClassName = request_url.capitalize() + 'RMDCommand'
        else:
            commandClassName = 'AllRMDCommand'

        # Dynamic class instantiation
        module_name = 'src.commands.' + module_name + '.' + commandClassName
        clazz = getClass(module_name)

        if clazz is not None:
            self.__setupLayout()
            commandClassInstance = clazz()
            output = commandClassInstance.outputReport()

            if callback_function is not None:
                output = '%s(%s)' % (callback_function, output)

            self.wfile.write(output)
        else:
            self.__notFound()

    def __setupLayout(self):
        self.send_response(200)
        self.send_header("Content/Type", "application/json")
        self.end_headers()

    def __notFound(self):
        self.send_response(404)
        self.end_headers()