code = """import re
import json

docs = json.loads(open(locals()['var_function-call-17046440918725083585'], 'r').read())
projects_data = []

keywords = ['emergency', 'FEMA']

project_pattern = re.compile(r'\n\n([A-Z][a-zA-Z0-9&\s,-\/()'\\]+?)\n(?:\(cid:190\)|\s*Project Description:|\s*Updates:)', re.DOTALL)

for doc in docs:
    text = doc['text']
    matches = list(project_pattern.finditer(text))

    for i, match in enumerate(matches):
        project_name = match.group(1).strip()
        start_index = match.start()

        if i + 1 < len(matches):
            end_index = matches[i+1].start()
        else:
            end_index = len(text)
        
        project_content = text[start_index:end_index]

        if any(keyword.lower() in project_name.lower() or keyword.lower() in project_content.lower() for keyword in keywords):
            status = "N/A"
            if "completed" in project_content.lower():
                status = "completed"
            elif "under construction" in project_content.lower() or "begin construction" in project_content.lower():
                status = "construction"
            elif "design" in project_content.lower() or "preliminary design" in project_content.lower() or "awaiting final fema/caloes approval" in project_content.lower():
                status = "design"
            elif "not started" in project_content.lower() or "identified but not begun" in project_content.lower():
                status = "not started"

            projects_data.append({
                "Project_Name": project_name,
                "Status": status
            })

print('__RESULT__:')
print(json.dumps(projects_data))"""

env_args = {'var_function-call-6356119364886939959': ['civic_docs'], 'var_function-call-17046440918725083585': 'file_storage/function-call-17046440918725083585.json'}

exec(code, env_args)
