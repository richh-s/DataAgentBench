code = """import json
import re

# Load data
funding_path = locals()['var_function-call-1630870777495368104']
docs_path = locals()['var_function-call-1630870777495368997']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(docs_path, 'r') as f:
    docs_data = json.load(f)

# Concatenate all text
full_text = "\n".join([d['text'] for d in docs_data])

# Project names from funding
projects = []
for row in funding_data:
    projects.append({
        'name': row['Project_Name'],
        'amount': float(row['Amount']),
        'id': row['Funding_ID']
    })

total_funding = 0.0
matched_projects = []

# Define keywords
disaster_suffixes = ["(FEMA Project)", "(CalJPIA Project)", "(CalOES Project)", "(FEMA)", "(CalOES)"]
disaster_keywords = ["FEMA", "CalOES", "Woolsey Fire", "Disaster", "Emergency", "CalJPIA"]

# Helper to find project in text
def find_project_context(name, text):
    # Try exact match
    pattern = re.escape(name)
    matches = list(re.finditer(pattern, text, re.IGNORECASE))
    
    # If not found, try root name (remove suffix)
    if not matches:
        root = re.sub(r"\s*\(.*?\)$", "", name)
        if root != name and len(root) > 5:
            pattern = re.escape(root)
            matches = list(re.finditer(pattern, text, re.IGNORECASE))
    
    if not matches:
        return None
        
    combined_context = ""
    for m in matches:
        start = m.end()
        # grab next 1000 chars
        combined_context += text[start : start + 1000] + "\n"
    
    return combined_context

# Keywords indicating start
start_indicators = ["Begin Construction", "Start Construction", "Advertise", "Awarded", "Bids", "Project Schedule", "Start Date"]

for p in projects:
    name = p['name']
    amount = p['amount']
    
    # Check if name implies disaster
    name_is_disaster = any(s in name for s in disaster_suffixes)
    
    # Find context
    context = find_project_context(name, full_text)
    
    if not context:
        continue
        
    # Check context for disaster keywords
    context_is_disaster = any(k.lower() in context.lower() for k in disaster_keywords)
    
    is_disaster = name_is_disaster or context_is_disaster
    
    if not is_disaster:
        continue
        
    # Check Start Date in context
    is_started_2022 = False
    
    # Split context into lines
    lines = context.split('\n')
    for line in lines:
        # Check if line contains 2022
        if "2022" in line:
            # Check if line indicates start
            if any(ind in line for ind in start_indicators):
                is_started_2022 = True
                break
            # Also check if it's a "Updates" line that implies start events like "received bids"
            if "received" in line.lower() and "bids" in line.lower():
                is_started_2022 = True
                break
    
    if is_started_2022:
        total_funding += amount
        matched_projects.append({'name': name, 'amount': amount})

print("__RESULT__:")
print(json.dumps({'total_funding': total_funding, 'matches': matched_projects}))"""

env_args = {'var_function-call-1630870777495368104': 'file_storage/function-call-1630870777495368104.json', 'var_function-call-1630870777495368997': 'file_storage/function-call-1630870777495368997.json'}

exec(code, env_args)
