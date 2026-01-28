code = """import json

# Let's check what variables are available
print("Checking storage variables...")

# The MongoDB results should be accessible via the variable names provided
mongodb_var = 'var_functions.query_db:2'
funding_var = 'var_functions.query_db:5'

# Try to access them
try:
    mongo_file_path = locals()[mongodb_var]
    print(f"MongoDB result stored at: {mongo_file_path}")
    
    # Read the JSON file
    with open(mongo_file_path, 'r') as f:
        civic_docs = json.load(f)
    
    print(f"Loaded {len(civic_docs)} documents from MongoDB")
    print(f"First document keys: {list(civic_docs[0].keys())}")
    print(f"First document preview: {str(civic_docs[0])[:500]}...")
    
except Exception as e:
    print(f"Error accessing MongoDB result: {e}")

try:
    funding_file_path = locals()[funding_var]
    print(f"\nFunding result stored at: {funding_file_path}")
    
    # Read the JSON file
    with open(funding_file_path, 'r') as f:
        funding_data = json.load(f)
    
    print(f"Loaded {len(funding_data)} records from Funding DB")
    print(f"First record: {funding_data[0]}")
    
except Exception as e:
    print(f"Error accessing funding result: {e}")"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
