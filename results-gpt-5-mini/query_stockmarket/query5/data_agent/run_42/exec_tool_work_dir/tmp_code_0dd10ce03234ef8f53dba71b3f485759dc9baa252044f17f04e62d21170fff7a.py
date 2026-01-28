code = """import json
# Load the previous query result which is stored under var_call_8xCDs1LrHdq65SHNpZ4C4JAn
data_source = var_call_8xCDs1LrHdq65SHNpZ4C4JAn
if isinstance(data_source, str):
    with open(data_source, 'r') as f:
        data = json.load(f)
else:
    data = data_source
symbols = [rec['Symbol'] for rec in data]
# Ensure uniqueness and sort
symbols = sorted(list(dict.fromkeys(symbols)))
import json
print("__RESULT__:")
print(json.dumps(symbols))"""

env_args = {'var_call_8xCDs1LrHdq65SHNpZ4C4JAn': 'file_storage/call_8xCDs1LrHdq65SHNpZ4C4JAn.json'}

exec(code, env_args)
