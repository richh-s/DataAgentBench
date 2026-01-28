code = """import json

# Access the files from storage
civic_docs_file = locals()['var_functions.query_db:20']
funding_file = locals()['var_functions.query_db:6']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Find all funding records for disaster projects that started in 2022
disaster_2022_projects = {}

# Check each funding record
for fund in funding_data:
    proj_name = fund['Project_Name']
    
    # Check if it's a disaster project (contains FEMA, CalOES, CalJPIA, or has disaster suffixes)
    disaster_indicators = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'fire', 'emergency', 'recovery']
    is_disaster = any(indicator in proj_name for indicator in disaster_indicators)
    
    if is_disaster:
        # Check if the project mentions 2022 in any civic document
        mentions_2022 = False
        for doc in civic_docs:
            if '2022' in doc['text'] and proj_name.split('(')[0].strip() in doc['text']:
                mentions_2022 = True
                break
        
        if mentions_2022:
            amount = int(fund['Amount'])
            key = proj_name
            disaster_2022_projects[key] = disaster_2022_projects.get(key, 0) + amount

# Calculate total funding
total_funding = sum(disaster_2022_projects.values())

print('__RESULT__:')
result = {
    'total_funding': total_funding,
    'num_projects': len(disaster_2022_projects),
    'project_details': disaster_2022_projects
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:30': {'total_disaster_funding': 1410000, 'disaster_projects_count': 27}}

exec(code, env_args)
