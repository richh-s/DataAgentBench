code = """import json, os

civic_docs = None
funding = None

# Try different variable naming patterns
for key in list(globals().keys()):
    if 'query_db' in str(key) and '0' in str(key):
        print('Found potential civic docs key:', key)
        civic_docs = globals()[key]
    
    if 'query_db' in str(key) and '5' in str(key):
        print('Found potential funding key:', key)  
        funding = globals()[key]

# Load the data
if civic_docs:
    if isinstance(civic_docs, str) and os.path.exists(civic_docs):
        with open(civic_docs, 'r') as f:
            civic_docs_data = json.load(f)
    else:
        civic_docs_data = civic_docs
    print('Loaded', len(civic_docs_data), 'civic documents')
else:
    civic_docs_data = []

if funding:
    if isinstance(funding, str) and os.path.exists(funding):
        with open(funding, 'r') as f:
            funding_data = json.load(f)
    else:
        funding_data = funding
    print('Loaded', len(funding_data), 'funding records')
else:
    funding_data = []

if civic_docs_data:
    print('Sample civic doc:', json.dumps(civic_docs_data[0])[:300])
    
if funding_data:
    print('Sample funding:', json.dumps(funding_data[0]))

print('__RESULT__:', json.dumps({'civic_count': len(civic_docs_data), 'funding_count': len(funding_data)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
