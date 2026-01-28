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
    
    spring_terms = ['spring', 'march', 'april', 'may', 'mar', 'apr', 'may']
    date_lower = date_str.lower()
    
    # Check month numbers 03, 04, 05
    if any(f'2022-{month:02d}' in date_str or f'2022/{month:02d}' in date_str for month in [3,4,5]):
        return True
    
    # Check spring terms
    if any(term in date_lower for term in spring_terms):
        return True
    
    return False

# Extract projects from civic docs
spring_projects = set()
project_patterns = [
    r'^\s*([A-Z][^\n\.\(]{10,100}?(?:Project|Improvements|Repairs|System|Facility|Infrastructure)[^\n\.\(]{0,50})\s*$',
]

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        if len(line) < 10 or len(line) > 150:
            continue
        
        # Check if line looks like a project name
        project_indicators = ['project', 'improvements', 'repairs', 'system', 'facility', 'infrastructure']
        has_project = any(indicator in line.lower() for indicator in project_indicators)
        
        # Check for capital letters at start (title case)
        has_title_case = line and line[0].isupper()
        
        if has_project and has_title_case:
            # Look for date in nearby text (current line and surrounding lines)
            context = ' '.join(lines[max(0, lines.index(line)-2):min(len(lines), lines.index(line)+3)])
            
            # Check for Spring 2022 dates
            if is_spring_2022(context):
                # Clean project name
                proj_name = re.sub(r'^[\-\u2022\u00b7\*\d\.\s]+', '', line)
                proj_name = re.sub(r'\s+', ' ', proj_name).strip()
                spring_projects.add(proj_name)

# Also extract from the structured parts of documents
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for patterns like "Project Schedule:" or "Complete Design:" with dates
    schedule_sections = re.findall(r'Project Schedule[^\n]*\n([^\n]*(?:2022)[^\n]*)', text, re.IGNORECASE)
    
    for section in schedule_sections:
        if is_spring_2022(section):
            # Find project name before this section
            before_section = text[:text.find(section)]
            project_matches = re.findall(r'^\s*([A-Z][^\n\.\(]{10,80}?(?:Project|Improvements|Repairs|System|Facility|Infrastructure)[^\n\.\(]{0,30})\s*$', before_section, re.MULTILINE)
            if project_matches:
                proj_name = project_matches[-1].strip()
                spring_projects.add(proj_name)

print('__RESULT__:')
print(json.dumps({
    'spring_projects_extracted': len(spring_projects),
    'spring_projects_list': list(spring_projects)[:30]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_docs_sample': "{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\"}}

exec(code, env_args)
