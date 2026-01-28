code = """import json

# Access file paths from locals()
civic_docs_path = locals()['var_function-call-8728366382386706787']
funding_data_path = locals()['var_function-call-8728366382386704966']

# Load data
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)
with open(funding_data_path, 'r') as f:
    funding_data = json.load(f)

# Build funding map
funding_map = {}
for row in funding_data:
    funding_map[row['Project_Name'].strip()] = row['Amount']

projects_found = {} # Name -> List of start dates

# Function to check date
def is_target_date(d_str):
    d = d_str.lower()
    if '2022' in d:
        if 'spring' in d: return True
        # Months
        if 'march' in d or 'april' in d or 'may' in d: return True
    return False

# Parse
for doc in civic_docs:
    lines = doc['text'].splitlines()
    curr_proj = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        
        # Identify Project Name
        # Look ahead
        is_new_proj = False
        for k in range(i+1, min(i+5, len(lines))):
            nxt = lines[k].strip()
            if not nxt: continue
            if '(cid:190)' in nxt or 'Updates:' in nxt:
                # Also check if line is not header
                if 'Capital Improvement' not in line and 'Agenda Item' not in line:
                    is_new_proj = True
            break
        
        if is_new_proj:
            curr_proj = line
            if curr_proj not in projects_found:
                projects_found[curr_proj] = []
        
        if curr_proj:
            # Look for start info
            low = line.lower()
            if 'begin construction' in low:
                parts = line.split(':')
                if len(parts) > 1:
                    projects_found[curr_proj].append(parts[1].strip())

# Filter for Spring 2022
target_projects = []
for p, dates in projects_found.items():
    for d in dates:
        if is_target_date(d):
            target_projects.append(p)
            break

# Calculate funding
total_funding = 0
matched_projects = []
unmatched = []

for p in target_projects:
    # Try exact match
    if p in funding_map:
        total_funding += funding_map[p]
        matched_projects.append(p)
    else:
        # Try case-insensitive
        found = False
        for fp in funding_map:
            if fp.lower() == p.lower():
                total_funding += funding_map[fp]
                matched_projects.append(p)
                found = True
                break
        
        if not found:
            unmatched.append(p)

print("__RESULT__:")
print(json.dumps({
    "count": len(matched_projects), 
    "total_funding": total_funding,
    "projects": matched_projects,
    "unmatched": unmatched,
    "debug_dates": {k:v for k,v in projects_found.items() if v}
}))"""

env_args = {'var_function-call-8728366382386706787': 'file_storage/function-call-8728366382386706787.json', 'var_function-call-8728366382386704966': 'file_storage/function-call-8728366382386704966.json'}

exec(code, env_args)
