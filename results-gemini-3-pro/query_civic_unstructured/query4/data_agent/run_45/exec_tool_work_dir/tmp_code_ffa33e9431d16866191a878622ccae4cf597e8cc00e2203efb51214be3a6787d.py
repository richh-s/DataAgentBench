code = """import json
import re

# Load data
with open(locals()['var_function-call-11755073423388004543'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-11755073423388006536'], 'r') as f:
    funding_data = json.load(f)

# Create a set of valid project names from funding data for matching
valid_project_names = set(item['Project_Name'] for item in funding_data)

# Helper function to normalize strings for comparison
def normalize(text):
    return text.strip()

# Extract projects and their start dates
projects_started_spring_2022 = []

# Regex for start date
# Look for "Begin Construction: <Date>" or "Start: <Date>" or similar
# We specifically look for "Spring 2022" or "Spring, 2022"
date_pattern = re.compile(r'(Begin Construction|Start Date|Construction Start|Scheduled Start)\s*[:\-]?\s*(.*?Spring.*?2022)', re.IGNORECASE)

# We also need to extract project blocks.
# Strategy: Iterate through lines. If a line is in valid_project_names, it's a project header.
# specific extraction logic.

found_projects = {}

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if line is a project name
        # Sometimes the project name in text might have extra spaces or slight variations
        # But based on hints, they match.
        if line in valid_project_names:
            current_project = line
            if current_project not in found_projects:
                found_projects[current_project] = {'dates': []}
            continue
            
        # If we are inside a project block, look for dates
        if current_project:
            # Check for start date
            match = date_pattern.search(line)
            if match:
                found_projects[current_project]['dates'].append(match.group(2))
            
            # Stop if we hit another project (this is handled by the "if line in valid_project_names" check above)
            # But we need to be careful if a line matches a project name by accident.
            # Usually project names are distinctive.

# Filter for Spring 2022
target_projects = []
for project, data in found_projects.items():
    dates = data['dates']
    # Check if any date string indicates Spring 2022
    # The regex captured the string containing Spring 2022, so if we have a match, it's a candidate.
    # But wait, the regex specifically looked for "Spring...2022".
    # So if there is any entry in dates, it means we found a start date in Spring 2022.
    if len(dates) > 0:
        target_projects.append(project)

# Now calculate total funding
total_funding = 0
project_count = 0
matched_projects_with_funding = []

for project in target_projects:
    # Find funding
    # There might be multiple funding records for one project? The table has Project_Name.
    # A project might appear multiple times with different funding sources.
    # I should sum all funding for the project.
    
    p_funding = 0
    found = False
    for record in funding_data:
        if record['Project_Name'] == project:
            p_funding += int(record['Amount'])
            found = True
    
    if found:
        matched_projects_with_funding.append(project)
        total_funding += p_funding
        project_count += 1

print("__RESULT__:")
print(json.dumps({"count": project_count, "total_funding": total_funding, "projects": matched_projects_with_funding}))"""

env_args = {'var_function-call-11755073423388006536': 'file_storage/function-call-11755073423388006536.json', 'var_function-call-11755073423388004543': 'file_storage/function-call-11755073423388004543.json'}

exec(code, env_args)
