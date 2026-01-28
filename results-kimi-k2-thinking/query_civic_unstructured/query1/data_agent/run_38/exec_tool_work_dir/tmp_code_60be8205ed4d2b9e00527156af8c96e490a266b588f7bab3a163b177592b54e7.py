code = """import json
import re

# Access the civic documents data
civic_docs_path = locals()['var_functions.query_db:5']

# Load the data
if isinstance(civic_docs_path, str):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_path

print('Number of civic docs loaded:', len(civic_docs))

# Extract project information using regex patterns
all_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Find sections for capital projects
    # Look for "Capital Improvement Projects (Design)" section
    design_section_pattern = r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Disaster Recovery Projects|DISASTER RECOVERY|$)'
    design_match = re.search(design_section_pattern, text, re.DOTALL | re.IGNORECASE)
    
    if design_match:
        design_section = design_match.group(1)
        # Extract project names from this section
        # Look for lines that are likely project names
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            if not line or len(line) < 5:
                continue
            
            # Skip lines with certain markers
            if line.startswith('(') or line.startswith('•') or 'cid:' in line:
                continue
            if line.isupper():
                continue
            
            # Skip schedule/updates lines
            lower_line = line.lower()
            skip_terms = ['updates:', 'project schedule:', 'complete design:', 'advertise:', 'begin construction:', 'project description:', 'estimated schedule:']
            if any(term in lower_line for term in skip_terms):
                continue
            
            # Skip if all digits or common words
            if line.lower() in ['design', 'construction', 'not started', 'page']:
                continue
            
            # Skip header/footer content
            skip_phrases = ['public works', 'commission', 'agenda', 'report', 'meeting', 'prepared by', 'approved by', 'subject']
            if any(phrase in line.lower() for phrase in skip_phrases):
                continue
            
            # This appears to be a project name
            project_name = line
            for prefix in ['·', '•', '-', '▪']:
                if project_name.startswith(prefix):
                    project_name = project_name[1:].strip()
            
            # Avoid duplicates
            project_key = (project_name, 'design', 'capital')
            if project_key not in [(p['Project_Name'], p['status'], p['type']) for p in all_projects]:
                all_projects.append({
                    'Project_Name': project_name,
                    'status': 'design',
                    'type': 'capital'
                })

print('Capital projects with design status found:', len(all_projects))
for i, proj in enumerate(all_projects[:20]):
    print('  ', i+1, '.', proj['Project_Name'])

# Convert to JSON
result = json.dumps(all_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
