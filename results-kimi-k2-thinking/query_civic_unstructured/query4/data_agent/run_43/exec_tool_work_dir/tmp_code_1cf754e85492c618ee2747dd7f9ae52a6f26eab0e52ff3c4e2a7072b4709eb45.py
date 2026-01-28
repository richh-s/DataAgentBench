code = """import json

# Debug: Print what variables we have available
print("Available variables:")
for key in list(locals().keys()):
    if key.startswith('var_functions'):
        print(f"  {key}")

# Access the file paths
civic_docs_file = locals()['var_functions.query_db:4']
funding_file = locals()['var_functions.query_db:5']

print(f"\nCivic docs file: {civic_docs_file}")
print(f"Funding file: {funding_file}")

# Read civic docs file
with open(civic_docs_file, 'r') as f:
    civic_content = f.read()
    
print(f"\nCivic docs content length: {len(civic_content)}")
print(f"First 200 chars: {civic_content[:200]}")

# Read funding file  
with open(funding_file, 'r') as f:
    funding_content = f.read()

print(f"\nFunding content length: {len(funding_content)}")
print(f"First 200 chars: {funding_content[:200]}")

# Try to parse both files
try:
    civic_docs = json.loads(civic_content)
    print(f"\nSuccessfully parsed civic_docs as JSON array, count: {len(civic_docs)}")
except Exception as e:
    print(f"\nFailed to parse civic_docs as array: {e}")
    civic_docs = []

try:
    funding = json.loads(funding_content)
    print(f"Successfully parsed funding as JSON array, count: {len(funding)}")
except Exception as e:
    print(f"Failed to parse funding as array: {e}")
    funding = []

print("__RESULT__:")
print(json.dumps({
    "civic_docs_parsed": len(civic_docs),
    "funding_parsed": len(funding)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
