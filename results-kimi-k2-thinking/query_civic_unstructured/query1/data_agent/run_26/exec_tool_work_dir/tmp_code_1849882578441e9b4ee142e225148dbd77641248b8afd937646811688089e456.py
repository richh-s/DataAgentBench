code = """import json

# Load funding data (projects > $50,000)
with open('var_functions.query_db:0', 'r') as f:
    funding_data = json.load(f)

# Create a dictionary mapping lowercased project names to funding amounts
funded_amounts = {}
for record in funding_data:
    proj_name = record['Project_Name'].strip().lower()
    funded_amounts[proj_name] = int(record['Amount'])

# Load civic documents data
with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

# Parse documents to find capital projects with design status
# Look for "Capital Improvement Projects (Design)" section
import re

design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the design section
    design_section = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Disaster Recovery Projects|DISASTER RECOVERY PROJECTS)', 
                              text, re.DOTALL | re.IGNORECASE)
    
    if design_section:
        section_text = design_section.group(1)
        lines = section_text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            if line and len(line) > 5:
                # Check if this is a project name (followed by updates/schedule in next lines)
                next_lines = '\n'.join(lines[i+1:i+4])
                if 'Updates:' in next_lines or 'Project Schedule:' in next_lines or 'Estimated Schedule:' in next_lines:
                    # Skip control lines and metadata
                    if not any(skip in line for skip in ['Capital Improvement', 'Page', 'Item', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:', '(cid:', '▪', '•']):
                        design_projects.append(line)

# Count projects with funding > 50000
count = 0
for project in design_projects:
    proj_lower = project.lower()
    
    # Direct match
    if proj_lower in funded_amounts and funded_amounts[proj_lower] > 50000:
        count += 1
    else:
        # Partial match check
        for funded_name, amount in funded_amounts.items():
            if (proj_lower in funded_name or funded_name in proj_lower) and amount > 50000:
                count += 1
                break

print('__RESULT__:')
print(json.dumps({
    'total_design_projects': len(design_projects),
    'count_over_50000': count
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}}

exec(code, env_args)
