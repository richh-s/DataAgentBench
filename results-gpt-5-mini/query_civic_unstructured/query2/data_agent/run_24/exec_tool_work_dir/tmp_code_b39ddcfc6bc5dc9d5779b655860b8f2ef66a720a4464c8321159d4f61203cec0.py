code = """import json

# To provide details, load funding data and filter park-related projects identified
with open(var_call_jifqAMOUNn9PorNbe5w6A4Vg, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Find all funding records with 'park' or 'playground' in the Project_Name
park_records = [
    {'Project_Name': r.get('Project_Name',''), 'Amount': int(r.get('Amount',0))}
    for r in funding if 'park' in r.get('Project_Name','').lower() or 'playground' in r.get('Project_Name','').lower()
]

print("__RESULT__:")
print(json.dumps(park_records))"""

env_args = {'var_call_hrawrctsouX7uyMEWqR3rdZM': ['civic_docs'], 'var_call_vr3n5PyiecSjEweMrZb1UBzg': ['Funding'], 'var_call_QNC7P8mjljZASGfnnZi9S4PP': 'file_storage/call_QNC7P8mjljZASGfnnZi9S4PP.json', 'var_call_jifqAMOUNn9PorNbe5w6A4Vg': 'file_storage/call_jifqAMOUNn9PorNbe5w6A4Vg.json', 'var_call_tLI5AGkLxPC0Dm9UGN4L4tvU': 'Total funding for park-related projects completed in 2022: $1123000'}

exec(code, env_args)
