code = """import json
import pandas as pd

NEWLINE = chr(10)

path_docs = locals()['var_function-call-10835669272488718990']
path_fund = locals()['var_function-call-10835669272488721645']

with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

with open(path_fund, 'r') as f:
    funding_data = json.load(f)

for r in funding_data:
    r['Amount'] = int(r['Amount'])

df_funding = pd.DataFrame(funding_data)

def get_base_name(name):
    if '(' in name:
        return name.split('(')[0].strip()
    return name.strip()

base_name_groups = {}
for _, row in df_funding.iterrows():
    base = get_base_name(row['Project_Name'])
    if base not in base_name_groups:
        base_name_groups[base] = []
    base_name_groups[base].append(row)

full_text = ""
for doc in civic_docs:
    full_text += doc['text'] + NEWLINE

total_amount = 0
matched_details = []

for base_name, rows in base_name_groups.items():
    idx = full_text.find(base_name)
    if idx != -1:
        # Context window 3000
        context = full_text[idx:idx+3000]
        
        marker = 'Begin Construction:'
        st = None
        if marker in context:
            after = context.split(marker)[1]
            st = after.split(NEWLINE)[0].strip()
        
        is_disaster = False
        has_suffix = False
        for row in rows:
            rn = row['Project_Name'].lower()
            if 'fema' in rn or 'caloes' in rn or 'disaster' in rn:
                has_suffix = True
                break
        
        # Check context keywords
        c_lower = context.lower()
        context_has_keyword = False
        if 'fema' in c_lower or 'caloes' in c_lower or 'disaster' in c_lower:
            context_has_keyword = True

        if has_suffix or context_has_keyword:
            is_disaster = True
            
        # Refine by Section if possible to avoid false positives?
        # But if suffix is present, we trust it.
        # If no suffix, rely on context keywords.
        
        if st and '2022' in st:
            if is_disaster:
                group_total = sum(r['Amount'] for r in rows)
                total_amount += group_total
                matched_details.append({'name': base_name, 'amount': group_total, 'start': st})

print('__RESULT__:')
print(json.dumps({'total_amount': total_amount, 'projects': matched_details}))"""

env_args = {'var_function-call-10835669272488718990': 'file_storage/function-call-10835669272488718990.json', 'var_function-call-10835669272488721645': 'file_storage/function-call-10835669272488721645.json', 'var_function-call-474033538740406040': {'status': 'loaded', 'docs_count': 5, 'funding_count': 500}, 'var_function-call-6347203935522351673': {'total_amount': 1184000, 'projects': [{'name': '2021 Annual Street Maintenance', 'amount': 24000, 'start': 'Spring 2022'}, {'name': 'Annual Street Maintenance', 'amount': 23000, 'start': 'Spring 2022'}, {'name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'amount': 168000, 'start': 'Spring 2022'}, {'name': 'Civic Center Stormwater Diversion Structure', 'amount': 64000, 'start': 'Spring 2022'}, {'name': 'Encinal Canyon Road Drainage Improvements', 'amount': 146000, 'start': 'Fall 2022'}, {'name': 'Latigo Canyon Road Culvert Repairs', 'amount': 137000, 'start': 'April 2022'}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'amount': 188000, 'start': 'April 2022'}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'amount': 214000, 'start': 'Spring 2022'}, {'name': 'Trancas Canyon Park Slope Stabilization Project', 'amount': 143000, 'start': 'Spring 2022'}, {'name': 'Westward Beach Road Shoulder Repairs', 'amount': 77000, 'start': 'Fall 2022'}]}, 'var_function-call-2203215841011505581': {'total_amount': 905000, 'projects': [{'name': 'Encinal Canyon Road Drainage Improvements', 'amount': 146000, 'start': 'Fall 2022', 'section': 'Unknown'}, {'name': 'Latigo Canyon Road Culvert Repairs', 'amount': 137000, 'start': 'April 2022', 'section': 'Unknown'}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'amount': 188000, 'start': 'April 2022', 'section': 'Capital'}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'amount': 214000, 'start': 'Spring 2022', 'section': 'Unknown'}, {'name': 'Trancas Canyon Park Slope Stabilization Project', 'amount': 143000, 'start': 'Spring 2022', 'section': 'Unknown'}, {'name': 'Westward Beach Road Shoulder Repairs', 'amount': 77000, 'start': 'Fall 2022', 'section': 'Unknown'}]}}

exec(code, env_args)
