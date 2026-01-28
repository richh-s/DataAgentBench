code = """import json, re, os, sys

# Try different approaches to load the data
print('Attempting to load data...')

# First, check what we have in locals
keys = list(locals().keys())
print('Available keys:', [k for k in keys if 'query_db' in k])

# Try to access the data
try:
    funding_path = locals()['var_functions.query_db:66']
    print('Funding path:', funding_path, type(funding_path))
    
    if isinstance(funding_path, str) and os.path.exists(funding_path):
        with open(funding_path, 'r') as f:
            funding_data = json.load(f)
        print('Loaded funding data successfully')
    else:
        print('Funding path not found')
        funding_data = []
        
    civic_path = locals()['var_functions.query_db:67']
    print('Civic path:', civic_path, type(civic_path))
    
    if isinstance(civic_path, str) and os.path.exists(civic_path):
        with open(civic_path, 'r') as f:
            civic_docs = json.load(f)
        print('Loaded civic docs successfully')
    else:
        print('Civic path not found')
        civic_docs = []
        
    print(f'Data sizes: funding={len(funding_data)}, civic={len(civic_docs)}')
    
    # Build funding map
    fund_map = {}
    for r in funding_data:
        name = r.get('Project_Name', '')
        amt = int(r.get('Amount', 0))
        if name:
            fund_map[name] = fund_map.get(name, 0) + amt
    
    print(f'Funding map has {len(fund_map)} entries')
    
    # Find disaster projects with disaster keywords in their names
    disaster_funding = {}
    for name, amt in fund_map.items():
        if any(k in name.upper() for k in ['FEMA', 'CALOES', 'CALJPIA', 'WOOLSEY', 'DISASTER', 'RECOVERY']):
            disaster_funding[name] = amt
    
    total_funding = sum(disaster_funding.values())
    print(f'Found {len(disaster_funding)} disaster projects with total funding ${total_funding:,}')
    
    result = {
        'total_funding_for_disaster_related_projects': total_funding,
        'number_of_disaster_projects': len(disaster_funding),
        'sample_projects': list(disaster_funding.keys())[:5]
    }
    
    print('__RESULT__:')
    print(json.dumps(result))
    
except Exception as e:
    print('Error:', e)
    result = {'error': str(e)}
    print('__RESULT__:')
    print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}, 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json'}

exec(code, env_args)
