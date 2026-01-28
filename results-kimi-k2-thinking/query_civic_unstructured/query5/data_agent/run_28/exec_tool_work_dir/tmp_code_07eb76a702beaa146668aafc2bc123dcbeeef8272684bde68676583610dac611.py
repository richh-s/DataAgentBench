code = """import json
import re

civic_docs_file = locals()['var_functions.query_db:2']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

funding_file = locals()['var_functions.query_db:6']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

def extract_disaster_projects_from_text(text):
    projects = []
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Look for lines that seem like project names
        if (len(line.split()) >= 2 and 
            (line.istitle() or line.isupper()) and
            not any(keyword in line.lower() for keyword in ['project schedule', 'updates', 'recommended action', 
                                                         'subject', 'to:', 'from:', 'date:', 'meeting date:', 'item'])):
            
            project_name = line
            
            # Check if disaster-related (contains FEMA, CalOES, etc or common disaster terms)
            disaster_indicators = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'fire', 'emergency', 'recovery', 'Woolsey']
            is_disaster = any(indicator.lower() in project_name.lower() for indicator in disaster_indicators)
            
            # Look for 2022 start dates in nearby lines
            found_2022 = False
            for j in range(max(0, i-5), min(len(lines), i+15)):
                context_line = lines[j].strip()
                if '2022' in context_line and any(phase in context_line.lower() for phase in ['complete design', 'advertise', 'begin construction', 'construction', 'start']):
                    found_2022 = True
                    break
            
            if is_disaster and found_2022:
                projects.append(project_name)
    
    return projects

all_projects = []
for doc in civic_docs:
    projects = extract_disaster_projects_from_text(doc['text'])
    all_projects.extend(projects)

print('__RESULT__:')
print(json.dumps({
    'disaster_projects_2022': list(set(all_projects)),
    'total_found': len(set(all_projects))
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
