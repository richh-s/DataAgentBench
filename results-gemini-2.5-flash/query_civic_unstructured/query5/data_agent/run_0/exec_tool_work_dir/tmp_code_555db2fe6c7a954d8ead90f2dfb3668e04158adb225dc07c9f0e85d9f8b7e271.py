code = """import pandas as pd
import json
import re

# Load the civic documents data
with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

disaster_projects_found = set()

for doc in civic_docs_data:
    text = doc['text']

    # This regex attempts to broadly capture a project name and its associated schedule/update details.
    # It looks for a capitalized line (potential project name) followed by (cid:xxx) bullet points
    # that often contain 'Updates' and 'Schedule'.
    # The goal is to capture enough context to determine if it's disaster-related and started in 2022.
    # Using a raw string literal (r'...') for the regex pattern.
    project_block_pattern = re.compile(
        r"^(?P<Project_Name>[A-Z][A-Za-z0-9\s&,-_\':\/.()]+?)$\n" # Project Name line
        r"(?P<Details>(?:\\(cid:\\d+?\\)[\\s\\S]*?)*?)" # Captures all (cid:xxx) lines that follow non-greedily
        , re.MULTILINE
    )

    for match in project_block_pattern.finditer(text):
        project_name = match.group("Project_Name").strip()
        details = match.group("Details").strip()

        # Combine project name and details for keyword searching to get full context.
        full_project_context = project_name + " " + details

        is_disaster = False
        # Check for disaster keywords in the combined context (case-insensitive).
        if re.search(r"FEMA|CalOES|CalJPIA|Disaster Recovery", full_project_context, re.IGNORECASE):
            is_disaster = True
        
        if is_disaster:
            # Search for a 2022 date associated with construction start or completion within the details.
            # This regex looks for phrases like "Begin Construction:", "Construction was completed:", "Completed:"
            # followed by a date string that explicitly contains "2022".
            date_match = re.search(
                r"(?:Begin\\sConstruction|Construction\\swas\\scompleted|Completed):\\s*"
                r"(?P<Date_Info>\\b2022\\b(?:[-\\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\\s]\\d{2})?)",
                details, re.IGNORECASE
            )
            
            if date_match:
                # If both disaster keywords and a 2022 start/completion date are found,
                # add the project name to our set to ensure uniqueness.
                disaster_projects_found.add(project_name)

# Convert the set of unique project names to a list for the next step.
project_names_list = list(disaster_projects_found)

print("__RESULT__:")
print(json.dumps(project_names_list))"""

env_args = {'var_function-call-4922019997739677456': ['civic_docs'], 'var_function-call-788512929960335419': 'file_storage/function-call-788512929960335419.json', 'var_function-call-9254905820928177274': [], 'var_function-call-6587616414360749789': [], 'var_function-call-3446571632783907127': [], 'var_function-call-2261813058681952031': [], 'var_function-call-8822505650285935510': [], 'var_function-call-8392476062244336283': [], 'var_function-call-11102447910259671137': ['Funding']}

exec(code, env_args)
