code = """import json

# Load funding data
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Create funding lookup for projects > $50,000
funding_lookup = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_lookup[item['Project_Name'].strip()] = amount

# Extract capital design projects using simple heuristics
# Look for lines that appear to be project names in design sections
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Check if we are entering a capital design section
        if 'Capital Improvement Projects' in line and 'Design' in line:
            in_design_section = True
            continue
        
        # Check if we are leaving the design section (next major section)
        if in_design_section and (line.startswith('Capital') and ('Construction' in line or 'Not Started' in line)):
            in_design_section = False
            continue
        if in_design_section and line.startswith('DISASTER'):
            in_design_section = False
            continue
        
        # Extract project names
        if in_design_section and len(line) > 5 and len(line) < 150:
            # Skip lines with metadata keywords
            skip = False
            metadata_terms = ['Updates:', 'Schedule:', 'Page', 'Agenda', 'RECOMMENDED', 'DISCUSSION', 'Staff', 'City', 'Spring', 'Summer', 'Fall', 'Winter', 'Complete Design', 'cid:', 'Complete Design', 'Advertise']
            for term in metadata_terms:
                if term in line:
                    skip = True
                    break
            
            if not skip and not line.startswith('(') and 'COMPLETE DESIGN' not in line.upper():
                # Clean the name (remove parenthetical suffixes)
                parts = line.split('(')
                clean_name = parts[0].strip()
                if clean_name and len(clean_name) > 5:
                    design_projects.add(clean_name)

# Match design projects with funding
matched_count = 0
for design_name in design_projects:
    # Try to match with funding data
    for fund_name in funding_lookup.keys():
        if design_name == fund_name:
            matched_count += 1
            break
        elif fund_name.startswith(design_name + ' '):
            matched_count += 1
            break
        elif fund_name.startswith(design_name + '('):
            matched_count += 1
            break

result = str(matched_count)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
