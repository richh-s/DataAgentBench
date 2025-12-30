code = """import pandas as pd
import json
import re

# Load the civic documents data
with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

disaster_projects_starting_2022_names = set()

for doc in civic_docs_data:
    text = doc['text']

    # Iterate through each line of the document to identify potential project names.
    lines = text.split('\n')
    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # Heuristic for a project name: starts with a capital or digit, not a bullet, not a header, reasonable length.
        is_potential_project_name = bool(re.match(r'^[A-Z0-9][A-Za-z0-9\\s&,-_\':\/.()]+?$', stripped_line)) and \
                                  not stripped_line.startswith('(cid:') and \
                                  not stripped_line.startswith('Agenda Item') and \
                                  not stripped_line.startswith('Page ') and \
                                  len(stripped_line) > 5

        if is_potential_project_name:
            project_name = stripped_line
            # Create a context window around the project name to search for details.
            # Look at the project name line itself and the next few lines for schedule and disaster keywords.
            context_lines = lines[i:min(i + 10, len(lines))]
            project_context = "\n".join(context_lines)

            is_disaster = False
            # Check for disaster keywords within the project's immediate context.
            if re.search(r'FEMA|CalOES|CalJPIA|Disaster Recovery', project_context, re.IGNORECASE):
                is_disaster = True
            
            if is_disaster:
                # Search for a '2022' date associated with starting/completion within the context.
                date_match = re.search(
                    r'(?:Begin\\sConstruction|Construction\\swas\\scompleted|Completed):\\s*'
                    r'(?P<Date_Info>\\b2022\\b(?:[-\\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\\s]\\d{2})?)'
                    , project_context, re.IGNORECASE
                )
                
                if date_match:
                    # If both conditions are met, add the project name to the set.
                    disaster_projects_starting_2022_names.add(project_name)

# Convert the set to a list for JSON serialization.
unique_disaster_projects_2022 = list(disaster_projects_starting_2022_names)

print("__RESULT__:")
print(json.dumps(unique_disaster_projects_2022))"""

env_args = {'var_function-call-4922019997739677456': ['civic_docs'], 'var_function-call-788512929960335419': 'file_storage/function-call-788512929960335419.json', 'var_function-call-9254905820928177274': [], 'var_function-call-6587616414360749789': [], 'var_function-call-3446571632783907127': [], 'var_function-call-2261813058681952031': [], 'var_function-call-8822505650285935510': [], 'var_function-call-8392476062244336283': [], 'var_function-call-11102447910259671137': ['Funding']}

exec(code, env_args)
