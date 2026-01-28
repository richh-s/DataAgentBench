code = """import json
import re

# Load civic documents and funding data
civic_docs = json.load(open(locals()['var_functions.query_db:36']))
funding_data = json.load(open(locals()['var_functions.query_db:40']))

# Get the full funding dataset for matching
all_funding = json.load(open(locals()['var_functions.query_db:24']))

# Create a comprehensive funding lookup by project name
funding_lookup = {}
for record in all_funding:
    proj_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_lookup[proj_name] = amount

# Helper function to detect Spring 2022 dates
def is_spring_2022(date_text):
    if not isinstance(date_text, str) or '2022' not in date_text:
        return False
    
    # Check for spring indicators
    spring_indicators = ['spring', 'march', 'april', 'may', 'mar', 'apr', 'may']
    text_lower = date_text.lower()
    
    # Check named spring months
    has_spring_term = any(ind in text_lower for ind in spring_indicators)
    
    # Check numeric spring months (03, 04, 05)
    has_spring_number = any(f'2022-{month:02d}' in date_text or f'2022/{month:02d}' in date_text 
                           for month in [3, 4, 5])
    
    return has_spring_term or has_spring_number

# Extract project information from civic documents
spring_2022_projects = set()
project_info = {}

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    lines = text.split('\n')
    
    # Look for project titles (lines that start with capital letters and contain project keywords)
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip obvious non-project lines
        if len(line) < 15 or len(line) > 200:
            continue
        
        # Skip header/footer lines
        skip_patterns = ['Agenda', 'Commission', 'Prepared by', 'Approved by', 'Subject:', 'To:', 'From:', 'Date:', 'RECOMMENDED', 'DISCUSSION:', 'Page ', 'Item ', 'Chair ', 'Members of']
        if any(pattern in line for pattern in skip_patterns):
            continue
        
        # Check if line contains project keywords
        project_keywords = ['Project', 'Improvements', 'Repairs', 'System', 'Facility', 'Infrastructure', 'Program']
        has_project_keyword = any(keyword in line for keyword in project_keywords)
        
        # Check if line starts with capital letter or number (project identifier)
        starts_with_title = line and (line[0].isupper() or line[0].isdigit())
        
        if has_project_keyword and starts_with_title:
            # Look for Spring 2022 dates in surrounding context
            context_lines = lines[max(0, i-5):min(len(lines), i+6)]
            context_text = ' '.join(context_lines)
            
            # Check if this project has a Spring 2022 date
            if is_spring_2022(context_text):
                # Clean up project name
                clean_name = re.sub(r'^[\d\*\-\u2022\u00b7\s]+', '', line)
                clean_name = re.sub(r'\s+', ' ', clean_name).strip()
                
                # Remove common artifacts
                clean_name = re.sub(r'\(cid:\d+\)', '', clean_name)
                
                if clean_name and '\n' not in clean_name:
                    spring_2022_projects.add(clean_name)

# Also include project names that explicitly have "2022" and spring indicators
for proj_name in funding_lookup.keys():
    if is_spring_2022(proj_name):
        spring_2022_projects.add(proj_name)
    elif '2022' in proj_name and any(term in proj_name.lower() for term in ['annual', 'morning', 'view']):
        # Handle special cases like "2022 Annual Street Maintenance", "2022 Morning View..."
        spring_2022_projects.add(proj_name)

# Match projects with funding data
matched_projects = {}
total_funding = 0

for proj_name in spring_2022_projects:
    # Direct exact match
    if proj_name in funding_lookup:
        amount = funding_lookup[proj_name]
        matched_projects[proj_name] = amount
        total_funding += amount
    else:
        # Try normalized matching (remove common suffixes)
        proj_normalized = proj_name.lower().replace('project', '').replace('improvements', '').replace('repairs', '').strip()
        
        for fund_name in funding_lookup:
            fund_normalized = fund_name.lower().replace('project', '').replace('improvements', '').replace('repairs', '').strip()
            
            # Check if normalized names match substantially
            if (proj_normalized in fund_normalized or fund_normalized in proj_normalized) and len(proj_normalized) > 15:
                if proj_name not in matched_projects:
                    amount = funding_lookup[fund_name]
                    matched_projects[proj_name] = amount
                    total_funding += amount
                break
            # Check for substring matches with key project identifiers
            elif proj_name.split()[0] in fund_name and len(proj_name.split()[0]) > 3:
                if fund_name in funding_lookup:
                    amount = funding_lookup[fund_name]
                    matched_projects[proj_name] = amount
                    total_funding += amount
                    break

# Create final results
result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding,
    'projects': []
}

# Add detailed project information
for proj, amount in sorted(matched_projects.items(), key=lambda x: x[1], reverse=True):
    result['projects'].append({
        'project_name': proj,
        'funding_amount': amount
    })

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_docs_sample': "{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\"}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'civic_docs_loaded': 5, 'first_doc_sample': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.list_db:38': ['civic_docs'], 'var_functions.query_db:40': [{'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}]}

exec(code, env_args)
