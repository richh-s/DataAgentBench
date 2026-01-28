code = """import json
import re

# Read the civic docs from the file path stored in the variable
civic_docs_file = locals()['var_functions.query_db:2']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

print('Loaded {} civic documents'.format(len(civic_docs)))

# Extract project information from text
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split by lines to find project headings and details
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and lines that are clearly not project names
        if not line or line.startswith('(') or line.startswith('●') or line.startswith('■'):
            continue
            
        # Skip common agenda headings
        skip_terms = ['capital improvement', 'disaster recovery', 'public works', 'commission meeting', 'agenda report', 'page ', 'item #', 'to:', 'prepared by:', 'approved by:', 'date prepared:', 'meeting date:', 'subject:', 'recommended action:', 'discussion:']
        if any(term in line.lower() for term in skip_terms):
            continue
            
        # Check if this might be a project name (look ahead for project indicators)
        next_text = ''
        if i + 1 < len(lines):
            look_ahead = []
            for j in range(i+1, min(i+4, len(lines))):
                look_ahead.append(lines[j].strip())
            next_text = ' '.join(look_ahead).lower()
        
        # If next lines contain project indicators, this is likely a project name
        project_indicators = ['updates:', 'schedule:', 'complete', 'design', 'construction', 'project', 'description']
        if any(indicator in next_text for indicator in project_indicators):
            # Found a project
            if current_project:
                projects.append(current_project)
            
            current_project = {
                'Project_Name': line,
                'topic': '',
                'status': '',
                'st': '',
                'et': '',
                'source_doc': filename
            }
            
            # Extract potential topics from name
            name_lower = line.lower()
            topics = []
            if 'park' in name_lower:
                topics.append('park')
            if 'road' in name_lower or 'street' in name_lower:
                topics.append('road')
            if 'drain' in name_lower or 'storm' in name_lower:
                topics.append('drainage')
            if 'warning' in name_lower:
                topics.append('emergency warning')
            if 'playground' in name_lower:
                topics.append('playground')
                
            current_project['topic'] = ', '.join(topics)
        
        # Extract status and dates from updates and schedule
        if current_project:
            line_lower = line.lower()
            
            # Check for completed status
            if any(word in line_lower for word in ['completed', 'notice of completion', 'construction was completed']):
                current_project['status'] = 'completed'
                # Try to extract year
                year_match = re.search(r'(202\d)', line)
                if year_match:
                    current_project['et'] = year_match.group(1)
            
            # Check for specific completion dates
            if 'complete construction' in line_lower or 'complete:' in line_lower:
                year_match = re.search(r'(202\d)', line)
                if year_match:
                    current_project['et'] = year_match.group(1)
                    current_project['status'] = 'completed'
            
            # Default to design status if design mentioned
            if 'design' in line_lower and not current_project['status']:
                current_project['status'] = 'design'
    
    # Save the last project
    if current_project:
        projects.append(current_project)

print('Extracted {} potential projects'.format(len(projects)))

# Show first 10 projects for verification
for i, p in enumerate(projects[:10]):
    print('{}. {} | Topic: {} | Status: {} | End: {}'.format(i+1, p['Project_Name'], p['topic'], p['status'], p['et']))

# Filter for park-related projects completed in 2022
park_projects_2022 = []
for p in projects:
    # Check if park-related
    if 'park' not in p['topic'].lower() and 'park' not in p['Project_Name'].lower():
        continue
    
    # Check if completed in 2022
    et = p.get('et', '')
    status = p.get('status', '')
    
    if '2022' in et and status == 'completed':
        park_projects_2022.append(p)

print('\nFound {} park projects completed in 2022:'.format(len(park_projects_2022)))
for p in park_projects_2022:
    print('- {} (End: {}, Status: {}, Doc: {})'.format(p['Project_Name'], p['et'], p['status'], p['source_doc']))

# Save the filtered projects
output_path = '/tmp/park_projects_2022.json'
with open(output_path, 'w') as f:
    json.dump(park_projects_2022, f, indent=2)

print('\nPark projects saved to ' + output_path)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
