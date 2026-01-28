code = """import json, re

# Load both datasets
with open(locals()['var_functions.query_db:24'], 'r') as f:
    all_funding = json.load(f)

with open(locals()['var_functions.query_db:36'], 'r') as f:
    civic_docs = json.load(f)

# Create funding map
funding_map = {item['Project_Name']: int(item['Amount']) for item in all_funding}

# Identify Spring 2022 projects from funding data
spring_2022_funding = {}
for name, amount in funding_map.items():
    # Projects with 2022 in name
    if '2022' in name:
        spring_2022_funding[name] = amount
    # Projects with Spring indicators
    elif any(term in name.lower() for term in ['spring', 'march', 'april', 'may']) and '2022' in name:
        spring_2022_funding[name] = amount

# Direct answer
result = {
    'count': len(spring_2022_funding),
    'total': sum(spring_2022_funding.values())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_docs_sample': "{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\"}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'civic_docs_loaded': 5, 'first_doc_sample': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.list_db:38': ['civic_docs'], 'var_functions.query_db:40': [{'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}]}

exec(code, env_args)
