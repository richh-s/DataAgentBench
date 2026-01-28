code = """import json
import re

# Load the MongoDB documents file
mongo_file = locals()['var_functions.query_db:0']
with open(mongo_file, 'r') as f:
    documents = json.load(f)

# Extract project information from documents
projects = []

# Regular expressions to extract project information
for doc in documents:
    text = doc.get('text', '')
    
    # Search for Spring 2022 projects in the text
    spring_patterns = [
        r'2022\s*-\s*Spring',
        r'Spring\s*2022',
        r'2022\s*-\s*[Mm][Aa][Rr]',
        r'2022\s*-\s*[Aa][Pp][Rr]',
        r'2022\s*-\s*[Mm][Aa][Yy]',
        r'Complete\s+Design\s*:\s*Spring\s+2022',
        r'Advertise\s*:\s*Spring\s+2022',
        r'Begin\s+Construction\s*:\s*Spring\s+2022',
        r'Project\s+Schedule\s*:\s*.*\n\s*\(cid:\w+\)\s*Complete\s+Design\s*:\s*Spring\s+2022',
    ]
    
    # Look for project sections
    text_lines = text.split('\n')
    for i, line in enumerate(text_lines):
        line = line.strip()
        
        # Skip headers and section titles
        skip_patterns = [
            'Public Works', 'Commission', 'To:', 'Prepared by:', 'Approved by:', 
            'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:',
            'DISCUSSION:', 'Page', 'Agenda Item', 'Capital Improvement Projects',
            'Updates:', 'Project Schedule:', 'Project Description:', 'Estimated Schedule:'
        ]
        
        should_skip = False
        for pattern in skip_patterns:
            if pattern in line or line.startswith(pattern.split(':')[0]):
                should_skip = True
                break
        
        if should_skip or len(line) < 5:
            continue
            
        # Check if this looks like a project name
        project_indicators = ['Project', 'Resurfacing', 'Improvements', 'Repairs', 'Drainage',
                             'Structure', 'Replacement', 'Study', 'Phase', 'System', 'Facility',
                             'Installation', 'Improvement', 'Construction']
        
        has_indicator = any(indicator.lower() in line.lower() for indicator in project_indicators)
        
        # Look at context around this line for spring 2022 references
        context = '\n'.join(text_lines[max(0, i-8):min(len(text_lines), i+8)])
        
        # Check if spring 2022 is mentioned in the context
        spring_found = any(re.search(pattern, context) for pattern in spring_patterns)
        
        if has_indicator and spring_found:
            # Determine project type
            proj_type = 'capital'
            if any(word in line.lower() for word in ['fema', 'caloes', 'caljpia', 'fire', 'disaster', 'woolsey']):
                proj_type = 'disaster'
            
            # Determine status
            status = 'design'  # default
            if 'Complete Construction' in context or 'completed' in context.lower():
                status = 'completed'
            elif 'Not Started' in text:
                status = 'not started'
            
            # Determine topic
            topic = ''
            if any(word in line.lower() for word in ['storm', 'drain']):
                topic = 'storm drain'
            elif any(word in line.lower() for word in ['park', 'playground']):
                topic = 'park'
            elif any(word in line.lower() for word in ['road', 'highway', 'street']):
                topic = 'road'
            elif any(word in line.lower() for word in ['bridge']):
                topic = 'bridge'
            elif any(word in line.lower() for word in ['guardrail']):
                topic = 'guardrail'
            elif any(word in line.lower() for word in ['emergency', 'warning', 'siren']):
                topic = 'emergency warning'
            elif 'fema' in line.lower():
                topic = 'FEMA'
            
            project_info = {
                'project_name': line,
                'start_date': '2022-Spring',
                'status': status,
                'type': proj_type,
                'topic': topic,
            }
            
            # Check if this project was already added
            if not any(p['project_name'] == line for p in projects):
                projects.append(project_info)

print(f"Found {len(projects)} Spring 2022 projects from civic documents")

# Show some of the projects
for p in projects[:15]:
    print(f"Project: {p['project_name']}, Status: {p['status']}, Type: {p['type']}, Topic: {p['topic']}")

# Now load the funding data
funding_file = locals()['var_functions.query_db:2']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

print(f"\nFound {len(funding_records)} funding records")

# Show some sample funding records
for f in funding_records[:5]:
    print(f"Project: {f['Project_Name']}, Amount: ${f['Amount']}")

# Merge project data with funding data
results = []
total_funding = 0

for project in projects:
    project_name = project['project_name']
    
    # Look for matching funding records
    # Need to normalize project names for matching
    normalized_proj_name = project_name.lower().strip()
    
    for fund in funding_records:
        fund_name = fund['Project_Name'].lower().strip()
        
        # Direct match or partial match
        if (normalized_proj_name in fund_name or 
            fund_name in normalized_proj_name or
            normalized_proj_name.replace('project', '').strip() in fund_name or
            fund_name.replace('project', '').strip() in normalized_proj_name):
            amount = int(fund['Amount'])
            results.append({
                'project_name': project['project_name'],
                'funding_project_name': fund['Project_Name'],
                'start_date': project['start_date'],
                'status': project['status'],
                'type': project['type'],
                'topic': project['topic'],
                'funding_amount': amount
            })
            total_funding += amount
            break

print(f"\nFound funding for {len(results)} projects")
print(f"Total funding: ${total_funding}")

result_summary = {
    'count': len(results),
    'total_funding': total_funding,
    'projects': results
}

print('__RESULT__:')
print(json.dumps(result_summary))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
