code = """import json
import difflib

# Load data
with open(locals()['var_function-call-7721797773547696454'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_function-call-11187982915613525112'], 'r') as f:
    civic_docs = json.load(f)

# Funding > 50k
funded_projects = {}
for item in funding_data:
    try:
        amount = float(item['Amount'])
        if amount > 50000:
            funded_projects[item['Project_Name'].strip()] = amount
    except ValueError:
        pass

# Extract Design Lines
design_lines = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    in_design = False
    for line in lines:
        line = line.strip()
        if not line: continue
        if 'Capital Improvement Projects (Design)' in line:
            in_design = True
            continue
        if in_design:
            if 'Capital Improvement Projects' in line and '(Design)' not in line:
                in_design = False
            elif 'Disaster Recovery Projects' in line:
                in_design = False
        
        if in_design:
            # Filter junk
            if line.lower().startswith('page') or 'agenda item' in line.lower(): continue
            if any(x in line for x in ['Updates:', 'Schedule:', 'To:', 'From:', 'Subject:', 'Complete Design:', 'Advertise:', 'Construction:']): continue
            if not line[0].isalnum(): continue
            design_lines.append(line)

design_lines = list(set(design_lines))

# Match
matches = []
unmatched_lines = []
matched_funding_keys = set()

for line in design_lines:
    found = False
    # Exact
    if line in funded_projects:
        matches.append(line)
        matched_funding_keys.add(line)
        found = True
    else:
        # Check case-insensitive
        for fp in funded_projects:
            if fp.lower() == line.lower():
                matches.append(fp)
                matched_funding_keys.add(fp)
                found = True
                break
    
    if not found:
        unmatched_lines.append(line)

# Fuzzy check for unmatched
print("UNMATCHED LINES from Text:")
for l in unmatched_lines:
    print(f" - {l}")

print("\nUNMATCHED FUNDING (>50k):")
unmatched_funding = [k for k in funded_projects if k not in matched_funding_keys]
for k in unmatched_funding:
    print(f" - {k}")
    
print("\n__RESULT__:")
print(json.dumps({"matches_count": len(matches)}))"""

env_args = {'var_function-call-10821165667219444455': ['Funding'], 'var_function-call-10821165667219446426': ['civic_docs'], 'var_function-call-7721797773547696454': 'file_storage/function-call-7721797773547696454.json', 'var_function-call-7721797773547696997': 'file_storage/function-call-7721797773547696997.json', 'var_function-call-11187982915613525112': 'file_storage/function-call-11187982915613525112.json', 'var_function-call-6235686114409333614': {'count': 10, 'matches': ['Outdoor Warning Signs', 'Permanent Skate Park', 'Malibu Canyon Road Traffic Study', 'Westward Beach Road Drainage Improvements Project', 'PCH Median Improvements Project', 'Civic Center Stormwater Diversion Structure', 'Latigo Canyon Road Retaining Wall Repair Project', 'Malibu Bluffs Park South Walkway Repairs', 'Storm Drain Master Plan', 'PCH at Trancas Canyon Road Right Turn Lane']}}

exec(code, env_args)
