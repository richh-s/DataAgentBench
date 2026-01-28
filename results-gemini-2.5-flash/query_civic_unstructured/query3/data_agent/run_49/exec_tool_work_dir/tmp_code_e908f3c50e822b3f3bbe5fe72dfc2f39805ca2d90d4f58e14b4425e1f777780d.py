code = """import pandas as pd
import re
import json

# Load the full result from the file
with open(locals()['var_function-call-13801791921657955456'], 'r') as f:
    civic_docs_data = json.load(f)

projects = []

for doc in civic_docs_data:
    text = doc['text']
    
    # Regex to find project blocks. This is a heuristic and might need refinement.
    # Look for lines that seem to be project titles followed by updates/schedules.
    project_blocks = re.split(r"\n\n(?!\s*(?:Page \d+ of \d+|Agenda Item # \d+\.\d+|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|RECOMMENDED ACTION:|DISCUSSION:))(?=[A-Z][a-zA-Z0-9\s&,-]+\n(?:\(cid:190\)\|\(cid:131\)\|Updates:|Project Schedule:|Estimated Schedule:|Project Description:|DISCUSSION:))", text)

    # The first split part is usually the header, not a project block
    if project_blocks and len(project_blocks) > 0:
        header = project_blocks[0]
        project_blocks = project_blocks[1:]
    else:
        project_blocks = [text] # If splitting fails, treat whole text as one block

    for block in project_blocks:
        project_name_match = re.search(r'^\n*([A-Z][a-zA-Z0-9\s&,-]+(?:\(FEMA Project\)|\(CalJPIA Project\)|\(CalOES Project\))?)\n', block, re.MULTILINE)
        if project_name_match:
            project_name = project_name_match.group(1).strip()
            
            # Check for keywords related to emergency or FEMA in the project name or block
            if re.search(r'emergency|FEMA|disaster', project_name, re.IGNORECASE) or \
               re.search(r'emergency|FEMA|disaster', block, re.IGNORECASE):

                status = "unknown"
                if "Updates: Project is currently under construction" in block:
                    status = "under construction"
                elif "Construction was completed" in block or "Construction completed" in block:
                    status = "completed"
                elif "preliminary design phase" in block or "working with the consultant to finalize the design plans" in block or "Plans are under review" in block:
                    status = "design"
                elif "identified but not begun" in block or "waiting for the agreement" in block or "Project to be discussed" in block:
                    status = "not started"
                
                project_type = "unknown"
                if "Capital Improvement Projects" in text or "Capital Improvement Projects" in block:
                    project_type = "capital"
                if "Disaster Recovery Projects" in text or "Disaster Recovery Projects" in block:
                    project_type = "disaster"

                topic = []
                if re.search(r'emergency', block, re.IGNORECASE):
                    topic.append('emergency')
                if re.search(r'FEMA', block, re.IGNORECASE):
                    topic.append('FEMA')
                if re.search(r'fire', block, re.IGNORECASE):
                    topic.append('fire')
                if re.search(r'storm drain|drainage', block, re.IGNORECASE):
                    topic.append('storm drain/drainage')

                if project_name and status != "unknown" and (topic or project_type == "disaster"):
                    projects.append({
                        "Project_Name": project_name,
                        "topic": ", ".join(list(set(topic))),
                        "type": project_type,
                        "status": status
                    })

projects_df = pd.DataFrame(projects)

# Remove duplicates based on Project_Name
projects_df = projects_df.drop_duplicates(subset=['Project_Name'])

# Filter for projects related to 'emergency' or 'FEMA' more explicitly, in case regex missed some
projects_df = projects_df[projects_df['topic'].str.contains('emergency|FEMA', case=False, na=False) | projects_df['type'].str.contains('disaster', case=False, na=False)]

print("__RESULT__:")
print(projects_df.to_json(orient='records'))"""

env_args = {'var_function-call-13801791921657955456': 'file_storage/function-call-13801791921657955456.json'}

exec(code, env_args)
