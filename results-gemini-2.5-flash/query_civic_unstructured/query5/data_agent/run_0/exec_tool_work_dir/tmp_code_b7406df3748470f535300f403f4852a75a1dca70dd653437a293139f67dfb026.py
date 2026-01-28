code = """import pandas as pd
import json
import re

# Load the civic documents data
with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

disaster_projects_starting_2022_names = set()

for doc in civic_docs_data:
    text = doc['text']

    # Find all possible project names. A project name is often a capitalized line.
    # Using single quotes for regex and escaping the internal single quote. Backslashes are doubled for regex special chars.
    potential_project_name_matches = re.finditer('^[A-Z][A-Za-z0-9\\s&,-_\'\\/.()]+?$', text, re.MULTILINE)

    for name_match in potential_project_name_matches:
        project_name = name_match.group(0).strip()

        # Define a context window around the potential project name
        context_start = max(0, name_match.start() - 500)
        context_end = min(len(text), name_match.end() + 500)
        project_context = text[context_start:context_end]

        is_disaster = False
        # Check for disaster keywords in the project context (case-insensitive)
        if re.search('FEMA|CalOES|CalJPIA|Disaster Recovery', project_context, re.IGNORECASE):
            is_disaster = True
        
        if is_disaster:
            start_date_2022 = None
            # Search for a 2022 date within the project context associated with start/completion.
            # Backslashes are doubled for regex special chars.
            date_match = re.search(
                '(?:Begin\\sConstruction|Construction\\swas\\scompleted|Completed):?\\s*'
                '(?P<Date_Info>\\b2022\\b(?:[-\\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\\s]\\d{2})?)'
                , project_context, re.IGNORECASE
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
