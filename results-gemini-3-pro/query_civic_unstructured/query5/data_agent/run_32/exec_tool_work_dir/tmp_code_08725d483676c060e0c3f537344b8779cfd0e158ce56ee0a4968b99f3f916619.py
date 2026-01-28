code = """import json
import pandas as pd

NEWLINE = chr(10)

path_docs = locals()['var_function-call-10835669272488718990']
path_fund = locals()['var_function-call-10835669272488721645']

with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

with open(path_fund, 'r') as f:
    funding_data = json.load(f)

# Convert Amounts to int
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
        # Determine Section
        # Search backwards for "Projects"
        # We look at the preceding 2000 chars
        preamble = full_text[max(0, idx-2000):idx]
        
        # Find last occurrence of "Capital Improvement Projects" or "Disaster Recovery Projects"
        cap_idx = preamble.rfind("Capital Improvement Projects")
        dis_idx = preamble.rfind("Disaster Recovery Projects")
        
        section_type = "Unknown"
        if cap_idx > dis_idx:
            section_type = "Capital"
        elif dis_idx > cap_idx:
            section_type = "Disaster"
        
        # Extract Start Date from context (forward)
        context = full_text[idx:idx+1000]
        marker = 'Begin Construction:'
        st = None
        if marker in context:
            after = context.split(marker)[1]
            st = after.split(NEWLINE)[0].strip()
        
        # Determine if Disaster-related
        is_disaster = False
        
        # 1. Check explicit Section
        if section_type == "Disaster":
            is_disaster = True
        elif section_type == "Capital":
            is_disaster = False
            # BUT: some projects under Capital might be disaster related (e.g. FEMA funded)?
            # The hint says "Projects have two types: 'capital' ... and 'disaster'".
            # If the document categorizes them, we should trust it?
            # Or trust the funding suffixes?
            # "Disaster project names often include suffixes like '(FEMA Project)'".
            # If a project is listed under Capital but has FEMA suffix, is it Disaster?
            # Probably yes.
            pass
        
        # 2. Check Suffixes in Funding Data
        has_disaster_suffix = False
        for row in rows:
            rn = row['Project_Name'].lower()
            if 'fema' in rn or 'caloes' in rn or 'disaster' in rn:
                has_disaster_suffix = True
                break
        
        if has_disaster_suffix:
            is_disaster = True
            
        # 3. Check keywords in context if Section is Unknown
        if section_type == "Unknown" and not is_disaster:
             c_lower = context.lower()
             if 'fema' in c_lower or 'caloes' in c_lower or 'disaster' in c_lower:
                 is_disaster = True

        # Check year 2022 in Start Date
        if st and '2022' in st:
            if is_disaster:
                group_total = sum(r['Amount'] for r in rows)
                total_amount += group_total
                matched_details.append({'name': base_name, 'amount': group_total, 'start': st, 'section': section_type})

print('__RESULT__:')
print(json.dumps({'total_amount': total_amount, 'projects': matched_details}))"""

env_args = {'var_function-call-10835669272488718990': 'file_storage/function-call-10835669272488718990.json', 'var_function-call-10835669272488721645': 'file_storage/function-call-10835669272488721645.json', 'var_function-call-474033538740406040': {'status': 'loaded', 'docs_count': 5, 'funding_count': 500}, 'var_function-call-6347203935522351673': {'total_amount': 1184000, 'projects': [{'name': '2021 Annual Street Maintenance', 'amount': 24000, 'start': 'Spring 2022'}, {'name': 'Annual Street Maintenance', 'amount': 23000, 'start': 'Spring 2022'}, {'name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'amount': 168000, 'start': 'Spring 2022'}, {'name': 'Civic Center Stormwater Diversion Structure', 'amount': 64000, 'start': 'Spring 2022'}, {'name': 'Encinal Canyon Road Drainage Improvements', 'amount': 146000, 'start': 'Fall 2022'}, {'name': 'Latigo Canyon Road Culvert Repairs', 'amount': 137000, 'start': 'April 2022'}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'amount': 188000, 'start': 'April 2022'}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'amount': 214000, 'start': 'Spring 2022'}, {'name': 'Trancas Canyon Park Slope Stabilization Project', 'amount': 143000, 'start': 'Spring 2022'}, {'name': 'Westward Beach Road Shoulder Repairs', 'amount': 77000, 'start': 'Fall 2022'}]}}

exec(code, env_args)
