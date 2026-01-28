code = """import json

# Load MongoDB documents
mongo_file = locals()['var_functions.query_db:2']
with open(mongo_file, 'r') as f:
    docs = json.load(f)

# Load all funding records
funding_file = locals()['var_functions.query_db:48']
with open(funding_file, 'r') as f:
    all_funding = json.load(f)

print('Loaded', len(docs), 'documents and', len(all_funding), 'funding records')

# Look for projects with Spring 2022 start dates
spring_2022_projects = []

for doc in docs:
    text = doc.get('text', '')
    text_lower = text.lower()
    
    # Check if this document mentions Spring 2022 or relevant months
    if '2022' in text_lower and ('spring' in text_lower or 'march' in text_lower or 'april' in text_lower or 'may' in text_lower):
        # Extract lines that look like project names
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            # Skip empty and short lines
            if len(line) < 10:
                continue
            
            # Skip header lines
            lower_line = line.lower()
            header_words = ['public works', 'agenda', 'item', 'to:', 'prepared', 'approved', 'date', 'meeting', 'subject:', 'recommended', 'discussion:', 'page']
            if any(word in lower_line for word in header_words):
                continue
            
            # Look for project-like lines (contain capital letters, reasonable length)
            if len(line) < 100 and any(c.isupper() for c in line):
                # Check if this project has schedule info following it
                next_lines = '\n'.join(lines[i:i+15])
                next_lower = next_lines.lower()
                
                # Check for Spring 2022 indicators
                spring_indicators = ['spring 2022', '2022-spring', 'march 2022', 'april 2022', 'may 2022']
                has_spring_date = any(indicator in next_lower for indicator in spring_indicators)
                
                if has_spring_date:
                    spring_2022_projects.append(line)

# Remove duplicates
deduplicated_projects = []
seen = set()
for proj in spring_2022_projects:
    if proj not in seen:
        seen.add(proj)
        deduplicated_projects.append(proj)

print('Found', len(deduplicated_projects), 'unique projects starting in Spring 2022')

# Import re for name normalization
import re

def normalize_project_name(name):
    n = name.lower().strip()
    n = re.sub(r'\s+', ' ', n)
    n = re.sub(r'\([^)]*\)', '', n)
    return n.strip()

# Create lookup for funding records
funding_lookup = {}
for fund in all_funding:
    normalized = normalize_project_name(fund['Project_Name'])
    funding_lookup[normalized] = fund

# Match projects with funding
matched_projects = []
for project_name in deduplicated_projects:
    normalized_proj = normalize_project_name(project_name)
    
    # Direct match
    if normalized_proj in funding_lookup:
        matched_projects.append({
            'project_name': project_name,
            'funding_record': funding_lookup[normalized_proj]
        })
    else:
        # Try partial matching
        for fund_norm, fund_record in funding_lookup.items():
            if (normalized_proj in fund_norm or fund_norm in normalized_proj) and abs(len(normalized_proj) - len(fund_norm)) < 25:
                matched_projects.append({
                    'project_name': project_name,
                    'funding_record': fund_record
                })
                break

# Calculate total funding
total_funding = sum(int(project['funding_record']['Amount']) for project in matched_projects)

# Prepare final results
final_results = {
    'spring_2022_projects_count': len(matched_projects),
    'total_funding': total_funding,
    'matched_projects': [
        {
            'project_name': p['project_name'],
            'funding_name': p['funding_record']['Project_Name'],
            'amount': int(p['funding_record']['Amount']),
            'source': p['funding_record']['Funding_Source']
        }
        for p in matched_projects
    ]
}

print('__RESULT__:')
print(json.dumps(final_results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': {'key': 'var_functions.query_db:2', 'type': "<class 'str'>", 'length': 38}, 'var_functions.execute_python:18': {'total_docs': 5, 'sample_keys': ['_id', 'filename', 'text'], 'doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 202'}, 'var_functions.query_db:20': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.execute_python:36': {'doc_count': 5}, 'var_functions.execute_python:38': {'spring_2022_docs': 4, 'total_docs': 5}, 'var_functions.execute_python:42': {'spring_2022_projects_count': 0, 'total_funding': 0}, 'var_functions.execute_python:44': {'funding_records': 10, 'sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.query_db:46': [{'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
