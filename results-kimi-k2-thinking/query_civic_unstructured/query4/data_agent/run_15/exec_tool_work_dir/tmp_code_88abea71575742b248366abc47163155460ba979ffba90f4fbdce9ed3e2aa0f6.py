code = """import json
import re

# Load data files
civic_docs_file = locals()['var_functions.query_db:20']
funding_file = locals()['var_functions.query_db:24']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Create funding lookup dictionary
funding_lookup = {}
for record in funding_data:
    proj_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_lookup[proj_name] = amount

# Function to check if text contains Spring 2022 date
def has_spring_2022(text):
    if not text or not isinstance(text, str):
        return False
    
    if '2022' not in text:
        return False
    
    # Check for Spring months
    spring_indicators = ['spring', 'march', 'april', 'may', 'mar', 'apr', 'may']
    text_lower = text.lower()
    
    # Check numeric months
    if any(m in text for m in ['2022-03', '2022-04', '2022-05', '2022/03', '2022/04', '2022/05']):
        return True
    
    # Check named months
    if any(ind in text_lower for ind in spring_indicators):
        return True
    
    return False

# Extract potential Spring 2022 projects
potential_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        # Skip short lines and lines that look like headers/footers
        if len(line) < 10 or len(line) > 150:
            continue
        
        # Skip common non-project lines
        skip_words = ['Agenda', 'Commission', 'Prepared by', 'Approved by', 'Subject:', 'RECOMMENDED', 'DISCUSSION:', 'To:', 'From:', 'Date:', 'Meeting date:']
        if any(skip in line for skip in skip_words):
            continue
        
        # Check if line mentions both a project and 2022 spring date
        project_words = ['project', 'improvements', 'repairs', 'system', 'facility', 'infrastructure']
        has_project_word = any(pw in line.lower() for pw in project_words)
        
        if has_project_word:
            if has_spring_2022(line):
                # Clean up line
                proj_name = re.sub(r'^[\d\-\*\.]+\s*', '', line)
                proj_name = proj_name.strip()
                if proj_name:
                    potential_projects.add(proj_name)

# Projects explicitly with 2022 in name
for proj_name in funding_lookup.keys():
    if '2022' in proj_name and has_spring_2022(proj_name):
        potential_projects.add(proj_name)

# Match with funding data
confirmed_projects = {}
total_funding = 0

for proj in potential_projects:
    # Direct match
    if proj in funding_lookup:
        amount = funding_lookup[proj]
        confirmed_projects[proj] = amount
        total_funding += amount
    else:
        # Try partial matching
        proj_clean = proj.lower().replace('project', '').replace('improvements', '').strip()
        
        for fund_proj in funding_lookup:
            fund_clean = fund_proj.lower().replace('project', '').replace('improvements', '').strip()
            # Check if one contains the other
            if proj_clean and fund_clean:
                if proj_clean in fund_clean or fund_clean in proj_clean:
                    # Avoid duplicates
                    if fund_proj not in confirmed_projects:
                        amount = funding_lookup[fund_proj]
                        confirmed_projects[fund_proj] = amount
                        total_funding += amount
                    break

output = {
    'count': len(confirmed_projects),
    'total_funding': total_funding,
    'projects': list(confirmed Projects.keys())
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_docs_sample': "{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\"}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'civic_docs_loaded': 5, 'first_doc_sample': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
