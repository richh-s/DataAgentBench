code = """import json
import re

# Load funding data from the stored file path
funding_file_path = var_functions.query_db_2
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents from the stored file path
civic_file_path = var_functions.query_db_5
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Loaded {len(funding_data)} funding records")
print(f"Loaded {len(civic_docs)} civic documents")

# Create a dictionary of funding data keyed by project name for fast lookup
funding_dict = {}
for record in funding_data:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    if amount > 50000:
        funding_dict[project_name] = {
            'amount': amount,
            'funding_id': record.get('Funding_ID'),
            'funding_source': record.get('Funding_Source')
        }

print(f"Found {len(funding_dict)} projects with funding > $50,000")

# Function to extract project information from civic document text
def extract_projects_from_text(text):
    projects = []
    
    # Look for project sections in the text
    # Common patterns for projects: lines followed by ", then status and type info
    
    # Split text into lines for processing
    lines = text.split('\n')
    current_project = None
    
    for line in lines:
        line = line.strip()
        
        # Look for project name patterns - typically a title line
        if line and len(line) > 5 and not line.startswith('(') and not line.startswith('*'):
            # Check if this might be a project name (not a heading or status line)
            if not any(keyword in line.lower() for keyword in ['project schedule', 'updates', 'discussion', 'recommended action', 'agenda']):
                # Check next few lines for status/type information
                if len(line) < 100:  # Likely a project name, not a paragraph
                    current_project = {
                        'name': line,
                        'status': None,
                        'type': None,
                        'topics': []
                    }
                    projects.append(current_project)
        
        # Extract status and type information
        if current_project:
            lower_line = line.lower()
            
            # Check for status indicators
            if 'design' in lower_line:
                current_project['status'] = 'design'
            elif 'completed' in lower_line:
                current_project['status'] = 'completed'
            elif 'not started' in lower_line:
                current_project['status'] = 'not started'
            
            # Check for type indicators
            if 'capital' in lower_line or 'capital improvement' in lower_line:
                current_project['type'] = 'capital'
            elif 'fema' in lower_line or 'disaster' in lower_line or 'recovery' in lower_line:
                current_project['type'] = 'disaster'
                
            # Check for topics
            if any(topic in lower_line for topic in ['park', 'road', 'drainage', 'storm', 'bridge', 'playground']):
                topics = []
                for topic in ['park', 'road', 'drainage', 'storm drain', 'bridge', 'playground', 'fire', 'emergency', 'fema']:
                    if topic in lower_line:
                        topics.append(topic)
                if topics:
                    current_project['topics'].extend(topics)
    
    return projects

# Extract all projects from civic documents
all_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    projects = extract_projects_from_text(text)
    all_projects.extend(projects)

print(f"Extracted {len(all_projects)} potential projects from documents")

# Filter for capital projects with design status and that have funding > $50k
capital_design_projects_with_funding = []

for project in all_projects:
    if (project.get('type') == 'capital' and 
        project.get('status') == 'design' and
        project.get('name') in funding_dict):
        
        funding_info = funding_dict[project.get('name')]
        capital_design_projects_with_funding.append({
            'project_name': project.get('name'),
            'status': project.get('status'),
            'type': project.get('type'),
            'topics': list(set(project.get('topics', []))),  # remove duplicates
            'funding_amount': funding_info['amount'],
            'funding_source': funding_info['funding_source']
        })

print(f"Found {len(capital_design_projects_with_funding)} capital projects with design status and funding > $50,000")

# Show some examples
for proj in capital_design_projects_with_funding[:5]:
    print(f"  - {proj['project_name']}: ${proj['funding_amount']}")

# Save results to JSON format
result_json = json.dumps({
    'count': len(capital_design_projects_with_funding),
    'projects': capital_design_projects_with_funding
})

print("__RESULT__:")
print(result_json)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
