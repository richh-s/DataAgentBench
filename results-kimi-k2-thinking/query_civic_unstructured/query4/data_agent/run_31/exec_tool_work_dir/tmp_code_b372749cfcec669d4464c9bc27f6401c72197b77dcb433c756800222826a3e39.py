code = """import json
import pandas as pd

# Access the result from the storage using the key name
result_data = locals().get('var_functions.query_db:2')

print(f"Type of result_data: {type(result_data)}")
print(f"Value of result_data: {result_data[:500] if isinstance(result_data, str) else str(result_data)[:500]}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding']}

exec(code, env_args)
