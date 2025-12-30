code = """import json

funding = var_call_fsnMnMGYuVlZlVb0U5IhMidD

disaster_keywords = ['(FEMA', '(CalOES', '(CalJPIA', 'Disaster']

total = 0
projects = []
for row in funding:
    name = row['Project_Name']
    if any(k in name for k in disaster_keywords):
        total += int(row['Amount'])
        projects.append(name)

result = {"total_disaster_funding_assuming_2022_start": total, "projects_included": projects}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_V6M3AKnxaPZ2NomV2QZm3Dvv': 'file_storage/call_V6M3AKnxaPZ2NomV2QZm3Dvv.json', 'var_call_fsnMnMGYuVlZlVb0U5IhMidD': 'file_storage/call_fsnMnMGYuVlZlVb0U5IhMidD.json'}

exec(code, env_args)
