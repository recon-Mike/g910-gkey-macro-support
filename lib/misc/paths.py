import os
import sys
from lib.misc import is_installed
from lib.misc import create_config
from pathlib import Path


main_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
if is_installed.is_installed():
    config_dir = os.path.join(Path.home(), ".g910-gkeys-config")
    config_path = config_dir + "/config.json"

    if not os.path.exists(config_dir):
        print("Creating directory: "+config_dir)
        os.makedirs(config_dir)
        create_config.create()

else:
    config_dir = os.path.join(main_dir, "config")
    config_path = config_dir + "/config.json"

logs_path = config_dir+"/log.txt"