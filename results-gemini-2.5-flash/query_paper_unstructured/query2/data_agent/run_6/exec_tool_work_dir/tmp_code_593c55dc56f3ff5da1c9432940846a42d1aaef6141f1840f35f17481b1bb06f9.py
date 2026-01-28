code = """import json
import pandas as pd

with open(locals()['var_function-call-15841017489305148665'], 'r') as f:
    citations_data = json.load(f)

titles = [item["title"] for item in citations_data]
print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_function-call-15841017489305148665': 'file_storage/function-call-15841017489305148665.json'}

exec(code, env_args)
