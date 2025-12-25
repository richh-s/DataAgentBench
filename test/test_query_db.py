import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common_scaffold.tools.ListDBTool import ListDBTool
from common_scaffold.tools.QueryDBTool import QueryDBTool
import logging_config

import yaml
import json

def get_schemas():
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
        # "yelp"
        # "agnews",
        "music_brainz_20k",
    ]:
        db_config_path = f"/home/ruiying/DataAgentBench/query_{task}/db_config.yaml"
        list_tool = ListDBTool(
            log_path="test_list_db.jsonl",
            name="test_list_db",
            db_config_path=f"/home/ruiying/DataAgentBench/query_{task}/db_config.yaml",
            check_load=True
        )
        query_tool = QueryDBTool(
            log_path="test_query_db.jsonl",
            name="test_query_db",
            db_config_path=db_config_path,
            check_load=False
        )
        with open(db_config_path, 'r') as f:
            db_configs = yaml.safe_load(f)
        db_names = list(db_configs['db_clients'].keys())
        for db_name in db_names:
            result = list_tool.exec(
                args={
                    "db_name": db_name
                }
            )
            table_list = result['result']
            for table in table_list:
                if db_configs['db_clients'][db_name]['db_type'] == "mongo":
                    query = json.dumps(
                        {
                            "collection": table,
                            "limit": 1
                        }
                    )
                else:
                    if table.lower() != table:
                        query = f'SELECT * FROM "{table}" LIMIT 1;'
                    else:
                        query = f'SELECT * FROM {table} LIMIT 1;'
                query_result = query_tool.exec(
                    args={
                        "db_name": db_name,
                        "query": query
                    }
                )
                print(f"{task}/{db_name}/{table}: {list(query_result['result'][0].keys())}")
        list_tool.clean_up()
        query_tool.clean_up()


def test_readonly():
    for task in [
        "crmarenapro",
    ]:
        db_config_path = f"/home/ruiying/DataAgentBench/query_{task}/db_config.yaml"
        list_tool = ListDBTool(
            log_path="test_list_db.jsonl",
            name="test_list_db",
            db_config_path=f"/home/ruiying/DataAgentBench/query_{task}/db_config.yaml",
            check_load=True
        )
        query_tool = QueryDBTool(
            log_path="test_query_db.jsonl",
            name="test_query_db",
            db_config_path=db_config_path,
            check_load=False
        )
        with open(db_config_path, 'r') as f:
            db_configs = yaml.safe_load(f)
        db_names = list(db_configs['db_clients'].keys())
        for db_name in db_names:
            result = list_tool.exec(
                args={
                    "db_name": db_name
                }
            )
            table_list = result['result']
            for table in table_list:
                db_type = db_configs['db_clients'][db_name]['db_type']
                if db_type == "mongo":
                    continue
                elif db_type == "postgres":
                    query = "SHOW transaction_read_only;"
                elif db_type == "duckdb":
                    query = "CREATE TABLE __should_fail(x INT);"
                elif db_type == "sqlite":
                    query = "CREATE TABLE __test_read_only__(x INTEGER);"
                else:
                    raise NotImplementedError(f"DB type {db_type} not supported for read-only check.")
                query_result = query_tool.exec(
                    args={
                        "db_name": db_name,
                        "query": query
                    }
                )
                print(f"{task}/{db_name}/{table}: {query_result['result']}")
        list_tool.clean_up()
        query_tool.clean_up()

def test():
    for task in [
        # "bookreview",
        # "crmarenapro",
        # "DEPS_DEV_V1",
        "GITHUB_REPOS",
        # "googlelocal",
        # "PANCANCER_ATLAS",
        # "PATENTS",
        # "stockindex",
        # "stockmarket",
        # "yelp"
    ]:
        db_config_path = f"/home/ruiying/DataAgentBench/query_{task}/db_config.yaml"
        list_tool = ListDBTool(
            log_path="test_list_db.jsonl",
            name="test_list_db",
            db_config_path=f"/home/ruiying/DataAgentBench/query_{task}/db_config.yaml",
            check_load=True
        )
        query_tool = QueryDBTool(
            log_path="test_query_db.jsonl",
            name="test_query_db",
            db_config_path=db_config_path,
            check_load=False
        )
        with open(db_config_path, 'r') as f:
            db_configs = yaml.safe_load(f)
        # db_names = list(db_configs['db_clients'].keys())
        db_names = ["artifacts_database"]
        for db_name in db_names:
            result = list_tool.exec(
                args={
                    "db_name": db_name
                }
            )
            table_list = result['result']
            for table in table_list:
                if db_configs['db_clients'][db_name]['db_type'] == "mongo":
                    query = json.dumps(
                        {
                            "collection": table,
                            "limit": 1
                        }
                    )
                else:
                    if table.lower() != table:
                        query = f'SELECT * FROM "{table}" LIMIT 100;'
                    else:
                        query = f'SELECT * FROM {table} LIMIT 100;'
                query_result = query_tool.exec(
                    args={
                        "db_name": db_name,
                        "query": query
                    }
                )
                print(f"{task}/{db_name}/{table}: {list(query_result['result'])}")
        list_tool.clean_up()
        query_tool.clean_up()


if __name__ == "__main__":  
    get_schemas()
    # test()
    # test_readonly()