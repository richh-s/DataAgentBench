code = """import json

# Get the file paths
civic_path = locals()['var_functions.query_db:2']
funding_path = locals()['var_functions.query_db:6']

# Load the data
with open(civic_path) as f:
    civic_docs = json.load(f)
with open(funding_path) as f:
    funding_records = json.load(f)

# Convert amounts to integers
for rec in funding_records:
    rec['Amount'] = int(rec['Amount'])

# Look for completed park projects in 2022
found_projects = []
park_keywords = ['park', 'playground', 'walkway', 'green street', 'shade', 'bluffs', 'arbors', 'benches', 'workout']

for doc in civic_docs:
    lines = doc['text'].split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if '2022' in line and 'completed' in line.lower():
            # Look backwards for project name (max 5 lines)
            for j in range(max(0, i-5), i):
                prev = lines[j].strip()
                if len(prev) < 100 and '(cid:' not in prev and not prev.startswith('Page'):
                    # Check if park-related
                    prev_lower = prev.lower()
                    if any(keyword in prev_lower for keyword in park_keywords):
                        found_projects.append(prev)

# Match with funding records
matched = []
for project_name in found_projects:
    project_lower = project_name.lower()
    for fund in funding_records:
        fund_lower = fund['Project_Name'].lower()
        # Check for match
        if project_lower in fund_lower or fund_lower in project_lower:
            matched.append({
                'project_name': project_name,
                'funding_record': fund['Project_Name'],
                'amount': fund['Amount']
            })
            break

# Calculate total funding
total = sum(m['amount'] for m in matched)

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'projects': matched}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:4', 'var_functions.query_db:6', '__builtins__', 'json'], 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_sample_keys': ['_id', 'filename', 'text'], 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.execute_python:36': {'civic_type': "<class 'str'>", 'funding_type': "<class 'str'>", 'civic_is_file': True, 'funding_is_file': True}, 'var_functions.execute_python:44': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_text': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:'}}

exec(code, env_args)
