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
    
    # Find sections for design projects
    if 'Capital Improvement Projects' in text and 'Design' in text:
        lines = text.split('\n')
        in_design_section = False
        
        for i, line in enumerate(lines):
            line_clean = line.strip()
            
            # Check if we're entering the design section
            if 'Capital Improvement Projects' in line_clean and 'Design' in line_clean:
                in_design_section = True
                continue
                
            # Check if we're leaving the design section
            if in_design_section and ('Capital Improvement Projects' in line_clean and 'Construction' in line_clean):
                break
            if in_design_section and ('Capital Improvement Projects' in line_clean and 'Not Started' in line_clean):
                break
            if in_design_section and 'Disaster Recovery Projects' in line_clean:
                break
                
            # Extract project names within design section
            if in_design_section and line_clean:
                # Skip section headers, bullet points, and update/schedule lines
                if not line_clean.startswith('(') and not line_clean.startswith('•') and not line_clean.startswith('▪') \
                   and 'Updates:' not in line_clean and 'Project Schedule:' not in line_clean \
                   and 'Estimated Schedule:' not in line_clean and 'Project Description:' not in line_clean \
                   and 'RECOMMENDED ACTION:' not in line_clean and 'DISCUSSION:' not in line_clean \
                   and not any(keyword in line_clean for keyword in ['Complete Design:', 'Advertise:', 'Begin Construction:', 'Final Design:', 'Page']):
                    
                    # Check if next line contains project updates/schedule
                    if i + 1 < len(lines):
                        next_line = lines[i + 1].strip()
                        if 'Updates:' in next_line or 'Project Schedule:' in next_line or 'Estimated Schedule:' in next_line:
                            if len(line_clean) > 5:  # Filter out short irrelevant lines
                                design_capital_projects.append({
                                    'project_name': line_clean,
                                    'type': 'capital',
                                    'status': 'design'
                                })

# Now match design capital projects with funded projects > $50,000
matched_projects = []
for project in design_capital_projects:
    proj_name_lower = project['project_name'].lower()
    
    # Direct match
    if proj_name_lower in funded_projects:
        matched_projects.append({
            'project_name': project['project_name'],
            'funding': funded_projects[proj_name_lower]['amount']
        })
    else:
        # Fuzzy match - check if any funded project contains this name or vice versa
        for funded_name_lower, funded_info in funded_projects.items():
            # Check for substring match with length difference constraint
            if (proj_name_lower in funded_name_lower or funded_name_lower in proj_name_lower):
                if abs(len(proj_name_lower) - len(funded_name_lower)) < 25:
                    matched_projects.append({
                        'project_name': project['project_name'],
                        'funded_as': funded_info['original_name'],
                        'funding': funded_info['amount']
                    })
                    break

count_over_50000 = sum(1 for p in matched_projects if p['funding'] > 50000)

print('__RESULT__:')
print(json.dumps({
    'total_design_capital_projects': len(design_capital_projects),
    'matched_funded_projects': len(matched_projects),
    'count_over_50000': count_over_50000,
    'projects': [p for p in matched_projects if p['funding'] > 50000]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}}

exec(code, env_args)
