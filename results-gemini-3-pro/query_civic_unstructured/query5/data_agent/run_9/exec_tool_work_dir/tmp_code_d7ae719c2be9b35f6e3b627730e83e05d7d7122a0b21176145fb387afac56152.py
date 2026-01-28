code = """import json
import re

# Load civic docs
with open(locals()['var_function-call-4378397036862682776'], 'r') as f:
    civic_docs = json.load(f)

# Load funding data
with open(locals()['var_function-call-15946472843602217785'], 'r') as f:
    funding_data = json.load(f)

full_text = "\n".join([d['text'] for d in civic_docs])

# Markers
marker_updates = "(cid:190) Updates:"
marker_desc = "(cid:190) Project Description:"
placeholder = "__MARKER__"

text = full_text.replace(marker_updates, placeholder).replace(marker_desc, placeholder)
segments = text.split(placeholder)

parsed_projects = []
ignore_headers = [
    "Capital Improvement Projects (Design)",
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Capital Improvement Projects and Disaster Recovery Projects Status",
    "Report",
    "Public Works",
    "Commission Meeting"
]

for i in range(len(segments) - 1):
    current_segment = segments[i].strip()
    next_segment = segments[i+1]
    
    lines = current_segment.split('\n')
    lines = [l.strip() for l in lines if l.strip()]
    
    if not lines:
        continue
        
    project_name = lines[-1]
    # Simple heuristic to go back one line if the last line is a known header
    if project_name in ignore_headers:
        if len(lines) > 1:
            project_name = lines[-2]
            
    parsed_projects.append({"name": project_name, "body": next_segment})

target_projects = []
keywords = ["FEMA", "CalOES", "Disaster", "Woolsey", "Fire"]

for p in parsed_projects:
    name = p["name"]
    body = p["body"]
    
    # Check Disaster
    is_disaster = False
    if any(k.upper() in name.upper() for k in keywords):
        is_disaster = True
    elif any(k.upper() in body.upper() for k in keywords):
        is_disaster = True
        
    # Check Start 2022
    starts_in_2022 = False
    # Regex: "Begin Construction: <text>"
    # We look for 2022 in that text.
    match = re.search(r"Begin [Cc]onstruction:?\s*(.*?)\n", body, re.IGNORECASE)
    if match:
        if "2022" in match.group(1):
            starts_in_2022 = True
            
    # Also check "Start Date"
    if not starts_in_2022:
        match_start = re.search(r"Start [Dd]ate:?\s*(.*?)\n", body, re.IGNORECASE)
        if match_start:
            if "2022" in match_start.group(1):
                starts_in_2022 = True
                
    if is_disaster and starts_in_2022:
        target_projects.append(name)

# Match Funding
total_funding = 0
matched_details = []

for text_name in target_projects:
    t_n = " ".join(text_name.split())
    
    # Prepare variants for matching
    # 1. Exact
    # 2. Starts with
    # 3. Without "Project" suffix
    
    variants = [t_n]
    if t_n.endswith(" Project"):
        variants.append(t_n[:-8].strip())
        
    row_sum = 0
    matched_rows = []
    
    for row in funding_data:
        f_n = " ".join(row['Project_Name'].split())
        amt = int(row['Amount'])
        
        match = False
        for v in variants:
            if f_n == v or f_n.startswith(v + " "): # Prefix match with space boundary
                match = True
            # Also allow simple startswith if no space? e.g. "Project A (FEMA)" starts with "Project A"
            elif f_n.startswith(v + "("): 
                match = True
            elif f_n == v:
                match = True
                
        if match:
            # Avoid double counting if multiple variants match the same row (unlikely)
            if row['Funding_ID'] not in matched_rows:
                row_sum += amt
                matched_rows.append(row['Funding_ID'])
                
    matched_details.append({"name": text_name, "sum": row_sum})
    total_funding += row_sum

print("__RESULT__:")
print(json.dumps({"target_projects": target_projects, "matched_details": matched_details, "total_funding": total_funding}))"""

env_args = {'var_function-call-7229016850937380290': ['civic_docs'], 'var_function-call-7229016850937378739': ['Funding'], 'var_function-call-15946472843602215220': 'file_storage/function-call-15946472843602215220.json', 'var_function-call-15946472843602217785': 'file_storage/function-call-15946472843602217785.json', 'var_function-call-4378397036862682776': 'file_storage/function-call-4378397036862682776.json'}

exec(code, env_args)
