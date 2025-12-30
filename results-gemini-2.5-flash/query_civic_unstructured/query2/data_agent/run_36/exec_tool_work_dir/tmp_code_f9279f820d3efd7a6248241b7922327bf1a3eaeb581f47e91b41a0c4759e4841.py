code = """import pandas as pd
import re
import json

funding_data = json.loads(locals()['var_function-call-13812960451374386902'])
civic_docs_file_path = locals()['var_function-call-8903793629185941567']

with open(civic_docs_file_path, 'r') as f:
    civic_docs_data = json.load(f)

extracted_projects = []

for doc in civic_docs_data:
    text = doc['text']
    # Split text into lines to process them individually
    lines = text.split('\n') # Use \n to represent a literal newline character in the string

    # Iterate through lines to find completion indicators
    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # Check for completion in 2022
        if ('construction was completed' in stripped_line.lower() or 'complete construction:' in stripped_line.lower()) and '2022' in stripped_line:
            # Found a line indicating completion in 2022. Now, look backwards for the project name.
            project_name_candidate = None
            for j in range(i - 1, max(-1, i - 5), -1): # Look back up to 5 lines
                prev_line = lines[j].strip()
                # Exclude lines that are clearly not project names (bullets, headings, etc.)
                if prev_line and not prev_line.startswith(('(cid:', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:', 'RECOMMENDED ACTION:', 'DISCUSSION:', 'Updates:', 'Project Schedule:', 'Estimated Schedule:', 'Project Description:', 'Capital Improvement Projects', 'Disaster Recovery Projects', 'Page')) and len(prev_line.split()) >= 2:
                    project_name_candidate = prev_line
                    break # Found a potential project name, stop looking further back

            if project_name_candidate and 'park' in project_name_candidate.lower():
                extracted_projects.append({
                    'Project_Name': project_name_candidate,
                    'status': 'completed',
                    'et_year': '2022',
                    'topic': 'park'
                })

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

env_args = {'var_function-call-13812960451374386902': 'file_storage/function-call-13812960451374386902.json', 'var_function-call-8903793629185941567': 'file_storage/function-call-8903793629185941567.json'}

exec(code, env_args)
