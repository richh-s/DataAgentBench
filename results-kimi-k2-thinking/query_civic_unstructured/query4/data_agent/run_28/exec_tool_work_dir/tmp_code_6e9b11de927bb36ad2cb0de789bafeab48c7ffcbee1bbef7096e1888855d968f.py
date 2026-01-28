code = """import json
import re

# Load MongoDB documents
mongo_file = locals()['var_functions.query_db:2']
with open(mongo_file, 'r') as f:
    docs = json.load(f)

# Load all funding records
funding_file = locals()['var_functions.query_db:48']
with open(funding_file, 'r') as f:
    all_funding = json.load(f)

print('Documents:', len(docs), 'Funding records:', len(all_funding))

# Look for spring 2022 date patterns
spring_dates = re.compile(r'(spring|march|april|may)\s*2022', re.IGNORECASE)

extracted_projects = []

for doc in docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Check if document mentions spring 2022
    if spring_dates.search(text.lower()):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if not line or len(line) < 10:
                continue
            
            # Skip metadata lines
            lower_line = line.lower()
            if 'public works' in lower_line or 'agenda' in lower_line or 'item' in lower_line or 'page' in lower_line or 'prepared by' in lower_line:
                continue
            
            # Look for lines that might be project names (contain capitals, not too short/long)
            if 10 < len(line) < 100 and any(c.isupper() for c in line):
                # Check following lines for spring 2022
                next_lines = '\n'.join(lines[i:i+12])
                if spring_dates.search(next_lines.lower()):
                    extracted_projects.append(line)

unique_projects = list(set(extracted_projects))
print('Extracted projects:', len(unique_projects))
for p in unique_projects[:5]:
    print(' -', p)

# Normalize function
def normalize(name):
    n = name.lower().strip()
    n = re.sub(r'\s+', ' ', n)
    n = re.sub(r'\(fema[^\)]*\)', '', n)
    n = re.sub(r'\(caloes[^\)]*\)', '', n)
    n = re.sub(r'\(caljpia[^\)]*\)', '', n)
    return n.strip()

# Create funding lookup
funding_by_norm = {}
for fund in all_funding:
    norm = normalize(fund['Project_Name'])
    funding_by_norm[norm] = fund

# Match projects
matched_projects = []
for proj in unique_projects:
    norm_proj = normalize(proj)
    
    # Direct match
    if norm_proj in funding_by_norm:
        matched_projects.append({
            'name': proj,
            'funding': funding_by_norm[norm_proj]
        })
    else:
        # Try partial matching
        for norm_fund, fund in funding_by_norm.items():
            if norm_proj in norm_fund or norm_fund in norm_proj:
                matched_projects.append({
                    'name': proj,
                    'funding': fund
                })
                break

total_funding = sum(int(m['funding']['Amount']) for m in matched_projects)

result = {
    'count': len(matched_projects),
    'total_funding': total_funding,
    'projects': [{'name': m['name'], 'amount': int(m['funding']['Amount']), 'source': m['funding']['Funding_Source']} for m in matched_projects]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': {'key': 'var_functions.query_db:2', 'type': "<class 'str'>", 'length': 38}, 'var_functions.execute_python:18': {'total_docs': 5, 'sample_keys': ['_id', 'filename', 'text'], 'doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 202'}, 'var_functions.query_db:20': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.execute_python:36': {'doc_count': 5}, 'var_functions.execute_python:38': {'spring_2022_docs': 4, 'total_docs': 5}, 'var_functions.execute_python:42': {'spring_2022_projects_count': 0, 'total_funding': 0}, 'var_functions.execute_python:44': {'funding_records': 10, 'sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.query_db:46': [{'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
