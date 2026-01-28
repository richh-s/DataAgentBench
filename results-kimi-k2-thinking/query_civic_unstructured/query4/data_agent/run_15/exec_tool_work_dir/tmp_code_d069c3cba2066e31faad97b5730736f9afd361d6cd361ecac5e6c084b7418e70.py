code = """import json
import re

# Load the JSON files into Python objects
civic_file = locals()['var_functions.query_db:36']
funding_2022_file = locals()['var_functions.query_db:40']
all_funding_file = locals()['var_functions.query_db:24']

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_2022_file, 'r') as f:
    funding_2022 = json.load(f)

with open(all_funding_file, 'r') as f:
    all_funding = json.load(f)

# Create funding lookup
funding_lookup = {}
for record in all_funding:
    funding_lookup[record['Project_Name']] = int(record['Amount'])

# Function to check Spring 2022
def is_spring_2022(text):
    if not isinstance(text, str):
        return False
    if '2022' not in text:
        return False
    spring_terms = ['spring', 'march', 'april', 'may']
    has_spring = any(term in text.lower() for term in spring_terms)
    return has_spring

# Find Spring 2022 projects
spring_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) > 15 and any(kw in line for kw in ['Project', 'Improvements', 'Repairs']):
                if '2022' in line:
                    # Check if Spring-related
                    context = ' '.join(lines[max(0, lines.index(line)-3):lines.index(line)+4])
                    if is_spring_2022(context):
                        clean_name = re.sub(r'^[\d*\-.]+\s*', '', line).strip()
                        spring_projects.add(clean_name)

# Check funding records with 2022
for proj_name in funding_lookup.keys():
    if '2022' in proj_name:
        if is_spring_2022(proj_name):
            spring_projects.add(proj_name)

# Match and calculate
matched = {}
total = 0
for proj in spring_projects:
    if proj in funding_lookup:
        matched[proj] = funding_lookup[proj]
        total += funding_lookup[proj]

# Clean up output
output = {'count': len(matched), 'total_funding': total, 'projects': list(matched.items())}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_docs_sample': "{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\"}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'civic_docs_loaded': 5, 'first_doc_sample': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.list_db:38': ['civic_docs'], 'var_functions.query_db:40': [{'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}]}

exec(code, env_args)
