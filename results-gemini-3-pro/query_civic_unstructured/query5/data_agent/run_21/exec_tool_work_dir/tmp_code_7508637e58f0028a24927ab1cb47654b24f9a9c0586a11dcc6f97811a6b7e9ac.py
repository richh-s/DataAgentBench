code = """import json
import re

# Load data
with open(locals()['var_function-call-1312699190325446696'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-18394559643170776925'], 'r') as f:
    civic_docs = json.load(f)
    text = civic_docs[0]['text'] if civic_docs else ""

def normalize(name):
    # Remove (FEMA...), (CalOES...), (CalJPIA...)
    # Use brackets for parens
    n = re.sub(r'[(](FEMA|CalOES|CalJPIA).*?[)]', '', name, flags=re.IGNORECASE)
    return n.strip().lower()

funding_map = {}
disaster_names = set()

for rec in funding_data:
    raw = rec['Project_Name']
    norm = normalize(raw)
    
    if norm not in funding_map:
        funding_map[norm] = []
    funding_map[norm].append(rec)
    
    if 'FEMA' in raw or 'CalOES' in raw or 'CalJPIA' in raw:
        disaster_names.add(norm)

# Split lines safely
lines = text.splitlines()
projects = {}
current_p = None
current_buff = []

known_names = list(funding_map.keys())
known_names.sort(key=len, reverse=True)

for i, line in enumerate(lines):
    l = line.strip()
    if not l: continue
    
    l_norm = l.lower()
    
    match = None
    if l_norm in known_names:
        match = l_norm
    else:
        for kn in known_names:
            if l_norm == kn:
                match = kn
                break
    
    if match:
        is_header = False
        for offset in range(1, 6):
            if i + offset < len(lines):
                nl = lines[i+offset].strip().lower()
                if "updates" in nl or "project description" in nl or "project schedule" in nl or "estimated schedule" in nl:
                    is_header = True
                    break
        
        if is_header:
            if current_p:
                projects[current_p] = "\n".join(current_buff)
            current_p = match
            current_buff = []
            continue

    if current_p:
        current_buff.append(line)

if current_p:
    projects[current_p] = "\n".join(current_buff)

results = []
total_funding = 0

for p_norm, p_text in projects.items():
    start_year = None
    
    # Check lines for Start info
    for line in p_text.splitlines():
        line_lower = line.lower()
        # "Begin Construction"
        if "begin construction" in line_lower:
            if "2022" in line:
                start_year = 2022
            elif "2023" in line:
                start_year = 2023
        # "Construction was completed" -> implies start earlier. 
        # But question asks for projects that STARTED in 2022.
        # If completed Nov 2022, started 2022 is possible but not guaranteed.
        # However, looking at the preview: "Bluffs Park Shade Structure" completed Nov 2022.
        # It's a small structure. Likely started in 2022.
        # "Broad Beach Road Water Quality Repair" completed Nov 2022.
        # I'll enable a heuristic: if completed in late 2022, assume started 2022?
        # Or look for "began"
        elif "began" in line_lower or "started" in line_lower:
             if "construction" in line_lower and "2022" in line:
                 start_year = 2022
    
    is_disaster = False
    if p_norm in disaster_names:
        is_disaster = True
    if "fema" in p_text.lower() or "caloes" in p_text.lower() or "caljpia" in p_text.lower() or "disaster" in p_text.lower():
        is_disaster = True
        
    if start_year == 2022 and is_disaster:
        amount = 0
        for rec in funding_map.get(p_norm, []):
            amount += int(rec['Amount'])
        
        results.append({
            "name": p_norm,
            "amount": amount
        })
        total_funding += amount

print("__RESULT__:")
print(json.dumps({"projects": results, "total": total_funding}))"""

env_args = {'var_function-call-7116383370985667147': ['Funding'], 'var_function-call-7116383370985666072': 'file_storage/function-call-7116383370985666072.json', 'var_function-call-1312699190325446696': 'file_storage/function-call-1312699190325446696.json', 'var_function-call-18394559643170776925': 'file_storage/function-call-18394559643170776925.json'}

exec(code, env_args)
