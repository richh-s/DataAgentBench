code = """import pandas as pd
import json
import re

# Load the civic documents data
with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

disaster_projects_starting_2022_names = set()

for doc in civic_docs_data:
    text = doc['text']

    # This regex aims to capture project blocks more reliably.
    # It looks for a project name (capitalized line) and captures the text following it (details)
    # until it encounters another capitalized line (potential next project) or a major section header, or end of document.
    # Using a raw string (r'...') to simplify backslash handling in regex.
    project_block_pattern = re.compile(
        r"^(?P<Project_Name>[A-Z][A-Za-z0-9\s&,-_':\/.()]+?)$\n"  # Project Name (starts with capital, ends line)
        r"(?P<Details>(?:(?!^[A-Z][A-Za-z0-9\s&,-_':\/.()]+?$|^Agenda Item #|^Page \d+ of \d+)[\s\S])*?)"
        , re.MULTILINE
    )

    for match in project_block_pattern.finditer(text):
        project_name = match.group("Project_Name").strip()
        details = match.group("Details").strip()

        is_disaster = False
        # Check for disaster keywords in the project name or its details (case-insensitive)
        if re.search(r"FEMA|CalOES|CalJPIA|Disaster Recovery", project_name + " " + details, re.IGNORECASE):
            is_disaster = True
        
        if is_disaster:
            start_date_2022 = None
            # Search for a 2022 date within the details, specifically for start/completion related phrases.
            # Using a raw string (r'...') for the date regex.
            date_match = re.search(
                r"(?:Begin\sConstruction|Construction\swas\scompleted|Completed):\s*"
                r"(?P<Date_Info>\b2022\b(?:[-\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\s]\d{2})?)"
                , details, re.IGNORECASE
            )
            
            if date_match:
                start_date_2022 = date_match.group("Date_Info").strip()
                disaster_projects_starting_2022_names.add(project_name)

# Convert the set to a list for JSON serialization
final_project_names = list(disaster_projects_starting_2022_names)

print("__RESULT__:")
print(json.dumps(final_project_names))"""

env_args = {'var_function-call-4922019997739677456': ['civic_docs'], 'var_function-call-788512929960335419': 'file_storage/function-call-788512929960335419.json', 'var_function-call-9254905820928177274': [], 'var_function-call-6587616414360749789': [], 'var_function-call-3446571632783907127': [], 'var_function-call-2261813058681952031': [], 'var_function-call-8822505650285935510': [], 'var_function-call-8392476062244336283': []}

exec(code, env_args)
