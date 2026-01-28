code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-14770944468380468337'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-14241512510866870290'], 'r') as f:
    civic_docs = json.load(f)

# Helper to check if project is park related
def is_park_related(name, text_block):
    keywords = ['park', 'playground', 'recreation', 'open space', 'trail']
    name_lower = name.lower()
    for k in keywords:
        if k in name_lower:
            return True
    return False

# Helper to check completion
def check_completion(text_block):
    text_lower = text_block.lower()
    if '2022' not in text_lower:
        return False
    
    # Check for "Construction was completed" or "Complete Construction" + 2022
    lines = text_block.split('\n')
    for line in lines:
        l = line.lower()
        if '2022' in l:
            if 'construction' in l and ('completed' in l or 'complete' in l):
                return True
            # Also "Construction was completed, November 2022"
            if 'construction was completed' in l:
                return True
    return False

# Parse documents
extracted_projects = []
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    clean_lines = [l.strip() for l in lines if l.strip()]
    
    i = 0
    while i < len(clean_lines):
        line = clean_lines[i]
        
        # Look ahead for "Updates:" or "Project Schedule:"
        if i + 1 < len(clean_lines):
            next_line = clean_lines[i+1]
            if 'Updates:' in next_line or 'Project Description:' in next_line or 'Project Schedule:' in next_line:
                # Potential project name
                # Avoid headers
                if "Capital Improvement Projects" in line:
                    i += 1
                    continue
                    
                project_name = line
                
                # Extract block
                block_lines = []
                j = i + 1
                while j < len(clean_lines):
                    sub_line = clean_lines[j]
                    # Check if this sub_line is a new project name
                    if j + 1 < len(clean_lines):
                        next_sub = clean_lines[j+1]
                        if ('Updates:' in next_sub or 'Project Description:' in next_sub) and not ('Updates:' in sub_line or 'Project Description:' in sub_line):
                            # Ensure sub_line is not a bullet
                            if not (sub_line.startswith('(') or sub_line.startswith('\u2022') or sub_line.startswith('-')):
                                break
                    block_lines.append(sub_line)
                    j += 1
                
                extracted_projects.append({
                    'name': project_name,
                    'text': "\n".join(block_lines)
                })
                i = j
                continue
        i += 1

# Filter
results = []
for p in extracted_projects:
    if is_park_related(p['name'], p['text']):
        if check_completion(p['text']):
            results.append(p)

# Match funding
total_funding = 0
matched_details = []
funding_df = pd.DataFrame(funding_data)

for p in results:
    p_name = p['name']
    match = funding_df[funding_df['Project_Name'] == p_name]
    if match.empty:
         match = funding_df[funding_df['Project_Name'].str.lower() == p_name.lower()]
    
    if not match.empty:
        amount = int(match['Amount'].sum())
        total_funding += amount
        matched_details.append({'name': p_name, 'amount': amount})
    else:
        matched_details.append({'name': p_name, 'amount': 0, 'status': 'Unmatched'})

print("__RESULT__:")
print(json.dumps({'matched': matched_details, 'total': total_funding}))"""

env_args = {'var_function-call-18374819534709684417': 'file_storage/function-call-18374819534709684417.json', 'var_function-call-14770944468380468337': 'file_storage/function-call-14770944468380468337.json', 'var_function-call-14241512510866870290': 'file_storage/function-call-14241512510866870290.json'}

exec(code, env_args)
