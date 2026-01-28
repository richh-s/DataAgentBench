code = """import json

# Load the complete dataset paths
funding_path = locals()['var_functions.execute_python:2']
civic_path = locals()['var_functions.query_db:8']

# Read funding data  
with open(funding_path, 'r') as f:
    funding_all = json.load(f)

# Read civic documents
with open(civic_path, 'r') as f:
    civic_all = json.load(f)

# Create sets for matching
capital_design_projects = set()
funding_projects_over_50k = set()

# Build funding set for projects > $50,000
for item in funding_all:
    if int(item['Amount']) > 50000:
        funding_projects_over_50k.add(item['Project_Name'].strip())

# Extract capital design projects from civic documents
for doc in civic_all:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Split by sections to find capital design areas
    sections = text.split('\n\n')
    in_design_section = False
    
    for section in sections:
        if 'Capital Improvement Projects' in section and 'Design' in section:
            # Found a design section, now extract project names
            lines = section.split('\n')
            for line in lines:
                line = line.strip()
                if not line or len(line) < 6:
                    continue
                
                # Skip lines that are obviously not project names
                if any(keyword in line for keyword in ['Updates:', 'Schedule:', 'Page', 'Agenda', 'RECOMMENDED', 'DISCUSSION']):
                    continue
                if line.startswith('Staff') or line.startswith('City') or line.startswith('('):
                    continue
                if 'Spring' in line or 'Summer' in line or 'Fall' in line or 'Winter' in line:
                    continue
                if 'COMPLETE DESIGN' in line.upper() or 'Advertise' in line:
                    continue
                
                # Add the project name (remove parenthetical suffixes for matching)
                base_name = line.split('(')[0].strip()
                if len(base_name) > 5:
                    capital_design_projects.add(base_name)

# Match the projects
count = 0
for design_project in capital_design_projects:
    for funding_project in funding_projects_over_50k:
        # Exact match or design project is prefix of funding project
        if design_project == funding_project or funding_project.startswith(design_project + ' '):
            count += 1
            break

print('__RESULT__:')
print(count)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:82': [{'count': '276'}], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:96': 7}

exec(code, env_args)
