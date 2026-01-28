code = """import json
import re

funding_path = locals()['var_function-call-12281122830220394756']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

docs_path = locals()['var_function-call-3253055519445541233']
with open(docs_path, 'r') as f:
    docs = json.load(f)

# Concatenate text safely
lines = []
for d in docs:
    # Split by lines to avoid huge string issues
    lines.extend(d['text'].split('\n'))

def clean_project_name(name):
    # Remove parens with FEMA/CalOES
    return re.sub(r'\s*\((FEMA|CalOES|CalJPIA).*?\)', '', name).strip()

funding_map = {}
for record in funding_data:
    cname = clean_project_name(record['Project_Name'])
    if cname not in funding_map:
        funding_map[cname] = []
    funding_map[cname].append(record)

search_names = list(funding_map.keys())

target_dates = ["spring 2022", "march 2022", "april 2022", "may 2022"]
start_markers = ["begin construction", "start date", "construction start"]

found_projects = set()

for i, line in enumerate(lines):
    line_clean = line.strip()
    if len(line_clean) < 5: continue
    
    # Check for project name match
    matched_name = None
    for name in search_names:
        # Check for exact or near exact match
        # Avoid partial matches like "Park" matching "Trancas Canyon Park"
        # Check if line IS the name (ignoring case)
        if name.lower() == line_clean.lower():
            matched_name = name
            break
        # Or if line contains name and is not too long
        elif name.lower() in line_clean.lower() and len(line_clean) < len(name) + 10:
             matched_name = name
             break
    
    if matched_name:
        # Check next 20 lines for start date
        chunk = lines[i:i+25]
        chunk_text = " ".join(chunk).lower() # join with space to handle wrap? No, distinct lines better.
        
        # Check line by line in chunk
        for c_line in chunk:
            c_line_lower = c_line.lower()
            # Check for date presence
            has_date = False
            for td in target_dates:
                if td in c_line_lower:
                    has_date = True
                    break
            
            if has_date:
                # Check for start marker in same line
                has_marker = False
                for sm in start_markers:
                    if sm in c_line_lower:
                        has_marker = True
                        break
                
                if has_marker:
                    found_projects.add(matched_name)
                    # print(f"Found: {matched_name} at {c_line}")
                    break

# Calculate totals
count = len(found_projects)
total_funding = 0
for name in found_projects:
    for r in funding_map[name]:
        total_funding += int(r['Amount'])

print("__RESULT__:")
print(json.dumps({"count": count, "total_funding": total_funding, "projects": list(found_projects)}))"""

env_args = {'var_function-call-3253055519445541233': 'file_storage/function-call-3253055519445541233.json', 'var_function-call-14502065749304076563': ['Funding'], 'var_function-call-12281122830220394756': 'file_storage/function-call-12281122830220394756.json'}

exec(code, env_args)
