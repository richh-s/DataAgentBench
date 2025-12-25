import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common_scaffold.tools.ListDBTool import ListDBTool
import logging_config

import yaml

def list_all():
    for task in [
        # "bookreview",
        # "crmarenapro",
        # "DEPS_DEV_V1",
        # "GITHUB_REPOS",
        # "googlelocal",
        # "PANCANCER_ATLAS",
        # "PATENTS",
        # "stockindex",
        # "stockmarket",
        # "yelp",
        # "agnews",
        "music_brainz_20k",
    ]:
        db_config_path = f"/home/ruiying/DataAgentBench/query_{task}/db_config.yaml"
        tool = ListDBTool(
            log_path="test_list_db.jsonl",
            name="test_list_db",
            db_config_path=f"/home/ruiying/DataAgentBench/query_{task}/db_config.yaml",
            check_load=True
        )
        with open(db_config_path, 'r') as f:
            db_configs = yaml.safe_load(f)
        db_names = list(db_configs['db_clients'].keys())
        for db_name in db_names:
            result = tool.exec(
                args={
                    "db_name": db_name
                }
            )
            print(f"{task}/{db_name}:{result['result']}")
        tool.clean_up()

if __name__ == "__main__":  
    list_all()