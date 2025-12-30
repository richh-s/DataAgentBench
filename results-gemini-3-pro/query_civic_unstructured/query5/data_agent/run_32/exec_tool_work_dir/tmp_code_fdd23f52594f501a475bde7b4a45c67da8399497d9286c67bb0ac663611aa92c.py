code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-10835669272488718990'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-10835669272488721645'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)

# Helper to clean name
def get_base_name(name):
    if '(' in name:
        return name.split('(')[0].strip()
    return name.strip()

# Group funding by base name
base_name_groups = {}
for _, row in df_funding.iterrows():
    base = get_base_name(row['Project_Name'])
    if base not in base_name_groups:
        base_name_groups[base] = []
    base_name_groups[base].append(row)

# Combine text
full_text = ""
for doc in civic_docs:
    full_text += doc['text'] + "\n"

matched_projects = []
total_amount = 0
processed_bases = set()

for base_name, rows in base_name_groups.items():
    if base_name in processed_bases:
        continue
    
    # Search in text
    idx = full_text.find(base_name)
    if idx != -1:
        # Extract context
        context = full_text[idx:idx+2000] # 2000 chars should cover the section
        
        # Check start date
        st = None
        # Look for "Begin Construction:"
        marker = "Begin Construction:"
        if marker in context:
            # Extract text after marker
            after_marker = context.split(marker)[1]
            # Take first line
            line = after_marker.split('\n')[0].strip()
            st = line
        
        # Check disaster
        is_disaster = False
        
        # Check explicit in project names
        for row in rows:
            rn = row['Project_Name'].lower()
            if "fema" in rn or "caloes" in rn or "disaster" in rn:
                is_disaster = True
                break
        
        # Check keywords in context
        c_lower = context.lower()
        if not is_disaster:
            if "fema" in c_lower or "caloes" in c_lower or "disaster" in c_lower or "woolsey" in c_lower:
                is_disaster = True
        
        # Check year 2022
        if st and "2022" in st:
            if is_disaster:
                # Sum amounts for this group
                group_total = 0
                for row in rows:
                    group_total += row['Amount']
                    matched_projects.append({
                        "Project_Name": row['Project_Name'],
                        "Amount": row['Amount'],
                        "Start": st
                    })
                total_amount += group_total
        
        processed_bases.add(base_name)

print("__RESULT__:")
print(json.dumps({
    "matched_projects": matched_projects, 
    "total_amount": total_amount
}, indent=2))"""

env_args = {'var_function-call-10835669272488718990': 'file_storage/function-call-10835669272488718990.json', 'var_function-call-10835669272488721645': 'file_storage/function-call-10835669272488721645.json', 'var_function-call-474033538740406040': {'status': 'loaded', 'docs_count': 5, 'funding_count': 500}}

exec(code, env_args)
