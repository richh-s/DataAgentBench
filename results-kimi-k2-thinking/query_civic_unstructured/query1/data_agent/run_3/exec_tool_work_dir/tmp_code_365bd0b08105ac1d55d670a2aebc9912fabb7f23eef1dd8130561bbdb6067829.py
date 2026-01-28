code = """import json
import re
from collections import defaultdict

# Access the variables containing file paths
funding_data_file = locals()['var_functions.query_db:2']
civic_docs_file = locals()['var_functions.query_db:5']

# Read the funding data from the file
with open(funding_data_file, 'r') as f:
    funding_data = json.load(f)

# Read the civic documents data from the file
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Extract projects from civic documents with their status, type, and other details
projects_info = {}

def extract_topics(project_name):
    """Extract topics from project name based on keywords"""
    topics = []
    name_lower = project_name.lower()
    
    if 'park' in name_lower:
        topics.append('park')
    if any(word in name_lower for word in ['road', 'street', 'avenue', 'drive', 'highway']):
        topics.append('road')
    if 'drain' in name_lower or 'storm' in name_lower:
        topics.append('drainage')
    if 'bridge' in name_lower:
        topics.append('bridge')
    if 'playground' in name_lower:
        topics.append('playground')
    if 'fema' in name_lower:
        topics.append('FEMA')
    if 'warning' in name_lower or 'siren' in name_lower:
        topics.append('emergency warning')
    if 'water' in name_lower:
        topics.append('water treatment')
    if 'guardrail' in name_lower:
        topics.append('guardrail')
    if 'median' in name_lower:
        topics.append('median')
    if 'crosswalk' in name_lower:
        topics.append('crosswalk')
    
    return ','.join(topics) if topics else 'general infrastructure'

# Process each document to find capital projects with design status
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for "Capital Improvement Projects (Design)" section
    design_section_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?=\n\n[A-Z]|$)', text, re.DOTALL)
    
    if design_section_match:
        design_section = design_section_match.group(1)
        
        # Extract project names - they appear as bolded titles or standalone lines
        # Look for lines that are project names followed by bullet points
        lines = design_section.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if (line and 
                len(line) > 5 and 
                not line.startswith('\u2022') and 
                not line.startswith('-') and 
                ':' not in line and 
                'Updates' not in line and 
                'Project Schedule' not in line and
                'Complete Design' not in line and
                'Advertise' not in line and
                'Begin Construction' not in line):
                
                # Check if next lines contain project indicators
                if i + 1 < len(lines) and ('Updates' in lines[i+1] or '\u2022' in lines[i+1]):
                    projects_info[line] = {
                        'type': 'capital',
                        'status': 'design',
                        'topic': extract_topics(line)
                    }

    # Also look for projects that have "design" context
    # Find project patterns like "Project Name\n\u2022 Updates:"
    project_patterns = re.findall(r'\n([A-Z][a-zA-Z\s&\-\/]+?)\n\s*[\u2022\-]\s*(?:Updates?|Status|Project Schedule):', text)
    
    for project_name in project_patterns:
        project_name = project_name.strip()
        if (project_name and len(project_name) > 10 and 
            'Capital Improvement' not in project_name and
            'Disaster Recovery' not in project_name):
            
            # Check surrounding context for design status
            idx = text.find(project_name)
            if idx > 0:
                context = text[max(0, idx-200):idx+200]
                if 'design' in context.lower() or 'Design' in context:
                    projects_info[project_name] = {
                        'type': 'capital',
                        'status': 'design',
                        'topic': extract_topics(project_name)
                    }

# Filter projects that are actually capital projects based on topics/content
capital_design_projects = {}
for name, info in projects_info.items():
    # Ensure it's a capital project (not disaster/FEMA focused)
    if 'fema' not in name.lower() and 'disaster' not in name.lower():
        capital_design_projects[name] = info

# Now match with funding data
matches = []

for funding_record in funding_data:
    project_name = funding_record['Project_Name']
    amount = int(funding_record['Amount'])
    
    # Skip if amount <= 50000
    if amount <= 50000:
        continue
    
    # Check exact match
    if project_name in capital_design_projects:
        project_info = capital_design_projects[project_name]
        matches.append({
            'project_name': project_name,
            'amount': amount,
            'funding_source': funding_record['Funding_Source'],
            'topics': project_info['topic']
        })
    else:
        # Check for base name match (remove suffixes like (CalOES Project))
        base_name = re.sub(r'\s*\([^)]*\)$', '', project_name)
        if base_name in capital_design_projects:
            project_info = capital_design_projects[base_name]
            matches.append({
                'project_name': project_name,
                'base_name': base_name,
                'amount': amount,
                'funding_source': funding_record['Funding_Source'],
                'topics': project_info['topic']
            })

# Get unique projects by base name
unique_projects = {}
for match in matches:
    # Use base_name if available, otherwise use full project_name
    key = match.get('base_name', match['project_name'])
    if key not in unique_projects:
        unique_projects[key] = match

# Count the result
count = len(unique_projects)

# Build result
result = {
    'count': count,
    'projects': list(unique_projects.values())
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
