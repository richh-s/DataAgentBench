code = """# Check what variables are available
all_vars = [k for k in globals().keys() if 'var_functions' in k]
print('Variables containing var_functions:', all_vars)

# The actual variable names should be:
# var_functions.query_db:2  (for funding)
# var_functions.query_db:5  (for civic docs)

# Let's try to access them using the globals() dictionary directly
funding_key = None
civic_key = None

for key in globals().keys():
    if 'query_db' in str(key) and '2' in str(key):
        funding_key = key
        print('Found funding key:', funding_key)
    if 'query_db' in str(key) and '5' in str(key):
        civic_key = key
        print('Found civic key:', civic_key)

# Now access the actual data
if funding_key and civic_key:
    funding_path = globals()[funding_key]
    civic_path = globals()[civic_key]
    
    print('Funding path:', funding_path)
    print('Civic path:', civic_path)
    
    # Load the data
    import json
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
    
    with open(civic_path, 'r') as f:
        civic_docs = json.load(f)
    
    print('Loaded %d funding records' % len(funding_data))
    print('Loaded %d civic documents' % len(civic_docs))
else:
    print('Could not find keys')"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
