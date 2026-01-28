code = """import json
mongo_file = locals()['var_functions.query_db:2']
with open(mongo_file, 'r') as f:
    docs = json.load(f)

# Look for project schedules with Spring 2022 patterns
spring_2022_projects = []

patterns = [
    r'([A-Z][A-Za-z\s\-&]+?)(?=\s*\n).*?(?:advertise|begin construction|complete design|start).*?[\:\-]\s*(spring\s+2022|2022\s+spring|march\s+2022|april\s+2022|may\s+2022)',
    r'(spring\s+2022|2022\s+spring|march\s+2022|april\s+2022|may\s+2022)',
]

import re

for doc in docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Find all Spring 2022 date mentions with context
    for match in re.finditer(r'([A-Za-z\s\-&]+?)(?=\n)', text):
        line = match.group(1).strip()
        if len(line) > 20 and not any(skip in line.lower() for skip in ['public works', 'agenda', 'item', 'to:', 'prepared']):
            # Look ahead for schedule info
            start_pos = match.end()
            context = text[start_pos:start_pos+300].lower()
            
            if any(ind in context for ind in ['spring 2022', '2022-spring', 'march 2022', 'april 2022', 'may 2022']):
                if 'advertise' in context or 'begin construction' in context or 'complete design' in context:
                    spring_2022_projects.append(line)

unique_projects = list(set(spring_2022_projects))
print('Spring 2022 projects found:', len(unique_projects))

result = {
    'count': len(unique_projects), 
    'projects': unique_projects[:15]  # First 15
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': {'key': 'var_functions.query_db:2', 'type': "<class 'str'>", 'length': 38}, 'var_functions.execute_python:18': {'total_docs': 5, 'sample_keys': ['_id', 'filename', 'text'], 'doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 202'}, 'var_functions.query_db:20': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.execute_python:36': {'doc_count': 5}, 'var_functions.execute_python:38': {'spring_2022_docs': 4, 'total_docs': 5}}

exec(code, env_args)
