code = """import pandas as pd
import re
import json

# Load the full result from the file
with open(locals()['var_function-call-13801791921657955456'], 'r') as f:
    civic_docs_data = json.load(f)

projects = []

# This regex attempts to find a Project Name followed by its description block
# The description block is captured until the next similar "Project Name" pattern or end of text.
# The project name pattern is improved to be more specific.
project_pattern = re.compile(
    r'(?P<project_name>[A-Z][a-zA-Z0-9\\s&,-]+(?:\\(FEMA Project\\)|\\(CalJPIA Project\\)|\\(CalOES Project\\))?)\\n'
    r'(?P<description_block>(?:\\(cid:\\d+\\)|[\\s\\S])*?(?=\\n\\n[A-Z][a-zA-Z0-9\\s&,-]+(?:\\(FEMA Project\\)|\\(CalJPIA Project\\)|\\(CalOES Project\\))?\\n|\\Z))'
)


for doc in civic_docs_data:
    text = doc['text']

    for match in project_pattern.finditer(text):
        project_name = match.group('project_name').strip()
        description_block = match.group('description_block')

        # Check for keywords in project name or description
        if re.search(r'emergency|FEMA|disaster', project_name, re.IGNORECASE) or \
           re.search(r'emergency|FEMA|disaster', description_block, re.IGNORECASE):

            status = "unknown"
            if "Updates: Project is currently under construction" in description_block:
                status = "under construction"
            elif "Construction was completed" in description_block or "Construction completed" in description_block:
                status = "completed"
            elif "preliminary design phase" in description_block or "working with the consultant to finalize the design plans" in description_block or "Plans are under review" in description_block:
                status = "design"
            elif "identified but not begun" in description_block or "waiting for the agreement" in description_block or "Project to be discussed" in description_block:
                status = "not started"
            
            project_type = "unknown"
            if "Capital Improvement Projects" in text or "Capital Improvement Projects" in description_block:
                project_type = "capital"
            if "Disaster Recovery Projects" in text or "Disaster Recovery Projects" in description_block:
                project_type = "disaster"

            topic = []
            if re.search(r'emergency', description_block, re.IGNORECASE):
                topic.append('emergency')
            if re.search(r'FEMA', description_block, re.IGNORECASE):
                topic.append('FEMA')
            if re.search(r'fire', description_block, re.IGNORECASE):
                topic.append('fire')
            if re.search(r'storm drain|drainage', description_block, re.IGNORECASE):
                topic.append('storm drain/drainage')
            
            # Ensure at least one relevant topic or disaster type
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

# Additional filtering to ensure relevance if the initial regex was too broad
projects_df = projects_df[projects_df['topic'].str.contains('emergency|FEMA', case=False, na=False) | projects_df['type'].str.contains('disaster', case=False, na=False)]

print("__RESULT__:")
print(projects_df.to_json(orient='records'))"""

env_args = {'var_function-call-13801791921657955456': 'file_storage/function-call-13801791921657955456.json'}

exec(code, env_args)
