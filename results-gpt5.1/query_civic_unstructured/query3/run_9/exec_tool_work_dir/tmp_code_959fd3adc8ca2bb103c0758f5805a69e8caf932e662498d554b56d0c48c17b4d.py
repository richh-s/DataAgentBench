code = """import json, re

# Load funding data
funding = var_call_YGvBWdLAeEkhrrQgAR23O1JK

# Identify emergency/FEMA-related projects by name keywords
emergency_keywords = ['emergency', 'FEMA']

results = []
for row in funding:
    name = row['Project_Name']
    if any(kw.lower() in name.lower() for kw in emergency_keywords):
        results.append({
            'Project_Name': name,
            'Funding_Source': row['Funding_Source'],
            'Amount': int(row['Amount']),
            'Status': None
        })

result_json = json.dumps(results)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_YGvBWdLAeEkhrrQgAR23O1JK': 'file_storage/call_YGvBWdLAeEkhrrQgAR23O1JK.json', 'var_call_begk8cUNiP3lhgZk4Ahx6xxe': 'file_storage/call_begk8cUNiP3lhgZk4Ahx6xxe.json'}

exec(code, env_args)
