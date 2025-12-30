code = """import json
import re

# Load data
with open(locals()['var_function-call-1312699190325446696'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-18394559643170776925'], 'r') as f:
    civic_docs = json.load(f)
    text = civic_docs[0]['text'] if civic_docs else ""

# Normalize name helper
def normalize(name):
    # Remove distinct suffixes for matching
    # (FEMA...), (CalOES...), (CalJPIA...)
    n = re.sub(r'\((FEMA|CalOES|CalJPIA).*?\)', '', name, flags=re.IGNORECASE)
    return n.strip().lower()

# Map base name to records
# And identify disaster base names
funding_map = {}
disaster_names = set()

for rec in funding_data:
    raw = rec['Project_Name']
    norm = normalize(raw)
    
    if norm not in funding_map:
        funding_map[norm] = []
    funding_map[norm].append(rec)
    
    if re.search(r'(FEMA|CalOES|CalJPIA)', raw, re.IGNORECASE):
        disaster_names.add(norm)

# Extract projects from text
lines = text.split('\n')
projects = {}
current_p = None
current_buff = []

# List of known normalized names
known_names = list(funding_map.keys())
# Sort by length desc
known_names.sort(key=len, reverse=True)

for i, line in enumerate(lines):
    l = line.strip()
    if not l: continue
    
    # Check if line matches a project name
    l_norm = l.lower()
    
    # Exact match check
    match = None
    if l_norm in known_names:
        match = l_norm
    else:
        # Check if line is just a known name (ignoring punctuation?)
        for kn in known_names:
            if l_norm == kn:
                match = kn
                break
    
    if match:
        # Verify it's a header by looking ahead for keywords
        is_header = False
        # Look ahead up to 5 lines
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

# Analyze
results = []
total_funding = 0

for p_norm, p_text in projects.items():
    # Check start date
    # Look for "Begin Construction: <Date>"
    # Regex: Begin Construction:\s*([A-Za-z0-9\s]+)
    
    start_match = re.search(r'Begin Construction:?\s*([A-Za-z0-9\s]+)', p_text, re.IGNORECASE)
    start_str = start_match.group(1).strip() if start_match else ""
    
    # Check if year 2022
    started_2022 = False
    if "2022" in start_str:
        started_2022 = True
    
    # Check "Updates" for "began" or "started"
    if not started_2022:
        # e.g. "Construction was completed November 2022" -> Not started 2022 necessarily
        # "Construction began November 2022"
        if re.search(r'(began|started)\s+(in\s+)?([A-Za-z]+\s+)?2022', p_text, re.IGNORECASE):
            started_2022 = True
            start_str = "Found in text: 2022"

    # Check is disaster
    is_disaster = False
    if p_norm in disaster_names:
        is_disaster = True
    if re.search(r'(FEMA|CalOES|CalJPIA|Disaster|Woolsey)', p_text, re.IGNORECASE):
        is_disaster = True
        
    if started_2022 and is_disaster:
        # Sum funding
        amount = 0
        for rec in funding_map.get(p_norm, []):
            amount += int(rec['Amount'])
        
        results.append({
            "name": p_norm,
            "start_info": start_str,
            "amount": amount
        })
        total_funding += amount

print("__RESULT__:")
print(json.dumps({"projects": results, "total": total_funding}))"""

env_args = {'var_function-call-7116383370985667147': ['Funding'], 'var_function-call-7116383370985666072': 'file_storage/function-call-7116383370985666072.json', 'var_function-call-1312699190325446696': 'file_storage/function-call-1312699190325446696.json', 'var_function-call-18394559643170776925': 'file_storage/function-call-18394559643170776925.json'}

exec(code, env_args)
