code = """import json
import re

# Keys
k1 = 'var_function-call-4764481022315539258'
k2 = 'var_function-call-4764481022315538299'

# Load
with open(locals()[k1], 'r') as f:
    funding_data = json.load(f)
with open(locals()[k2], 'r') as f:
    civic_docs = json.load(f)

# Join text
texts = []
for d in civic_docs:
    texts.append(d.get('text', ''))
full_text = chr(10).join(texts)

# Define Logic
def get_base_name(name):
    # simple replace loop
    clean = name
    clean = clean.replace(" (FEMA Project)", "")
    clean = clean.replace(" (CalOES Project)", "")
    clean = clean.replace(" (FEMA/CalOES Project)", "")
    clean = clean.replace(" (CalJPIA Project)", "")
    return clean.strip()

# Headers
h_design = "Capital Improvement Projects (Design)"
h_const = "Capital Improvement Projects (Construction)"
h_not = "Capital Improvement Projects (Not Started)"

# Find headers
indices = []
for m in re.finditer(re.escape(h_design), full_text, re.IGNORECASE):
    indices.append((m.start(), "design"))
for m in re.finditer(re.escape(h_const), full_text, re.IGNORECASE):
    indices.append((m.start(), "construction"))
for m in re.finditer(re.escape(h_not), full_text, re.IGNORECASE):
    indices.append((m.start(), "not started"))

indices.sort(key=lambda x: x[0])

results = []

for rec in funding_data:
    p_name = rec['Project_Name']
    base = get_base_name(p_name)
    
    # Check name relevance
    rel_name = "emergency" in p_name.lower() or "fema" in p_name.lower()
    
    # Find in text
    matches = list(re.finditer(re.escape(base), full_text, re.IGNORECASE))
    
    status = "not started"
    rel_context = False
    
    if len(matches) > 0:
        match = matches[0]
        start = match.start()
        end = match.end()
        
        # Status
        curr = "not started"
        for i, s in indices:
            if i < start:
                curr = s
            else:
                break
        
        # Block
        b_end = end + 1000
        for i, _ in indices:
            if end < i < b_end:
                b_end = i
                break
        
        block = full_text[end:b_end].lower()
        
        # Check completed
        if "completed" in block and "construction" in block:
            curr = "completed"
            
        status = curr
        
        # Check context
        if "emergency" in block or "fema" in block:
            rel_context = True
            
    if rel_name or rel_context:
        results.append({
            "Project_Name": p_name,
            "Funding_Source": rec['Funding_Source'],
            "Amount": rec['Amount'],
            "Status": status
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-2829182929966082996': ['civic_docs'], 'var_function-call-2829182929966082987': ['Funding'], 'var_function-call-8308376506612223274': 'file_storage/function-call-8308376506612223274.json', 'var_function-call-8308376506612220475': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-6271954007842849888': 'file_storage/function-call-6271954007842849888.json', 'var_function-call-6271954007842851063': [{'count(*)': '500'}], 'var_function-call-4764481022315539258': 'file_storage/function-call-4764481022315539258.json', 'var_function-call-4764481022315538299': 'file_storage/function-call-4764481022315538299.json'}

exec(code, env_args)
