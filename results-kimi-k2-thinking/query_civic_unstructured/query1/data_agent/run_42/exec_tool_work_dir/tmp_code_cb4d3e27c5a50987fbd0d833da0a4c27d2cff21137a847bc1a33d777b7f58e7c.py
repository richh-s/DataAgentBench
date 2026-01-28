code = """import json

funding_path = var_functions.query_db_6
mongo_path = var_functions.query_db_2

# Load funding data
funding_records = []
with open(funding_path) as f:
    funding_records = json.load(f)

# Load mongo data
mongo_data = []
with open(mongo_path) as f:
    mongo_data = json.load(f)

# Get projects with funding > 50000
funding_projects = {}
for f in funding_records:
    if f["Amount"] > 50000:
        funding_projects[f["Project_Name"]] = f

# Extract design status projects from mongo
projects_in_design = []
for doc in mongo_data:
    text = doc.get("text", "")
    lines = text.split("\n")
    in_design_section = False
    
    for line in lines:
        clean_line = line.strip()
        if "Capital Improvement Projects (Design)" in clean_line:
            in_design_section = True
        elif "Capital Improvement Projects (Construction)" in clean_line or "Capital Improvement Projects (Not Started)" in clean_line:
            in_design_section = False
        elif in_design_section and clean_line and not clean_line.startswith("(") and not clean_line.startswith("•"):
            # Filter out non-project lines
            skip_terms = ["Updates:", "Schedule:", "To:", "Subject:", "Page", "Prepared by:", "Approved by:", "Date prepared:", "RECOMMENDED ACTION", "DISCUSSION", "Consultant", "Staff is", "Staff will", "City is", "City will", "Project is", "Plans are", "Bids are"]
            should_skip = any(term in clean_line for term in skip_terms)
            if not should_skip and len(clean_line) > 5 and not clean_line.isupper():
                projects_in_design.append(clean_line)

# Find matches
matches = []
for design_proj in projects_in_design:
    for funding_name in funding_projects:
        if funding_name.lower() in design_proj.lower() or design_proj.lower() in funding_name.lower():
            matches.append(funding_name)
            break

result = len(matches)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
