code = """import json
print("__RESULT__:")
print(json.dumps("No matching papers found."))"""

env_args = {'var_call_qd8ghf56ina4oLgVSTtgHAEe': 'file_storage/call_qd8ghf56ina4oLgVSTtgHAEe.json', 'var_call_y7ScKsSvVOgLH8cgVecmeKns': ['paper_docs'], 'var_call_s4Y0c3KrmsdgEEjFDJJdS7vc': 'file_storage/call_s4Y0c3KrmsdgEEjFDJJdS7vc.json', 'var_call_FAiE0kw2eBnAn2tksfA8lCja': []}

exec(code, env_args)
