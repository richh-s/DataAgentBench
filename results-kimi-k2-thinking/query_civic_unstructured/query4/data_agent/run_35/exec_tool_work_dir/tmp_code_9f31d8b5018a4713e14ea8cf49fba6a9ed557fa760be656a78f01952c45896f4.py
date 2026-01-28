code = """import json, re, pandas as pd

# Load the data from files
with open('file_storage/functions.query_db:6.json', 'r') as f:
    funding = json.load(f)
with open('file_storage/functions.query_db:50.json', 'r') as f:
    spring_docs = json.load(f)

# Create funding DataFrame
funding_df = pd.DataFrame(funding)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Extract Spring 2022 project names and match with funding
project_funding_pairs = []
inferred_projects = set()

# Process each document that contains Spring 2022
for doc in spring_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for lines containing project names (heuristic)
        if line and not line.isupper() and len(line) > 10:
            # Skip headers
            if any(pattern in line for pattern in ['Page', 'Agenda Item', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:', 'Capital Improvement Projects', 'Disaster Recovery Projects']):
                continue
            
            # Check if this line is a project name (starts with year or has FEMA suffix or is descriptive)
            is_project = False
            if re.match(r'^\d{4}\s+[A-Z].+', line) and len(line) > 15:
                is_project = True
            elif re.search(r'\((FEMA|CalOES|CalJPIA|FEMA/CalOES)\s+Project\)', line):
                is_project = True
            elif len(line.split()) > 2 and line[0].isupper() and not any(word in line.lower() for word in ['schedule', 'updates', 'description']):
                is_project = True
            
            if is_project:
                # Look ahead for Spring 2022 mentions
                for j in range(i+1, min(i+15, len(lines))):
                    next_line = lines[j]
                    if '2022' in next_line and 'Spring' in next_line:
                        if any(action in next_line for action in ['Begin', 'Complete Design', 'Start', 'Advertise', 'Award']):
                            # Found a Spring 2022 project
                            project_name = line
                            
                            # Find funding for this project
                            matches = funding_df[funding_df['Project_Name'] == project_name]
                            
                            if not matches.empty:
                                for _, match in matches.iterrows():
                                    project_funding_pairs.append({
                                        'project': project_name,
                                        'funding': int(match['Amount']),
                                        'source': match['Funding_Source']
                                    })
                            else:
                                # Try matching without parenthetical suffix
                                base_name = re.sub(r'\s+\([^)]*\)$', '', project_name).strip()
                                if base_name != project_name:
                                    matches = funding_df[funding_df['Project_Name'] == base_name]
                                    if not matches.empty:
                                        for _, match in matches.iterrows():
                                            project_funding_pairs.append({
                                                'project': project_name,
                                                'funding': int(match['Amount']),
                                                'source': match['Funding_Source']
                                            })
                            
                            inferred_projects.add(project_name)
                            break

# Remove duplicates and calculate totals
unique_projects = {}
for item in project_funding_pairs:
    p_name = item['project']
    if p_name not in unique_projects:
        unique_projects[p_name] = item
    else:
        # If duplicate, keep the larger funding amount
        if item['funding'] > unique_projects[p_name]['funding']:
            unique_projects[p_name] = item

final_projects = list(unique_projects.values())
project_count = len(final_projects)
total_funding = sum(p['funding'] for p in final_projects)

print('__RESULT__:')
print(json.dumps({
    'num_projects': project_count,
    'total_funding': total_funding,
    'projects': [p['project'] for p in final_projects]
}))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:12': ['civic_docs'], 'var_functions.execute_python:16': {'funding_result_type': "<class 'str'>", 'funding_result_preview': 'file_storage/functions.query_db:6.json', 'civic_result_type': "<class 'str'>", 'civic_result_preview': 'file_storage/functions.query_db:10.json'}, 'var_functions.execute_python:18': {'funding_records': 500, 'civic_docs_count': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': 24000}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': 45000}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': 38000}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': 23000}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': 79000}], 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_docs_count': 5, 'total_funding_amount': 28094000, 'sample_project_names': ['2021 Annual Street Maintenance', '2022 Annual Street Maintenance', '2022 Morning View Resurfacing & Storm Drain Improvements', 'Annual Street Maintenance', 'Birdview Avenue Improvements']}, 'var_functions.execute_python:32': {'refs': [{'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring/Summer 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Final Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Advertise: Spring/Summer 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Award Contract and Begin Construction: Spring/Summer 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': 'sending this project out to bid during the Spring of 2022.', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': 'Commission will then review the project in Spring 2022 before final', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Completion Date: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) The project design will commence during the Spring 2022.', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': 'started and is anticipated to be completed by the Spring of 2022.', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01272021-1626.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01272021-1626.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01272021-1626.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03022021-1648.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03022021-1648.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03022021-1648.txt'}, {'line': '(cid:131) Completion Date: Spring 2022', 'file': 'malibucity_agenda__03022021-1648.txt'}, {'line': '(cid:131) Advertise: Spring/Summer 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Final Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': 'Commission will then review the project in Spring 2022 before final', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Begin Design: Late Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Advertise: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Advertise: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Completion Date: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': 'beginning in Spring 2022.', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': 'completed by Spring 2022.', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}], 'count': 44}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:46': {'funding_records': 500, 'civic_documents': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'sample_civic_keys': ['_id', 'filename', 'text']}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
