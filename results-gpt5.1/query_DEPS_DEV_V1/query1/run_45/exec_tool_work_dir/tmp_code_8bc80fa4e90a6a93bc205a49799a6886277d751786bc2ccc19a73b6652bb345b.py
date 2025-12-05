code = """import json, pandas as pd
from pathlib import Path

# Load latest NPM versions
latest_path = Path(var_call_pgR8DklvvqL0NfufEWRJX6uP)
latest = pd.DataFrame(json.loads(latest_path.read_text()))

# Take a manageable subset of packages to join (DuckDB may still handle all, but we'll keep it small first)
subset = latest[['System','Name','Version']]
subset_json = subset.to_json(orient='records')

print("__RESULT__:")
print(json.dumps(subset_json))"""

env_args = {'var_call_4BEVO5hAgGcLgquVMr5Bdrhu': ['project_info', 'project_packageversion'], 'var_call_5OrxSyEs6MnaamORRvkWrCoU': 'file_storage/call_5OrxSyEs6MnaamORRvkWrCoU.json', 'var_call_pgR8DklvvqL0NfufEWRJX6uP': 'file_storage/call_pgR8DklvvqL0NfufEWRJX6uP.json'}

exec(code, env_args)
