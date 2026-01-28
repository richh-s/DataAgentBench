code = """import json
import re

# Load the data from the stored files
funding_file = var_functions.query_db:0
civic_file = var_functions.query_db:1

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs_data = json.load(f)

# Create lookup for funding amounts
funding_dict = {}
for item in funding_data:
    funding_dict[item['Project_Name']] = int(item['Amount'])

# Initialize list to track projects
projects_with_design_status = []

# Process each civic document
for doc in civic_docs_data:
    if 'text' not in doc:
        continue
        
    text = doc['text']
    
    # Look for the Capital Improvement Projects (Design) section
    if 'Capital Improvement Projects (Design)' in text:
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            design_section = parts[1].split('\n\n')[0]
            
            # Find all project names in this section
            # Project names are typically followed by bullet points or specific markers
            lines = design_section.split('\n')
            for line in lines:
                line = line.strip()
                # Look for lines that might be project names (not bullet points)
                if (line and len(line) > 5 and not line.startswith('(') and 
                    not line.startswith('-') and 'Updates' not in line and 
                    'Schedule' not in line and ':' not in line and
                    line == line.strip()):
                    
                    # Check if this matches a funded project
                    if line in funding_dict and funding_dict[line] > 50000:
                        projects_with_design_status.append({
                            'Project_Name': line,
                            'Amount': funding_dict[line]
                        })

# Remove duplicates
unique_projects = {}
for proj in projects_with_design_status:
    unique_projects[proj['Project_Name']] = proj

result_json = json.dumps({
    'count': len(unique_projects),
    'projects': list(unique_projects.keys())
})

print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
