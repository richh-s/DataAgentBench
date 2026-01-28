code = """import json
import re

# Load the datasets
with open(locals()['var_functions.query_db:42'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_functions.query_db:44'], 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup dictionary
funding_dict = {}
for record in funding_data:
    proj_name = record.get('Project_Name', '')
    amount = int(str(record.get('Amount', 0)))
    if proj_name and amount > 0:
        funding_dict[proj_name] = funding_dict.get(proj_name, 0) + amount

# Extract Spring 2022 projects from civic documents
spring_2022_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Look for Spring 2022 date patterns
    # Patterns to match: 2022-Spring, 2022-March, 2022-April, 2022-May, etc.
    spring_patterns = [
        r'2022\s*-\s*Spring',
        r'2022\s*-\s*March',
        r'2022\s*-\s*April', 
        r'2022\s*-\s*May',
        r'2022\s*-\s*03',
        r'2022\s*-\s*04',
        r'2022\s*-\s*05',
        r'2022\s*March',
        r'2022\s*April',
        r'2022\s*May'
    ]
    
    # Check if document contains Spring 2022 dates
    has_spring_2022 = any(re.search(pattern, text, re.IGNORECASE) for pattern in spring_patterns)
    
    if has_spring_2022:
        # Split into lines and find project names
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if not line or len(line) > 100:  # Skip empty and very long lines
                continue
            
            # Skip header/footer lines
            skip_terms = ['page', 'agenda', 'item', 'public works', 'commission', 'prepared by', 'approved by', 'date prepared', 'meeting date']
            if any(term in line.lower() for term in skip_terms):
                continue
            
            # Look for project names (typically uppercase first letter, not too long)
            if len(line) > 5 and line[0].isupper():
                # Check context after this line for Spring 2022
                context_lines = lines[i:i+10]  # Look ahead up to 10 lines
                context = ' '.join(context_lines)
                
                # Check if context contains Spring 2022 indicators
                context_has_spring_2022 = any(re.search(pattern, context, re.IGNORECASE) for pattern in spring_patterns)
                
                if context_has_spring_2022:
                    # Additional check: make sure it's not a status/header line
                    if not any(keyword in line.lower() for keyword in ['updates:', 'schedule:', 'status report', 'discussion:', 'recommended action']):
                        spring_2022_projects.add(line)

# Match Spring 2022 projects with funding
matched_projects = []
matched_funding = 0

for proj_name in spring_2022_projects:
    # Exact match
    if proj_name in funding_dict:
        amount = funding_dict[proj_name]
        matched_projects.append({
            'project_name': proj_name,
            'funding': amount
        })
        matched_funding += amount
        continue
    
    # Try fuzzy matching for projects with suffixes like (FEMA Project)
    proj_base = proj_name.split(' (')[0]
    for funded_proj in funding_dict:
        # Check if project name matches (exact, or base name match, or partial match)
        if (proj_name == funded_proj or 
            funded_proj.startswith(proj_base + ' (') or
            proj_base.lower() in funded_proj.lower()):
            amount = funding_dict[funded_proj]
            matched_projects.append({
                'project_name': proj_name,
                'matched_funding_name': funded_proj,
                'funding': amount
            })
            matched_funding += amount
            break

# Count unique projects (by base name to avoid double-counting similar variants)
unique_project_bases = set()
for proj in matched_projects:
    base_name = proj['project_name'].split(' (')[0]
    unique_project_bases.add(base_name)

result = {
    'spring_2022_project_count': len(unique_project_bases),
    'total_funding': matched_funding,
    'matched_projects': matched_projects[:10]  # Show first 10 for debugging
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_documents': 5, 'status': 'loaded'}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'funding_records': 500, 'civic_documents': 5, 'status': 'data_loaded'}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': {'civic_docs_loaded': 5, 'funding_records_loaded': 500, 'status': 'ready_to_process'}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'funding_records': 500, 'civic_documents': 3}}

exec(code, env_args)
