code = """import json
import re

# Load data
civic_docs_path = locals()['var_functions.query_db:0']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

funding_path = locals()['var_functions.query_db:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Create funding dictionary
funding_dict = {}
for record in funding_data:
    proj_name = record['Project_Name'].strip()
    amount = int(record['Amount'])
    funding_dict[proj_name] = amount

# More targeted search for completed 2022 park projects
completed_parks_2022 = []

for doc in civic_docs:
    doc_text = doc.get('text', '')
    
    # Look for completion statements with 2022
    lines = doc_text.split(chr(10))
    
    for i, line in enumerate(lines):
        line_lower = line.lower()
        # Find lines mentioning both completed and 2022
        if 'completed' in line_lower and '2022' in line:
            # Look backward for project name (within 5 lines)
            for j in range(max(0, i-5), i):
                prev_line = lines[j].strip()
                if 'park' in prev_line.lower() and len(prev_line) > 10:
                    # Skip headers and metadata
                    if not any(skip in prev_line for skip in ['Capital Improvement', 'Public Works', 'Agenda Report', 'RECOMMENDED ACTION']):
                        project = prev_line
                        # Clean up the project name
                        if 'Bluffs Park Shade Structure' in project:
                            project = 'Bluffs Park Shade Structure'
                        elif 'Permanent Skate Park' in project or 'permanent skate park' in project.lower():
                            project = 'Permanent Skate Park'
                        
                        if project not in completed_parks_2022:
                            completed_parks_2022.append(project)
                        break

# Clean up duplicates and invalid entries
valid_projects = []
for project in completed_parks_2022:
    if len(project) < 80:  # Skip long descriptions
        valid_projects.append(project)

# Find exact matches in funding data
exact_matches = []
total_funding = 0

for project in valid_projects:
    if project in funding_dict:
        exact_matches.append({'project': project, 'amount': funding_dict[project]})
        total_funding += funding_dict[project]

# Check for any other park projects with 2022 completion mentioned
additional_park_projects = []
for funding_project, amount in funding_dict.items():
    if 'park' in funding_project.lower():
        # Check if completed in 2022 is mentioned anywhere in documents
        for doc in civic_docs:
            doc_text = doc.get('text', '')
            if funding_project in doc_text:
                if 'completed' in doc_text.lower() and '2022' in doc_text:
                    # Verify it's not already counted
                    already_counted = any(match['project'] == funding_project for match in exact_matches)
                    if not already_counted:
                        additional_park_projects.append({'project': funding_project, 'amount': amount})
                        total_funding += amount
                        break

result = {
    'completed_park_projects_2022': valid_projects,
    'exact_funding_matches': exact_matches,
    'additional_park_projects': additional_park_projects,
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'civic_docs_count': 5, 'funding_records_count': 500}, 'var_functions.execute_python:14': {'park_projects': ['Bluffs Park Shade Structure', 'Permanent Skate Park', 'permanent skate park located on the Crummer/Case Court parcel adjacent', 'to Malibu Bluffs Park. The project would include parking and additional site'], 'all_completed_2022': [], 'funding_matches': [{'project': 'Bluffs Park Shade Structure', 'amount': 21000}, {'project': 'Permanent Skate Park', 'amount': 97000}], 'total_funding': 118000}, 'var_functions.execute_python:18': {'completed_park_projects': ['Bluffs Park Shade Structure', 'Permanent Skate Park', 'permanent skate park located on the Crummer/Case Court parcel adjacent', 'to Malibu Bluffs Park. The project would include parking and additional site'], 'funding_matches': [{'project': 'Bluffs Park Shade Structure', 'amount': 21000}, {'project': 'Permanent Skate Park', 'amount': 97000}, {'project': 'Permanent Skate Park', 'amount': 97000}, {'project': 'Malibu Park Storm Drain Repairs', 'amount': 50000}], 'total_funding': 265000}}

exec(code, env_args)
