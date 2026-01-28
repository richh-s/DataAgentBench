code = """import pandas as pd
import json
import re

# Load funding data
with open(locals()['var_function-call-14481153673372787681'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load civic documents data
with open(locals()['var_function-call-12785932103837883149'], 'r') as f:
    civic_docs_data = json.load(f)

project_details = []

for doc in civic_docs_data:
    text = doc['text']

    # Regex patterns to extract project name and status/topic
    # Pattern for "Project Name (Status)" or "Project Name - Status"
    # Also capture lines that might indicate topics like "emergency warning" or "FEMA Project"
    # This is a general approach and might need refinement for edge cases.
    # Look for lines that seem to describe projects and their status or related keywords.

    # Look for "Capital Improvement Projects (Design)", "Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"
    # Then look for project names under these headers and their associated updates/schedules which often indicate status.

    # Simplified extraction for project names and checking for keywords
    lines = text.split('\n')
    current_category = ""
    for line in lines:
        line = line.strip()
        if "Capital Improvement Projects (Design)" in line or "Capital Improvement Projects (Construction)" in line or "Capital Improvement Projects (Not Started)" in line or "Disaster Recovery Projects" in line:
            current_category = line.replace("Capital Improvement Projects", "").strip().replace("(", "").replace(")", "")
        elif line.startswith(("(cid:190) Project Schedule:", "(cid:190) Updates:", "(cid:190) Project Description:", "(cid:131)")):
            continue # Skip update/schedule details themselves for now, focus on project names
        elif line and not line.startswith("Agenda Item") and not line.startswith("Page") and not line.startswith("To:") and not line.startswith("Prepared by:") and not line.startswith("Approved by:") and not line.startswith("Date prepared:") and not line.startswith("Meeting date:") and not line.startswith("Subject:") and not line.startswith("RECOMMENDED ACTION:") and not line.startswith("DISCUSSION:"):
            # Try to identify project names. This is a heuristic and might need tuning.
            # Assuming a project name is a significant line not part of boilerplate or sub-details.
            # Check for keywords "emergency" or "FEMA" in the project name itself or infer status from category.
            project_name = line.replace("(cid:131)", "").replace("(cid:190)", "").strip()

            # Simple check for project status from category. This is a simplification.
            status = current_category if current_category else "Unknown"

            # Look for topics "emergency" or "FEMA" within the project name or line
            topic = []
            if "emergency" in project_name.lower():
                topic.append("emergency")
            if "FEMA" in project_name.lower():
                topic.append("FEMA")

            # Also check for disaster related project names
            if "disaster" in project_name.lower() and "recovery" in project_name.lower():
                topic.append("disaster")

            # If no direct keyword match in the name, but it's a Disaster Recovery Project category
            if "Disaster Recovery Projects" in current_category and not topic:
                 topic.append("disaster")

            # Check if any topic keyword is present or if the name implies FEMA/emergency
            if topic or "fema" in project_name.lower() or "emergency" in project_name.lower() or "warning" in project_name.lower():
                 # Further refinement: associate status with the project. For now, using the category.
                 # More robust parsing would involve looking at the "Updates" and "Project Schedule" sections right after a project name.
                 project_details.append({'Project_Name': project_name, 'status': status, 'topic': ', '.join(topic)})


# Convert to DataFrame
projects_df = pd.DataFrame(project_details)

# Remove duplicates based on Project_Name, keeping the first occurrence
projects_df = projects_df.drop_duplicates(subset=['Project_Name'])

# Merge funding data with project details
merged_df = pd.merge(funding_df, projects_df, on='Project_Name', how='inner')

# Filter for projects related to "emergency" or "FEMA"
filtered_df = merged_df[merged_df['Project_Name'].str.contains('FEMA', case=False) | merged_df['Project_Name'].str.contains('emergency', case=False) | merged_df['topic'].str.contains('emergency', case=False) | merged_df['topic'].str.contains('FEMA', case=False)]

# Select and rename columns for the final output
final_result = filtered_df[['Project_Name', 'Funding_Source', 'Amount', 'status']].to_json(orient='records')

print('__RESULT__:')
print(final_result)"""

env_args = {'var_function-call-14481153673372787681': 'file_storage/function-call-14481153673372787681.json', 'var_function-call-12785932103837883149': 'file_storage/function-call-12785932103837883149.json'}

exec(code, env_args)
