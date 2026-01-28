code = """import re
import json

docs = json.loads(open(locals()['var_function-call-17046440918725083585'], 'r').read())
projects_data = []

keywords = ['emergency', 'FEMA']

# Regex to find project titles and their starting positions
# Project titles are typically on a new line, start with a capital,
# and are followed by a newline and then (cid:190) or "Updates:" or "Project Description:"
# The regex is carefully constructed and escaped for the `code` argument.
project_title_pattern = re.compile(r'\\n([A-Z][a-zA-Z0-9&\\s,-\/()]+?)\\n(?:\\(cid:190\\)|\\s*Updates:|\\s*Project Description:|\\s*Project Schedule:)', re.DOTALL)


for doc in docs:
    text = doc['text']
    
    # Find all project titles and their spans
    project_matches = []
    for m in project_title_pattern.finditer(text):
        # Store the project name (group 1) and its starting index
        project_matches.append((m.group(1).strip(), m.start()))

    # Now, iterate through the matches to extract content for each project
    for i in range(len(project_matches)):
        project_name, start_idx = project_matches[i]
        
        # Determine the end index for the current project's content
        if i + 1 < len(project_matches):
            end_idx = project_matches[i+1][1] # Content ends before the next project's start
        else:
            end_idx = len(text) # Last project, goes to end of document

        project_content = text[start_idx:end_idx]

        # Check if 'emergency' or 'FEMA' is in the project name or content
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
