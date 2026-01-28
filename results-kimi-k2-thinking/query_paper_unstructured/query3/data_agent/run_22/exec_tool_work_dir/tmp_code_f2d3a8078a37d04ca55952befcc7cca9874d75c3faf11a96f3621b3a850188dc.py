code = """import json
import os

# Read MongoDB data - store variable name as a string to handle special characters
var_name = "var_functions.query_db:9"
mongo_data = locals()[var_name]

# The result may be a list directly or a file path
if isinstance(mongo_data, str) and mango_data.endswith('.json'):
    # If it's a .json file, open and read it
    with open(mongo_data, 'r') as f:
        mongo_data = json.load(f)

print("MongoDB data loaded successfully")
print(f"Number of records: {len(mongo_data)}")
print(f"First record: {json.dumps(mongo_data[:1], indent=2)}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
