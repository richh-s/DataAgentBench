code = """import json
import re

# Load funding results
with open(locals()['var_function-call-2752695128907644383'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-10485844614487521069'], 'r') as f:
    civic_docs = json.load(f)

# Filter funding for > 50,000
funded_projects = {}
for item in funding_data:
    try:
        amount = int(item['Amount'])
        if amount > 50000:
            funded_projects[item['Project_Name'].strip()] = amount
    except ValueError:
        pass

# Extract design projects from civic docs
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Normalize text newlines
    text = text.replace('\r\n', '\n')
    
    # Find the section "Capital Improvement Projects (Design)"
    section_header = "Capital Improvement Projects (Design)"
    start_idx = text.find(section_header)
    
    if start_idx == -1:
        continue
        
    start_idx += len(section_header)
    
    # Find the end of the section
    # Use a list of possible next headers
    next_headers = [
        "Capital Improvement Projects (Construction)",
        "Capital Improvement Projects (Not Started)",
        "Disaster Recovery Projects",
        "Public Works Commission"
    ]
    
    end_idx = len(text)
    for header in next_headers:
        idx = text.find(header, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    section_text = text[start_idx:end_idx]
    
    # Split by lines
    lines = [line.strip() for line in section_text.split('\n') if line.strip()]
    
    for i, line in enumerate(lines):
        # Check if next line indicates this is a project title
        if i + 1 < len(lines):
            next_line = lines[i+1]
            # Look for keywords that signify the start of details
            if "Updates:" in next_line or "Project Description:" in next_line or "Project Updates:" in next_line:
                p_name = line.strip()
                # Simple heuristic to avoid noise
                if len(p_name) > 3 and "Page" not in p_name:
                    design_projects.add(p_name)

# Matching logic
matches = []
normalized_funding = {k.lower(): k for k in funded_projects.keys()}

for dp in design_projects:
    dp_norm = dp.lower()
    
    # Check for exact or starts-with match
    matched_name = None
    
    if dp_norm in normalized_funding:
        matched_name = normalized_funding[dp_norm]
    else:
        # Check if any funding project starts with this name (handling suffixes)
        # Or if the design project name is contained in the funding project name
        for fname_norm, original_name in normalized_funding.items():
            if fname_norm.startswith(dp_norm) or dp_norm in fname_norm:
                # We need to be reasonably sure
                # If dp is "Storm Drain Master Plan" and fname is "Storm Drain Master Plan (FEMA Project)" -> Match
                matched_name = original_name
                break
    
    if matched_name:
        matches.append(matched_name)

# Deduplicate matches
unique_matches = sorted(list(set(matches)))

print("__RESULT__:")
print(json.dumps({"count": len(unique_matches), "matches": unique_matches, "extracted_projects": list(design_projects)}))"""

env_args = {'var_function-call-2752695128907644383': 'file_storage/function-call-2752695128907644383.json', 'var_function-call-2752695128907641442': 'file_storage/function-call-2752695128907641442.json', 'var_function-call-10485844614487521069': 'file_storage/function-call-10485844614487521069.json'}

exec(code, env_args)
