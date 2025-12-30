code = """import json
import re

# Load Funding Data
funding_path = locals()['var_function-call-12281122830220394756']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load Civic Docs
docs_path = locals()['var_function-call-3253055519445541233']
with open(docs_path, 'r') as f:
    docs = json.load(f)

full_text = "\n".join([d['text'] for d in docs])
lines = full_text.split('\n')

# Normalize funding names to get search keys
# Heuristic: Remove content in parentheses if it contains FEMA, CalOES, CalJPIA
def clean_project_name(name):
    return re.sub(r'\s*\((FEMA|CalOES|CalJPIA).*?\)', '', name).strip()

funding_map = {} # clean_name -> list of records
for record in funding_data:
    cname = clean_project_name(record['Project_Name'])
    if cname not in funding_map:
        funding_map[cname] = []
    funding_map[cname].append(record)

search_names = list(funding_map.keys())

# Find projects starting in Spring 2022
# Start Time (st) keywords: "Begin Construction", "Start Date", "Construction Start"
# Target Date: Spring 2022 => "Spring 2022", "March 2022", "April 2022", "May 2022", "03-2022", "04-2022", "05-2022"
# Also checking for "Spring, 2022"

target_dates = ["spring 2022", "march 2022", "april 2022", "may 2022"]
start_markers = ["begin construction", "start date", "construction start", "advertise"] # Advertise might be start for some, but typically construction. 
# Prompt says "started". I'll stick to "Begin Construction" or explicit Start.
# Wait, "Advertise" is a phase. "Begin Construction" is better.
# Let's start with strict "Begin Construction" and see.

found_projects = set()

# iterate through text to find project blocks
# We'll look for lines that match a search_name
for i, line in enumerate(lines):
    line_clean = line.strip()
    if not line_clean: continue
    
    # Check if line matches a project name
    # Exact match or close match? The text might have "Project" at the end while funding name doesn't, or vice versa.
    # Funding names often include "Project" (e.g. "Westward Beach Road Repair Project").
    
    # We check if the line contains the project name (case insensitive)
    # and is relatively short (to avoid matching sentences mentioning the project)
    
    potential_projects = []
    for name in search_names:
        if len(name) > 10 and name.lower() in line_clean.lower():
             # If line length is close to name length (e.g. within 10 chars)
             if len(line_clean) < len(name) + 20:
                 potential_projects.append(name)
    
    if not potential_projects:
        continue
        
    # Pick the longest match
    best_match = max(potential_projects, key=len)
    
    # Look ahead for "Spring 2022" start
    # Scan next 20 lines
    chunk = lines[i:i+25]
    chunk_text = "\n".join(chunk).lower()
    
    is_spring_2022 = False
    
    # Regex to find Date associated with Start
    # Look for "Begin Construction: ... Spring 2022"
    # or "Start ... Spring 2022"
    
    # Pattern: (marker) ... (date)
    # Check for target dates in the chunk
    for date_str in target_dates:
        if date_str in chunk_text:
            # Check context
            # We want to ensure it's a start date, not "Complete Design: Spring 2022"
            # Find the line with the date
            for c_line in chunk:
                if date_str in c_line.lower():
                    # Check if this line or previous line has a start marker
                    if any(m in c_line.lower() for m in start_markers):
                        is_spring_2022 = True
                        # print(f"Found Match: {best_match} -> {c_line}")
                        break
                    # If marker is in previous line (e.g. "Begin Construction:\nSpring 2022")
                    # We need to handle that, but typically they are on same line in these docs
            if is_spring_2022: break
    
    if is_spring_2022:
        found_projects.add(best_match)

# Calculate funding
total_funding = 0
count = 0
matched_records = []

for name in found_projects:
    records = funding_map[name]
    # Sum all amounts?
    # Or count the project once?
    # "How many projects" -> count of unique projects (based on name).
    # "Total funding" -> sum of amounts for these projects.
    count += 1
    for r in records:
        total_funding += int(r['Amount'])
        matched_records.append(r)

print("__RESULT__:")
print(json.dumps({"count": count, "total_funding": total_funding, "projects": list(found_projects)}))"""

env_args = {'var_function-call-3253055519445541233': 'file_storage/function-call-3253055519445541233.json', 'var_function-call-14502065749304076563': ['Funding'], 'var_function-call-12281122830220394756': 'file_storage/function-call-12281122830220394756.json'}

exec(code, env_args)
