code = """import json

# Get file paths from storage variables
funding_path = var_functions.query_db:2
civic_path = var_functions.query_db:6

# Open and load funding data
funding_file = open(funding_path, 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Open and load civic documents
civic_file = open(civic_path, 'r')
civic_docs = json.load(civic_file)
civic_file.close()

# Create a dictionary of funding projects with amount > 50000
# Key: project name, Value: funding amount
funding_dict = {}
for record in funding_data:
    amount = float(record['Amount'])
    if amount > 50000:
        name = record['Project_Name']
        funding_dict[name] = amount
        
        # Also add a cleaned version without parenthetical suffixes
        # This handles cases like "Project Name (FEMA Project)"
        import re
        clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        if clean_name != name:
            funding_dict[clean_name] = amount

# Find capital design projects in civic documents
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    is_in_design_section = False
    
    for line in lines:
        line = line.strip()
        
        # Check if we're entering the design section
        if 'Capital Improvement Projects (Design)' in line:
            is_in_design_section = True
            continue
            
        # Check if we're leaving the design section  
        if 'Capital Improvement Projects (Construction)' in line:
            is_in_design_section = False
            continue
        
        # Process lines in the design section
        if is_in_design_section and line and len(line) > 15:
            # Skip disaster recovery projects
            if 'FEMA' in line or 'CalOES' in line or 'CalJPIA' in line or 'fire' in line:
                continue
            
            # Skip meta lines and headers
            if line.startswith('(') or 'Page' in line or 'Agenda' in line:
                continue
                
            if 'RECOMMENDED' in line.upper() or 'UPDATES:' in line.upper() or 'SCHEDULE:' in line.upper():
                continue
                
            if 'Capital Improvement Projects' in line:
                continue
            
            # Add to our list of capital design projects
            capital_design_projects.append(line)

# Count how many capital design projects have funding > 50000
count = 0

for project in capital_design_projects:
    # Check exact match first
    if project in funding_dict:
        count += 1
    else:
        # Check cleaned version
        import re
        clean_project = re.sub(r'\s*\([^)]*\)\s*$', '', project).strip()
        if clean_project in funding_dict:
            count += 1

# Return just the count
result = count
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
