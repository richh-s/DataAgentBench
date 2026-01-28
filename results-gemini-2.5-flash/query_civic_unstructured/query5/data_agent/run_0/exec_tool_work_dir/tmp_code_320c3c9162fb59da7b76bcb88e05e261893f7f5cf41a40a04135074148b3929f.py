code = """import pandas as pd
import json
import re

# Load the civic documents data
with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

disaster_projects_starting_2022_names = set()

for doc in civic_docs_data:
    text = doc['text']

    # Split the document into lines for easier processing
    lines = text.split('\n')
    
    current_project_name = None
    current_project_details_buffer = []

    for line_num, line in enumerate(lines):
        stripped_line = line.strip()

        # Heuristic to identify a potential project name.
        # A project name is often a capitalized line, not a bullet point or a common header/footer.
        # Using a raw string (r"...") for the regex pattern.
        # The character class includes: alphanumeric, whitespace, &, comma, hyphen, underscore, single quote, colon, slash, period, parentheses.
        is_potential_project_name = bool(re.match(r"^[A-Z0-9][A-Za-z0-9\\s&,-_\':/\\.\\(\\)]+?$", stripped_line)) and \
                                  not stripped_line.startswith("(cid:") and \
                                  not stripped_line.startswith("Agenda Item") and \
                                  not stripped_line.startswith("Page ") and \
                                  len(stripped_line) > 5 # Filter out very short lines that are unlikely to be project names

        if is_potential_project_name:
            # If we were previously collecting details for a project, process it before starting a new one.
            if current_project_name:
                full_project_context = current_project_name + ' ' + ' '.join(current_project_details_buffer)
                
                is_disaster = False
                # Check for disaster keywords in the collected project context (case-insensitive).
                if re.search(r"FEMA|CalOES|CalJPIA|Disaster Recovery", full_project_context, re.IGNORECASE):
                    is_disaster = True
                
                if is_disaster:
                    # Search for a '2022' date within the full project context, associated with start/completion phrases.
                    date_match = re.search(
                        r"(?:Begin\\sConstruction|Project\\sSchedule:\\sBegin\\sConstruction|Construction\\swas\\scompleted|Completed):\\s*"
                        r"(?P<Date_Info>\\b2022\\b(?:[-\\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\\s]\\d{2})?)",
                        full_project_context, re.IGNORECASE
                    )
                    if date_match:
                        # If both disaster-related and 2022 start/completion date are found, add project name.
                        disaster_projects_starting_2022_names.add(current_project_name)

            # Start collecting for the new project.
            current_project_name = stripped_line
            current_project_details_buffer = []
        elif current_project_name:
            # If not a new project name, and we're in a project context, append the line to the details buffer.
            current_project_details_buffer.append(stripped_line)
    
    # After iterating through all lines, process the very last project block in the document, if any.
    if current_project_name:
        full_project_context = current_project_name + ' ' + ' '.join(current_project_details_buffer)
        
        is_disaster = False
        if re.search(r"FEMA|CalOES|CalJPIA|Disaster Recovery", full_project_context, re.IGNORECASE):
            is_disaster = True
        
        if is_disaster:
            date_match = re.search(
                r"(?:Begin\\sConstruction|Project\\sSchedule:\\sBegin\\sConstruction|Construction\\swas\\scompleted|Completed):\\s*"
                r"(?P<Date_Info>\\b2022\\b(?:[-\\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\\s]\\d{2})?)",
                full_project_context, re.IGNORECASE
            )
            if date_match:
                disaster_projects_starting_2022_names.add(current_project_name)

# Convert the set of unique project names to a list for JSON serialization.
unique_disaster_projects_2022 = list(disaster_projects_starting_2022_names)

# Now query the funding database for these projects.
if unique_disaster_projects_2022:
    # Prepare a list of project names for SQL IN clause.
    # SQL requires strings to be quoted, e.g., "'Project A', 'Project B'".
    # Escape single quotes within project names if any exist before quoting.
    # No project names from preview seem to have internal single quotes.
    quoted_project_names = [f"'{name.replace("'", "''")}'" for name in unique_disaster_projects_2022]
    project_names_sql = ", ".join(quoted_project_names)
    
    # Construct the SQL query to get funding for these projects.
    # Placeholder for query_db call, to be executed in the next step.
    # print(f"SELECT SUM(Amount) FROM Funding WHERE Project_Name IN ({project_names_sql});")
    # For now, just output the project names to ensure extraction is correct.
    print('__RESULT__:')
    print(json.dumps(unique_disaster_projects_2022))

else:
    print('__RESULT__:')
    print(json.dumps([]))"""

env_args = {'var_function-call-4922019997739677456': ['civic_docs'], 'var_function-call-788512929960335419': 'file_storage/function-call-788512929960335419.json', 'var_function-call-9254905820928177274': [], 'var_function-call-6587616414360749789': [], 'var_function-call-3446571632783907127': [], 'var_function-call-2261813058681952031': [], 'var_function-call-8822505650285935510': [], 'var_function-call-8392476062244336283': [], 'var_function-call-11102447910259671137': ['Funding']}

exec(code, env_args)
