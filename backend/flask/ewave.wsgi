import sys
import os
sys.path.insert(0,"/var/www/ewave/backend/flask")

activate_env=os.path.expanduser("/home/jormaig/.virtualenvs/cv/bin/activate_this.py")
execfile(activate_env,dict(__file__=activate_env))

from ewave import app as application
