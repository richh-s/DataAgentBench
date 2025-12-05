code = """import json, pandas as pd
from pathlib import Path

# Load full clinical table
path = Path(var_call_rhHmindLQucFzXWVG2Z9RccB)
clinical = pd.read_json(path)

print('__RESULT__:')
print(json.dumps(list(clinical.columns)))"""

env_args = {'var_call_kRmO7uUWCAWJSP5qC9Hgpiqv': 'file_storage/call_kRmO7uUWCAWJSP5qC9Hgpiqv.json', 'var_call_e3bldMRdqowvnQW1Wfo3fARX': ['clinical_info'], 'var_call_rhHmindLQucFzXWVG2Z9RccB': 'file_storage/call_rhHmindLQucFzXWVG2Z9RccB.json'}

exec(code, env_args)
