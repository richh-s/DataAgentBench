code = """import json, os, sys
print('BEGIN CHECK')

# Check for the stored result variables
civic_key = 'var_functions.query_db:0'
funding_key = 'var_functions.query_db:5'

print('Looking for civic docs variable...')
if civic_key in globals():
    civic_docs = globals()[civic_key]
    print('Found civic docs, type:', type(civic_docs))
    if isinstance(civic_docs, str) and os.path.exists(civic_docs):
        print('Civic docs is a file path:', civic_docs)
        with open(civic_docs, 'r') as f:
            civic_data = json.load(f)
        print('Loaded civic data, count:', len(civic_data))
    else:
        civic_data = civic_docs
        print('Civic docs is direct data, count:', len(civic_docs))
else:
    print('Civic docs variable NOT found')
    civic_data = []

print('Looking for funding variable...')
if funding_key in globals():
    funding = globals()[funding_key]
    print('Found funding, type:', type(funding))
    if isinstance(funding, str) and os.path.exists(funding):
        print('Funding is a file path:', funding)
        with open(funding, 'r') as f:
            funding_data = json.load(f)
        print('Loaded funding data, count:', len(funding_data))
    else:
        funding_data = funding
        print('Funding is direct data, count:', len(funding))
else:
    print('Funding variable NOT found')
    funding_data = []

print('CHECK COMPLETE')
print('Civic docs:', len(civic_data), 'records')
print('Funding:', len(funding_data), 'records')

if civic_data and funding_data:
    print('First civic doc keys:', list(civic_data[0].keys()))
    print('First funding record:', json.dumps(funding_data[0]))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
