code = """import json
import re
from collections import defaultdict

# Read the funding data from the file
with open(var_functions.query_db:2, 'r') as f:
    funding_data = json.load(f)

# Read the civic documents data from the file
with open(var_functions.query_db:5, 'r') as f:
    civic_docs = json.load(f)

# Extract projects from civic documents with their status, type, and other details
# Projects are mentioned throughout the text with specific patterns
projects_info = {}

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project sections - capital projects with design status
    # Pattern 1: Projects under "Capital Improvement Projects (Design)" heading
    design_section_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)\n\n[A-Z]', text, re.DOTALL)
    
    if design_section_match:
        design_section = design_section_match.group(1)
        
        # Extract project names from this section - they appear as titles
        # Look for patterns like "PCH Median Improvements Project" followed by updates
        project_blocks = re.findall(r'\n([A-Z][a-zA-Z\s&\-]+?)(?=\n\(|\n\u2022|\n[A-Z][a-zA-Z\s&\-]+?:|\n\n)', design_section)
        
        for project_name in project_blocks:
            project_name = project_name.strip()
            if project_name and len(project_name) > 5 and 'Updates:' not in project_name and 'Project Schedule:' not in project_name:
                projects_info[project_name] = {
                    'type': 'capital',
                    'status': 'design',
                    'topic': extract_topics(project_name)
                }
    
    # Look for individual project mentions with status indicators
    # Pattern for project names followed by status info
    project_patterns = [
        r'([A-Z][a-zA-Z\s&\-]+?)(?=\s*\n\s*[\u2022\-]\s+(Updates|Project Schedule|Status):)',
        r'([A-Z][a-zA-Z\s&\-]+?)(?=\s*\n\s*\u2022)',
    ]
    
    for pattern in project_patterns:
        matches = re.finditer(pattern, text)
        for match in matches:
            project_name = match.group(1).strip()
            if (project_name and len(project_name) > 5 and 
                'Project' in project_name and 
                project_name not in ['Public Works', 'Capital Improvement', 'Disaster Recovery']):
                
                # Check if this project is in a design context
                context_start = max(0, match.start() - 200)
                context = text[context_start:match.end() + 200]
                
                if 'Design' in context or 'design' in context:
                    projects_info[project_name] = {
                        'type': 'capital',
                        'status': 'design',
                        'topic': extract_topics(project_name)
                    }

def extract_topics(project_name):
    """Extract topics from project name based on keywords"""
    topics = []
    name_lower = project_name.lower()
    
    if 'park' in name_lower:
        topics.append('park')
    if any(word in name_lower for word in ['road', 'street', 'avenue', 'drive']):
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

# DEBUG: Print some extracted projects
print("DEBUG: Some extracted projects from civic docs:")
project_names = list(projects_info.keys())[:10]
for name in project_names:
    print(f"  - {name}: {projects_info[name]}")
print(f"Total projects extracted: {len(projects_info)}")

# Now match funding data with civic data
matches = []

for funding_record in funding_data:
    project_name = funding_record['Project_Name']
    amount = int(funding_record['Amount'])
    
    # Check for exact match or partial match
    if project_name in projects_info:
        project_info = projects_info[project_name]
        if project_info['type'] == 'capital' and project_info['status'] == 'design':
            matches.append({
                'project_name': project_name,
                'amount': amount,
                'funding_source': funding_record['Funding_Source'],
                'topics': project_info['topic']
            })
    else:
        # Check for partial matches (e.g., without suffixes like "(CalOES Project)")
        base_name = re.sub(r'\s*\([^)]*\)$', '', project_name)
        if base_name in projects_info:
            project_info = projects_info[base_name]
            if project_info['type'] == 'capital' and project_info['status'] == 'design':
                matches.append({
                    'project_name': project_name,
                    'base_name': base_name,
                    'amount': amount,
                    'funding_source': funding_record['Funding_Source'],
                    'topics': project_info['topic']
                })

# Count unique projects
unique_projects = {}
for match in matches:
    base_name = match.get('base_name', match['project_name'])
    if base_name not in unique_projects:
        unique_projects[base_name] = match

# DEBUG: Print matches
print(f"\nDEBUG: Found {len(matches)} total matches, {len(unique_projects)} unique projects")
print("DEBUG: Some matching projects:")
for project in list(unique_projects.values())[:10]:
    print(f"  - {project['project_name']}: ${project['amount']}")

# Final count
count = len(unique_projects)

# Create JSON-serializable result
result_data = {
    'count': count,
    'projects': list(unique_projects.values())
}

print('__RESULT__:')
print(json.dumps(result_data, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
