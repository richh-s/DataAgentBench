code = """import json, re, pandas as pd

# Load funding data
funding = json.load(open('file_storage/functions.query_db:6.json'))
docs = json.load(open('file_storage/functions.query_db:50.json'))

# Build funding lookup
funding_dict = {}
for item in funding:
    funding_dict[item['Project_Name']] = int(item['Amount'])

# Find projects with Spring 2022 start dates
found_projects = []

for doc in docs:
    text = doc['text']
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Look for Spring 2022 in schedule lines
        if '2022' in line and 'Spring' in line:
            # Look backwards for project name
            for j in range(i-1, max(i-8, -1), -1):
                prev = lines[j].strip()
                if prev and len(prev) > 10 and not prev.isupper():
                    # Skip headers
                    if not any(x in prev for x in ['Page', 'Agenda Item', 'To:', 'Prepared by:', 'Subject:', 'RECOMMENDED', 'DISCUSSION:']):
                        # Get actual project name (could be multiple lines up)
                        actual_name = prev
                        
                        # Try to find funding
                        if actual_name in funding_dict:
                            found_projects.append({
                                'name': actual_name,
                                'funding': funding_dict[actual_name]
                            })
                        # Try variations
                        elif actual_name.replace(' Project', '') in funding_dict:
                            found_projects.append({
                                'name': actual_name,
                                'funding': funding_dict[actual_name.replace(' Project', '')]
                            })
                        # Try without parenthetical
                        else:
                            clean_name = re.sub(r'\s+\([^)]*\)$', '', actual_name)
                            if clean_name in funding_dict:
                                found_projects.append({
                                    'name': actual_name,
                                    'funding': funding_dict[clean_name]
                                })
                        break
        i += 1

# Remove duplicates
unique_projects = {}
for p in found_projects:
    if p['name'] not in unique_projects:
        unique_projects[p['name']] = p

final_list = list(unique_projects.values())
total_funding = sum(p['funding'] for p in final_list)

print('__RESULT__:')
print(json.dumps({
    'count': len(final_list),
    'total_funding': total_funding,
    'projects': [p['name'] for p in final_list]
}))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:12': ['civic_docs'], 'var_functions.execute_python:16': {'funding_result_type': "<class 'str'>", 'funding_result_preview': 'file_storage/functions.query_db:6.json', 'civic_result_type': "<class 'str'>", 'civic_result_preview': 'file_storage/functions.query_db:10.json'}, 'var_functions.execute_python:18': {'funding_records': 500, 'civic_docs_count': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': 24000}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': 45000}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': 38000}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': 23000}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': 79000}], 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_docs_count': 5, 'total_funding_amount': 28094000, 'sample_project_names': ['2021 Annual Street Maintenance', '2022 Annual Street Maintenance', '2022 Morning View Resurfacing & Storm Drain Improvements', 'Annual Street Maintenance', 'Birdview Avenue Improvements']}, 'var_functions.execute_python:32': {'refs': [{'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring/Summer 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Final Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Advertise: Spring/Summer 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Award Contract and Begin Construction: Spring/Summer 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': 'sending this project out to bid during the Spring of 2022.', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': 'Commission will then review the project in Spring 2022 before final', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Completion Date: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) The project design will commence during the Spring 2022.', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': 'started and is anticipated to be completed by the Spring of 2022.', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01272021-1626.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01272021-1626.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01272021-1626.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03022021-1648.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03022021-1648.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03022021-1648.txt'}, {'line': '(cid:131) Completion Date: Spring 2022', 'file': 'malibucity_agenda__03022021-1648.txt'}, {'line': '(cid:131) Advertise: Spring/Summer 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Final Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': 'Commission will then review the project in Spring 2022 before final', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Begin Design: Late Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Advertise: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Advertise: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Completion Date: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': 'beginning in Spring 2022.', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': 'completed by Spring 2022.', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}], 'count': 44}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:46': {'funding_records': 500, 'civic_documents': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'sample_civic_keys': ['_id', 'filename', 'text']}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
