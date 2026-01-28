code = """import json

# Read the civic documents from file
civic_docs_result = locals()['var_functions.query_db:28']
if isinstance(civic_docs_result, str) and civic_docs_result.endswith('.json'):
    with open(civic_docs_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_result

# Count total documents found with 2022
doc_count = len(civic_docs)

# Look for the specific document and extract text
target_doc = None
for doc in civic_docs:
    if doc.get('filename') == 'malibucity_agenda_03222023-2060.txt':
        target_doc = doc
        break

result = {
    'documents_with_2022': doc_count,
    'target_doc_found': target_doc is not None
}

if target_doc:
    text = target_doc.get('text', '')
    lines = text.split('\n')
    
    # Find all lines with 2022 and Spring/March/April/May
    spring_2022_lines = []
    for i, line in enumerate(lines):
        if '2022' in line:
            if any(season in line for season in ['Spring', 'spring', 'March', 'April', 'May', 'Mar ', 'Apr ', 'May ']):
                spring_2022_lines.append({'line_num': i, 'text': line.strip()})
    
    result['spring_2022_lines'] = spring_2022_lines[:10]
    result['total_spring_2022_refs'] = len(spring_2022_lines)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:8': {'civic_docs_count': 5, 'funding_records_count': 5, 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:21': [{'total_records': '500'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
