code = """import json
import re

with open('var_functions.query_db:14', 'r') as f:
    civic_docs = json.load(f)

with open('var_functions.query_db:8', 'r') as f:
    funding_data = json.load(f)

print('Loaded documents and funding data')

def extract_projects(text):
    projects = []
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
            
        skip_words = ['page', 'agenda item', 'public works commission', 'capital improvement', 'disaster recovery']
        if any(word in line.lower() for word in skip_words):
            continue
            
        if (not line.startswith(('(', '·', '-', '•')) and 
            not any(phrase in line.lower() for phrase in ['updates:', 'project schedule:', 'complete design:', 'advertise:', 'begin construction:', 'estimated schedule:']) and
            (line.istitle() or sum(1 for c in line if c.isupper()) > len(line) * 0.3)):
            
            if line in ['Capital Improvement Projects (Design)', 'Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']:
                continue
                
            project = {'name': line, 'status': None, 'start_time': None, 'type': None, 'topics': []}
            
            # Look for schedule info
            for j in range(i+1, min(i+20, len(lines))):
                next_line = lines[j].strip()
                
                if 'Schedule:' in next_line:
                    for k in range(j+1, min(j+10, len(lines))):
                        schedule_line = lines[k].strip()
                        if re.search(r'2022[-\s](Spring|March|April|May|03|04|05)', schedule_line, re.IGNORECASE) or 'Spring 2022' in schedule_line:
                            project['start_time'] = '2022-Spring'
                            break
                
                name_lower = line.lower()
                if any(word in name_lower for word in ['fema', 'fire', 'woolsey']):
                    project['type'] = 'disaster'
                elif any(word in name_lower for word in ['road', 'bridge', 'park', 'street', 'drainage', 'storm', 'water', 'infrastructure']):
                    project['type'] = 'capital'
                
                if 'park' in name_lower:
                    project['topics'].append('park')
                if 'road' in name_lower or 'street' in name_lower:
                    project['topics'].append('road')
                if 'drainage' in name_lower or 'storm' in name_lower:
                    project['topics'].append('drainage')
                if 'fema' in name_lower:
                    project['topics'].append('fema')
                
                if project['start_time']:
                    break
            
            if project['start_time'] == '2022-Spring':
                projects.append(project)
    
    return projects

all_projects = []
for doc in civic_docs:
    projects = extract_projects(doc.get('text', ''))
    all_projects.extend(projects)

project_names = [p['name'] for p in all_projects]
print('Spring 2022 projects count:', len(all_projects))

matching_funds = []
total_funding = 0

for project in all_projects:
    project_name = project['name']
    
    for fund in funding_data:
        fund_name = fund.get('Project_Name', '')
        
        if fund_name == project_name or project_name in fund_name:
            amount = int(fund.get('Amount', 0))
            matching_funds.append({'project': project_name, 'fund_name': fund_name, 'amount': amount})
            total_funding += amount
            break

result = {
    'project_count': len(all_projects),
    'total_funding': total_funding,
    'project_names': project_names,
    'funding_matches_count': len(matching_funds)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
