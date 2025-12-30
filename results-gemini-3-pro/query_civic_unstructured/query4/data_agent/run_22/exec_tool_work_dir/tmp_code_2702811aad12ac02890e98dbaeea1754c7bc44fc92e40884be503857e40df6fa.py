code = """import json
import pandas as pd

# Load funding data
with open(locals()['var_function-call-8904296491751843034'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Load civic docs
with open(locals()['var_function-call-8494922430906473506'], 'r') as f:
    civic_docs = json.load(f)

target_projects = set()

def is_spring_2022(date_str):
    if not date_str:
        return False
    s = date_str.lower().strip()
    # Check 2022 and Spring keywords
    if "2022" in s:
        if "spring" in s:
            return True
        if "march" in s or "april" in s or "may" in s:
            return True
    return False

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    buffer_line = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if line.lower().startswith('page ') or 'agenda item' in line.lower():
            continue
            
        # Check for update marker (cid:190)
        if '(cid:190)' in line:
            if buffer_line:
                current_project = buffer_line
        
        # Check for start date
        if current_project and "begin construction" in line.lower():
            parts = line.split(':')
            if len(parts) >= 2:
                date_part = parts[-1].strip()
                if is_spring_2022(date_part):
                    target_projects.add(current_project)
        
        # Buffer line update
        if not '(cid:190)' in line and not '(cid:131)' in line:
            buffer_line = line

# Matching
total_funding = 0
matched_projects = []

target_list = list(target_projects)

for idx, row in funding_df.iterrows():
    f_name = row['Project_Name'].strip()
    match = False
    for p in target_list:
        p_clean = p.strip()
        # Exact or close match
        if p_clean.lower() == f_name.lower():
            match = True
        elif p_clean.lower() in f_name.lower() or f_name.lower() in p_clean.lower():
             if len(p_clean) > 8 and len(f_name) > 8:
                 match = True
        if match:
            break
    
    if match:
        matched_projects.append(f_name)
        total_funding += row['Amount']

# Remove duplicates in matched_projects if any (but iterating funding rows so duplicates only if multiple funding entries for same project)
# Funding table usually has 1 entry per project source? "Funding_ID" implies specific grants.
# So if a project has multiple funding sources, we sum them all.

print("__RESULT__:")
print(json.dumps({
    "count": len(target_projects),
    "funding": total_funding,
    "projects": list(target_projects)
}))"""

env_args = {'var_function-call-1649366549132259120': 'file_storage/function-call-1649366549132259120.json', 'var_function-call-17157926342599850647': 'file_storage/function-call-17157926342599850647.json', 'var_function-call-8904296491751843034': 'file_storage/function-call-8904296491751843034.json', 'var_function-call-8494922430906473506': 'file_storage/function-call-8494922430906473506.json'}

exec(code, env_args)
