code = """import json
import re

# Load civic documents
civic_docs_file = '/tmp/tmpz5hptp8z.json'
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_file = '/tmp/tmphs_qx5r1.json'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    current_project = None
    project_info = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Detect project names (followed by project content)
        if len(line) > 5 and not line.startswith('('):
            # Look ahead to see if this is project content
            is_project = False
            for next_line in lines[i+1:i+5]:
                nll = next_line.lower()
                if any(m in nll for m in ['updates:', 'project schedule:', 'complete construction:', '(cid:']):
                    is_project = True
                    break
            
            if is_project:
                # Save previous project if valid
                if current_project and project_info:
                    if project_info.get('status') == 'completed' and '2022' in project_info.get('et', ''):
                        park_projects_2022.append(project_info)
                
                current_project = line
                project_info = {
                    'Project_Name': line,
                    'status': '',
                    'et': '',
                    'topic': ''
                }
                
                # Set topic from name
                pl = line.lower()
                topics = []
                if 'park' in pl:
                    topics.append('park')
                if 'playground' in pl:
                    topics.append('playground')
                if 'fema' in pl:
                    topics.append('FEMA')
                project_info['topic'] = ', '.join(topics)
        
        # Check for completion info
        if current_project and project_info:
            ll = line.lower()
            if any(phrase in ll for phrase in ['completed', 'complete construction', 'construction was completed', 'notice of completion']):
                project_info['status'] = 'completed'
                
                patterns = [
                    r'(\w+\s+2022)\b', r'(2022-\w+)\b', r'(\b2022\b)',
                    r'(Fall\s+2022)', r'(Summer\s+2022)', r'(Spring\s+2022)', r'(Winter\s+2022)',
                    r'(January\s+2022)', r'(February\s+2022)', r'(March\s+2022)',
                    r'(April\s+2022)', r'(May\s+2022)', r'(June\s+2022)',
                    r'(July\s+2022)', r'(August\s+2022)', r'(September\s+2022)',
                    r'(October\s+2022)', r'(November\s+2022)', r'(December\s+2022)'
                ]
                
                for pat in patterns:
                    m = re.search(pat, line, re.IGNORECASE)
                    if m:
                        project_info['et'] = m.group(1)
                        break
    
    if current_project and project_info:
        if project_info.get('status') == 'completed' and '2022' in project_info.get('et', ''):
            park_projects_2022.append(project_info)

# Filter for park-related
park_related = []
for p in park_projects_2022:
    if 'park' in p.get('topic', '').lower() or 'playground' in p.get('topic', '').lower():
        park_related.append(p)

# Match funding
matches = []
for f in funding_data:
    fname = f['Project_Name'].lower()
    for p in park_related:
        pname = p['Project_Name'].lower()
        if fname == pname or fname in pname or pname in fname:
            matches.append({
                'project': p['Project_Name'],
                'funding': f['Project_Name'],
                'amount': int(f['Amount'])
            })

# Sum amounts
total = sum(m['amount'] for m in matches)

result = {
    'park_projects': park_related,
    'funding_matches': matches,
    'total_funding': total
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
