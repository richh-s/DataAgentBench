code = """import pandas as pd

# Load funding data from the file
funding_data = pd.read_json(var_call_WjWmvkEvl9g85o2GCMRC3b3w)

# Filter funding data for projects with amounts greater than $50,000
filtered_funding = funding_data[funding_data['Amount'].astype(float) > 50000][['Project_Name']]

# Load civic docs data from the file
civic_docs_data = pd.read_json(var_call_gnXnUmN1rSZH0CXQ2ZO9ikPw)

# Extract projects with 'design' status
projects_design = []
for doc in civic_docs_data['text']:
    # A basic extraction could be using simple string search methods or regex
    if 'Design' in doc:
        # Simulating extraction by finding 'Design' projects
        project_lines = [line for line in doc.split('\n') if 'Design' in line]
        for line in project_lines:
            # This is a simplistic approach; in reality, we would need a more sophisticated extraction logic
            project_name = line.split(':')[0].strip()  # Assuming project name is before the first colon
            projects_design.append({'Project_Name': project_name})

# Convert to DataFrame
projects_design_df = pd.DataFrame(projects_design)

# Merge the funding data with project designs to find those that match
merged_data = pd.merge(filtered_funding, projects_design_df, on='Project_Name', how='inner')

# Count the number of unique design projects with funding
count_design_funded = merged_data['Project_Name'].nunique()

# Output the final count
print('__RESULT__:')
print(count_design_funded)"""

env_args = {'var_call_WjWmvkEvl9g85o2GCMRC3b3w': 'file_storage/call_WjWmvkEvl9g85o2GCMRC3b3w.json', 'var_call_gnXnUmN1rSZH0CXQ2ZO9ikPw': 'file_storage/call_gnXnUmN1rSZH0CXQ2ZO9ikPw.json'}

exec(code, env_args)
