from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]))
from common_scaffold.agent_tools import list_dbs
import yaml

with open("db_config.yaml") as f:
    db_config = yaml.safe_load(f)

db_clients = db_config["db_clients"]

print(list_dbs("businessinfo_dataset", db_clients))