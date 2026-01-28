code = """import json, os, re

# Load civic documents data
filepath = locals().get('var_functions.query_db:2')
if isinstance(filepath, str) and os.path.exists(filepath):
    with open(filepath, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = []

# Simple extraction based on FEMA/disaster keywords
projects = []
for doc in civic_docs:
    text = doc['text']
    filename = doc['filename']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Detect project names based on patterns
        name_keywords = ['Project', 'Improvements', 'Repairs', 'System', 'Facility', 'Study']
        if any(kw in line for kw in name_keywords) and len(line) < 150:
            project_name = line
            
            # Check if disaster-related
            is_disaster = any(kw in project_name.lower() for kw in ['fema', 'disaster', 'recovery', 'fire'])
            
            if not is_disaster:
                # Search next few lines
                j = i + 1
                while j < min(i + 10, len(lines)):
                    next_line = lines[j].lower()
                    if 'fema' in next_line or 'caloes' in next_line or 'disaster' in next_line:
                        is_disaster = True
                        break
                    j += 1
            
            if is_disaster:
                # Find start date
                st = None
                j = i + 1
                while j < min(i + 15, len(lines)):
                    schedule_line = lines[j]
                    if 'Schedule:' in schedule_line or 'Complete Design:' in schedule_line:
                        # Look for year pattern
                        year_match = re.search(r'202[0-3]', schedule_line)
                        if year_match:
                            st = schedule_line
                            break
                    j += 1
                
                projects.append({
                    'name': project_name,
                    'st': st,
                    'file': filename
                })

# Filter for 2022
projects_2022 = [p for p in projects if p['st'] and '2022' in p['st']]

print('__RESULT__:')
print(json.dumps({
    'projects_raw': len(projects),
    'projects_2022': len(projects_2022),
    'names': [p['name'] for p in projects_2022]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': {'success': True, 'num_docs': 5}}

exec(code, env_args)
