code = """import json
import re

# Load funding data (projects > $50,000)
with open(var_functions.query_db:0, 'r') as f:
    funding_data = json.load(f)

# Create a dictionary of funded projects for easy lookup
funded_projects = {}
for record in funding_data:
    proj_name = record['Project_Name'].strip().lower()
    funded_projects[proj_name] = {
        'original_name': record['Project_Name'],
        'amount': int(record['Amount'])
    }

# Load civic documents
with open(var_functions.query_db:2, 'r') as f:
    civic_docs = json.load(f)

# Parse civic documents to extract capital projects with design status
design_capital_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for the design section more simply
    if 'Capital Improvement Projects' in text and 'Design' in text:
        # Extract lines that are likely project names
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line_clean = line.strip()
            # Skip lines that are too short or contain keywords
            if len(line_clean) > 10 and not any(skip in line_clean for skip in [
                'Capital Improvement', 'Disaster Recovery', 'Updates:', 'Project Schedule:', 
                'Estimated Schedule:', 'Project Description:', 'RECOMMENDED ACTION:', 
                'DISCUSSION:', 'Page', 'Item', 'To:', 'Prepared by:', 'Approved by:',
                'Date prepared:', 'Meeting date:', 'Subject:', '•', '▪', '(cid:'
            ]):
                # Check if this looks like a project name by checking nearby context
                if i + 1 < len(lines) and ('Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1]):
                    design_capital_projects.append({
                        'project_name': line_clean,
                        'type': 'capital',
                        'status': 'design'
                    })

# Match with funded projects
matched_projects = []
count_over_50000 = 0

for project in design_capital_projects:
    proj_name_lower = project['project_name'].lower()
    
    # Direct match
    if proj_name_lower in funded_projects:
        amount = funded_projects[proj_name_lower]['amount']
        if amount > 50000:
            count_over_50000 += 1
        matched_projects.append({
            'project_name': project['project_name'],
            'funding': amount
        })
    else:
        # Fuzzy match
        for funded_name_lower, funded_info in funded_projects.items():
            if proj_name_lower in funded_name_lower or funded_name_lower in proj_name_lower:
                amount = funded_info['amount']
                if amount > 50000:
                    count_over_50000 += 1
                matched_projects.append({
                    'project_name': project['project_name'],
                    'funded_as': funded_info['original_name'],
                    'funding': amount
                })
                break

print('__RESULT__:')
print(json.dumps({
    'design_capital_projects_count': len(design_capital_projects),
    'count_over_50000': count_over_50000
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}}

exec(code, env_args)
