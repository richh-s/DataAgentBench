code = """import json
import pandas as pd

# Load data
funding_data = json.load(open(locals()['var_function-call-10596372274131677177']))
funding_df = pd.DataFrame(funding_data)

projects = ["Bluffs Park Shade Structure", "Point Dume Walkway Repairs"]

results = []
for p in projects:
    match = funding_df[funding_df['Project_Name'] == p]
    amount = 0
    if not match.empty:
        amount = match['Amount'].iloc[0]
    else:
        # try partial
        match = funding_df[funding_df['Project_Name'].str.contains(p, regex=False)]
        if not match.empty:
             amount = match['Amount'].iloc[0]
    
    results.append({'name': p, 'amount': amount})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-15461874300401161107': ['civic_docs'], 'var_function-call-15461874300401161542': ['Funding'], 'var_function-call-10596372274131677177': 'file_storage/function-call-10596372274131677177.json', 'var_function-call-10596372274131674166': 'file_storage/function-call-10596372274131674166.json', 'var_function-call-14690968047652835103': {'total_funding': 21000, 'projects': [{'name': 'Bluffs Park Shade Structure', 'amount': 21000}]}, 'var_function-call-8365704528830104402': [{'name': 'Bluffs Park Shade Structure', 'text': '(cid:190) Updates: Construction was completed November 2022. Notice of completion filed January 2023 Page 4 of 6 Agenda Item # 4.B. '}, {'name': 'Broad Beach Road Water Quality Repair', 'text': '(cid:190) Updates: (cid:131) Construction was completed, November 2022 (cid:131) Notice of completion filed January 2023 '}, {'name': 'Point Dume Walkway Repairs', 'text': '(cid:190) Updates: (cid:131) Construction was completed, November 2022 (cid:131) Notice of completion filed January 2023 Capital Improvement Projects (Not Started) '}, {'name': 'amenities such as trash cans, benches, tables, and restrooms.', 'text': '(cid:190) Updates: (cid:131) In May 2021, the Council approved funding for additional engineering work related to the project. Staff has worked with the consultant over the past several months to comp'}, {'name': 'amenities such as trash cans, benches, tables, and restrooms.', 'text': '(cid:190) Updates: (cid:131) In May 2021, the Council approved funding for additional engineering work related to the project. Staff has worked with the consultant over the past several months to comp'}]}

exec(code, env_args)
