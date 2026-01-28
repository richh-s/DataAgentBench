code = """import json

# Load Spring 2022 documents
file_path = locals()['var_functions.query_db:32']
with open(file_path, 'r') as f:
    spring_docs = json.load(f)

print('Total Spring 2022 docs: ' + str(len(spring_docs)))

# Extract potential project names
project_candidates = []

for doc in spring_docs:
    text = doc['text']
    lines = text.split('\n')
    for line in lines:
        clean_line = line.strip()
        if clean_line and len(clean_line) > 5:
            if not clean_line.startswith('(') and not clean_line.startswith('•'):
                project_candidates.append(clean_line)

# Remove duplicates
candidates_unique = list(set(project_candidates))

print('Candidates: ' + str(len(candidates_unique)))

# Show sample data for manual review
print('\nSample lines from first doc:')
for doc in spring_docs[:1]:
    lines = doc['text'].split('\n')[:30]
    for i, line in enumerate(lines):
        print(str(i) + ': ' + line[:80])

result = {'doc_count': len(spring_docs), 'candidates': len(candidates_unique)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:30': {'doc_count': 5, 'spring_count': 5}, 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
