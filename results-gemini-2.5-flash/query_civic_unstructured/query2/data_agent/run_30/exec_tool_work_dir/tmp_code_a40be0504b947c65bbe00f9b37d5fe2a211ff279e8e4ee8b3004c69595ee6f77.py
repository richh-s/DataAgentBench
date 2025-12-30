code = """import json
import re

with open(locals()['var_function-call-7990474508499764104'], 'r') as f:
    civic_docs = json.load(f)

completed_park_projects_2022_names = []

for doc in civic_docs:
    text = doc['text']

    # Project blocks often start with a capitalized project name and include details until the next project or end of document.
    # Using a more forgiving pattern to capture project names and their associated text blocks.
    # Using a raw string (r'...') to avoid excessive backslash escaping for regex itself, 
    # but still need to be careful with Python string literal escapes if triple quotes are used.
    # The pattern looks for a project name (starting with capital letters/numbers/&) followed by any character (non-greedy) 
    # until the next project name pattern or the end of the document.

    # This regex attempts to capture a project name on a new line, and then all subsequent lines
    # until it finds another line that looks like a project name (starts with caps, ends with Project/Park/Playground/etc)
    # or it reaches the end of the text. 
    project_pattern = re.compile(
        r'(?m)^([A-Z][a-zA-Z0-9&\\s\\-]+(?:Project|Park|Playground|Improvements)?(?:\\s\\(FEMA Project\\))?)\n' # Project Name
        r'((?:(?!^[A-Z][a-zA-Z0-9&\\s\\-]+(?:Project|Park|Playground|Improvements)?(?:\\s\\(FEMA Project\\))?).)*)', # Details block
        re.DOTALL
    )

    for project_name_raw, details_raw in project_pattern.findall(text):
        project_name = project_name_raw.strip()
        details = details_raw.strip()

        is_park_project = False
        # Check if 'Park' or 'Playground' is explicitly in the project name
        if 'Park' in project_name or 'Playground' in project_name:
            is_park_project = True
        # Also check in details if topic explicitly mentions park or playground
        elif re.search(r'topic:\\s*.*?park|playground', details, re.IGNORECASE):
            is_park_project = True

        if is_park_project:
            # Check for completion status and 2022 in the details block
            # Looking for variations of "completed" and "2022" near each other.
            # This pattern is more flexible for different phrasing.
            if re.search(r'completed.*?2022|2022.*?completed', details, re.IGNORECASE) or \
               re.search(r'Construction was completed.*?2022|2022.*?Construction was completed', details, re.IGNORECASE) or \
               re.search(r'Notice of completion filed.*?2022|2022.*?Notice of completion filed', details, re.IGNORECASE):
                
                # Ensure the 2022 refers to the completion date/year, not just mentioned elsewhere
                # This regex checks for words related to 'complete' or 'construction' followed by a year, or a month-year combo
                if re.search(r'(?:completed|Complete Construction|Complete Design|November|December|January|February|March|April|May|June|July|August|September|October).*?2022', details, re.IGNORECASE):
                    completed_park_projects_2022_names.append(project_name)

# Remove duplicates
unique_completed_park_projects_2022 = list(set(completed_park_projects_2022_names))

print("__RESULT__:")
print(json.dumps(unique_completed_park_projects_2022)))"""

env_args = {'var_function-call-2531287041203044027': ['civic_docs'], 'var_function-call-7990474508499764104': 'file_storage/function-call-7990474508499764104.json', 'var_function-call-16366149949085286234': ['test'], 'var_function-call-18034137513589187498': ['Funding']}

exec(code, env_args)
