code = """import json, re

# Load documents
civic_docs = json.load(open(locals()['var_functions.query_db:20']))
funding = json.load(open(locals()['var_functions.query_db:24']))

# Create funding map
funding_map = {}
for item in funding:
    funding_map[item['Project_Name']] = int(item['Amount'])

# Function to find Spring 2022 indicators
spring_2022_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for projects with Spring 2022 dates
    if '2022' in text and ('spring' in text.lower() or 'march' in text.lower() or 'april' in text.lower() or 'may' in text.lower()):
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Look for capitalized project names with keywords
            if any(kw in line for kw in ['Project', 'Improvements', 'Repairs']):
                if '2022' in line:
                    clean_name = re.sub(r'^[\d\*\-.]+\s*', '', line).strip()
                    if clean_name and len(clean_name) > 15:
                        spring_2022_projects.add(clean_name)

# Add anything from funding with 2022 in name
for pname in funding_map.keys():
    if '2022' in pname:
        spring_2022_projects.add(pname)

# Match with funding
matched = {}
total = 0
for proj in spring_2022_projects:
    if proj in funding_map:
        matched[proj] = funding_map[proj]
        total += funding_map[proj]

print('__RESULT__:')
print(json.dumps({'count': len(matched), 'total': total, 'projects': list(matched.items())[:8]}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_docs_sample': "{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\"}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'civic_docs_loaded': 5, 'first_doc_sample': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
