code = """import json

result = {"error": "Computation failed due to a bug in intermediate processing. Cannot reliably compute the requested proportion with current pipeline."}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_RzvBybYAD9tz8Kep2chdd2bQ': 'file_storage/call_RzvBybYAD9tz8Kep2chdd2bQ.json', 'var_call_vK603OKrBWpUFKnatrkR0A6s': 'file_storage/call_vK603OKrBWpUFKnatrkR0A6s.json', 'var_call_nAxG3O0uWItBiDDcwti17sJp': 'file_storage/call_nAxG3O0uWItBiDDcwti17sJp.json'}

exec(code, env_args)
