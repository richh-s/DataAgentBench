code = """import json
import re

with open(locals()['var_function-call-7990474508499764104'], 'r') as f:
    civic_docs = json.load(f)

completed_park_projects_2022 = set()

for doc in civic_docs:
    text = doc['text']
    
    # Split text into potential project sections. A project section starts with a bold/capitalized title
    # and contains details. Using a regex that captures a title line and everything until the next title or end of string.
    # Using r"""...""" for multi-line string in Python code itself for readability and to avoid escaping issues for inner quotes.
    # Ensure internal regex backslashes are properly escaped for Python string literals (e.g., \s becomes \\s).
    sections = re.findall(
        r'(?m)^([A-Z][a-zA-Z0-9&\\s\\-]+(?:Project|Park|Playground|Improvements)?(?:\\s\\(FEMA Project\\))?)\n' # Project Name
        r'((?:(?!^[A-Z][a-zA-Z0-9&\\s\\-]+(?:Project|Park|Playground|Improvements)?(?:\\s\\(FEMA Project\\))?).)*)', # Details block
        text, re.DOTALL
    )

    for project_name_raw, details_raw in sections:
        project_name = project_name_raw.strip()
        details = details_raw.strip()

        is_park_project = False
        if 'Park' in project_name or 'Playground' in project_name: # Check project name directly
            is_park_project = True
        # Additional check within details if topic explicitly mentions park or playground
        elif re.search(r'topic:\\s*.*?park|playground', details, re.IGNORECASE):
            is_park_project = True

        if is_park_project:
            # Look for completion status and 2022 year within the details.
            # This regex aims to capture phrases indicating completion and the year 2022.
            # Examples: "completed November 2022", "Complete Construction: Fall 2022", "Construction was completed, November 2022"
            completion_2022_pattern = re.compile(
                r'(?:completed|Construction was completed|Notice of completion filed|Complete Construction:|Complete Design:).*?2022|\\b2022\\b(?:-(?:Spring|Fall|0[1-9]|1[0-2])|\\s(?:January|February|March|April|May|June|July|August|September|October|November|December))'
                , re.IGNORECASE | re.DOTALL
            )
            if completion_2022_pattern.search(details):
                # Clean up any (cid:xxx) artifacts from the project name
                cleaned_name = re.sub(r'\\(cid:190\\)|\\s\\(cid:131\\)', '', project_name).strip()
                completed_park_projects_2022.add(cleaned_name)

print("__RESULT__:")
print(json.dumps(list(completed_park_projects_2022))))"""

env_args = {'var_function-call-2531287041203044027': ['civic_docs'], 'var_function-call-7990474508499764104': 'file_storage/function-call-7990474508499764104.json', 'var_function-call-16366149949085286234': ['test'], 'var_function-call-18034137513589187498': ['Funding']}

exec(code, env_args)
