code = """import json
from pathlib import Path
# Load the pairs file produced earlier
p = Path(var_call_Cl2PGDtjPTh0xSN30RGJ2iLR)
pairs = json.loads(p.read_text())
# extract unique names
names = sorted(list({p['Name'] for p in pairs}))
print("__RESULT__:")
print(json.dumps(names))"""

env_args = {'var_call_5AMYD8MyDFKO01JvVzZWn3eS': ['packageinfo'], 'var_call_BaSR9ijbE3x4QXyQoGOzRPFT': ['project_info', 'project_packageversion'], 'var_call_faxdiIQt980BBkyMR5n1KUWN': 'file_storage/call_faxdiIQt980BBkyMR5n1KUWN.json', 'var_call_Cl2PGDtjPTh0xSN30RGJ2iLR': 'file_storage/call_Cl2PGDtjPTh0xSN30RGJ2iLR.json'}

exec(code, env_args)
