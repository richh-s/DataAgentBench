code = """import json
import re
from datetime import datetime

# Load the full patent data from the stored file
patent_data_path = locals()['var_functions.query_db:5']
with open(patent_data_path, 'r') as f:
    patent_data = json.load(f)

# Let's examine the structure and date format
sample_dates = []
for i, record in enumerate(patent_data[:10]):
    date_str = record['publication_date']
    sample_dates.append((i, date_str))

# Also, let's check one CPC entry format
sample_cpc = patent_data[0]['cpc']
sample_dates, sample_cpc[:200] if sample_cpc else "No CPC""""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'total_records': '277813'}]}

exec(code, env_args)
