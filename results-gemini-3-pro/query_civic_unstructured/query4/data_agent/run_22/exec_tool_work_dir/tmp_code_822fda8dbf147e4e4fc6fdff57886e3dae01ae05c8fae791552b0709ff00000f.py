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
    # "spring 2022", "2022-spring", "spring, 2022"
    if "2022" in s and "spring" in s:
        return True
    # March, April, May 2022
    if "2022" in s:
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
            
        # Ignore pages/agenda
        if line.lower().startswith('page ') or 'agenda item' in line.lower():
            continue
            
        # Check for update marker. The text uses (cid:190)
        # We also check for unicode chars if they exist
        if '(cid:190)' in line or '\u00be' in line:
            # The previous buffer_line is the project name
            if buffer_line:
                current_project = buffer_line
        
        # Check for start date
        if current_project and "begin construction" in line.lower():
            # Extract date
            # Format: "Begin Construction: <Date>"
            parts = line.split(':')
            if len(parts) >= 2:
                date_part = parts[-1].strip()
                if is_spring_2022(date_part):
                    target_projects.add(current_project)
        
        # Update buffer
        # Only update if line doesn't look like a bullet or marker
        if not ('(cid:190)' in line or '\u00be' in line or '(cid:131)' in line):
            buffer_line = line

# Filter funding
matched_funding_amount = 0
matched_count = 0

# Convert set to list
target_list = list(target_projects)
print("Target Projects:", target_list)

# We need to sum funding for these projects.
# Match names.
for idx, row in funding_df.iterrows():
    f_name = row['Project_Name'].strip()
    
    # Check match
    is_match = False
    for p in target_list:
        # Exact match or substring?
        # Data descriptions say "matches the project names that can be extracted".
        # Let's try flexible matching.
        p_clean = p.strip()
        if p_clean.lower() == f_name.lower():
            is_match = True
        elif p_clean.lower() in f_name.lower() or f_name.lower() in p_clean.lower():
            # If length is sufficient to avoid false positives
            if len(p_clean) > 5 and len(f_name) > 5:
                is_match = True
        
        if is_match:
            break
            
    if is_match:
        matched_funding_amount += row['Amount']
        matched_count += 1

print("__RESULT__:")
print(json.dumps({
    "num_projects": len(target_projects), 
    "total_funding": matched_funding_amount,
    "matched_projects_count": matched_count
}))"""

env_args = {'var_function-call-1649366549132259120': 'file_storage/function-call-1649366549132259120.json', 'var_function-call-17157926342599850647': 'file_storage/function-call-17157926342599850647.json', 'var_function-call-8904296491751843034': 'file_storage/function-call-8904296491751843034.json', 'var_function-call-8494922430906473506': 'file_storage/function-call-8494922430906473506.json'}

exec(code, env_args)
