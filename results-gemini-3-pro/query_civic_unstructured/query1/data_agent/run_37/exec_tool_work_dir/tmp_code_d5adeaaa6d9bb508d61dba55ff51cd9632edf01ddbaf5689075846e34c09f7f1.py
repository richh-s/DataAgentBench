code = """import json

# Load Funding Data
with open('var_function-call-2838577088197188033.json', 'r') as f:
    funding_data = json.load(f)

high_funding_projects = {}
for entry in funding_data:
    name = entry['Project_Name'].strip()
    high_funding_projects[name.lower()] = name

# Load Civic Docs Data
with open('var_function-call-11182446621266237343.json', 'r') as f:
    civic_docs = json.load(f)

doc_text = civic_docs[0]['text']
lines = doc_text.split('\n')

# Section Headers
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
    
    # Stop if we hit the next section
    if construction_header in clean_line or not_started_header in clean_line:
        in_design = False
        break
        
    if in_design:
        # Filter out junk
        # Junk starts with special chars or keywords
        lower_line = clean_line.lower()
        if clean_line.startswith("(cid:") or \
           clean_line.startswith("Updates:") or \
           clean_line.startswith("Project Schedule:") or \
           clean_line.startswith("Page ") or \
           clean_line.startswith("Agenda Item") or \
           lower_line.startswith("prepared by") or \
           lower_line.startswith("approved by") or \
           lower_line.startswith("date prepared") or \
           lower_line.startswith("estimated schedule"):
             continue
        
        # Additional filtering based on content
        if "Complete Design" in clean_line or "Advertise" in clean_line or "Begin Construction" in clean_line:
            continue
            
        extracted_names.append(clean_line)

# Match against Funding DB
matches = set()
unmatched = []

for name in extracted_names:
    name_lower = name.lower()
    found = False
    
    # Check against all high funding projects
    for db_name_lower, db_name_original in high_funding_projects.items():
        # Exact or Substring match
        # We need to be careful with short strings, but project names are usually distinct
        if name_lower == db_name_lower or \
           name_lower in db_name_lower or \
           db_name_lower in name_lower:
            matches.add(db_name_original)
            found = True
            # Don't break immediately if we want to find the *best* match, but here any match > 50k is sufficient to count the *project*?
            # Actually, the question asks "How many capital projects...".
            # If "Project A" matches "Project A (FEMA)", it counts as 1.
            break
    
    if not found:
        unmatched.append(name)

print("__RESULT__:")
print(json.dumps({"count": len(matches), "matches": list(matches), "unmatched": unmatched, "extracted": extracted_names}))"""

env_args = {'var_function-call-2838577088197188033': 'file_storage/function-call-2838577088197188033.json', 'var_function-call-2838577088197188526': 'file_storage/function-call-2838577088197188526.json', 'var_function-call-7878716980368608955': ['civic_docs'], 'var_function-call-11182446621266237343': 'file_storage/function-call-11182446621266237343.json'}

exec(code, env_args)
