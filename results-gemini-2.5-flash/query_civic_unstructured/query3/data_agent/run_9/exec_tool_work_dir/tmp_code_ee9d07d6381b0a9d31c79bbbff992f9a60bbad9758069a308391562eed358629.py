code = """import re
import json

docs = json.loads(open(locals()['var_function-call-17046440918725083585'], 'r').read())
projects_data = []

keywords = ['emergency', 'FEMA']

for doc in docs:
    text = doc['text']

    # Regex to find project names and their subsequent descriptions
    project_sections = re.findall(r'\n([A-Z][a-zA-Z0-9&\s,-\/()'\\]+?)(?:\n|\(cid:190\))', text)

    for i in range(len(project_sections)):
        project_name = project_sections[i].strip()

        # Define the content for the current project
        if i + 1 < len(project_sections):
            project_content = text[text.find(project_sections[i]):text.find(project_sections[i+1])]
        else:
            project_content = text[text.find(project_sections[i]):]

        # Check if 'emergency' or 'FEMA' is in the project name or content
        if any(keyword in project_name or keyword in project_content for keyword in keywords):
            
            status_match = re.search(r'status:\s*([a-zA-Z\s-]+)', project_content, re.IGNORECASE)
            status = status_match.group(1).strip() if status_match else "N/A"

            # Add more specific status extraction for "Capital Improvement Projects (Design)", "Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)"
            if "Capital Improvement Projects (Design)" in project_content:
                status = "design"
            elif "Capital Improvement Projects (Construction)" in project_content:
                status = "construction"
            elif "Capital Improvement Projects (Not Started)" in project_content:
                status = "not started"
            elif "Updates: Project is currently under construction" in project_content:
                status = "construction"
            elif "Construction was completed" in project_content:
                status = "completed"

            projects_data.append({
                "Project_Name": project_name,
                "Status": status
            })

print('__RESULT__:')
print(json.dumps(projects_data))"""

env_args = {'var_function-call-6356119364886939959': ['civic_docs'], 'var_function-call-17046440918725083585': 'file_storage/function-call-17046440918725083585.json'}

exec(code, env_args)
