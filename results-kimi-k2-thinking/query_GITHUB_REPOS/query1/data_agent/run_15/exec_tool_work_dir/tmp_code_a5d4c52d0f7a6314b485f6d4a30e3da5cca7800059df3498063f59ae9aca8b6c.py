code = """import json
import re

# Access the language data from the first query
languages_data = var_functions.query_db:0

# Access the README data from the second query  
readme_data = var_functions.query_db:2

# First, check the data types
print(f"Type of languages_data: {type(languages_data)}")
print(f"Type of readme_data: {type(readme_data)}")

# Then, examine the actual structure
if isinstance(languages_data, list) and len(languages_data) > 0:
    print(f"First item in languages_data: {type(languages_data[0])}")
    if isinstance(languages_data[0], dict):
        print(f"Keys: {list(languages_data[0].keys())}")
        print(f"Sample: {languages_data[0]}")
else:
    print("languages_data is not a list or is empty")

if isinstance(readme_data, list) and len(readme_data) > 0:
    print(f"First item in readme_data: {type(readme_data[0])}")
    if isinstance(readme_data[0], dict):
        print(f"Keys: {list(readme_data[0].keys())}")
        print(f"Sample: {readme_data[0]}")
else:
    print("readme_data is not a list or is empty")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
