code = """import json

# Paths
d_path = locals()['var_function-call-14510963906005286500']
f_path = locals()['var_function-call-14510963906005285081']

# Load
with open(d_path, 'r') as f:
    docs = json.load(f)
with open(f_path, 'r') as f:
    funds = json.load(f)

# Get known names
known_names = set()
for r in funds:
    if 'Project_Name' in r:
        known_names.add(r['Project_Name'].strip())

found = []

def check_text(p_name, text):
    # Check park
    # Topic keywords check: "park"
    txt_lower = text.lower()
    name_lower = p_name.lower()
    
    is_park = False
    if 'park' in name_lower:
        is_park = True
    elif 'park' in txt_lower:
        is_park = True
    
    # Check completed 2022
    is_completed = False
    if 'completed' in txt_lower and '2022' in txt_lower:
        # Check specific phrases
        if 'was completed' in txt_lower:
            is_completed = True
        elif 'completed,' in txt_lower:
            is_completed = True
        elif 'completed november 2022' in txt_lower: # Example
            is_completed = True
            
    return is_park and is_completed

for doc in docs:
    lines = doc['text'].split('\n')
    curr_proj = None
    buffer = []
    
    for line in lines:
        s = line.strip()
        if s in known_names:
            # Process prev
            if curr_proj:
                full_txt = ' '.join(buffer)
                if check_text(curr_proj, full_txt):
                    found.append(curr_proj)
            
            curr_proj = s
            buffer = []
        else:
            if curr_proj:
                buffer.append(s)
    
    # Last
    if curr_proj:
        full_txt = ' '.join(buffer)
        if check_text(curr_proj, full_txt):
            found.append(curr_proj)

unique_found = list(set(found))

total = 0
for r in funds:
    if r['Project_Name'].strip() in unique_found:
        # Amount might be string or int
        val = r['Amount']
        if isinstance(val, str):
            val = int(val)
        total += val

print('__RESULT__:')
print(json.dumps({'projects': unique_found, 'total': total}))"""

env_args = {'var_function-call-7656597533557058168': 'file_storage/function-call-7656597533557058168.json', 'var_function-call-7656597533557058431': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-14510963906005286500': 'file_storage/function-call-14510963906005286500.json', 'var_function-call-14510963906005285081': 'file_storage/function-call-14510963906005285081.json', 'var_function-call-13072667451122930611': 500}

exec(code, env_args)
