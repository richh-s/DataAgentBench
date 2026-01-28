code = """import pandas as pd
import json
import re

# Load the civic documents data
with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

disaster_projects_starting_2022_names = set()

# Define the regex patterns using raw string literals with double quotes
# This helps avoid issues with single quotes inside the regex and simplifies backslash handling.
PROJECT_NAME_PATTERN = r"^[A-Z0-9][A-Za-z0-9\s&,-_':/\.\(\)]+?$"
DATE_MATCH_PATTERN = r"(?:Begin\sConstruction|Project\sSchedule:\sBegin\sConstruction|Construction\swas\scompleted|Completed):\s*(?P<Date_Info>\b2022\b(?:[-\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\s]\d{2})?)"
DISASTER_KEYWORDS_PATTERN = r"FEMA|CalOES|CalJPIA|Disaster Recovery"

for doc in civic_docs_data:
    text = doc['text']

    lines = text.split('\n')
    
    current_project_name = None
    current_project_details_buffer = []

    for line in lines:
        stripped_line = line.strip()

        is_potential_project_name = bool(re.match(PROJECT_NAME_PATTERN, stripped_line)) and \
                                  not stripped_line.startswith("(cid:") and \
                                  not stripped_line.startswith("Agenda Item") and \
                                  not stripped_line.startswith("Page ") and \
                                  len(stripped_line) > 5

        if is_potential_project_name:
            if current_project_name:
                full_project_context = current_project_name + ' ' + ' '.join(current_project_details_buffer)
                
                is_disaster = False
                if re.search(DISASTER_KEYWORDS_PATTERN, full_project_context, re.IGNORECASE):
                    is_disaster = True
                
                if is_disaster:
                    date_match = re.search(DATE_MATCH_PATTERN, full_project_context, re.IGNORECASE)
                    if date_match:
                        disaster_projects_starting_2022_names.add(current_project_name)

            current_project_name = stripped_line
            current_project_details_buffer = []
        elif current_project_name:
            current_project_details_buffer.append(stripped_line)
    
    if current_project_name:
        full_project_context = current_project_name + ' ' + ' '.join(current_project_details_buffer)
        
        is_disaster = False
        if re.search(DISASTER_KEYWORDS_PATTERN, full_project_context, re.IGNORECASE):
            is_disaster = True
        
        if is_disaster:
            date_match = re.search(DATE_MATCH_PATTERN, full_project_context, re.IGNORECASE)
            if date_match:
                disaster_projects_starting_2022_names.add(current_project_name)

unique_disaster_projects_2022 = list(disaster_projects_starting_2022_names)

print('__RESULT__:')
print(json.dumps(unique_disaster_projects_2022))"""

env_args = {'var_function-call-4922019997739677456': ['civic_docs'], 'var_function-call-788512929960335419': 'file_storage/function-call-788512929960335419.json', 'var_function-call-9254905820928177274': [], 'var_function-call-6587616414360749789': [], 'var_function-call-3446571632783907127': [], 'var_function-call-2261813058681952031': [], 'var_function-call-8822505650285935510': [], 'var_function-call-8392476062244336283': [], 'var_function-call-11102447910259671137': ['Funding']}

exec(code, env_args)
