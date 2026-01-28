code = """import json
import re

# Load funding data
with open(locals()['var_function-call-14384747128822080394'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-12725139888695263289'], 'r') as f:
    civic_docs = json.load(f)

# Set of all project names in funding db for validation/matching
funding_map = {item['Project_Name'].strip(): item['Amount'] for item in funding_data}

extracted_projects = []

# Regex for bullets or weird chars
# (cid:190) is \u00be (3/4 fraction), (cid:131) is \u0192 (function symbol) - strictly speaking these are mapping artifacts.
# In the text preview they appear as strings "(cid:190)" and "(cid:131)".
# So I should check for lines starting with these strings.

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    in_target_section = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check for section headers
        if "Capital Improvement Projects (Design)" in line:
            in_target_section = True
            continue
        
        if "Capital Improvement Projects" in line and "(Design)" not in line:
            # Entering another Capital section (Construction, Not Started)
            in_target_section = False
        
        if "Disaster Recovery Projects" in line:
            in_target_section = False
            
        if in_target_section:
            # filter out noise
            if line.startswith("(cid:190)") or line.startswith("(cid:131)"):
                continue
            if line.startswith("Updates:") or line.startswith("Project Schedule:") or line.startswith("Estimated Schedule:"):
                continue
            if "Page" in line and "of" in line:
                continue
            if "Agenda Item" in line:
                continue
            if line.lower().startswith("complete design") or line.lower().startswith("begin construction") or line.lower().startswith("advertise"):
                continue
            
            # Additional heuristic: Project names usually don't end with ":"
            if line.endswith(":"):
                continue

            # It seems the lines that remain are project names.
            # However, some noise might persist.
            # Let's check if the line is a known project in funding_map (exact match)
            # or if it looks like a name.
            
            # Also, sometimes the text has "2022 Morning View..."
            # The DB might have "Morning View..."?
            # Let's collect potential names.
            extracted_projects.append(line)

# Now filter and count
capital_design_projects = []
for proj in extracted_projects:
    # Try exact match
    if proj in funding_map:
        capital_design_projects.append(proj)
    else:
        # Try fuzzy or clean up?
        # Maybe the year prefix?
        # "2022 Morning View Resurfacing & Storm Drain Improvements"
        # Let's check if there's a match without the year?
        pass

# Check amounts
count = 0
matches = []

for proj in set(capital_design_projects): # Use set to avoid duplicates if multiple docs
    amount = float(funding_map[proj])
    if amount > 50000:
        count += 1
        matches.append((proj, amount))

print("__RESULT__:")
print(json.dumps({"count": count, "matches": matches, "extracted_candidates": extracted_projects}))"""

env_args = {'var_function-call-14384747128822080394': 'file_storage/function-call-14384747128822080394.json', 'var_function-call-12725139888695263289': 'file_storage/function-call-12725139888695263289.json'}

exec(code, env_args)
