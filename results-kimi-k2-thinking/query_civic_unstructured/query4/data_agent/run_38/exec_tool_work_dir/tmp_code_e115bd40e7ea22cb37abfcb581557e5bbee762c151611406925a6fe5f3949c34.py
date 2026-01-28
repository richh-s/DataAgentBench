code = """# Check available variables in the local scope
import glob, json, os

# List available files in the results directory
result_files = glob.glob('/var/results/*.json')
print("Available result files:")
for file in result_files:
    print(f"  {file}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
