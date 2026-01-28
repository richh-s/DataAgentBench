code = """# Let's load the funding data from the file path
import json

try:
    funding_file = var_functions.query_db_8
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
except:
    # Try different variable access
    result = globals().get('var_functions.query_db:8')
    if isinstance(result, str):
        with open(result, 'r') as f:
            funding_data = json.load(f)
    else:
        funding_data = result

# Count total funding for disaster projects
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'emergency', 'disaster']
total_funding = 0
disaster_projects = []

for record in funding_data:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    
    if any(keyword in project_name for keyword in disaster_keywords):
        disaster_projects.append(project_name)
        total_funding += amount

print('Total disaster projects:', len(disaster_projects))
print('Total disaster funding (all years):', total_funding)

# Look for the specific file to extract project dates
# Since we need projects that started in 2022, let's check which projects have 2022 in their schedule
civic_file = var_functions.query_db_26
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

print('\nCivic documents loaded:', len(civic_data))

# Extract project information from text
text = civic_data[0].get('text', '')
print('\nLooking for 2022 start dates and disaster projects...')

# Look for disaster projects and their schedules
import re

# Find project names with their schedules
project_sections = re.findall(r'([A-Za-z\s&\-]+?\(cid:\d+\) Updates:.*?(?=\n\n|$))', text, re.DOTALL)

disaster_projects_2022 = []

for section in project_sections:
    # Check if it mentions 2022 or has disaster keywords
    if '2022' in section or any(keyword in section for keyword in disaster_keywords):
        # Extract project name (usually first line)
        lines = section.split('\n')
        project_name = lines[0].strip()
        if project_name and len(project_name) < 100:  # Filter out noise
            disaster_projects_2022.append(project_name)

print('\nPotential 2022 disaster projects:', len(disaster_projects_2022))
for proj in disaster_projects_2022:
    print(' -', proj)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
