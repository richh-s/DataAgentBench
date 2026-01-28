code = """import json
import re
import pandas as pd

# Load funding data
funding_file = locals()['var_functions.query_db:8']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:9']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding dataframe
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Function to check if text indicates Spring 2022
def is_spring_2022(text):
    if not text:
        return False
    
    text_lower = text.lower()
    spring_indicators = [
        '2022-spring', '2022-march', '2022-april', '2022-may',
        'spring 2022', 'march 2022', 'april 2022', 'may 2022'
    ]
    
    return any(indicator in text_lower for indicator in spring_indicators)

# Extract projects from documents
projects_2022_spring = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names (typically not bullet points, have key terms)
        if (line and 
            len(line) > 10 and
            not line.startswith('(') and
            not line.startswith('•') and
            not line.startswith('cid:') and
            line.upper() != line):
            
            # Check if it looks like a project name
            project_keywords = ['project', 'improvement', 'repair', 'drainage', 'resurfacing', 'replacement', 'bridge', 'culvert', 'road', 'street', 'park', '2022', '2023']
            if any(keyword in line.lower() for keyword in project_keywords):
                current_project = line
                
                # Look ahead for date information
                if i + 1 < len(lines):
                    next_lines = '\n'.join(lines[i:i+5])
                    if is_spring_2022(next_lines):
                        projects_2022_spring.append(current_project)

# Remove duplicates
projects_2022_spring = list(set(projects_2022_spring))

print('__RESULT__:')
print(json.dumps({
    'found_projects': projects_2022_spring,
    'count': len(projects_2022_spring)
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_docs': 5, 'sample_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:'}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}], 'sample_civic': 9796}}

exec(code, env_args)
