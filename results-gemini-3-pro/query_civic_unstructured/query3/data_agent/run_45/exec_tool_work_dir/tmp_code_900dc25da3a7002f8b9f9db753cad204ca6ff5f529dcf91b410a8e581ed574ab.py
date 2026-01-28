code = """import json
import re

# Load Funding Data
with open('var_function-call-7626981016965622443.json', 'r') as f:
    funding_data = json.load(f)

# Load Civic Docs
with open('var_function-call-7626981016965621198.json', 'r') as f:
    civic_docs = json.load(f)

full_text = ""
for d in civic_docs:
    full_text += d['text'] + "\n"

# Headers
headers_map = {
    "Capital Improvement Projects (Design)": {"status": "design"},
    "Capital Improvement Projects (Construction)": {"status": "construction"},
    "Capital Improvement Projects (Not Started)": {"status": "not started"},
    "Disaster Recovery Projects (Design)": {"status": "design"},
    "Disaster Recovery Projects (Construction)": {"status": "construction"},
    "Disaster Recovery Projects (Not Started)": {"status": "not started"}
}

# Find headers
header_positions = []
for header, info in headers_map.items():
    # Escape header just in case, though plain string find is safer if no regex chars
    # using re to be case insensitive
    for match in re.finditer(re.escape(header), full_text, re.IGNORECASE):
        header_positions.append({"pos": match.start(), "info": info})

header_positions.sort(key=lambda x: x['pos'])

# Project Names
project_names = [r['Project_Name'] for r in funding_data]
# Sort longest first
project_names.sort(key=len, reverse=True)

final_occurrences = []
found_indices = set()

for pname in project_names:
    start = 0
    while True:
        idx = full_text.find(pname, start)
        if idx == -1:
            break
        
        # Check overlap
        # simple check: if any index in range(idx, idx+len) is in found_indices, skip
        # or better: since we process longest first, if we find an overlap, it must be with a previously found LONGER name?
        # No, we process longest first. So if we find a match now, and it overlaps with something in found_indices,
        # that implies the characters are already claimed by a LONGER name.
        # So we skip this match.
        
        is_overlap = False
        for i in range(idx, idx + len(pname)):
            if i in found_indices:
                is_overlap = True
                break
        
        if not is_overlap:
            # Claim indices
            for i in range(idx, idx + len(pname)):
                found_indices.add(i)
            final_occurrences.append({"name": pname, "start": idx, "end": idx + len(pname)})
            
        start = idx + 1 # advance by 1 to find other overlaps or next

final_occurrences.sort(key=lambda x: x['start'])

results = []
keywords = ["emergency", "FEMA", "fire", "warning"]

for i, proj in enumerate(final_occurrences):
    p_start = proj['start']
    
    # Determine header
    status = "unknown"
    # Find last header before p_start
    # Filter headers < p_start
    prev_headers = [h for h in header_positions if h['pos'] < p_start]
    if prev_headers:
        status = prev_headers[-1]['info']['status']
    
    # Determine snippet end
    # Next project start or next header start
    next_boundary = len(full_text)
    
    # Check next project
    if i + 1 < len(final_occurrences):
        next_boundary = min(next_boundary, final_occurrences[i+1]['start'])
    
    # Check next header
    next_headers = [h for h in header_positions if h['pos'] > p_start]
    if next_headers:
        next_boundary = min(next_boundary, next_headers[0]['pos'])
        
    snippet = full_text[proj['end']:next_boundary]
    
    # Refine Status
    final_status = status
    if status == "construction":
        # Check completion
        if "completed" in snippet.lower() or "notice of completion" in snippet.lower():
            final_status = "completed"
        else:
            final_status = "design" # Map active construction to design per Hint constraints
    elif status == "unknown":
        final_status = "not started" # Default fallback? Or maybe 'design'?
        
    # Check relevance
    is_relevant = False
    if any(k.lower() in proj['name'].lower() for k in keywords):
        is_relevant = True
    if any(k.lower() in snippet.lower() for k in keywords):
        is_relevant = True
        
    if is_relevant:
        # Get Funding Info
        f_rec = next((r for r in funding_data if r['Project_Name'] == proj['name']), None)
        if f_rec:
            results.append({
                "Project_Name": proj['name'],
                "Funding_Source": f_rec['Funding_Source'],
                "Amount": f_rec['Amount'],
                "Status": final_status
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-2419378835906552192': ['Funding'], 'var_function-call-2419378835906551985': ['civic_docs'], 'var_function-call-7626981016965622443': 'file_storage/function-call-7626981016965622443.json', 'var_function-call-7626981016965621198': 'file_storage/function-call-7626981016965621198.json'}

exec(code, env_args)
