code = """import json
import pandas as pd
import re

# Load funding data
with open(locals()['var_function-call-8904296491751843034'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Load civic docs
with open(locals()['var_function-call-8494922430906473506'], 'r') as f:
    civic_docs = json.load(f)

# Helper to identify spring 2022
def is_spring_2022(date_str):
    if not date_str:
        return False
    date_str = date_str.lower().strip()
    
    # Explicit "Spring 2022"
    if "spring 2022" in date_str or "spring, 2022" in date_str or "2022-spring" in date_str:
        return True
    
    # Check for months in 2022
    # Spring = March, April, May
    if "2022" in date_str:
        if "march" in date_str or "april" in date_str or "may" in date_str:
            return True
            
    return False

# Extraction logic
target_projects = set()

# Clean up lines function
def clean_line(line):
    return line.strip()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    buffer_line = None # Potential project name
    
    for line in lines:
        line = clean_line(line)
        if not line:
            continue
            
        # Skip headers/footers
        if line.lower().startswith("page ") or "agenda item" in line.lower():
            continue
        
        # Check for section start
        # The preview shows markers like (cid:190).
        # We also see bullets like (cid:131).
        
        is_update_header = "(cid:190)" in line or "\uf0be" in line or line.startswith("¾")
        
        if is_update_header:
            # The previous buffer_line was likely the project name
            if buffer_line:
                current_project = buffer_line
                # Clean up project name (sometimes it has noise)
                # print(f"Found Project: {current_project}")
            
        # Check for start date
        if current_project:
            # Heuristics for Start Date
            # "Begin Construction: <Date>"
            # "Begin construction: <Date>"
            if "begin construction" in line.lower():
                # Extract value
                parts = line.split(":", 1)
                if len(parts) > 1:
                    val = parts[1].strip()
                    if is_spring_2022(val):
                        target_projects.add(current_project)
                        # print(f"MATCH: {current_project} starts {val}")
                else:
                    # Maybe date is on next line? Handled by simple logic for now.
                    pass
        
        # Update buffer line if it's not a bullet/marker line
        if not is_update_header and not line.startswith("(cid:131)") and not line.startswith("¾"):
             buffer_line = line

# Filter funding
# We need to match names. The names in text might be slightly different or exact.
# Let's try exact match first, then fuzzy or containment.
# The funding table has "Project_Name".

# Let's print matched projects to debug
print("Matched Projects from Text:")
for p in target_projects:
    print(p)

matched_funding = []
total_funding = 0

# Convert target_projects to list for easier checking
target_list = list(target_projects)

for index, row in funding_df.iterrows():
    f_name = row['Project_Name']
    # Check if f_name is in our identified list
    # Use simple normalization
    
    # Try exact match or if one is substring of other (with caution)
    # The text extraction might preserve "2022 Morning View..." while funding has "2022 Morning View..."
    
    found = False
    for p in target_list:
        if p.lower() in f_name.lower() or f_name.lower() in p.lower():
            # Check length ratio to avoid matching "Road" to "Road Repair" incorrectly if names are short
            # But usually names are distinct enough.
            found = True
            break
    
    if found:
        matched_funding.append(row)
        total_funding += row['Amount']

print(f"\nTotal Funding: {total_funding}")
print(f"Number of projects (funding table matches): {len(matched_funding)}")

# We should answer "How many projects" (unique projects) and "Total funding".
# The query asks "How many projects started in Spring 2022".
# This refers to the projects identified in the docs.
# So count of unique projects in `target_projects` is the first answer (conceptually).
# But the funding total is for those projects.
# If a project is in docs but not in funding, it counts as a project but 0 funding?
# Or only projects that have funding?
# Usually "How many projects... and what is their total funding" implies the count of identified projects.
# But if I can't find funding for them, maybe I should mention that.
# However, the prompt says "The Project_Name in the Funding SQLite table matches the project names that can be extracted".
# So likely 1-to-1 match.

# Let's print the result JSON
result = {
    "num_projects": len(target_projects),
    "total_funding": total_funding,
    "projects": list(target_projects)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-1649366549132259120': 'file_storage/function-call-1649366549132259120.json', 'var_function-call-17157926342599850647': 'file_storage/function-call-17157926342599850647.json', 'var_function-call-8904296491751843034': 'file_storage/function-call-8904296491751843034.json', 'var_function-call-8494922430906473506': 'file_storage/function-call-8494922430906473506.json'}

exec(code, env_args)
