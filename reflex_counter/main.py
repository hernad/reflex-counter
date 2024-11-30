import re
import sys
from reflex.reflex import cli

def start():
	sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
	sys.exit(cli())

