code = """import json

# Load the funding data
funding_file = open('var_functions.query_db:0', 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Load the civic documents
civic_file = open('var_functions.query_db:2', 'r')
civic_docs = json.load(civic_file)
civic_file.close()

# Create a dictionary of funded projects (lowercase name -> amount)
funded_projects = {}
for record in funding_data:
    project_name = record['Project_Name'].strip().lower()
    funded_projects[project_name] = int(record['Amount'])

# Extract capital projects with design status from civic documents
design_capital_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start != -1:
        design_end = text.find('Capital Improvement Projects (Construction)', design_start)
        if design_end == -1:
            design_end = len(text)
        
        design_section = text[design_start:design_end]
        lines = design_section.split('\n')
        
        # Extract project names (lines that are likely project names)
        for i in range(len(lines)):
            line = lines[i].strip()
            if line and len(line) > 5:
                # Skip control lines and metadata
                if '▪' not in line and 'Updates:' not in line and 'Project Schedule:' not in line:
                    if 'Capital Improvement Projects' not in line and 'Page' not in line:
                        if 'RECOMMENDED ACTION:' not in line and 'DISCUSSION:' not in line:
                            # Check if followed by project details
                            if i + 1 < len(lines):
                                next_line = lines[i+1].strip()
                                if 'Updates:' in next_line or 'Project Schedule:' in next_line or 'Estimated Schedule:' in next_line:
                                    design_capital_projects.append(line.lower())

# Count projects with funding greater than $50,000
unique_design_projects = list(set(design_capital_projects))
count_over_50000 = 0

for project in unique_design_projects:
    if project in funded_projects and funded_projects[project] > 50000:
        count_over_50000 += 1

print('__RESULT__:')
print(json.dumps(count_over_50000))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:54': 0, 'var_functions.execute_python:72': {'funding': 'var_functions.query_db:0', 'civic': 'var_functions.query_db:2'}}

exec(code, env_args)
