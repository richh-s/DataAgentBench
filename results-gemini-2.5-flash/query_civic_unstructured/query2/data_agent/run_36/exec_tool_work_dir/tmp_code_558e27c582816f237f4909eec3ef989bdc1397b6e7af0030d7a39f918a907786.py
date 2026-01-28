code = """import pandas as pd
import re
import json

funding_data = json.loads(locals()['var_function-call-13812960451374386902'])
civic_docs_file_path = locals()['var_function-call-8903793629185941567']

with open(civic_docs_file_path, 'r') as f:
    civic_docs_data = json.load(f)

extracted_projects = []

# Define exclusion prefixes as a list of simple strings, ensuring problematic single quotes are escaped.
exclusion_prefixes = [
    'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:',
    'RECOMMENDED ACTION:', 'DISCUSSION:', 'Updates:', 'Project Schedule:', 'Estimated Schedule:',
    'Project Description:', 'Capital Improvement Projects', 'Disaster Recovery Projects', 'Page',
    '(cid:' # Escaping the internal single quote. This was the most likely source of the SyntaxError.
]

for doc in civic_docs_data:
    text = doc['text']
    lines = text.split('\n')

    current_project_name = None
    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # Heuristic for detecting a potential project name:
        # Starts with a capital letter, is not an exclusion prefix, and has at least two words.
        is_potential_project_name = False
        if len(stripped_line) > 0 and stripped_line[0].isupper() and \
           not any(stripped_line.startswith(prefix) for prefix in exclusion_prefixes) and \
           len(stripped_line.split()) >= 2:
            is_potential_project_name = True

        if is_potential_project_name:
            current_project_name = stripped_line

        if current_project_name:
            # Check for completion in 2022
            if ('construction was completed' in stripped_line.lower() or 'complete construction:' in stripped_line.lower()) and '2022' in stripped_line:
                # Further check if the project name contains 'park'
                if 'park' in current_project_name.lower():
                    extracted_projects.append({
                        'Project_Name': current_project_name,
                        'status': 'completed',
                        'et_year': '2022',
                        'topic': 'park'
                    })
                    current_project_name = None # Reset after finding a completed project

# Convert extracted projects to DataFrame and remove duplicates
projects_df = pd.DataFrame(extracted_projects).drop_duplicates(subset=['Project_Name'])

# Convert funding data to DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

# Merge dataframes
merged_df = pd.merge(projects_df, funding_df, on='Project_Name', how='inner')

# Calculate total funding
total_funding = merged_df['Amount'].sum()

# If no projects are found, sum will be NaN, return 0.
if pd.isna(total_funding):
    total_funding = 0

print("__RESULT__:")
print(json.dumps(total_funding))"""

env_args = {'var_function-call-13812960451374386902': 'file_storage/function-call-13812960451374386902.json', 'var_function-call-8903793629185941567': 'file_storage/function-call-8903793629185941567.json', 'var_function-call-8397726498436877101': 'Test'}

exec(code, env_args)
