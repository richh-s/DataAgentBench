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
        
        # Find potential disaster-related projects
        # Project names often appear in disaster/FEMA sections
        if 'Disaster' in text or 'FEMA' in text or 'Fire' in text or 'CalOES' in text or 'CalJPIA' in text:
            lines = text.split('\n')
            
            in_disaster_section = False
            
            for i, line in enumerate(lines):
                line = line.strip()
                
                # Check if we're entering disaster-related sections
                if any(section in line for section in ['Disaster Recovery', 'FEMA', 'CalOES Project', 'CalJPIA Project', 'Woolsey Fire']):
                    in_disaster_section = True
                    continue
                
                # Skip common non-project lines
                if not line or len(line) < 10:
                    continue
                    
                # Skip metadata lines
                if any(skip in line for skip in ['To:', 'Prepared', 'Approved', 'Date:', 'Meeting', 'Subject:', 'RECOMMENDED', 'DISCUSSION:', 'Page', 'Agenda', 'Commission', 'Chair', 'Members']):
                    continue
                
                # Skip section headers
                if any(header in line for header in ['Capital Improvement', 'Disaster Recovery', 'Projects (Design)', 'Projects (Construction)', 'Projects (Not Started)']):
                    continue
                
                # Check if this looks like a project name (not a bullet/update line)
                if not line.startswith('(') and not line.startswith('•'):
                    # Check if next line has project details
                    if i + 1 < len(lines):
                        next_line = lines[i + 1].strip()
                        if next_line.startswith('(') or 'Updates:' in next_line or 'Project' in next_line or 'Schedule' in next_line:
                            
                            # Look for start date in following lines
                            start_date = None
                            for j in range(i+1, min(i+8, len(lines))):
                                detail_line = lines[j]
                                # Look for date patterns like 2022, 2022-Spring, etc.
                                date_match = re.search(r'(\d{4})(?:\s*(?:-|)(?:Spring|Summer|Fall|Winter|[A-Za-z]+))?', detail_line)
                                if date_match:
                                    year = int(date_match.group(1))
                                    if year == 2022:
                                        start_date = date_match.group(0)
                                        break
                            
                            if start_date:  # Only add if it has a 2022 start date
                                projects.append({
                                    'Project_Name': line.strip(),
                                    'start_date': start_date,
                                    'type': 'disaster',
                                    'document_filename': filename
                                })
    
    return projects

# Extract projects starting in 2022 from civic documents
disaster_projects_2022 = extract_projects_from_docs(civic_docs)

# Create a DataFrame for easier processing
projects_df = pd.DataFrame(disaster_projects_2022)

# Create funding DataFrame
funding_df = pd.DataFrame(funding_data)

print('__RESULT__:')
print(json.dumps({
    'disaster_projects_2022_count': len(disaster_projects_2022),
    'sample_disaster_projects': disaster_projects_2022[:10],
    'funding_records_count': len(funding_data)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'sample_filename': 'malibucity_agenda_03222023-2060.txt', 'sample_text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'sample_funding_record': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}}

exec(code, env_args)
