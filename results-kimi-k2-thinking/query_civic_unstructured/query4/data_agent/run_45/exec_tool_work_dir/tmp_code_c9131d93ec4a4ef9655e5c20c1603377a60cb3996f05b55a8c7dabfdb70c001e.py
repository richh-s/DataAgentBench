code = """import json

# Load the funding data first
funding_file = locals()['var_functions.query_db:90']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Create funding lookup map
funding_map = {}
for record in funding_data:
    name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    if name and amount > 0:
        funding_map[name] = amount
        base_name = name.split('(')[0].strip()
        if base_name != name:
            funding_map[base_name] = amount

print('Funding map created with', len(funding_map), 'entries')

# Load civic documents
civic_file = locals()['var_functions.query_db:88']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print('Civic documents loaded:', len(civic_docs))

# Extract text from all documents to search for Spring 2022
all_text = ''
for doc in civic_docs:
    all_text += doc.get('text', '') + '\n'

# Check if Spring 2022 is mentioned
spring_indicators = ['2022-Spring', '2022-March', '2022-April', '2022-May']
found_spring = any(indicator in all_text for indicator in spring_indicators)
print('Spring 2022 mentioned in documents:', found_spring)

# Look at first document structure for project patterns
first_doc = civic_docs[0]
text = first_doc.get('text', '')

# Count documents with Spring 2022 mentions
doc_count_with_spring = 0
for doc in civic_docs:
    doc_text = doc.get('text', '')
    if any(indicator in doc_text for indicator in spring_indicators):
        doc_count_with_spring += 1

print('Documents with Spring 2022 mentions:', doc_count_with_spring)

# Extract likely project names (lines that are uppercase and contain PROJECT/IMPROVEMENTS)
all_lines = text.split('\n')
project_candidates = []
for line in all_lines:
    line = line.strip()
    if line and len(line) > 15:
        upper_ratio = sum(1 for c in line if c.isupper()) / max(1, len(line.replace(' ', '')))
        if upper_ratio > 0.2 and any(kw in line.upper() for kw in ['PROJECT', 'IMPROVEMENTS', 'REPAIRS']):
            project_candidates.append(line)

print('Project candidates in first doc:', len(project_candidates))
for p in project_candidates[:10]:
    print(' -', p[:80])

# Simple heuristic: projects with years in their name might indicate start year
year_projects = []
for candidate in project_candidates:
    if '2022' in candidate:
        year_projects.append(candidate)

print('Projects with 2022 in name:', len(year_projects))

# Final result calculation
matched_projects = []
total_funding = 0

for proj in year_projects:
    if proj in funding_map:
        amt = funding_map[proj]
        matched_projects.append({'project': proj, 'amount': amt})
        total_funding += amt
    else:
        base = proj.split('(')[0].strip()
        if base in funding_map:
            amt = funding_map[base]
            matched_projects.append({'project': proj, 'amount': amt})
            total_funding += amt

result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects[:10]
}

print('Final result:', result)
print('__RESULT__:')
import json as js
print(js.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:46': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:53': {'count': 0, 'projects': []}, 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:66': [{'total_records': '500'}], 'var_functions.list_db:82': ['civic_docs'], 'var_functions.list_db:84': ['civic_docs'], 'var_functions.query_db:86': [{'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}], 'var_functions.query_db:88': 'file_storage/functions.query_db:88.json', 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json'}

exec(code, env_args)
