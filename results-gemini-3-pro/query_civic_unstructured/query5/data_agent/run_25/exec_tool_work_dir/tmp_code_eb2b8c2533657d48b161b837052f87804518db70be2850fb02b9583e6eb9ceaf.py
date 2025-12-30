code = """import json
import re

path_fund = locals()['var_function-call-10469334728230477233']
path_civic = locals()['var_function-call-2938925832300121320']

with open(path_fund, 'r') as f:
    funding_data = json.load(f)

with open(path_civic, 'r') as f:
    civic_docs = json.load(f)

full_text = ""
for doc in civic_docs:
    full_text += doc['text'] + chr(10)

lines = full_text.split(chr(10))
projects = {}
current_name = None
current_text = []

def is_bullet(l):
    l = l.strip()
    return l.startswith("(cid:") or l.startswith("•") or l.startswith("-")

for i in range(len(lines)):
    line = lines[i].strip()
    if not line:
        continue
    
    # Check if this line is a project header
    # Heuristic: It's not a bullet, and the NEXT non-empty line IS a bullet or "Updates:"
    is_header = False
    if not is_bullet(line):
        # Look ahead
        for j in range(i+1, min(i+5, len(lines))):
            nl = lines[j].strip()
            if not nl: continue
            if is_bullet(nl) or nl.startswith("Updates:"):
                is_header = True
            break
    
    # Also ignore explicit headers
    if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
        is_header = False
        
    if is_header:
        # Save previous
        if current_name:
            projects[current_name] = chr(10).join(current_text)
        current_name = line
        current_text = []
    else:
        if current_name:
            current_text.append(line)

if current_name:
    projects[current_name] = chr(10).join(current_text)

# Analysis
total = 0
matches = []

# Normalize project keys for easier matching
norm_projects = {k.strip().lower(): v for k, v in projects.items()}

for item in funding_data:
    p_name = item['Project_Name']
    amt = float(item['Amount'])
    
    # Check disaster
    is_disaster = False
    if "FEMA" in p_name or "CalOES" in p_name or "CalJPIA" in p_name:
        is_disaster = True
        
    # Get text
    # Try exact match first
    txt = ""
    name_key = p_name.strip().lower()
    
    # Try removing suffix
    base_name = re.sub(r"\s*\(.*?\)$", "", p_name).strip().lower()
    
    if name_key in norm_projects:
        txt = norm_projects[name_key]
    elif base_name in norm_projects:
        txt = norm_projects[base_name]
    else:
        # fuzzy match in keys
        for k in norm_projects:
            if base_name in k:
                txt = norm_projects[k]
                break
    
    start_2022 = False
    
    # Check Start Date
    # 1. Year in Name
    if "2022" in p_name:
        start_2022 = True
    
    # 2. Year in Text
    if txt and not start_2022:
        # Look for "Begin Construction: ... 2022"
        # "Advertise: ... 2022"
        # "Start: ... 2022"
        
        # We can extract the "Project Schedule" section
        # Or just regex the whole text block
        
        # Patterns for 2022 start
        patterns = [
            r"Begin [Cc]onstruction.{0,50}2022",
            r"Start [Dd]ate.{0,50}2022",
            r"Advertise.{0,50}2022",
            r"Construction began.{0,50}2022"
        ]
        
        for pat in patterns:
            if re.search(pat, txt, re.IGNORECASE):
                start_2022 = True
                break
        
        # Special case: "Construction was completed November 2022"
        # If it completed in 2022, it *might* have started in 2022.
        # But if it started in 2021...
        # Let's check if there is a "completed" date in 2022 and NO start date mentioned.
        # If "Updates: Construction was completed... 2022", it implies active work in 2022.
        # The prompt asks "projects that started in 2022".
        # This usually means Start Date >= 2022-01-01.
        # So "Completed 2022" is NOT sufficient evidence of starting in 2022 (could start 2021).
        # I will stick to explicit start indicators.

    if is_disaster and start_2022:
        total += amt
        matches.append(p_name)

print("__RESULT__:")
print(json.dumps({"total": total, "matches": matches, "parsed_sample": list(norm_projects.keys())[:5]}))"""

env_args = {'var_function-call-10469334728230477233': 'file_storage/function-call-10469334728230477233.json', 'var_function-call-10469334728230474172': 'file_storage/function-call-10469334728230474172.json', 'var_function-call-2938925832300121320': 'file_storage/function-call-2938925832300121320.json', 'var_function-call-12502361018328116741': {'total': 87000.0, 'matches': ['Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)'], 'parsed_titles': ['Agenda Report', '03-22-23', 'Jorge Rubalcava, Senior Civil Engineer', 'Date prepared: March 15, 2023', 'Meeting date: March 22, 2023']}}

exec(code, env_args)
