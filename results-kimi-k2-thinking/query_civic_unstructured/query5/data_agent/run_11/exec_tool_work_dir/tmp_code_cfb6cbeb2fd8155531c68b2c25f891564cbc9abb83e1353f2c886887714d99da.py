code = """import json
import pandas as pd
import re

# Load civic documents
civic_file_path = locals()['var_functions.query_db:2']
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_file_path = locals()['var_functions.query_db:12']
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Function to extract project information from civic documents
def extract_projects_from_docs(docs):
    projects = []
    
    for doc in docs:
        text = doc.get('text', '')
        filename = doc.get('filename', '')
        
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            if not line or len(line) < 10:
                continue
            
            # Skip metadata and headers
            if any(marker in line for marker in ['To:', 'Prepared', 'Approved', 'Date:']):
                continue
            if any(marker in line for marker in ['Meeting', 'Subject:', 'RECOMMENDED', 'DISCUSSION:']):
                continue
            if any(marker in line for marker in ['Page', 'Agenda', 'Commission', 'Chair']):
                continue
            
            # Skip section headers
            if 'Capital Improvement' in line or 'Disaster Recovery' in line:
                continue
            if 'Projects (Design)' in line or 'Projects (Construction)' in line:
                continue
            if 'Projects (Not Started)' in line:
                continue
            
            # Look for disaster-related project names
            # Check if line contains disaster keywords and could be a project name
            if any(keyword in line for keyword in ['FEMA', 'CalOES', 'CalJPIA', '(FEMA', 'Fire']):
                # Check next line for project details
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    if next_line.startswith('(') or 'Updates:' in next_line or 'Project Schedule:' in next_line:
                        # Look for 2022 date
                        for j in range(i, min(i+8, len(lines))):
                            detail_line = lines[j]
                            if '2022' in detail_line:
                                # Check adjacent lines too for date
                                projects.append({
                                    'Project_Name': line.strip(),
                                    'type': 'disaster',
                                    'document_filename': filename
                                })
                                break
    
    return projects

# Extract disaster projects
disaster_projects = extract_projects_from_docs(civic_docs)

print('__RESULT__:')
print(json.dumps({
    'disaster_projects_found': len(disaster_projects),
    'sample_disaster_projects': disaster_projects[:10],
    'total_funding_records': len(funding_data)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'sample_filename': 'malibucity_agenda_03222023-2060.txt', 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_funding_record': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}}

exec(code, env_args)
