code = """import json
import pandas as pd

k1 = 'var_function-call-8904296491751843034'
k2 = 'var_function-call-8494922430906473506'

with open(locals()[k1], 'r') as f:
    d1 = json.load(f)
f_df = pd.DataFrame(d1)
f_df['Amount'] = pd.to_numeric(f_df['Amount'])
funding_names = f_df['Project_Name'].unique().tolist()

with open(locals()[k2], 'r') as f:
    d2 = json.load(f)

found_projects = set()

def get_matching_funding_project(candidate, f_names):
    cand = candidate.strip().lower()
    if len(cand) < 5: return None
    # Filter out obvious noise
    if "page" in cand or "agenda" in cand or "meeting" in cand: return None
    
    best_match = None
    # Try exact match first (case insensitive)
    for name in f_names:
        if name.lower() == cand:
            return name
    
    # Try containment
    for name in f_names:
        n_low = name.lower()
        if n_low in cand or cand in n_low:
            # check similarity
            # e.g. "Road Repair" vs "Road Repair Project"
            return name
    return None

def is_spring_2022(d):
    d = d.lower()
    if 'spring' in d and '2022' in d: return True
    if '2022' in d:
        if 'march' in d or 'april' in d or 'may' in d: return True
    return False

for doc in d2:
    txt = doc.get('text', '')
    lines = txt.splitlines()
    
    buf = ''
    curr_proj = None
    
    for line in lines:
        line = line.strip()
        if not line: continue
        
        # Check markers
        if 'Updates:' in line or 'Project Schedule:' in line or 'Project Description:' in line:
            if buf:
                # Validate buffer against funding names
                match = get_matching_funding_project(buf, funding_names)
                if match:
                    curr_proj = match
                else:
                    # If fuzzy match failed, maybe the candidate is valid but just not in funding?
                    # But for "Total Funding" we need it in funding.
                    # We can keep it if we want to count it, but if it has no funding, it adds 0.
                    # Given the prompt, let's assume valid projects are in funding.
                    curr_proj = None # Reset if not valid to avoid false positives
        
        if curr_proj and 'begin construction' in line.lower():
            parts = line.split(':')
            if len(parts) >= 2:
                d_str = parts[-1].strip()
                if is_spring_2022(d_str):
                    found_projects.add(curr_proj)
        
        # buffer
        if 'Updates:' not in line and 'Project Schedule:' not in line and 'Project Description:' not in line and '(cid:' not in line:
            buf = line

# Calculate funding
total_amt = 0
for p in found_projects:
    # Get amount from df
    # p is a name from funding_names
    row = f_df[f_df['Project_Name'] == p]
    if not row.empty:
        total_amt += row['Amount'].sum()

print('__RESULT__:')
print(json.dumps({'count': len(found_projects), 'funding': total_amt, 'projects': list(found_projects)}))"""

env_args = {'var_function-call-1649366549132259120': 'file_storage/function-call-1649366549132259120.json', 'var_function-call-17157926342599850647': 'file_storage/function-call-17157926342599850647.json', 'var_function-call-8904296491751843034': 'file_storage/function-call-8904296491751843034.json', 'var_function-call-8494922430906473506': 'file_storage/function-call-8494922430906473506.json', 'var_function-call-8656941930454797645': {'count': 12, 'funding': 203000, 'projects': ['(cid:131) Next public community meeting is scheduled for March 25th.', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'Agenda Item # 4.A.', 'shade structures at Malibu Bluffs Park.', '(cid:131) The project consultant has started the design of this project.', 'agreement will be sent to City Council in March.', 'project will begin in conjunction with the PCH Median Improvement', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'advertised for construction bids shortly after this date.', 'assessment district will be created.']}}

exec(code, env_args)
