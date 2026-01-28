code = """import json

with open(locals()['var_function-call-8771238045715909603'], 'r') as f:
    potential_projects = json.load(f)

park_projects = []
for p in potential_projects:
    if "park" in p['name'].lower():
        park_projects.append(p)

print("__RESULT__:")
print(json.dumps(park_projects))"""

env_args = {'var_function-call-14070122848874409329': ['civic_docs'], 'var_function-call-2375620709415017457': ['Funding'], 'var_function-call-15365523151233485332': 'file_storage/function-call-15365523151233485332.json', 'var_function-call-8977914089601309835': 'file_storage/function-call-8977914089601309835.json', 'var_function-call-5412922098617405934': ['Bluffs Park Shade Structure'], 'var_function-call-11008207917599906957': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}], 'var_function-call-17472290710313514127': [{'name': 'Bluffs Park Shade Structure', 'text': '(cid:190) Updates: Construction was completed November 2022. Notice of completion filed January 2023 Page 4 of 6 Agenda Item # 4.B.'}, {'name': 'Broad Beach Road Water Quality Repair', 'text': '(cid:190) Updates: (cid:131) Construction was completed, November 2022 (cid:131) Notice of completion filed January 2023'}, {'name': 'Point Dume Walkway Repairs', 'text': '(cid:190) Updates: (cid:131) Construction was completed, November 2022 (cid:131) Notice of completion filed January 2023 Capital Improvement Projects (Not Started)'}], 'var_function-call-13481005743254189109': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '79', 'Project_Name': 'Point Dume Walkway Repairs', 'Funding_Source': 'International Aid', 'Amount': '59000'}], 'var_function-call-8771238045715909603': 'file_storage/function-call-8771238045715909603.json', 'var_function-call-14462394121625594105': [{'Funding_ID': '55', 'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}]}

exec(code, env_args)
