code = """import pandas as pd
import json
import re

# Load funding data
with open(locals()['var_function-call-8331219460876978915'], 'r') as f:
    funding_data = json.load(f)
funded_projects_df = pd.DataFrame(funding_data)

# Load civic documents text
with open(locals()['var_function-call-17001069336408720417'], 'r') as f:
    civic_docs_data = json.load(f)

# Extract project information from civic documents
projects_info = []
for doc in civic_docs_data:
    text = doc['text']
    
    # Regex to find Capital Improvement Projects (Design)
    # This pattern looks for a section "Capital Improvement Projects (Design)" and then lists projects under it
    # It captures project names until another section header is found or the document ends.
    # It also captures project schedule information (which includes the design status)
    
    # Section for "Capital Improvement Projects (Design)"
    design_projects_section_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|\n\n)', text, re.DOTALL)
    if design_projects_section_match:
        design_section_text = design_projects_section_match.group(1)
        # Find project names and their statuses within this section
        # Project names usually start with a new line and are followed by updates and schedules.
        # We need to ensure that the status is 'Design' or implied as 'Design' from the section.
        
        # Regex to capture project name and its schedule (to check for design status)
        project_matches = re.findall(r'\n\n([A-Za-z0-9][^\n]*(?:Project)?)(?:\n\(cid:190\) Updates:.*?|)(?:\n\(cid:190\) Project Schedule:\n\n\(cid:131\) Complete Design: (.*?)(?:\n|$)|

', design_section_text, re.DOTALL)

        for match in project_matches:
            project_name = match[0].strip()
            design_complete_schedule = match[1].strip() if len(match) > 1 and match[1] else ''

            if project_name and ("Design" in design_complete_schedule or "Design" in design_section_text):
                projects_info.append({
                    "Project_Name": project_name,
                    "type": "capital",
                    "status": "design"
                })

# Convert extracted project info to DataFrame
extracted_projects_df = pd.DataFrame(projects_info)

# Filter for unique project names as they might appear multiple times in the text
extracted_projects_df = extracted_projects_df.drop_duplicates(subset=['Project_Name'])

# Join with funded projects
merged_df = pd.merge(funded_projects_df, extracted_projects_df, on='Project_Name', how='inner')

# Count the number of projects
result_count = len(merged_df)

print('__RESULT__:')
print(json.dumps(result_count))"""

env_args = {'var_function-call-8331219460876978915': 'file_storage/function-call-8331219460876978915.json', 'var_function-call-17001069336408720417': 'file_storage/function-call-17001069336408720417.json'}

exec(code, env_args)
