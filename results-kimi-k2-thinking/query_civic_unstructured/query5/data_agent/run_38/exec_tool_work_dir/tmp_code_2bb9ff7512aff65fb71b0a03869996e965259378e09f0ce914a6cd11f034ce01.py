code = """import json
import re

funding_path = var_functions.query_db:20
civic_docs_path = var_functions.query_db:21

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Loaded {len(funding_data)} funding records and {len(civic_docs)} civic documents")

# Identify disaster-related projects that started in 2022
disaster_projects_2022 = []

# Look for projects with:
# 1. Disaster/FEMA indicators in project name or context
# 2. 2022 start dates

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for disaster indicators
    disaster_indicators = ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)', 'FEMA/CalOES', 'disaster', 'emergency']
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check if this line or nearby lines contain disaster indicators
        context_window = 5
        start_idx = max(0, i - context_window)
        end_idx = min(len(lines), i + context_window + 1)
        context = '\n'.join(lines[start_idx:end_idx])
        
        has_disaster_indicator = any(indicator.lower() in context.lower() for indicator in disaster_indicators)
        
        if has_disaster_indicator:
            # Look for project names - typically lines that don't start with bullet points and look like titles
            if line and not line.startswith('(') and not line.startswith('•') and len(line) > 10:
                # Check if this might be a project name (contains 'Project', 'Improvements', 'Repairs', etc)
                project_keywords = ['Project', 'Improvements', 'Repairs', 'Maintenance', 'Drainage', 'Bridge', 'Culvert']
                if any(keyword in line for keyword in project_keywords):
                    project_name = line
                    
                    # Look for 2022 in the context
                    if '2022' in context:
                        # Determine start date - look for patterns
                        st = '2022'
                        
                        # More specific patterns
                        date_patterns = [
                            r'2022-\w+',
                            r'2022-\d{1,2}',
                            r'Spring\s+2022',
                            r'Fall\s+2022',
                            r'Summer\s+2022',
                            r'Winter\s+2022'
                        ]
                        
                        for pattern in date_patterns:
                            match = re.search(pattern, context, re.IGNORECASE)
                            if match:
                                st = match.group(0)
                                break
                        
                        # Clean up the project name
                        project_name = project_name.strip()
                        if project_name.endswith(':'):
                            project_name = project_name[:-1].strip()
                        
                        # Check if this is a unique project
                        exists = any(p['project_name'] == project_name for p in disaster_projects_2022)
                        if not exists:
                            disaster_projects_2022.append({
                                'project_name': project_name,
                                'st': st,
                                'source_doc': filename
                            })

# Also look for projects with 2022 in their name (like "2022 Morning View...")
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('2022'):
            # Check if this line looks like a project name
            project_keywords = ['Project', 'Improvements', 'Repairs', 'Maintenance', 'Drainage', 'Resurfacing']
            if any(keyword in line for keyword in project_keywords):
                # Check if disaster-related
                if 'storm' in line.lower() or 'drain' in line.lower():
                    project_name = line
                    if project_name.endswith(':'):
                        project_name = project_name[:-1]
                    
                    exists = any(p['project_name'] == project_name for p in disaster_projects_2022)
                    if not exists:
                        disaster_projects_2022.append({
                            'project_name': project_name,
                            'st': '2022',
                            'source_doc': filename
                        })

print(f"\nFound {len(disaster_projects_2022)} disaster projects that started in 2022:")
for p in disaster_projects_2022:
    print(f"- {p['project_name']}")

# Find funding for these projects
funding_matches = []
for project in disaster_projects_2022:
    project_name = project['project_name']
    
    for funding in funding_data:
        funding_project_name = funding.get('Project_Name', '')
        
        # Check for exact match or partial match
        if project_name == funding_project_name or funding_project_name.startswith(project_name):
            funding_matches.append({
                'project_name': project_name,
                'funding_project_name': funding_project_name,
                'amount': int(funding.get('Amount', 0))
            })
        elif project_name in funding_project_name:
            funding_matches.append({
                'project_name': project_name,
                'funding_project_name': funding_project_name,
                'amount': int(funding.get('Amount', 0))
            })

print(f"\nFound {len(funding_matches)} funding matches")

# Sum up the funding
total_funding = sum(match['amount'] for match in funding_matches)

result = {
    'total_funding_2022': total_funding,
    'project_count': len(disaster_projects_2022),
    'funding_count': len(funding_matches),
    'projects_with_funding': funding_matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:23': 'file_storage/functions.query_db:23.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:21': 'file_storage/functions.query_db:21.json'}

exec(code, env_args)
