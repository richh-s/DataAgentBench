code = """import json
import re

# Load all civic documents
civic_docs_path = locals()['var_functions.query_db:10']
if isinstance(civic_docs_path, str) and civic_docs_path.endswith('.json'):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_path

# Load all funding data
funding_path = locals()['var_functions.query_db:11']
if isinstance(funding_path, str) and funding_path.endswith('.json'):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_path

# Parse projects from civic documents - look for Spring 2022 schedules
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip header/footer lines
        if (not line or line.startswith('(') or line.startswith('cid:') or 
            line.startswith('Page') or line.startswith('Agenda') or 
            'Capital Improvement Projects' in line or 'RECOMMENDED ACTION' in line or
            'DISCUSSION:' in line or 'To:' in line or 'Prepared by:' in line or
            'Approved by:' in line or 'Date prepared:' in line or 'Meeting date:' in line or
            'Subject:' in line):
            continue
            
        # Look for project names followed by schedule indicators
        if len(line) > 3 and len(line) < 150:
            # Check if this line looks like a project name (has capitalized words)
            words = line.split()
            if len(words) >= 2 and sum(1 for w in words if w[0].isupper() if w) >= min(2, len(words)//2 + 1):
                # Look ahead for schedule info
                for j in range(i+1, min(i+12, len(lines))):
                    next_line = lines[j].strip()
                    
                    # Look for Spring 2022 in schedule
                    if '2022' in next_line and ('Spring' in next_line or 'spring' in next_line or 
                                             'March' in next_line or 'April' in next_line or 'May' in next_line or
                                             'march' in next_line or 'april' in next_line or 'may' in next_line):
                        spring_2022_projects.append({
                            'project_name': line.strip(),
                            'doc_id': doc.get('_id')
                        })
                        break
                    elif next_line == '' and j > i+3:
                        break

# Also use regex to find date patterns
for doc in civic_docs:
    text = doc.get('text', '')
    patterns = [
        r'([A-Z][a-zA-Z\s\-&]+?)\s*\n\s*(?:st:|Schedule:)\s*2022\s*[-\s]?(Spring|spring|March|April|May)',
        r'(?:Begin|Start|Complete|Finish)[\s\w]+:\s*Spring\s*2022[^\n]*([A-Z][a-zA-Z\s\-&]+?)(?:\n|$)',
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
        for match in matches:
            if isinstance(match, tuple) and match[0]:
                project_name = match[0].strip()
                if project_name and not any(p['project_name'] == project_name for p in spring_2022_projects):
                    spring_2022_projects.append({
                        'project_name': project_name,
                        'doc_id': doc.get('_id')
                    })
            elif isinstance(match, str) and match.strip():
                project_name = match.strip()
                if project_name and not any(p['project_name'] == project_name for p in spring_2022_projects):
                    spring_2022_projects.append({
                        'project_name': project_name,
                        'doc_id': doc.get('_id')
                    })

print('__RESULT__:')
print(json.dumps({
    'spring_projects_found': spring_2022_projects,
    'count': len(spring_2022_projects),
    'total_funding_records': len(funding_data)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:8': {'civic_docs_count': 5, 'funding_records_count': 5, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
