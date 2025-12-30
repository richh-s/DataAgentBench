code = """import json
import re

# Load data
with open(locals()['var_function-call-4764481022315539258'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-4764481022315538299'], 'r') as f:
    civic_docs = json.load(f)

full_text = "\n".join([d.get('text', '') for d in civic_docs])

def get_base_name(name):
    # Remove suffixes like (FEMA Project), (CalOES Project), etc.
    return re.sub(r'\s*\([^)]*Project\)', '', name).strip()

headers = {
    "Capital Improvement Projects (Design)": "design",
    "Capital Improvement Projects (Construction)": "construction", 
    "Capital Improvement Projects (Not Started)": "not started"
}

header_indices = []
for h, s in headers.items():
    for m in re.finditer(re.escape(h), full_text, re.IGNORECASE):
        header_indices.append((m.start(), s))
header_indices.sort(key=lambda x: x[0])

results = []

for record in funding_data:
    p_name = record['Project_Name']
    base_name = get_base_name(p_name)
    
    # Check name relevance
    is_relevant_name = "emergency" in p_name.lower() or "fema" in p_name.lower()
    
    # Search in text
    matches = list(re.finditer(re.escape(base_name), full_text, re.IGNORECASE))
    
    status = "not started" # Default
    found = False
    context_relevant = False
    
    if matches:
        found = True
        # Use first match
        match = matches[0]
        
        # Determine status from header
        current_s = "not started"
        for h_idx, h_s in header_indices:
            if h_idx < match.start():
                current_s = h_s
            else:
                break
        
        # Check for completed in text block
        # Look ahead 1000 chars
        start = match.end()
        end = start + 1000
        # Don't cross next header
        for h_idx, _ in header_indices:
            if start < h_idx < end:
                end = h_idx
                break
        
        block = full_text[start:end].lower()
        
        if "completed" in block:
             if "construction was completed" in block or "project was completed" in block or "notice of completion" in block:
                 current_s = "completed"
        
        # Check relevance in block
        if "emergency" in block or "fema" in block:
            context_relevant = True
            
        status = current_s
    
    if is_relevant_name or context_relevant:
        results.append({
            "Project_Name": p_name,
            "Funding_Source": record['Funding_Source'],
            "Amount": record['Amount'],
            "Status": status
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-2829182929966082996': ['civic_docs'], 'var_function-call-2829182929966082987': ['Funding'], 'var_function-call-8308376506612223274': 'file_storage/function-call-8308376506612223274.json', 'var_function-call-8308376506612220475': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-6271954007842849888': 'file_storage/function-call-6271954007842849888.json', 'var_function-call-6271954007842851063': [{'count(*)': '500'}], 'var_function-call-4764481022315539258': 'file_storage/function-call-4764481022315539258.json', 'var_function-call-4764481022315538299': 'file_storage/function-call-4764481022315538299.json'}

exec(code, env_args)
