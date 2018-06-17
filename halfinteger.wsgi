import sys

if sys.version_info[0] < 3:
    raise Exception(
        "Python3 required! Current (wrong) version: '%s'" % sys.version_info)


sys.path.insert(0, "/var/www/halfinteger/")

from halfinteger import app as application
application.secret_key = 'my secret key'
