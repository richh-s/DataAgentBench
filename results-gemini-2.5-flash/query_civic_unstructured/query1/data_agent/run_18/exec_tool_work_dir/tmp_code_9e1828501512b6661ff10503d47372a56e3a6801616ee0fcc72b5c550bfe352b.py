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

projects_info = []

for doc in civic_docs_data:
    text = doc['text']
    
    # Use a broader regex to find sections that might contain design projects
    # This pattern looks for any section starting with 'Capital Improvement Projects' and captures its content
    capital_projects_sections = re.findall(r'Capital Improvement Projects \((.*?)\)\n(.*?)(?=(?:Capital Improvement Projects \(|Disaster Recovery Projects|\Z))', text, re.DOTALL)

    for section_type, section_content in capital_projects_sections:
        # Check if this is a 'Design' section or contains design information
        if "Design" in section_type or re.search(r'(Complete Design|Final Design|preliminary design phase)', section_content, re.IGNORECASE):
            # Now extract project names within this section
            # Project names often appear at the beginning of a line and before 'Updates' or 'Project Schedule'
            # or are explicitly listed under a 'Design' heading.
            
            # Regex to find project names. It will capture the name and then anything until the next project or a new section.
            project_entries = re.findall(r'\n\n([A-Za-z0-9][^\n]*(?:Project|Improvements|Repair|Study|Plan|Replacement|Resurfacing)?)(?:\n\(cid:190\) Updates:.*?|\n\(cid:190\) Project Schedule:.*?|\n\(cid:190\) Project Description:.*?|(?=\n\n[A-Z0-9]))', section_content, re.DOTALL)

            for project_name_raw in project_entries:
                project_name = project_name_raw.strip()
                
                # Further filter to ensure it looks like a valid project name and not just a stray line
                if project_name and len(project_name) > 5 and not re.search("^(Updates|Schedule|Discussion|Recommended Action|Item|Page \d+ of \d+)", project_name, re.IGNORECASE):
                    projects_info.append({
                        "Project_Name": project_name,
                        "type": "capital",
                        "status": "design"
                    })

# Convert extracted project info to DataFrame
extracted_projects_df = pd.DataFrame(projects_info)

# Filter for unique project names
extracted_projects_df = extracted_projects_df.drop_duplicates(subset=['Project_Name'])

# Join with funded projects
merged_df = pd.merge(funded_projects_df, extracted_projects_df, on='Project_Name', how='inner')

# Count the number of projects
result_count = len(merged_df)

print('__RESULT__:')
print(json.dumps(result_count))"""

env_args = {'var_function-call-8331219460876978915': 'file_storage/function-call-8331219460876978915.json', 'var_function-call-17001069336408720417': 'file_storage/function-call-17001069336408720417.json'}

exec(code, env_args)
