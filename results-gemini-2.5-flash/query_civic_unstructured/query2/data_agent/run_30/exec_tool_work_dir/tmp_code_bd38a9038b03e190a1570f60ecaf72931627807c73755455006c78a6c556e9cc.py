code = """import json
import re

with open(locals()['var_function-call-7990474508499764104'], 'r') as f:
    civic_docs = json.load(f)

completed_park_projects_2022_names = set()

for doc in civic_docs:
    text = doc['text']
    
    # This regex attempts to capture a project name on a new line (starts with capital/digit, contains keywords)
    # and then the details block until the next similar project name or end of text. 
    # The project name part is group 1, details is group 2.
    # Using re.DOTALL to allow the details block to span multiple lines.
    # Using raw string literals for the regex to simplify backslash handling.
    project_pattern = re.compile(
        r'(?m)^([A-Z0-9][a-zA-Z0-9&\\s\\-]+(?:Project|Park|Playground|Improvements|Repairs)?(?:\\s\\(FEMA Project\\))?)\n'
        r'((?:(?!^[A-Z0-9][a-zA-Z0-9&\\s\\-]+(?:Project|Park|Playground|Improvements)?(?:\\s\\(FEMA Project\\))?).)*)',
        re.DOTALL
    )

    for project_name_raw, details_raw in project_pattern.findall(text):
        project_name = project_name_raw.strip()
        details = details_raw.strip()

        is_park_project = False
        if 'Park' in project_name or 'Playground' in project_name:
            is_park_project = True
        elif re.search(r'topic:\\s*.*?park|playground', details, re.IGNORECASE):
            is_park_project = True

        if is_park_project:
            # Check for completion status and the year 2022 within the details.
            # This pattern looks for "completed" or similar phrases in proximity to "2022" or a date in 2022.
            if re.search(r'(completed|Construction was completed|Notice of completion filed).*?2022', details, re.IGNORECASE) or \
               re.search(r'2022.*?(completed|Construction was completed|Notice of completion filed)', details, re.IGNORECASE) or \
               re.search(r'(Complete Construction|Complete Design):.*?2022', details, re.IGNORECASE) or \
               re.search(r'(?:November|December)\\s+2022', details, re.IGNORECASE):
                
                # Clean up (cid:xxx) artifacts from the project name before adding.
                cleaned_name = re.sub(r'\\(cid:190\\)|\\s\\(cid:131\\)', '', project_name).strip()
                completed_park_projects_2022_names.add(cleaned_name)

print("__RESULT__:")
print(json.dumps(list(completed_park_projects_2022_names))))"""

env_args = {'var_function-call-2531287041203044027': ['civic_docs'], 'var_function-call-7990474508499764104': 'file_storage/function-call-7990474508499764104.json', 'var_function-call-16366149949085286234': ['test'], 'var_function-call-18034137513589187498': ['Funding']}

exec(code, env_args)
