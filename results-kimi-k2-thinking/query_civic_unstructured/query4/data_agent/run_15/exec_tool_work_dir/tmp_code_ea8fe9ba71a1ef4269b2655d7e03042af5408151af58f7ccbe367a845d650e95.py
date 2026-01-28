code = """import json
import re

# Load data files
civic_docs_file = locals()['var_functions.query_db:5']
funding_file = locals()['var_functions.query_db:6']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Create funding lookup by project name
funding_lookup = {}
for record in funding_data:
    proj_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_lookup[proj_name] = amount

# Function to check if date indicates Spring 2022
def is_spring_2022(date_str):
    if not date_str or not isinstance(date_str, str):
        return False
    
    if '2022' not in date_str:
        return False
    
    spring_terms = ['spring', 'march', 'april', 'may']
    date_lower = date_str.lower()
    
    # Check month numbers 03, 04, 05
    for month in ['03', '3', '04', '4', '05', '5']:
        if f'2022-{month}' in date_str or f'2022/{month}' in date_str:
            return True
        if f'2022 {month}' in date_str:
            return True
    
    # Check spring terms
    if any(term in date_lower for term in spring_terms):
        return True
    
    return False

# Extract projects from civic docs
spring_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for patterns with dates
    # Find sections that mention both a project and a date
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) < 10 or len(line) > 200:
            continue
        
        # Check if this looks like a project title (starts with capital, has project keywords)
        project_keywords = ['project', 'improvements', 'repairs', 'system', 'facility', 'infrastructure', 'program']
        has_project_keyword = any(keyword in line.lower() for keyword in project_keywords)
        
        # Check if starts with capital letter or number
        starts_proper = line and (line[0].isupper() or line[0].isdigit())
        
        if has_project_keyword and starts_proper:
            # Check if there's a spring 2022 date in this line or nearby lines
            context_window = ' '.join(lines[max(0, i-3):min(len(lines), i+4)])
            
            if is_spring_2022(context_window):
                # Clean up the project name
                proj_name = re.sub(r'^[\-\u2022\u00b7\*\d\.\s]+', '', line)
                proj_name = re.sub(r'(cid:\d+)', '', proj_name)
                proj_name = re.sub(r'\s+', ' ', proj_name).strip()
                
                if proj_name and len(proj_name) > 10:
                    spring_projects.add(proj_name)

# Try to match with funding data
matched_projects = {}
total_funding = 0

for proj in spring_projects:
    # Direct match
    if proj in funding_lookup:
        matched_projects[proj] = funding_lookup[proj]
        total_funding += funding_lookup[proj]
    else:
        # Try fuzzy matching - check if any funding project contains this name or vice versa
        for fund_proj in funding_lookup:
            # Check if one string contains the other (normalized)
            proj_norm = proj.lower().replace('project', '').replace('improvements', '').strip()
            fund_norm = fund_proj.lower().replace('project', '').replace('improvements', '').strip()
            
            if (proj_norm in fund_norm or fund_norm in proj_norm) and len(proj_norm) > 10:
                if fund_proj in matched_projects:
                    continue
                matched_projects[proj] = funding_lookup[fund_proj]
                total_funding += funding_lookup[fund_proj]
                break

print('__RESULT__:')
print(json.dumps({
    'spring_projects_found': len(spring_projects),
    'funding_matches_found': len(matched_projects),
    'total_funding': total_funding,
    'projects': list(spring_projects),
    'matched_with_funding': list(matched_projects.keys())
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_docs_sample': "{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\"}}

exec(code, env_args)
