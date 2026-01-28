code = """import json
import re

# Read the civic documents data
civic_docs_path = locals()['var_functions.query_db:0']
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

# Read the funding data
funding_path = locals()['var_functions.query_db:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Extract park-related projects from funding data
park_projects = [record for record in funding_data if 'park' in record.get('Project_Name', '').lower()]

# Create a lookup for project names
project_name_lookup = {record['Project_Name'].lower().replace('project', '').strip(): record for record in park_projects}

# Find completed 2022 park projects from civic docs
completed_2022_park_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '').lower()
    
    # Look for park projects completed in 2022
    if 'park' in text and '2022' in text and 'completed' in text:
        # Extract project names and completion info
        lines = doc.get('text', '').split('\n')
        for line in lines:
            line_lower = line.lower()
            if 'park' in line_lower and len(line) < 80:  # Likely a project name
                # Check if completed in 2022
                if ('2022' in text and 'completed' in text):
                    completed_2022_park_projects.append({
                        'Project_Name': line.strip(),
                        'topic': 'park',
                        'status': 'completed',
                        'year': '2022'
                    })

# Based on the sample data we saw, Bluffs Park Shade Structure was completed November 2022
# Let's manually verify from the funding data which park projects might match

# Look for specific projects in funding data that might have been completed in 2022
key_projects = [
    'Bluffs Park Shade Structure',
    'Marie Canyon Green Streets', 
    'Broad Beach Road Water Quality Repair',
    'Point Dume Walkway Repairs'
]

# Check which of these are in the park list and have 2022 in civic docs
final_projects = []
for project in park_projects:
    proj_name = project['Project_Name']
    # Check if this project appears in civic docs as completed in 2022
    for doc in civic_docs_data:
        text = doc.get('text', '')
        if proj_name in text and '2022' in text and 'completed' in text.lower():
            final_projects.append(project)

print('__RESULT__:')
print(json.dumps({
    'park_projects_in_funding': len(park_projects),
    'potentially_completed_2022': len(final_projects),
    'completed_2022_park_projects': final_projects
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.execute_python:12': {'park_funding_projects_count': 20, 'sample_park_projects': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Funding_ID': '51', 'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Funding_ID': '52', 'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Funding_ID': '53', 'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Funding_ID': '55', 'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Funding_ID': '56', 'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}, {'Funding_ID': '57', 'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}]}}

exec(code, env_args)
