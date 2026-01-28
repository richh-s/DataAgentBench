code = """import json

# Load Funding Data
with open(locals()['var_function-call-1003584179187242714'], 'r') as f:
    funding_data = json.load(f)

funding_projects = {item['Project_Name']: item for item in funding_data}
project_names = list(funding_projects.keys())

# Load Civic Docs
with open(locals()['var_function-call-1003584179187241629'], 'r') as f:
    civic_docs = json.load(f)

def normalize(text):
    return text.strip().lower()

started_projects = set()
# Use single quotes to avoid JSON issues
target_dates = ['spring 2022', 'march 2022', 'april 2022', 'may 2022', 'spring, 2022', '03/2022', '04/2022', '05/2022']

debug_list = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    
    for line in lines:
        line_str = line.strip()
        if not line_str:
            continue
            
        # Check for project name
        found_name = None
        norm_line = normalize(line_str)
        
        # Simple exact match first
        if norm_line in [normalize(n) for n in project_names]:
             # Find the original name key
             for name in project_names:
                 if normalize(name) == norm_line:
                     found_name = name
                     break
        
        if found_name:
            current_project = found_name
            continue
            
        if current_project:
            lower_line = line_str.lower()
            
            # Start indicators
            if 'begin construction' in lower_line or 'start' in lower_line:
                # Check for target dates
                for date_str in target_dates:
                    if date_str in lower_line:
                        started_projects.add(current_project)
                        debug_list.append({'project': current_project, 'line': line_str})
                        break

total_funding = 0
for p in started_projects:
    total_funding += int(funding_projects[p]['Amount'])

print('__RESULT__:')
print(json.dumps({
    'count': len(started_projects),
    'total_funding': total_funding,
    'projects': list(started_projects),
    'debug': debug_list
}))"""

env_args = {'var_function-call-1003584179187242714': 'file_storage/function-call-1003584179187242714.json', 'var_function-call-1003584179187241629': 'file_storage/function-call-1003584179187241629.json'}

exec(code, env_args)
