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
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check if line might be a project name
        if line and len(line) > 3 and len(line) < 200:
            # Skip common headers
            skip_patterns = ['(', 'cid:', 'Page', 'Agenda', 'Capital Improvement', 'RECOMMENDED', 
                           'DISCUSSION:', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 
                           'Meeting date:', 'Subject:', 'From:', 'Department:', 'Public Works']
            if any(line.startswith(pattern) for pattern in skip_patterns):
                i += 1
                continue
            
            # Look for lines that could be project names (have capitalized words)
            words = line.split()
            if len(words) >= 2:
                capitalized_count = sum(1 for w in words if w and w[0].isupper())
                if capitalized_count >= 2:  # At least 2 capitalized words
                    # Look ahead for schedule information mentioning Spring 2022
                    for j in range(i+1, min(i+15, len(lines))):
                        next_line = lines[j].strip()
                        
                        # Check for Spring 2022 reference
                        if '2022' in next_line:
                            season_indicators = ['Spring', 'spring', 'March', 'April', 'May', 
                                               'march', 'april', 'may']
                            if any(season in next_line for season in season_indicators):
                                project_name = line.strip()
                                # Avoid duplicates
                                if not any(p['project_name'] == project_name for p in spring_2022_projects):
                                    spring_2022_projects.append({
                                        'project_name': project_name,
                                        'doc_id': doc.get('_id')
                                    })
                                break
                        # Stop if we hit a blank line after a few iterations
                        if next_line == '' and j > i+3:
                            break
        
        i += 1

# Also use regex to find date patterns in the entire text
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Pattern 1: Project name on one line, then date info on next
    pattern1 = r'([A-Z][a-zA-Z\\s\\-&]+?)\\s*\\n\\s*(?:st:|Schedule:|Timing:)\\s*.*?(?:2022).*?(?:Spring|spring|March|April|May)'
    matches = re.finditer(pattern1, text, re.IGNORECASE | re.MULTILINE)
    
    for match in matches:
        project_name = match.group(1).strip()
        if project_name and len(project_name) < 200:
            if not any(p['project_name'] == project_name for p in spring_2022_projects):
                spring_2022_projects.append({
                    'project_name': project_name,
                    'doc_id': doc.get('_id')
                })
    
    # Pattern 2: Date first, then project name
    pattern2 = r'(?:Begin|Start|Complete|Finish)[\\s\\w]+:\\s*Spring\\s*2022.*?\\n([A-Z][a-zA-Z\\s\\-&]+?)(?:\\n|$)'
    matches = re.finditer(pattern2, text, re.IGNORECASE)
    
    for match in matches:
        project_name = match.group(1).strip()
        if project_name and len(project_name) < 200:
            if not any(p['project_name'] == project_name for p in spring_2022_projects):
                spring_2022_projects.append({
                    'project_name': project_name,
                    'doc_id': doc.get('_id')
                })

result_data = {
    'spring_2022_projects': spring_2022_projects,
    'count': len(spring_2022_projects),
    'total_funding_records': len(funding_data)
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:8': {'civic_docs_count': 5, 'funding_records_count': 5, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
