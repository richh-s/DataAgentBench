code = """import json
import re

# Load data
funding_path = locals()['var_function-call-12281122830220394756']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

docs_path = locals()['var_function-call-3253055519445541233']
with open(docs_path, 'r') as f:
    docs = json.load(f)

# Process text
lines = []
for d in docs:
    lines.extend(d['text'].splitlines())

def clean_project_name(name):
    return re.sub(r'\s*\((FEMA|CalOES|CalJPIA).*?\)', '', name).strip()

funding_map = {}
for record in funding_data:
    cname = clean_project_name(record['Project_Name'])
    if cname not in funding_map:
        funding_map[cname] = []
    funding_map[cname].append(record)

search_names = list(funding_map.keys())

# Target: Spring 2022 (March, April, May)
target_dates = ["spring 2022", "march 2022", "april 2022", "may 2022"]
start_markers = ["begin construction", "start date", "construction start"]

found_projects = set()

for i, line in enumerate(lines):
    line_clean = line.strip()
    if len(line_clean) < 5: continue
    
    # Identify project name
    matched_name = None
    # Quick check optimization?
    # Iterate all search names is slow if list is huge (100+ names). 
    # But string matching is fast enough for 100 names and ~10k lines.
    
    line_lower = line_clean.lower()
    for name in search_names:
        if name.lower() == line_lower:
            matched_name = name
            break
        # Relaxed match: if line starts with name or name is in line (and line is header-like)
        # Check if name is in line and line is short
        elif name.lower() in line_lower and len(line_clean) < len(name) + 15:
             matched_name = name
             break
    
    if matched_name:
        # Check context for date
        # Check next 20 lines
        chunk = lines[i:i+20]
        
        for c_line in chunk:
            c_line_lower = c_line.lower()
            
            # Check for date and marker
            if any(td in c_line_lower for td in target_dates):
                if any(sm in c_line_lower for sm in start_markers):
                    found_projects.add(matched_name)
                    break

# Calculate results
count = len(found_projects)
total_funding = 0
for name in found_projects:
    for r in funding_map[name]:
        total_funding += int(r['Amount'])

print("__RESULT__:")
print(json.dumps({"count": count, "total_funding": total_funding, "projects": list(found_projects)}))"""

env_args = {'var_function-call-3253055519445541233': 'file_storage/function-call-3253055519445541233.json', 'var_function-call-14502065749304076563': ['Funding'], 'var_function-call-12281122830220394756': 'file_storage/function-call-12281122830220394756.json'}

exec(code, env_args)
