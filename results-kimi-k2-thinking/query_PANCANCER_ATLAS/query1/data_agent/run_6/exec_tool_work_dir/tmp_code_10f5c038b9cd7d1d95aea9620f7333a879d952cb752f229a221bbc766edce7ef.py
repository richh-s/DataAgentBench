code = """import json
clinical_data_path = var_functions.query_db:2
with open(clinical_data_path, 'r') as f:
    clinical_data = json.load(f)"""

env_args = {'var_functions.list_db:0': ['clinical_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
