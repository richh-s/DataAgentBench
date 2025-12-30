code = """import json

# Load Funding Data
f_path = locals()['var_function-call-18338097190438491803']
with open(f_path, 'r') as f:
    funding_data = json.load(f)

# Load Civic Docs
d_path = locals()['var_function-call-7592181240174987408']
with open(d_path, 'r') as f:
    civic_docs = json.load(f)

# Combine text
full_text = chr(10).join([doc['text'] for doc in civic_docs])

# Sections
sections = [
    ("design", "Capital Improvement Projects (Design)"),
    ("construction", "Capital Improvement Projects (Construction)"),
    ("not started", "Capital Improvement Projects (Not Started)")
]

section_positions = []
for status, header in sections:
    idx = full_text.find(header)
    if idx != -1:
        section_positions.append({"status": status, "start": idx, "header": header})

section_positions.sort(key=lambda x: x['start'])

# Add end positions
for i in range(len(section_positions) - 1):
    section_positions[i]['end'] = section_positions[i+1]['start']
if section_positions:
    section_positions[-1]['end'] = len(full_text)

# Find project occurrences
project_matches = []
for record in funding_data:
    p_name = record['Project_Name']
    idx = full_text.find(p_name)
    if idx != -1:
        status = "Unknown"
        for section in section_positions:
            if section['start'] <= idx < section['end']:
                status = section['status']
                break
        
        project_matches.append({
            "name": p_name,
            "idx": idx,
            "status": status,
            "funding_record": record
        })
    else:
        # If not found in text, check if name is relevant
        # If so, status is Unknown or maybe "not started" (default?)
        # For now, store with status "Unknown"
        keywords = ['emergency', 'fema']
        if any(k in p_name.lower() for k in keywords):
             project_matches.append({
                "name": p_name,
                "idx": -1,
                "status": "not started", # Assumption: if not in active report, maybe not started? Or completed long ago? I'll label "not listed"
                "funding_record": record
            })

# Sort matches
project_matches.sort(key=lambda x: x['idx'])

results = []
keywords = ['emergency', 'fema']

for i in range(len(project_matches)):
    match = project_matches[i]
    if match['idx'] == -1:
        # Came from name-only match
        results.append({
            "Project Name": match['name'],
            "Funding Source": match['funding_record']['Funding_Source'],
            "Amount": match['funding_record']['Amount'],
            "Status": match['status']
        })
        continue

    start = match['idx']
    # Determine end
    # Find next match with idx > start
    next_idx = len(full_text)
    
    # We can just look at the next element in sorted list if it has idx > start
    if i < len(project_matches) - 1:
        next_candidate = project_matches[i+1]['idx']
        if next_candidate > start:
            next_idx = next_candidate
            
    # Also clamp to section end
    current_section_end = len(full_text)
    for section in section_positions:
        if section['start'] <= start < section['end']:
            current_section_end = section['end']
            break
    
    end = min(next_idx, current_section_end)
    
    block = full_text[start:end]
    
    # Check keywords
    is_relevant = False
    if any(k in match['name'].lower() for k in keywords):
        is_relevant = True
    if any(k in block.lower() for k in keywords):
        is_relevant = True
        
    if is_relevant:
        final_status = match['status']
        # Refine status based on block content
        block_lower = block.lower()
        if final_status == "construction":
            if "construction was completed" in block_lower or "notice of completion" in block_lower:
                final_status = "completed"
            elif "under construction" in block_lower:
                final_status = "construction" # Keep as construction
        
        results.append({
            "Project Name": match['name'],
            "Funding Source": match['funding_record']['Funding_Source'],
            "Amount": match['funding_record']['Amount'],
            "Status": final_status
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-8827426620448851046': ['civic_docs'], 'var_function-call-8827426620448850527': ['Funding'], 'var_function-call-6655663227324629394': 'file_storage/function-call-6655663227324629394.json', 'var_function-call-7592181240174987408': 'file_storage/function-call-7592181240174987408.json', 'var_function-call-18338097190438491803': 'file_storage/function-call-18338097190438491803.json'}

exec(code, env_args)
