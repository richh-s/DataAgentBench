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

# Parse projects from civic documents
spring_2022_projects = []

# Patterns to identify projects and their details
project_patterns = [
    r'([A-Z][a-zA-Z\s\-&]+?(?:\s*\([^\)]*\))?\s*\n\s*(?:cid:\d+\))\s*Updates:',
    r'([A-Z][a-zA-Z\s\-&]+?(?:\s*\([^\)]*\))?)\s*\n\s*(?:cid:\d+\))\s*Project Schedule:',
    r'([A-Z][a-zA-Z\s\-&]+?(?:\s*\([^\)]*\))?)\s*\n\s*(?:cid:\d+\))\s*Estimated Schedule:'
]

# Look for Spring 2022 mentions in project schedules
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find all project sections
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project name indicators (usually on their own line, title case)
        if (line and not line.startswith('(') and not line.startswith('cid:') and 
            not line.startswith('Page') and not line.startswith('Agenda') and
            not line.startswith('Capital Improvement') and not line.startswith('RECOMMENDED') and
            not line.startswith('DISCUSSION:') and not line.startswith('To:') and
            not line.startswith('Prepared by:') and not line.startswith('Approved by:') and
            not line.startswith('Date prepared:') and not line.startswith('Meeting date:') and
            not line.startswith('Subject:') and len(line) > 3 and len(line) < 150 and
            ('Project' in line or any(word.isupper() for word in line.split()[:3]))):
            
            # Check if next few lines contain project indicators
            next_lines = ' '.join(lines[i+1:i+4])
            if 'Updates:' in next_lines or 'Project Schedule:' in next_lines or 'Estimated Schedule:' in next_lines:
                current_project = line
                
                # Look for Spring 2022 schedule in following lines
                for j in range(i+1, min(i+15, len(lines))):
                    schedule_line = lines[j]
                    if '2022' in schedule_line and ('Spring' in schedule_line or 'March' in schedule_line or 
                                                   'April' in schedule_line or 'May' in schedule_line or
                                                   'spring' in schedule_line or 'march' in schedule_line or
                                                   'april' in schedule_line or 'may' in schedule_line):
                        spring_2022_projects.append({
                            'project_name': current_project.strip(),
                            'doc_id': doc.get('_id'),
                            'schedule_line': schedule_line.strip()
                        })
                        break
                    elif 'Project Schedule:' in schedule_line or 'Estimated Schedule:' in schedule_line:
                        # Continue looking
                        pass
                    elif schedule_line.strip() == '' and j > i+5:
                        break

# Also look for project names with dates
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for patterns like "Project Name\n(st: 2022-Spring" or similar
    date_pattern = r'([A-Z][a-zA-Z\s\-&]+?(?:\s*\([^\)]*\))?)\s*\n.*?(?:\bst:|:|)\s*2022\s*[-\s]?(Spring|spring|March|April|May|march|april|may)'
    
    matches = re.findall(date_pattern, text, re.IGNORECASE | re.MULTILINE)
    for match in matches:
        if isinstance(match, tuple):
            project_name = match[0].strip()
        else:
            project_name = match.strip()
            
        if project_name and not any(p['project_name'] == project_name for p in spring_2022_projects):
            spring_2022_projects.append({
                'project_name': project_name,
                'doc_id': doc.get('_id')
            })

print('__RESULT__:')
print(json.dumps({
    'spring_2022_projects_raw': spring_2022_projects[:20],
    'count_raw': len(spring_2022_projects),
    'all_funding_records': len(funding_data)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:8': {'civic_docs_count': 5, 'funding_records_count': 5, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
