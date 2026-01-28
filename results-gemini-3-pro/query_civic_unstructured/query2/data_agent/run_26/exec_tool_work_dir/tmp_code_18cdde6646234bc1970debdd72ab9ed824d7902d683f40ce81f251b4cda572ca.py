code = """import json

# Fetch file paths
f_key = "var_function-call-14510963906005285081"
f_path = locals()[f_key]

with open(f_path, "r") as f:
    funds = json.load(f)

base_name = "Bluffs Park Shade Structure"
related_funds = []
total = 0

for r in funds:
    p_name = r.get("Project_Name", "")
    if base_name in p_name:
        related_funds.append(r)
        total += int(r.get("Amount", 0))

print("__RESULT__:")
print(json.dumps({"related_records": related_funds, "total": total}))"""

env_args = {'var_function-call-7656597533557058168': 'file_storage/function-call-7656597533557058168.json', 'var_function-call-7656597533557058431': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-14510963906005286500': 'file_storage/function-call-14510963906005286500.json', 'var_function-call-14510963906005285081': 'file_storage/function-call-14510963906005285081.json', 'var_function-call-13072667451122930611': 500, 'var_function-call-6857285951509526754': {'projects': ['Bluffs Park Shade Structure'], 'total_funding': 21000}}

exec(code, env_args)
