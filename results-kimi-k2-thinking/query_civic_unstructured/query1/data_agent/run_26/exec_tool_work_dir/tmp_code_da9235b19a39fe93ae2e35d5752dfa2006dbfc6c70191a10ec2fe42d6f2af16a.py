code = """import json

# Load data using the stored file paths
funding_file = var_functions.query_db:0
civic_file = var_functions.query_db:2

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding lookup dictionary
funding_lookup = {}
for record in funding_data:
    project_name = record['Project_Name'].strip().lower()
    funding_lookup[project_name] = int(record['Amount'])

# Extract capital projects with design status from civic documents
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    if 'Capital Improvement Projects (Design)' in text:
        start_pos = text.find('Capital Improvement Projects (Design)')
        end_pos = text.find('Capital Improvement Projects (Construction)', start_pos)
        if end_pos == -1:
            end_pos = len(text)
        
        design_section = text[start_pos:end_pos]
        lines = [line.strip() for line in design_section.split('\n') if line.strip()]
        
        # Extract project names (lines followed by project details)
        for i in range(len(lines)):
            line = lines[i]
            if line and len(line) > 5:
                # Skip metadata and control lines
                if '▪' not in line and 'Updates:' not in line and 'Project Schedule:' not in line:
                    if 'Capital Improvement' not in line and 'Page' not in line and 'RECOMMENDED' not in line:
                        # Check if followed by project updates/schedule
                        if i + 1 < len(lines) and ('Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1]):
                            design_projects.append(line.lower())

# Count unique projects with funding > $50,000
unique_design_projects = list(set(design_projects))
count_over_50000 = 0

for project in unique_design_projects:
    if project in funding_lookup and funding_lookup[project] > 50000:
        count_over_50000 += 1

print('__RESULT__:')
print(json.dumps(count_over_50000))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
