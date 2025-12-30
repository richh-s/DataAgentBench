code = """import pandas as pd
import re
import json

funding_data = json.loads(locals()['var_function-call-13812960451374386902'])
civic_docs_file_path = locals()['var_function-call-8903793629185941567']

with open(civic_docs_file_path, 'r') as f:
    civic_docs_data = json.load(f)

extracted_projects = []

# Define exclusion prefixes as a list of simple strings, without any special characters that could cause parsing issues
exclusion_keywords = [
    'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:',
    'RECOMMENDED ACTION:', 'DISCUSSION:', 'Updates:', 'Project Schedule:', 'Estimated Schedule:',
    'Project Description:', 'Capital Improvement Projects', 'Disaster Recovery Projects', 'Page'
]

for doc in civic_docs_data:
    text = doc['text']
    lines = text.split('\n') # Using literal newline character for splitting

    current_project_name = None
    
    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # Also exclude lines that contain '(cid:' from being project names.
        is_cid_line = '(cid:' in stripped_line

        # Heuristic for detecting a potential project name:
        # Starts with an uppercase letter, is not an exclusion keyword, is not a '(cid:' line, and has at least two words.
        is_potential_project_name_line = (
            len(stripped_line) > 0 and
            stripped_line[0].isupper() and
            not any(stripped_line.startswith(keyword) for keyword in exclusion_keywords) and
            not is_cid_line and # Exclude lines containing '(cid:'
            len(stripped_line.split()) >= 2
        )

        if is_potential_project_name_line:
            current_project_name = stripped_line

        # Only process if we have a current_project_name identified
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
                current_project_name = None # Reset after finding a completed project (or processing one)
            elif 'project is currently under construction' in stripped_line.lower():
                current_project_name = None # Reset if the project is under construction, not completed

# Convert extracted projects to DataFrame and remove duplicates
projects_df = pd.DataFrame(extracted_projects).drop_duplicates(subset=['Project_Name'])

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
