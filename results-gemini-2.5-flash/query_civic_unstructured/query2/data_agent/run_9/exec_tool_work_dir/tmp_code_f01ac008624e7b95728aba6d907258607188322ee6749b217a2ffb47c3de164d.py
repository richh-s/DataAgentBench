code = """import re
import json

file_path = locals()['var_function-call-4111322049544134174']

with open(file_path, 'r') as f:
    data = json.load(f)

completed_park_projects_2022 = []

for doc in data:
    text = doc.get('text', '')
    
    # Regex to find project names that contain 'Park' and are explicitly completed in 2022
    # This pattern looks for: Project Name (with 'Park')
    # followed by 'Updates:' or description, and then 'Construction was completed <Month> 2022'.
    project_completion_pattern = re.compile(
        r'([A-Za-z0-9\s_\-]+(?:\sPark[A-Za-z0-9\s_\-]+)?)\n\n(?:\(cid:\d+\))?\sUpdates:.*?Construction was completed ([A-Za-z]+\s2022)',
        re.DOTALL
    )
    
    for match in project_completion_pattern.finditer(text):
        project_name = match.group(1).strip()
        completion_date = match.group(2).strip()
        
        # Ensure 'park' is in the project name (case-insensitive) and it was completed in 2022
        if "park" in project_name.lower() and "2022" in completion_date:
            if project_name not in completed_park_projects_2022: # Avoid duplicates
                completed_park_projects_2022.append(project_name)

print("__RESULT__:")
print(json.dumps(completed_park_projects_2022))"""

env_args = {'var_function-call-3624698550735432088': ['civic_docs'], 'var_function-call-4588781190690673145': [], 'var_function-call-4111322049544134174': 'file_storage/function-call-4111322049544134174.json'}

exec(code, env_args)
