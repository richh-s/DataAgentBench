code = """import json, re

# Load data from the stored results
civic_docs_file = globals()['var_functions.query_db:0']
funding_file = globals()['var_functions.query_db:2']

# Read JSON data
civic_docs = json.load(open(civic_docs_file)) if isinstance(civic_docs_file, str) else civic_docs_file
funding_data = json.load(open(funding_file)) if isinstance(funding_file, str) else funding_file

# Create project extraction function
def extract_projects(text, filename):
    projects = []
    lines = text.split('\n')
    curr = None
    
    for line in lines:
        line = line.strip()
        if not line: continue
        if line.startswith('Page') or line.startswith('Agenda') or 'cid:' in line: continue
        
        # Project name detection
        is_project = False
        if len(line) < 100 and not line.isupper():
            has_keywords = 'Project' in line or 'Improvements' in line or 'Repairs' in line
            is_title_case = line.istitle() or (line[0].isupper() and ' ' in line)
            if has_keywords or (is_title_case and len(line.split()) > 2):
                is_project = True
        
        if is_project and not line.endswith(':'):
            if curr: projects.append(curr)
            curr = {'Project_Name': line, 'topic': '', 'type': '', 'status': '', 'st': '', 'et': '', 'file': filename}
            
            # Set type based on keywords
            if 'FEMA' in line or 'CalOES' in line or 'CalJPIA' in line:
                curr['type'] = 'disaster'
            elif 'Improvements' in line or 'Capital' in line:
                curr['type'] = 'capital'
            
            # Extract topics
            topics = []
            if 'emergency' in line.lower(): topics.append('emergency warning')
            if 'FEMA' in line: topics.append('FEMA')
            if 'siren' in line.lower() or 'warning' in line.lower(): topics.append('emergency warning')
            if 'drain' in line.lower() or 'storm' in line.lower(): topics.append('drainage')
            if 'road' in line.lower(): topics.append('road')
            if 'park' in line.lower(): topics.append('park')
            curr['topic'] = ', '.join(topics)
        
        elif curr:
            line_low = line.lower()
            # Status detection
            if 'design' in line_low and not curr['status']: curr['status'] = 'design'
            elif 'construction' in line_low: curr['status'] = 'construction'
            elif 'completed' in line_low and not curr['status']: curr['status'] = 'completed'
            elif 'not started' in line_low: curr['status'] = 'not started'
            
            # Date detection
            date_match = re.search(r'(Spring|Summer|Fall|Winter)[\s-](\d{4})', line, re.I)
            if date_match:
                date_str = f"{date_match.group(2)}-{date_match.group(1).title()}"
                if not curr['st']: curr['st'] = date_str
                elif not curr['et']: curr['et'] = date_str
    
    if curr: projects.append(curr)
    return projects

# Extract all projects
all_projects = []
for doc in civic_docs:
    all_projects.extend(extract_projects(doc['text'], doc['filename']))

# Filter emergency/FEMA projects
emergency_projects = []
for p in all_projects:
    name = p['Project_Name'].lower()
    topic = p['topic'].lower()
    if 'emergency' in name or 'fema' in name or 'emergency' in topic or 'fema' in topic:
        emergency_projects.append(p)

# Join with funding data
funding_lookup = {f['Project_Name']: f for f in funding_data}
results = []

for p in emergency_projects:
    proj_name = p['Project_Name']
    if proj_name in funding_lookup:
        f = funding_lookup[proj_name]
        results.append({
            'Project_Name': proj_name,
            'Funding_Source': f['Funding_Source'],
            'Amount': int(f['Amount']),
            'Status': p['status'],
            'Topic': p['topic']
        })

# Format final answer
result_text = f"Found {len(results)} emergency/FEMA projects with funding data:\n\n"
for r in results:
    result_text += f"Project: {r['Project_Name']}\n"
    result_text += f"  Funding: {r['Funding_Source']} (${r['Amount']:,})\n"
    result_text += f"  Status: {r['Status']}\n"
    result_text += f"  Topic: {r['Topic']}\n\n"

print('__RESULT__:')
print(json.dumps(result_text))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:18': {'civic_docs': 5, 'funding_records': 500, 'sample_civic_keys': ['_id', 'filename', 'text'], 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}}

exec(code, env_args)
