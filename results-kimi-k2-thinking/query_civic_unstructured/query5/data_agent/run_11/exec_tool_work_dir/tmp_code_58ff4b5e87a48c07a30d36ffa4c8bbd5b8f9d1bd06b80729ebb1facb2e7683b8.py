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

# Parse civic documents to extract project information
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project patterns: project names are typically on separate lines
    # and may be followed by project details
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Look for project names - they typically don't start with bullet points
        # and are followed by project details
        if (line and not line.startswith('(') and not line.startswith('\u2022') and 
            not line.startswith('\u00b7') and not line.startswith('Page') and
            not line.startswith('Agenda') and not any(line.startswith(str(num)) for num in range(10)) and
            len(line) > 10 and not line.startswith('To:') and not line.startswith('Prepared') and
            not line.startswith('Approved') and not line.startswith('Date') and
            not line.startswith('Meeting') and not line.startswith('Subject:') and
            not line.startswith('RECOMMENDED') and not line.startswith('DISCUSSION:') and
            not line.startswith('Capital Improvement') and not line.startswith('Disaster Recovery')):
            
            # Check if next line starts with project details (bullet points or parenthesis)
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if next_line.startswith('(') or 'Updates:' in next_line or 'Project Schedule:' in next_line:
                    current_project = line
                    
                    # Determine type (capital or disaster)
                    project_type = 'capital'  # default
                    if ('FEMA' in line or 'CalOES' in line or 'CalJPIA' in line or 
                        'Disaster' in text or 'disaster' in text.lower()):
                        # Check context - if this appears in disaster section
                        if 'Disaster' in text[:text.find(line)][-200:]:
                            project_type = 'disaster'
                    
                    # Look for start date information
                    start_date = None
                    # Search for date patterns in following lines
                    for j in range(i+1, min(i+10, len(lines))):
                        detail_line = lines[j]
                        if 'Complete Design:' in detail_line or 'Advertise:' in detail_line or 'Begin Construction:' in detail_line:
                            match = re.search(r'(\d{4})\s*(Spring|Summer|Fall|Winter)?', detail_line)
                            if match:
                                start_date = match.group(0)
                                break
                        elif '2022' in detail_line or '2023' in detail_line:
                            match = re.search(r'(\d{4})\s*(Spring|Summer|Fall|Winter)?', detail_line)
                            if match:
                                start_date = match.group(0)
                                break
                    
                    projects.append({
                        'Project_Name': current_project,
                        'type': project_type,
                        'st': start_date,
                        'document_filename': filename
                    })

print('__RESULT__:')
print(json.dumps({
    'total_projects_found': len(projects),
    'sample_projects': projects[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'sample_filename': 'malibucity_agenda_03222023-2060.txt', 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_funding_record': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}}

exec(code, env_args)
