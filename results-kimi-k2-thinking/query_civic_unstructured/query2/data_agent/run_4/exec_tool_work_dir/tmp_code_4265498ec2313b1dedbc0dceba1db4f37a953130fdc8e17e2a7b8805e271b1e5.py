code = """import json
import re

# Load the data from file paths
civic_path = locals()['var_functions.query_db:72']
funding_path = locals()['var_functions.query_db:6']

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Convert amounts to integers
for rec in funding_data:
    rec['Amount'] = int(rec['Amount'])

# Find park-related projects completed in 2022
park_projects_2022 = []
park_keywords = ['park', 'playground', 'walkway', 'green street', 'shade', 'bluffs', 'arbors', 'benches', 'workout', 'skate park']

for doc in civic_docs:
    text = doc['text']
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    for i, line in enumerate(lines):
        # Look for completion in 2022
        if '2022' in line and 'completed' in line.lower():
            # Look back for project name (up to 5 lines)
            for j in range(max(0, i-5), i):
                prev_line = lines[j]
                
                # Skip non-project lines
                if len(prev_line) > 100 or '(cid:' in prev_line or prev_line.startswith('Page'):
                    continue
                
                # Check if it's park-related
                prev_line_lower = prev_line.lower()
                if any(keyword in prev_line_lower for keyword in park_keywords):
                    # Clean up project name
                    clean_name = re.sub(r'\(cid:\d+\)', '', prev_line).strip()
                    clean_name = clean_name.replace('\u2013', '-').replace('\u201c', '"').replace('\u201d', '"')
                    clean_name = ' '.join(clean_name.split())
                    
                    if len(clean_name) > 8:
                        park_projects_2022.append({
                            'name': clean_name,
                            'completion_line': line,
                            'doc_id': doc['_id']
                        })
                        break

# Match with funding data
matched_funding = []

for park_project in park_projects_2022:
    project_name = park_project['name']
    project_name_lower = project_name.lower()
    
    for fund in funding_data:
        fund_name = fund['Project_Name']
        fund_name_lower = fund_name.lower()
        
        # Check for name match (one contains the other)
        if (project_name_lower in fund_name_lower or fund_name_lower in project_name_lower):
            matched_funding.append({
                'project_name': project_name,
                'funding_record_name': fund_name,
                'amount': fund['Amount'],
                'funding_source': fund['Funding_Source']
            })
            break

# Calculate total funding
total_funding = sum(f['amount'] for f in matched_funding)

result = {
    'total_funding_2022_park_projects': total_funding,
    'number_of_projects': len(matched_funding),
    'projects': matched_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:4', 'var_functions.query_db:6', '__builtins__', 'json'], 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_sample_keys': ['_id', 'filename', 'text'], 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.execute_python:36': {'civic_type': "<class 'str'>", 'funding_type': "<class 'str'>", 'civic_is_file': True, 'funding_is_file': True}, 'var_functions.execute_python:44': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_text': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:'}, 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json'}

exec(code, env_args)
