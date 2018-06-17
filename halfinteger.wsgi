import sys
import importlib

if sys.version_info[0] < 3:
    raise Exception(
        "Python3 required! Current (wrong) version: '%s'" % sys.version_info)

importlib.reload(sys)

sys.path.insert(0, "/var/www/halfinteger/")
sys.setdefaultencoding('utf-8') 

from halfinteger import app as application
application.secret_key = 'my secret key'
