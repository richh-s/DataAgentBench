code = """import json
import pandas as pd

business_file = str(var_functions.query_db:9)
with open(business_file, 'r') as f:
    business_data = json.load(f)

print('Total business records:', len(business_data))
print('First record keys:', business_data[0].keys())"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['review', 'tip', 'user'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
