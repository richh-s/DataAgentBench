code = """import json

# Load civic documents and funding data
civic_docs = json.load(open('var_functions.query_db:72'))
funding_data = json.load(open('var_functions.query_db:76'))

# Convert amounts to integers
for rec in funding_data:
    rec['Amount'] = int(rec['Amount'])

# Find park-related projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        # Check for 2022 completion
        if '2022' in line and 'completed' in line.lower():
            # Look back for project name
            for j in range(max(0, i-4), i):
                prev = lines[j].strip()
                # Check if it is park-related and reasonable length
                lower_prev = prev.lower()
                if ('park' in lower_prev or 'playground' in lower_prev or 
                    'walkway' in lower_prev or 'shade' in lower_prev or 'bluffs' in lower_prev):
                    if 10 < len(prev) < 100:
                        # Clean up the name
                        clean_name = prev.strip()
                        park_projects.append(clean_name)

# Match with funding data based on project names
matched_funding = []
for project in park_projects:
    project_lower = project.lower()
    for fund in funding_data:
        fund_name = fund['Project_Name']
        fund_lower = fund_name.lower()
        # Check if names match
        if (project_lower in fund_lower or fund_lower in project_lower):
            matched_funding.append({
                'project_name': project,
                'funding_record_name': fund_name,
                'amount': fund['Amount']
            })
            break

# Calculate total funding
total_funding = sum(f['amount'] for f in matched_funding)

result = {
    'total_funding': total_funding,
    'project_count': len(matched_funding),
    'projects': matched_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:4', 'var_functions.query_db:6', '__builtins__', 'json'], 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_sample_keys': ['_id', 'filename', 'text'], 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.execute_python:36': {'civic_type': "<class 'str'>", 'funding_type': "<class 'str'>", 'civic_is_file': True, 'funding_is_file': True}, 'var_functions.execute_python:44': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_text': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:'}, 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json', 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json'}

exec(code, env_args)
