code = """import re
import json

docs = json.loads(open(locals()['var_function-call-17046440918725083585'], 'r').read())
projects_data = []

keywords = ['emergency', 'FEMA']

for doc in docs:
    text = doc['text']

    # Splitting the document into potential project blocks
    # Looking for lines that start with capital letters followed by project-like content
    project_blocks = re.split(r'\n([A-Z][A-Za-z0-9&\s,-\/()']*[A-Za-z0-9&\s,-\/()])\n', text)

    # The split often creates empty strings or irrelevant sections, so we'll process pairs
    # The first element in project_blocks is usually before the first project, so we skip it.
    for i in range(1, len(project_blocks), 2):
        project_name = project_blocks[i].strip()
        project_content = project_blocks[i+1].strip() if i+1 < len(project_blocks) else ""

        # Check if 'emergency' or 'FEMA' is in the project name or content
        if any(keyword.lower() in project_name.lower() or keyword.lower() in project_content.lower() for keyword in keywords):

            status = "N/A"
            # More robust status extraction
            if "completed" in project_content.lower():
                status = "completed"
            elif "under construction" in project_content.lower() or "begin construction" in project_content.lower():
                status = "construction"
            elif "design" in project_content.lower() or "preliminary design" in project_content.lower():
                status = "design"
            elif "not started" in project_content.lower() or "identified but not begun" in project_content.lower():
                status = "not started"
            elif "awaiting final fema/caloes approval" in project_content.lower():
                status = "design" # Project is designed, awaiting approval to start construction


            projects_data.append({
                "Project_Name": project_name,
                "Status": status
            })

print('__RESULT__:')
print(json.dumps(projects_data))"""

env_args = {'var_function-call-6356119364886939959': ['civic_docs'], 'var_function-call-17046440918725083585': 'file_storage/function-call-17046440918725083585.json'}

exec(code, env_args)
