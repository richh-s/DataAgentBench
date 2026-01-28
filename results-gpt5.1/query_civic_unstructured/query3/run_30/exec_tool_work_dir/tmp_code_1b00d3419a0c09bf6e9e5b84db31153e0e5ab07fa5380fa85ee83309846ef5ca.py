code = """import json

with open(var_call_xYWvruUxNbCErO0RgNdw6NWK, 'r') as f:
    data = json.load(f)

seen = set()
unique = []
for r in data:
    key = (r['Project_Name'], r['Funding_Source'], r['Amount'], r['Status'])
    if key not in seen:
        seen.add(key)
        unique.append(r)

out = json.dumps(unique, indent=2)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_iXKQmSqNOtUStbPCKax21jbi': 'file_storage/call_iXKQmSqNOtUStbPCKax21jbi.json', 'var_call_lyic0f3E0crnxLpGiJSvd3FX': 'file_storage/call_lyic0f3E0crnxLpGiJSvd3FX.json', 'var_call_xYWvruUxNbCErO0RgNdw6NWK': 'file_storage/call_xYWvruUxNbCErO0RgNdw6NWK.json'}

exec(code, env_args)
