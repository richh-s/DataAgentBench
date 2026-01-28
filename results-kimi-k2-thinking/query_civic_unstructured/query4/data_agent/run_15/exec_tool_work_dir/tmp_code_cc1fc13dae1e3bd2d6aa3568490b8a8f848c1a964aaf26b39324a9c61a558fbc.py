code = """import json
import re

# Read data files
civic_docs_file = locals()['var_functions.query_db:20']
funding_file = locals()['var_functions.query_db:24']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Create funding lookup
funding_lookup = {}
for record in funding_data:
    proj_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_lookup[proj_name] = amount

# Helper to check if a date string is Spring 2022
def is_spring_2022(date_str):
    if not date_str or not isinstance(date_str, str):
        return False
    
    # Must contain 2022
    if '2022' not in date_str:
        return False
    
    # Check for Spring months
    spring_terms = ['spring', 'march', 'april', 'may', 'mar', 'apr', 'may']
    date_lower = date_str.lower()
    
    # Check for month numbers
    for month in ['03', '3', '04', '4', '05', '5']:
        if f'2022-{month}' in date_str or f'2022/{month}' in date_str or f'2022 {month}' in date_str:
            return True
    
    # Check for spring terms
    if any(term in date_lower for term in spring_terms):
        return True
    
    return False

# Extract projects from civic documents
spring_2022_projects = {}

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find all project title lines (start with capital letter/number, contain project keywords)
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) < 10 or len(line) > 150:
            continue
        
        # Check if line looks like a project name
        has_title = line[0].isupper() or line[0].isdigit()
        
        project_keywords = ['project', 'improvements', 'repairs', 'system', 'facility', 'infrastructure', 'program']
        has_keyword = any(keyword in line.lower() for keyword in project_keywords)
        
        if has_title and has_keyword:
            # Clean up the project name
            proj_name = re.sub(r'^[\-\u2022\u00b7\*\d\.\s]+', '', line)
            proj_name = re.sub(r'\s+', ' ', proj_name).strip()
            
            # Get context window around this line to look for dates
            context_start = max(0, i-5)
            context_end = min(len(lines), i+10)
            context = ' '.join(lines[context_start:context_end])
            
            # Check if Spring 2022 date appears in context
            if is_spring_2022(context):
                spring_2022_projects[proj_name] = True
            # Also check the project name itself (e.g., "2022 Morning View...")
            elif is_spring_2022(proj_name):
                spring_2022_projects[proj_name] = True

# Also check for projects with explicit "2022" in their name (likely started in 2022)
for proj_name in funding_lookup.keys():
    if '2022' in proj_name:
        # Check if project name suggests Spring (Morning, View, Spring, etc.)
        # For now, include all 2022 projects
        spring_2022_projects[proj_name] = True

filtered_projects = {}
for proj in spring_2022_projects:
    # Filter out obviously wrong ones
    if any(keyword in proj.lower() for keyword in ['project schedule', 'updates', 'complete design']):
        continue
    if '2023' in proj and '2022' not in proj:
        continue
    filtered_projects[proj] = True

# Match with funding and calculate totals
project_funding = {}
total_funding = 0
matched_count = 0

for proj_name in filtered_projects:
    # Direct match
    if proj_name in funding_lookup:
        amount = funding_lookup[proj_name]
        project_funding[proj_name] = amount
        total_funding += amount
        matched_count += 1
    else:
        # Try to find partial matches
        for fund_proj in funding_lookup:
            # Normalize names for comparison
            proj_norm = proj_name.lower().replace('project', '').replace('improvements', '').strip()
            fund_norm = fund_proj.lower().replace('project', '').replace('improvements', '').strip()
            
            # Check if they match substantially
            if proj_norm and fund_norm and (proj_norm in fund_norm or fund_norm in proj_norm):
                if abs(len(proj_norm) - len(fund_norm)) < 20:  # Similar length
                    amount = funding_lookup[fund_proj]
                    project_funding[proj_name] = amount
                    total_funding += amount
                    matched_count += 1
                    break

print('__RESULT__:')
print(json.dumps({
    'spring_2022_project_count': len(filtered_projects),
    'matched_with_funding': matched_count,
    'total_funding': total_funding,
    'projects_with_funding': project_funding
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_docs_sample': "{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\"}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'civic_docs_loaded': 5, 'first_doc_sample': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
