code = """import json

with open('var_function-call-2838577088197188033.json', 'r') as f:
    funding_data = json.load(f)

high_funding_projects = {}
for entry in funding_data:
    name = entry['Project_Name'].strip()
    high_funding_projects[name.lower()] = name

with open('var_function-call-11182446621266237343.json', 'r') as f:
    civic_docs = json.load(f)

doc_text = civic_docs[0]['text']
lines = doc_text.split('\n')

design_header = "Capital Improvement Projects (Design)"
construction_header = "Capital Improvement Projects (Construction)"
not_started_header = "Capital Improvement Projects (Not Started)"

in_design = False
extracted_names = []

for line in lines:
    clean_line = line.strip()
    if not clean_line:
        continue
        
    if design_header in clean_line:
        in_design = True
        continue
    
    if construction_header in clean_line:
        in_design = False
        break
    if not_started_header in clean_line:
        in_design = False
        break
        
    if in_design:
        lower_line = clean_line.lower()
        # Bad prefixes
        if clean_line.startswith("(cid:"): continue
        if clean_line.startswith("Updates:"): continue
        if clean_line.startswith("Project Schedule:"): continue
        if clean_line.startswith("Page "): continue
        if clean_line.startswith("Agenda Item"): continue
        if lower_line.startswith("prepared by"): continue
        if lower_line.startswith("approved by"): continue
        if lower_line.startswith("date prepared"): continue
        if lower_line.startswith("estimated schedule"): continue
        
        # Content checks
        if "Complete Design" in clean_line: continue
        if "Advertise" in clean_line: continue
        if "Begin Construction" in clean_line: continue
        
        extracted_names.append(clean_line)

matches = set()
unmatched = []

for name in extracted_names:
    name_lower = name.lower()
    found = False
    
    for db_name_lower, db_name_original in high_funding_projects.items():
        if name_lower == db_name_lower or name_lower in db_name_lower or db_name_lower in name_lower:
            matches.add(db_name_original)
            found = True
            break
    
    if not found:
        unmatched.append(name)

print("__RESULT__:")
print(json.dumps({"count": len(matches), "matches": list(matches), "unmatched": unmatched, "extracted": extracted_names}))"""

env_args = {'var_function-call-2838577088197188033': 'file_storage/function-call-2838577088197188033.json', 'var_function-call-2838577088197188526': 'file_storage/function-call-2838577088197188526.json', 'var_function-call-7878716980368608955': ['civic_docs'], 'var_function-call-11182446621266237343': 'file_storage/function-call-11182446621266237343.json'}

exec(code, env_args)
