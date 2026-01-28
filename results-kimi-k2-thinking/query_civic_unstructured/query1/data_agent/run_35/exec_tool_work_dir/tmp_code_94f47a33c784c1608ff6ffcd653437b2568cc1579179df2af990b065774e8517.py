code = """import json
import re

# Read the civic documents data
with open('var_functions.query_db:0', 'r') as f:
    civic_docs_data = json.load(f)

# Read the funding data  
with open('var_functions.query_db:1', 'r') as f:
    funding_data = json.load(f)

# Process civic documents to extract project information
projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    
    # Find design section - use single quotes for regex to avoid escaping issues
    design_section_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Disaster Recovery Projects|Capital Improvement Projects \(Not Started\)|$)', 
                                    text, re.DOTALL | re.IGNORECASE)
    
    if design_section_match:
        design_section = design_section_match.group(1)
        
        # Extract project names (lines that are likely project titles)
        section_lines = design_section.split('\n')
        
        for line in section_lines:
            line = line.strip()
            
            # Skip empty lines, bullets, and obvious non-project lines
            skip_patterns = [
                '•', '(', 'Page', 'cid:', 'Updates:', 'Schedule:', 
                'Project Schedule:', 'Estimated Schedule:', 'Project Description:',
                'Capital Improvement Projects', 'Disaster Recovery Projects',
                'Recommended Action', 'DISCUSSION:', 'Subject:', 'To:',
                'From:', 'Date', 'Prepared by', 'Approved by'
            ]
            
            should_skip = False
            for pattern in skip_patterns:
                if pattern in line:
                    should_skip = True
                    break
                    
            if should_skip or not line or len(line) < 10:
                continue
                
            if line.isupper() and len(line) < 50:
                continue  # Skip headers
                
            # Clean up the line to get project name
            project_name = line.strip()
            
            # Remove trailing colons 
            if project_name.endswith(':'):
                project_name = project_name[:-1].strip()
                
            # Skip if it's just common phrases
            lower_name = project_name.lower()
            if lower_name in ['updates', 'project schedule', 'estimated schedule', 
                            'recommended action', 'project description', 'discussion',
                            'public works', 'commission', 'subject']:
                continue
                
            # Add if it's a reasonable length and looks like a project name
            if 8 < len(project_name) < 150 and project_name[0].isalnum():
                projects.append({
                    'Project_Name': project_name,
                    'status': 'design',
                    'type': 'capital'
                })

# Remove duplicates based on project name
seen = set()
unique_projects = []
for p in projects:
    name = p['Project_Name']
    if name not in seen:
        seen.add(name)
        unique_projects.append(p)

projects = unique_projects

# Convert funding data to dict for lookup
funding_dict = {}
for item in funding_data:
    try:
        funding_dict[item['Project_Name']] = int(item['Amount'])
    except (ValueError, TypeError):
        continue

# Find projects with funding > $50,000 that are capital design projects
capital_design_projects = []
for project in projects:
    proj_name = project['Project_Name']
    
    # Check if this project has funding > 50000
    if proj_name in funding_dict and funding_dict[proj_name] > 50000:
        capital_design_projects.append({
            'Project_Name': proj_name,
            'Funding': funding_dict[proj_name],
            'Status': project['status'],
            'Type': project['type']
        })

# Count the results
count = len(capital_design_projects)

print('__RESULT__:')
print(json.dumps({
    'count': count,
    'total_projects_found': len(projects),
    'sample_projects': capital_design_projects[:5] if capital_design_projects else []
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
