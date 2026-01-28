code = """import json
# read the two stored call results
# var_call_sLaTz0Z8g10RWIGGpZVaB64i and var_call_EbazaK4i2Hyh0Ta8HA3bc0Eo are provided in storage
p = None
with open(var_call_sLaTz0Z8g10RWIGGpZVaB64i, 'r') as f:
    p = json.load(f)
q = None
with open(var_call_EbazaK4i2Hyh0Ta8HA3bc0Eo, 'r') as f:
    q = json.load(f)
# p is list of dicts with Symbol keys; q is list of table names
symbols_p = [d['Symbol'] for d in p]
tables = q
# compute intersection
intersect = sorted(list(set(symbols_p).intersection(set(tables))))
# print result as JSON string
import json
print("__RESULT__:")
print(json.dumps(intersect))"""

env_args = {'var_call_sLaTz0Z8g10RWIGGpZVaB64i': 'file_storage/call_sLaTz0Z8g10RWIGGpZVaB64i.json', 'var_call_EbazaK4i2Hyh0Ta8HA3bc0Eo': 'file_storage/call_EbazaK4i2Hyh0Ta8HA3bc0Eo.json'}

exec(code, env_args)
