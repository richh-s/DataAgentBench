code = """# Access the publication data from the most recent query
import json
import pandas as pd
from datetime import datetime
import re

# Get the file path from the latest query result
pub_file = locals()['var_functions.query_db:22']
print('Publication file path:', pub_file)

# Load publication data
with open(pub_file, 'r') as f:
    publication_data = json.load(f)

print('Loaded publication data, number of records:', len(publication_data))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
