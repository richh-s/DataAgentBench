code = """import pandas as pd
import re
import json

funding_data = json.loads(locals()['var_function-call-13812960451374386902'])
civic_docs_file_path = locals()['var_function-call-8903793629185941567']

with open(civic_docs_file_path, 'r') as f:
    civic_docs_data = json.load(f)

extracted_projects = []

# Simplified project name pattern for initial identification, ignoring suffixes for now
project_name_pattern = re.compile(r'^[A-Z][a-zA-Z0-9\s,&-]+', re.IGNORECASE)

# Exclusion prefixes, removed problematic characters like (cid:
exclusion_prefixes = (
    'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:',
    'RECOMMENDED ACTION:', 'DISCUSSION:', 'Updates:', 'Project Schedule:', 'Estimated Schedule:',
    'Project Description:', 'Capital Improvement Projects', 'Disaster Recovery Projects', 'Page'
)

for doc in civic_docs_data:
    text = doc['text']
    lines = text.split('\n')

    current_project_name = None
    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # Attempt to identify a project name. It should start with a capital letter, not be an exclusion prefix, and have at least two words.
        if project_name_pattern.match(stripped_line) and not stripped_line.startswith(exclusion_prefixes) and len(stripped_line.split()) >= 2:
            current_project_name = stripped_line

        # If a potential project name has been identified, check for completion in 2022
        if current_project_name:
            if ('construction was completed' in stripped_line.lower() or 'complete construction:' in stripped_line.lower()) and '2022' in stripped_line:
                # Check if the project name is park-related
                if 'park' in current_project_name.lower():
                    extracted_projects.append({
                        'Project_Name': current_project_name,
                        'status': 'completed',
                        'et_year': '2022',
                        'topic': 'park'
                    })
                    current_project_name = None # Reset after finding a completed project

# Convert extracted projects to DataFrame and remove duplicates based on Project_Name
projects_df = pd.DataFrame(extracted_projects).drop_duplicates(subset=['Project_Name'])

# Convert funding data to DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

# Merge dataframes to link projects with their funding
merged_df = pd.merge(projects_df, funding_df, on='Project_Name', how='inner')

# Calculate total funding for the filtered projects
total_funding = merged_df['Amount'].sum()

# Ensure total_funding is 0 if no matching projects are found, instead of NaN
if pd.isna(total_funding):
    total_funding = 0

print("__RESULT__:")
print(json.dumps(total_funding))"""

env_args = {'var_function-call-13812960451374386902': 'file_storage/function-call-13812960451374386902.json', 'var_function-call-8903793629185941567': 'file_storage/function-call-8903793629185941567.json'}

exec(code, env_args)
