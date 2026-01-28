code = """import json

# Read the data files
funding_file = var_functions.query_db_84
docs_file = var_functions.query_db_88

with open(funding_file, 'r') as f:
  funding_records = json.load(f)

with open(docs_file, 'r') as f:
  civic_docs = json.load(f)

# Build funding lookup by project name
funding_dict = {}
for record in funding_records:
  funding_dict[record['Project_Name']] = int(record['Amount'])

# Simple Spring 2022 extraction
spring_projects = []
for doc in civic_docs:
  text = doc.get('text', '')
  lines = text.split('\n')
  for i in range(len(lines)):
    line = lines[i]
    if 'Spring 2022' in line:
      # Look backward for project name
      for j in range(i-1, max(0, i-3), -1):
        prev = lines[j].strip().replace('•', '')
        if prev and len(prev) > 5:
          spring_projects.append(prev)
          break

# Get unique projects
unique_projects = list(set(spring_projects))

# Match with funding
matched = {}
for proj in unique_projects:
  if proj in funding_dict:
    matched[proj] = funding_dict[proj]

# Calculate totals
total_projects = len(matched)
total_funding = sum(matched.values())

print('SPRING 2022 PROJECTS:', total_projects)
print('TOTAL FUNDING:', total_funding)

data = {
  'total_projects': total_projects,
  'total_funding': total_funding,
  'projects': matched
}

print('__RESULT__:')
print(json.dumps(data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': 'Loaded 500 funding records', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.query_db:88': 'file_storage/functions.query_db:88.json'}

exec(code, env_args)
