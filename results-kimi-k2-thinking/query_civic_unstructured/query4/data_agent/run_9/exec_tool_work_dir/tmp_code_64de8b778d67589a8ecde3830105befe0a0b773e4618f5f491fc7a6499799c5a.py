code = """import json
import re

# Load civic documents from file path
civic_docs_path = locals()['var_functions.query_db:24']
if isinstance(civic_docs_path, str) and civic_docs_path.endswith('.json'):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_path

# Find Spring 2022 projects
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for Spring 2022 references and capture nearby project names
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check if line contains Spring 2022 date reference
        if '2022' in line and any(season in line for season in ['Spring', 'spring', 'March', 'April', 'May']):
            # Look backwards for project name (usually 1-5 lines before)
            for j in range(max(0, i-5), i):
                prev_line = lines[j].strip()
                
                # Skip common headers and markers
                skip_terms = ['(', 'cid:', 'Page', 'Agenda', 'Capital Improvement', 'RECOMMENDED', 
                            'DISCUSSION:', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 
                            'Meeting date:', 'Subject:', 'From:', 'Department:', 'Public Works',
                            'Project Schedule:', 'Project Updates:', 'Project Description:', 'Updates:']
                
                if any(prev_line.startswith(term) for term in skip_terms):
                    continue
                if not prev_line or len(prev_line) < 5 or len(prev_line) > 200:
                    continue
                
                # Check if line looks like a project name (has capitalized words, not just dates)
                words = prev_line.split()
                capitalized_words = [w for w in words if w and w[0].isupper()]
                
                if len(capitalized_words) >= 2:
                    project_name = prev_line.strip()
                    
                    # Avoid duplicates
                    if not any(p['project_name'] == project_name for p in spring_2022_projects):
                        spring_2022_projects.append({
                            'project_name': project_name,
                            'schedule_info': line,
                            'doc_id': doc.get('_id')
                        })

# If no projects found with first method, try a broader search
if not spring_2022_projects:
    for doc in civic_docs:
        text = doc.get('text', '')
        
        # Look for patterns like: Project Name [newline] ... Spring 2022
        pattern = r'([A-Z][a-zA-Z\s\-&]+?)\s*\n[^\n]*?(?:2022).*?(?:Spring|spring|March|April|May)'
        matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
        
        for project_name in matches:
            project_name = project_name.strip()
            if project_name and len(project_name) < 200:
                spring_2022_projects.append({
                    'project_name': project_name,
                    'doc_id': doc.get('_id')
                })

# Count unique projects
unique_projects = {}
for proj in spring_2022_projects:
    name = proj['project_name']
    unique_projects[name] = proj

result_data = {
    'spring_2022_projects': list(unique_projects.values()),
    'count': len(unique_projects),
    'sample_projects': list(unique_projects.values())[:10]
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:8': {'civic_docs_count': 5, 'funding_records_count': 5, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:21': [{'total_records': '500'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
