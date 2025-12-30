code = """import pandas as pd
import re
import json

# Load funding data
with open(locals()['var_function-call-11832248157003500024'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load civic docs data
with open(locals()['var_function-call-10525020737376482423'], 'r') as f:
    civic_docs_data = json.load(f)

project_details = []

for doc in civic_docs_data:
    text = doc['text']
    current_status = None
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if "Capital Improvement Projects (Design)" in line:
            current_status = "design"
        elif "Capital Improvement Projects (Construction)" in line or "Project is currently under construction" in line:
            current_status = "construction" # We'll map this to 'design' or 'completed' later for consistency if needed, but for now 'construction' is a good intermediate.
        elif "Capital Improvement Projects (Not Started)" in line:
            current_status = "not started"
        elif "Disaster Recovery Projects" in line:
            # Disaster projects can be in design, construction, or completed. We need to check further.
            pass

        # Try to extract project names and status
        # Corrected regex to use r"..." to avoid SyntaxError with ' inside raw string.
        project_name_match = re.search(r"^[A-Z][a-zA-Z0-9 &-,/\\()#\\.\\']{5,}[^:]$", line)
        if project_name_match:
            project_name = project_name_match.group(0).strip()
            # Try to infer status from surrounding text or the project name itself
            status_found = False
            if "Updates: Project is currently under construction" in text and project_name in text:
                current_status = "construction"
                status_found = True
            elif "Updates: Construction was completed" in text and project_name in text:
                current_status = "completed"
                status_found = True
            elif "Updates: Construction was completed November 2022. Notice of completion filed January 2023" in text and project_name in text:
                current_status = "completed"
                status_found = True
            elif "Updates: Construction was completed, January 2023" in text and project_name in text:
                current_status = "completed"
                status_found = True
            elif "Updates: Construction was completed, November 2022" in text and project_name in text:
                current_status = "completed"
                status_found = True
            elif "Updates: Project is in the preliminary design phase" in text and project_name in text:
                current_status = "design"
                status_found = True
            elif "Updates: Staff is working with the consultant to finalize the design plans for this project" in text and project_name in text:
                current_status = "design"
                status_found = True
            elif "Updates: Plans and specifications are being finalized by consultant" in text and project_name in text:
                current_status = "design"
                status_found = True
            elif "Updates: Staff is currently working on the final design plans" in text and project_name in text:
                current_status = "design"
                status_found = True
            elif "Updates: Project is currently out to bid" in text and project_name in text:
                current_status = "design" # Bidding implies design is mostly done, but not constructed.
                status_found = True
            elif "Updates: Awaiting final FEMA/CalOES approval for scope modification" in text and project_name in text:
                current_status = "design"
                status_found = True
            elif "Project is delayed due to the Cultural Resource review" in text and project_name in text:
                current_status = "design"
                status_found = True
            elif "Project was identified in the 2015 PCH Safety Study" in text and project_name in text:
                current_status = "not started"
                status_found = True
            elif "Project was identified in the City\u2019s Enhanced Watershed Management Plan (EWMP)" in text and project_name in text:
                current_status = "not started"
                status_found = True
            elif "Project is in the preliminary design phase" in text and project_name in text:
                current_status = "design"
                status_found = True
            elif "Updates: City has submitted an application through Measure R and is waiting for the agreement" in text and project_name in text:
                current_status = "not started"
                status_found = True
            elif "Updates: Construction was completed November 2022. Notice of completion filed January 2023" in text and project_name in text:
                current_status = "completed"
                status_found = True


            if current_status and project_name not in ["RECOMMENDED ACTION", "DISCUSSION", "Project Schedule", "Updates", "Agenda Item"]:
                 project_details.append({
                     "Project_Name": project_name,
                     "status": current_status
                 })

# Convert to DataFrame
project_status_df = pd.DataFrame(project_details)

# Clean project names - remove duplicates and keep the most recent status (or just unique for now)
# If a project appears multiple times with different statuses, this will keep the first one encountered in the text.
# For more robust solution, we would need to establish a hierarchy of statuses or chronological order.
project_status_df.drop_duplicates(subset=['Project_Name'], keep='last', inplace=True)


# Merge with funding data
merged_df = pd.merge(funding_df, project_status_df, on='Project_Name', how='inner')

# Filter for 'emergency' or 'FEMA' related projects
# This checks project name for FEMA related patterns and funding source for "Federal Assistance"
# It also includes project names from the civic docs that mention 'emergency' in their description.
# Given the hint about topics, we should also try to extract 'topic' more directly from the text if possible.
# However, for now, we will rely on keywords in project names and the description of the prompt.

# Let's re-evaluate how to determine 'emergency' or 'FEMA' related projects
# From the problem description:
# - Projects have two types: "capital" (Capital Improvement Projects) and "disaster" (Disaster Recovery Projects, often FEMA-funded or related to Woolsey Fire recovery).
# - The topic field contains comma-separated keywords. Common topics include: "park", "road", "FEMA", "fire", "emergency warning", "drainage", "storm drain", "highway", "bridge", "playground", "water treatment", "guardrail".
# - Disaster project names often include suffixes like "(FEMA Project)", "(CalJPIA Project)", or "(CalOES Project)".

# So, we need to consider:
# 1. Project_Name containing "(FEMA Project)", "(CalJPIA Project)", "(CalOES Project)" or "emergency"
# 2. Funding_Source being "Federal Assistance"
# 3. If we could extract a "topic" field, but the current text extraction for that is not robust enough.
# Let's adjust the filtering based on the available data.

# Refine project status based on keywords within project name in funding_df.
# This assumes that if a project name in funding_df contains certain keywords, it's related to 'emergency' or 'FEMA'.
# We will use this to refine the 'topic' and 'status' for projects that were only partially extracted from civic_docs.

# Add a 'topic' column to the merged_df, initially empty
merged_df['topic'] = ''

# Function to infer topic from Project_Name
def infer_topic(project_name):
    project_name_lower = project_name.lower()
    if 'fema' in project_name_lower or 'emergency' in project_name_lower or 'caloes' in project_name_lower:
        return 'emergency/fema'
    return ''

merged_df['topic'] = merged_df['Project_Name'].apply(infer_topic)

# Filter for projects with 'emergency/fema' topic or 'Federal Assistance' funding
filtered_df = merged_df[
    (merged_df['topic'].str.contains('emergency/fema', case=False, na=False)) |
    (merged_df['Funding_Source'].str.contains('Federal Assistance', case=False, na=False))
]

# Map 'construction' status to 'design' or 'completed' based on common sense if needed.
# For now, let's keep it as is, or we can make a choice. Let's map it to 'design' as it's still ongoing.
filtered_df.loc[filtered_df['status'] == 'construction', 'status'] = 'design'

# Select and rename columns for the final output
final_output = filtered_df[['Project_Name', 'Funding_Source', 'Amount', 'status']]

# Drop duplicates in the final output in case some projects were captured multiple times with same details.
final_output.drop_duplicates(inplace=True)

print("__RESULT__:")
print(final_output.to_json(orient='records'))"""

env_args = {'var_function-call-8285255969560779201': ['Funding'], 'var_function-call-11832248157003500024': 'file_storage/function-call-11832248157003500024.json', 'var_function-call-14637775399032922258': ['civic_docs'], 'var_function-call-10525020737376482423': 'file_storage/function-call-10525020737376482423.json'}

exec(code, env_args)
