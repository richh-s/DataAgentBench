code = """import json
from pathlib import Path

path = Path(var_call_g2KrDO4h9jsX29aDWbwp4DZN)
with open(path) as f:
    data = json.load(f)
union_sql = data["union_sql"]

out = json.dumps(union_sql)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_yxD1BwvtW2fcDdUbyQAXR2O9': 'file_storage/call_yxD1BwvtW2fcDdUbyQAXR2O9.json', 'var_call_VtowIwh6HR6V2l3VMkqd0jpu': 'file_storage/call_VtowIwh6HR6V2l3VMkqd0jpu.json', 'var_call_g2KrDO4h9jsX29aDWbwp4DZN': 'file_storage/call_g2KrDO4h9jsX29aDWbwp4DZN.json'}

exec(code, env_args)
