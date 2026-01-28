code = """import json
import re

# Load the data files
civic_docs = json.load(open(locals()['var_functions.query_db:20']))
funding_data = json.load(open(locals()['var_functions.query_db:24']))

# Create funding lookup map
funding_map = {}
for item in funding_data:
    funding_map[item['Project_Name']] = int(item['Amount'])

# Helper function to detect Spring 2022
def is_spring_2022(text):
    if not isinstance(text, str):
        return False
    if '2022' not in text:
        return False
    # Check for spring indicators
    spring_terms = ['spring', 'march', 'april', 'may']
    spring_numeric = ['2022-03', '2022-04', '2022-05']
    lower_text = text.lower()
    has_spring_term = any(term in lower_text for term in spring_terms)
    has_spring_number = any(num in text for num in spring_numeric)
    return has_spring_term or has_spring_number

# Extract projects from civic documents
springProjects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) < 15 or len(line) > 150:
            continue
        
        # Skip non-project lines
        skip_terms = ['Agenda', 'Commission', 'Prepared by', 'Approved by', 'Subject:', 'To:', 'From:']
        if any(term in line for term in skip_terms):
            continue
        
        # Check for project keywords
        project_terms = ['project', 'improvements', 'repairs', 'system', 'facility', 'infrastructure']
        has_project = any(term in line.lower() for term in project_terms)
        
        if has_project:
            # Check for Spring 2022 in this line or nearby context
            context = ' '.join(lines[max(0, i-5):min(len(lines), i+6)])
            if '2022' in line and is_spring_2022(line):
                proj_name = re.sub(r'^[\d\*\-.]+\s*', '', line).strip()
                if proj_name and len(proj_name) > 10:
                    springProjects.add(proj_name)
            elif is_spring_2022(context):
                proj_name = re.sub(r'^[\d\*\-.]+\s*', '', line).strip()
                if proj_name and len(proj_name) > 10:
                    springProjects.add(proj_name)

# Also include funding records from 2022 Spring
for proj_name in funding_map.keys():
    if '2022' in proj_name and 'spring' in proj_name.lower():
        springProjects.add(proj_name)

# Clean up the project list
finalProjects = set()
for proj in springProjects:
    clean_proj = re.sub(r'(cid:\d+)', '', proj).strip()
    clean_proj = re.sub(r'\s+', ' ', clean_proj)
    if len(clean_proj) > 10 and 'updates' not in clean_proj.lower():
        finalProjects.add(clean_proj)

# Match with funding and calculate totals
matchedProjects = {}
totalFunding = 0

for proj in finalProjects:
    if proj in funding_map:
        amount = funding_map[proj]
        matchedProjects[proj] = amount
        totalFunding += amount
    else:
        # Try fuzzy matching
        proj_clean = proj.lower().replace('project', '').strip()
        for fund_proj in funding_map:
            fund_clean = fund_proj.lower().replace('project', '').strip()
            if proj_clean in fund_clean or fund_clean in proj_clean:
                if fund_proj not in matchedProjects:
                    amount = funding_map[fund_proj]
                    matchedProjects[fund_proj] = amount
                    totalFunding += amount
                break

result = {
    'projectCount': len(matchedProjects),
    'totalFunding': totalFunding,
    'projects': list(matchedProjects.items())[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_docs_sample': "{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\"}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'civic_docs_loaded': 5, 'first_doc_sample': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
