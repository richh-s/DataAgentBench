code = """import json, re, pandas as pd

# Load data from files
with open('file_storage/functions.query_db:6.json') as f:
    funding_data = json.load(f)

with open('file_storage/functions.query_db:10.json') as f:
    civic_docs = json.load(f)

# Create DataFrame for funding
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Find Spring 2022 projects from civic documents
spring_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line: continue
        
        # Look for spring 2022 mentions
        if '2022' in line and ('Spring' in line or 'spring' in line):
            # Look backwards for project name (within 3 lines)
            for j in range(i-1, max(i-5, -1), -1):
                prev = lines[j].strip()
                if prev and not prev.isupper() and len(prev) > 10:
                    # Skip headers
                    if any(x in prev for x in ['Page', 'Agenda', 'To:', 'Prepared', 'Subject:', 'RECOMMENDED', 'DISCUSSION:']):
                        continue
                    spring_projects.append(prev)
                    break

# Get unique project names
unique_projects = list(set(spring_projects))

# Match with funding data
matched_funding = []
for proj in unique_projects:
    # Direct match
    matches = funding_df[funding_df['Project_Name'] == proj]
    if not matches.empty:
        for _, row in matches.iterrows():
            matched_funding.append({'name': proj, 'amount': int(row['Amount'])})
    else:
        # Try base name without suffix
        base = re.sub(r'\s+\([^)]*\)$', '', proj)
        matches = funding_df[funding_df['Project_Name'].str.contains(base, case=False, na=False)]
        if not matches.empty:
            for _, row in matches.iterrows():
                matched_funding.append({'name': proj, 'amount': int(row['Amount'])})

# Calculate totals
if matched_funding:
    total = sum(p['amount'] for p in matched_funding)
    count = len(matched_funding)
else:
    total = 0
    count = 0

result = {
    'num_projects': count,
    'total_funding': total,
    'projects': [p['name'] for p in matched_funding][:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:12': ['civic_docs'], 'var_functions.execute_python:16': {'funding_result_type': "<class 'str'>", 'funding_result_preview': 'file_storage/functions.query_db:6.json', 'civic_result_type': "<class 'str'>", 'civic_result_preview': 'file_storage/functions.query_db:10.json'}, 'var_functions.execute_python:18': {'funding_records': 500, 'civic_docs_count': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': 24000}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': 45000}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': 38000}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': 23000}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': 79000}], 'funding_columns': ['Funding_ID', 'Project_Name', 'Funding_Source', 'Amount']}, 'var_functions.execute_python:22': {'funding_records': 500, 'civic_docs_count': 5, 'total_funding_amount': 28094000, 'sample_project_names': ['2021 Annual Street Maintenance', '2022 Annual Street Maintenance', '2022 Morning View Resurfacing & Storm Drain Improvements', 'Annual Street Maintenance', 'Birdview Avenue Improvements']}, 'var_functions.execute_python:32': {'refs': [{'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring/Summer 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Final Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Advertise: Spring/Summer 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Award Contract and Begin Construction: Spring/Summer 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': 'sending this project out to bid during the Spring of 2022.', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': 'Commission will then review the project in Spring 2022 before final', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Completion Date: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) The project design will commence during the Spring 2022.', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': 'started and is anticipated to be completed by the Spring of 2022.', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01262022-1835.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__01272021-1626.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01272021-1626.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__01272021-1626.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03022021-1648.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03022021-1648.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03022021-1648.txt'}, {'line': '(cid:131) Completion Date: Spring 2022', 'file': 'malibucity_agenda__03022021-1648.txt'}, {'line': '(cid:131) Advertise: Spring/Summer 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Final Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': 'Commission will then review the project in Spring 2022 before final', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Begin Design: Late Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Advertise: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Advertise: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Completion Date: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': 'beginning in Spring 2022.', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Begin Construction: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': 'completed by Spring 2022.', 'file': 'malibucity_agenda__03232022-1869.txt'}, {'line': '(cid:131) Complete Design: Spring 2022', 'file': 'malibucity_agenda__03232022-1869.txt'}], 'count': 44}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
