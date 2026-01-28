code = """import json

civic_docs_file = locals()['var_functions.query_db:20']
funding_file = locals()['var_functions.query_db:6']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Match funding records with disaster-related projects
disaster_projects_funding = {}

for fund in funding_data:
    proj_name = fund['Project_Name']
    # Check if project name contains disaster indicators
    disaster_indicators = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'fire', 'emergency', 'recovery']
    is_disaster = any(indicator in proj_name for indicator in disaster_indicators)
    
    if is_disaster:
        amount = int(fund['Amount'])
        disaster_projects_funding[proj_name] = disaster_projects_funding.get(proj_name, 0) + amount

total_funding = sum(disaster_projects_funding.values())

print('__RESULT__:')
print(json.dumps({
    'total_disaster_funding': total_funding,
    'disaster_projects_count': len(disaster_projects_funding)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
