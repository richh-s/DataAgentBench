code = """import json

civic_key = 'var_function-call-10494056103338850643'
with open(locals()[civic_key], 'r') as f:
    civic_docs = json.load(f)

target_name = "Malibu Park Drainage Improvements"
found_lines = []

for doc in civic_docs:
    lines = doc['text'].splitlines()
    for i, line in enumerate(lines):
        if target_name in line:
            # Capture context
            context = lines[i:i+15]
            found_lines.append(context)

print("__RESULT__:")
print(json.dumps(str(found_lines)))"""

env_args = {'var_function-call-17786645428432444760': ['civic_docs'], 'var_function-call-17786645428432443965': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-9932309007747960995': 'file_storage/function-call-9932309007747960995.json', 'var_function-call-10494056103338850643': 'file_storage/function-call-10494056103338850643.json', 'var_function-call-10332075929140261895': 'file_storage/function-call-10332075929140261895.json', 'var_function-call-17814162175572024946': {'completed_park_projects': ['Bluffs Park Shade Structure', 'Malibu Park Drainage Improvements'], 'total_funding': 38000.0}}

exec(code, env_args)
