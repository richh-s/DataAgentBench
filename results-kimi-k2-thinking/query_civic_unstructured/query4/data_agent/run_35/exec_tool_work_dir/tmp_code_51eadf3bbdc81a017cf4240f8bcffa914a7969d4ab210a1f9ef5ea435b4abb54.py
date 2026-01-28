code = """import json
import re
import pandas as pd

# Load funding data
with open('file_storage/functions.query_db:6.json') as f:
    funding_raw = json.load(f)

# Load civic documents
with open('file_storage/functions.query_db:10.json') as f:
    civic_raw = json.load(f)

# Create funding DataFrame
funding_df = pd.DataFrame(funding_raw)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Extract projects with Spring 2022 from civic documents
spring_2022_projects = set()

for doc in civic_raw:
    text = doc['text']
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Look for schedule/action lines with Spring 2022
        if '2022' in line and ('Spring' in line or 'spring' in line):
            # Look backwards for project name (within reasonable distance)
            for j in range(i-1, max(i-10, -1), -1):
                prev_line = lines[j].strip()
                
                # Skip empty lines and headers
                if not prev_line or len(prev_line) < 10:
                    continue
                if prev_line.isupper():
                    continue
                if any(skip in prev_line for skip in ['Page', 'Agenda Item', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:']):
                    continue
                
                # This looks like a project name
                project_name = prev_line
                
                # Clean up common patterns
                if not any(keyword in project_name for keyword in ['Project Schedule', 'Updates', 'Project Description', 'cid', '---']):
                    spring_2022_projects.add(project_name)
                    break

# Convert to list for processing
project_list = list(spring_2022_projects)

# Match projects with funding data
total_funding = 0
funded_projects = []

for project in project_list:
    # Direct match first
    matches = funding_df[funding_df['Project_Name'] == project]
    
    if matches.empty:
        # Try base name without suffix
        base_name = re.sub(r'\s+\([^)]*\)$', '', project)
        matches = funding_df[funding_df['Project_Name'].str.contains(base_name, case=False, na=False)]
    
    if not matches.empty:
        for _, row in matches.iterrows():
            funded_projects.append({
                'Project_Name': project,
                'Funding_Amount': int(row['Amount']),
                'Funding_Source': row['Funding_Source']
            })
            total_funding += int(row['Amount'])

print('__RESULT__:')
print(json.dumps({
    'num_spring_2022_projects': len(funded_projects),
    'total_funding_amount': total_funding,
    'sample_projects': [p['Project_Name'] for p in funded_projects][:10]
}))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:12': ['civic_docs'], 'var_functions.execute_python:16': {'funding_result_type': "<class 'str'>", 'funding_result_preview': 'file_storage/functions.query_db:6.json', 'civic_result_type': "<class 'str'>", 'civic_result_preview': 'file_storage/functions.query_db:10.json'}, 'var_functions.execute_python:18': {'funding_records': 500, 'civic_docs_count': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': 24000}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': 45000}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': 38000}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': 23000}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': 79000}], 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_docs_count': 5, 'total_funding_amount': 28094000, 'sample_project_names': ['2021 Annual Street Maintenance', '2022 Annual Street Maintenance', '2022 Morning View Resurfacing & Storm Drain Improvements', 'Annual Street Maintenance', 'Birdview Avenue Improvements']}, 'var_functions.execute_python:32': {'refs': [{'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring/Summer 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Final Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Advertise: Spring/Summer 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Award Contract and Begin Construction: Spring/Summer 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': 'sending this project out to bid during the Spring of 2022.', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': 'Commission will then review the project in Spring 2022 before final', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Completion Date: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) The project design will commence during the Spring 2022.', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': 'started and is anticipated to be completed by the Spring of 2022.', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01272021-1626.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01272021-1626.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01272021-1626.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03022021-1648.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03022021-1648.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03022021-1648.txt'}, {'line': '(cid:131) Completion Date: Spring 2022', 'file': 'malibucity_agenda__03022021-1648.txt'}, {'line': '(cid:131) Advertise: Spring/Summer 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Final Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': 'Commission will then review the project in Spring 2022 before final', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Begin Design: Late Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Advertise: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Advertise: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Completion Date: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': 'beginning in Spring 2022.', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': 'completed by Spring 2022.', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}], 'count': 44}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:46': {'funding_records': 500, 'civic_documents': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'sample_civic_keys': ['_id', 'filename', 'text']}}

exec(code, env_args)
