code = """import json
import re

# Load civic docs
with open(locals()['var_function-call-4378397036862682776'], 'r') as f:
    civic_docs = json.load(f)

# Load funding data
with open(locals()['var_function-call-15946472843602217785'], 'r') as f:
    funding_data = json.load(f)

newline = chr(10)
full_text = newline.join([d['text'] for d in civic_docs])

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
    
    lines = current_segment.split(newline)
    lines = [l.strip() for l in lines if l.strip()]
    
    if not lines:
        continue
        
    project_name = lines[-1]
    
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
    # Use generic pattern
    match = re.search(r"Begin [Cc]onstruction:?\s*(.*?)" + newline, body, re.IGNORECASE)
    if match:
        if "2022" in match.group(1):
            starts_in_2022 = True
            
    if not starts_in_2022:
        match_start = re.search(r"Start [Dd]ate:?\s*(.*?)" + newline, body, re.IGNORECASE)
        if match_start:
            if "2022" in match_start.group(1):
                starts_in_2022 = True
                
    if is_disaster and starts_in_2022:
        target_projects.append(name)

# Match Funding
total_funding = 0
matched_details = []

# Keep track of used IDs to avoid double counting across projects if names overlap
used_funding_ids = set()

for text_name in target_projects:
    t_n = " ".join(text_name.split())
    
    variants = [t_n]
    if t_n.endswith(" Project"):
        variants.append(t_n[:-8].strip())
        
    row_sum = 0
    
    for row in funding_data:
        fid = row['Funding_ID']
        if fid in used_funding_ids:
            continue
            
        f_n = " ".join(row['Project_Name'].split())
        amt = int(row['Amount'])
        
        match = False
        for v in variants:
            # Check for exact, startswith space, startswith paren
            if f_n == v:
                match = True
            elif f_n.startswith(v + " "):
                match = True
            elif f_n.startswith(v + "("):
                match = True
                
        if match:
            row_sum += amt
            used_funding_ids.add(fid)
                
    matched_details.append({"name": text_name, "sum": row_sum})
    total_funding += row_sum

print("__RESULT__:")
print(json.dumps({"target_projects": target_projects, "matched_details": matched_details, "total_funding": total_funding}))"""

env_args = {'var_function-call-7229016850937380290': ['civic_docs'], 'var_function-call-7229016850937378739': ['Funding'], 'var_function-call-15946472843602215220': 'file_storage/function-call-15946472843602215220.json', 'var_function-call-15946472843602217785': 'file_storage/function-call-15946472843602217785.json', 'var_function-call-4378397036862682776': 'file_storage/function-call-4378397036862682776.json'}

exec(code, env_args)
