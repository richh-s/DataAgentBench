code = """import json
import re

# Load data from storage
mongo_key = 'var_functions.query_db:10'
funding_key = 'var_functions.query_db:5'

mongo_data = locals().get(mongo_key)
funding_data = locals().get(funding_key)

# Load MongoDB data
if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    with open(mongo_data, 'r') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = mongo_data if mongo_data else []

# Load funding data  
if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_data if funding_data else []

print('MongoDB docs count:', len(mongo_docs))
print('Funding records count:', len(funding_records))

if funding_records:
    print('Sample funding record:', funding_records[0])
    high_funding = [f for f in funding_records if int(f.get('Amount', 0)) > 50000]
    print('High funding records:', len(high_funding))

if mongo_docs:
    print('Sample mongo doc keys:', list(mongo_docs[0].keys()))
    text_sample = mongo_docs[0].get('text', '')[:300]
    print('Text sample:', text_sample[:100])

print('Data loaded')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
