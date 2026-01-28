code = """import json, os, sys

# Check what's in the local scope
print('Current directory files:')
for f in os.listdir('.'):
    print(f)

# Try to directly access the storage variables
print('\nAttempting to access funding data...')

try:
    # Funding data from var_functions.query_db:44
    funding_file = 'functions.query_db:44'
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
    print('Success! Loaded ' + str(len(funding_data)) + ' funding records')
    print('First record:', funding_data[0])
except Exception as e:
    print('Error loading funding:', e)

print('\nAttempting to access civic data...')
try:
    # Try different possible civic data file names
    possible_files = ['functions.query_db:24', 'functions.query_db:15', 'functions.query_db:18']
    civic_data = None
    for fname in possible_files:
        if os.path.exists(fname):
            with open(fname, 'r') as f:
                civic_data = json.load(f)
            print('Success! Loaded ' + str(len(civic_data)) + ' civic documents from ' + fname)
            break
    if civic_data:
        print('First civic doc keys:', list(civic_data[0].keys()))
except Exception as e:
    print('Error loading civic data:', e)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
