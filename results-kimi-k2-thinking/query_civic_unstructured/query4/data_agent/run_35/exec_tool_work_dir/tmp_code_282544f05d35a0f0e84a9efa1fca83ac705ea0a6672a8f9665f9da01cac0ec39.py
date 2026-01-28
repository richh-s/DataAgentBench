code = """import json
import re
import pandas as pd

# Load data
with open('file_storage/functions.query_db:6.json', 'r') as f:
    funding_data = json.load(f)

with open('file_storage/functions.query_db:10.json', 'r') as f:
    civic_docs = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Extract all projects from documents
all_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Skip headers
        if any(x in line for x in ['Page', 'Agenda Item', 'To:', 'Prepared by:', 'Approved by:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:']):
            continue
            
        project_name = None
        
        # Check if this line looks like a project name
        # Pattern 1: Starts with year
        if re.match(r'^\d{4}\s+[A-Z].+', line) and len(line)>15:
            project_name = line
        # Pattern 2: Contains FEMA/CalOES/CalJPIA
        elif re.search(r'\((FEMA|CalOES|CalJPIA|FEMA/CalOES)\s+Project\)', line) and len(line)>15:
            project_name = line
        # Pattern 3: Title case descriptive name
        elif len(line)>15 and not line.isupper() and ' ' in line and len(line.split())>2:
            project_name = line
            
        if project_name:
            # Look for Spring 2022 in following lines
            for j in range(i+1, min(i+15, len(lines))):
                next_line = lines[j]
                if '2022' in next_line and ('Spring' in next_line or 'spring' in next_line):
                    # Check if it's a schedule/action line
                    if any(word in next_line for word in ['Begin', 'Complete Design', 'Start', 'Advertise', 'Award', 'Design']):
                        all_projects.append({
                            'Project_Name': project_name,
                            'start_date': '2022-Spring',
                            'doc_id': doc['id']
                        })
                        break

# Remove duplicates
spring_projects = list({p['Project_Name']: p for p in all_projects}.values())

print('__RESULT__:')
print(json.dumps({
    'spring_2022_projects': len(spring_projects),
    'projects': [p['Project_Name'] for p in spring_projects][:15]
}))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:12': ['civic_docs'], 'var_functions.execute_python:16': {'funding_result_type': "<class 'str'>", 'funding_result_preview': 'file_storage/functions.query_db:6.json', 'civic_result_type': "<class 'str'>", 'civic_result_preview': 'file_storage/functions.query_db:10.json'}, 'var_functions.execute_python:18': {'funding_records': 500, 'civic_docs_count': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': 24000}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': 45000}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': 38000}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': 23000}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': 79000}], 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_docs_count': 5, 'total_funding_amount': 28094000, 'sample_project_names': ['2021 Annual Street Maintenance', '2022 Annual Street Maintenance', '2022 Morning View Resurfacing & Storm Drain Improvements', 'Annual Street Maintenance', 'Birdview Avenue Improvements']}, 'var_functions.execute_python:32': {'refs': [{'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring/Summer 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Final Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Advertise: Spring/Summer 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Award Contract and Begin Construction: Spring/Summer 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': 'sending this project out to bid during the Spring of 2022.', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': 'Commission will then review the project in Spring 2022 before final', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Completion Date: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) The project design will commence during the Spring 2022.', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': 'started and is anticipated to be completed by the Spring of 2022.', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01272021-1626.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01272021-1626.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01272021-1626.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03022021-1648.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03022021-1648.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03022021-1648.txt'}, {'line': '(cid:131) Completion Date: Spring 2022', 'file': 'malibucity_agenda__03022021-1648.txt'}, {'line': '(cid:131) Advertise: Spring/Summer 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Final Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': 'Commission will then review the project in Spring 2022 before final', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Begin Design: Late Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Advertise: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Advertise: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Completion Date: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': 'beginning in Spring 2022.', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': 'completed by Spring 2022.', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}], 'count': 44}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
