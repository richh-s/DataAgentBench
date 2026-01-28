code = """import json
import re

# Get the file paths from the locals() dictionary
civic_docs_file = locals()['var_functions.query_db:20']
funding_file = locals()['var_functions.query_db:6']

# Read the data files
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Let's find disaster-related projects that started in 2022
disaster_project_names = []

for doc in civic_docs:
    text = doc['text']
    
    # Check if document contains disaster indicators and 2022 dates
    if '2022' in text and ('FEMA' in text or 'CalOES' in text or 'CalJPIA' in text):
        # Extract likely project names (lines that are title case or uppercase)
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()
            if len(line) > 0 and (line.istitle() or line.isupper()):
                # Skip non-project headings
                skip_words = ['Subject', 'To:', 'From:', 'Date:', 'Meeting Date:', 'Public Works', 'Commission Meeting', 'Item', 'RECOMMENDED ACTION']
                if any(skip in line for skip in skip_words):
                    continue
                
                # Check if disaster-related
                disaster_indicators = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'fire', 'emergency', 'recovery']
                is_disaster = any(indicator in line for indicator in disaster_indicators)
                
                if is_disaster:
                    disaster_project_names.append(line)

# Remove duplicates
unique_disaster_projects = list(set(disaster_project_names))

print('__RESULT__:')
print(json.dumps({
    'disaster_projects_found': unique_disaster_projects,
    'count': len(unique_disaster_projects)
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_doc_keys': ['_id', 'filename', 'text'], 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
