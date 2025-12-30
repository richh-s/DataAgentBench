code = """import pandas as pd
import json
import re

# Load the civic documents data from storage
with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

disaster_projects_starting_2022_names = set()

# Define regex patterns as raw strings
# Project name candidate pattern: starts with a capital letter or digit, allows various chars, ends line
PROJECT_NAME_CANDIDATE_PATTERN = r"^[A-Z0-9][A-Za-z0-9\\s&,-_':/\\.\\(\\)]+?$"
# Keywords to identify disaster-related projects (case-insensitive)
DISASTER_KEYWORDS_PATTERN = r"FEMA|CalOES|CalJPIA|Disaster Recovery|Woolsey Fire|emergency|fire"
# Date pattern specifically looking for '2022' associated with start/completion phrases (case-insensitive)
DATE_2022_PATTERN = r"(?:Begin\\sConstruction|Project\\sSchedule:\\sBegin\\sConstruction|Construction\\swas\\scompleted|Completed):\\s*(?P<Date_Info>\\b2022\\b(?:[-\\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\\s]\\d{2})?)"

for doc in civic_docs_data:
    text = doc['text']
    lines = text.split('\\n')
    
    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # Check if the stripped line is a potential project name
        is_potential_project_name = bool(re.match(PROJECT_NAME_CANDIDATE_PATTERN, stripped_line)) and \
                                  not stripped_line.startswith("(cid:") and \
                                  not stripped_line.startswith("Agenda Item") and \
                                  not stripped_line.startswith("Page ") and \
                                  len(stripped_line) > 5

        if is_potential_project_name:
            project_name_candidate = stripped_line
            
            # Create a context window: the project name line and the next few lines (e.g., 5 lines) to capture details
            context_lines = lines[i : min(i + 5, len(lines))]
            project_context = " ".join(context_lines)

            # Check for disaster keywords in the project context
            is_disaster = bool(re.search(DISASTER_KEYWORDS_PATTERN, project_context, re.IGNORECASE))
            
            if is_disaster:
                # Check for a '2022' date in the project context that indicates start/completion
                date_match = re.search(DATE_2022_PATTERN, project_context, re.IGNORECASE)
                if date_match:
                    disaster_projects_starting_2022_names.add(project_name_candidate)

# Convert the set of unique project names to a list
unique_disaster_projects_2022 = list(disaster_projects_starting_2022_names)

# Now, construct the SQL query to get funding for these projects
if unique_disaster_projects_2022:
    # Prepare project names for an SQL IN clause. Escape single quotes within project names for SQL compatibility.
    quoted_project_names = [f"'{name.replace(\"'\", \"''\")}'" for name in unique_disaster_projects_2022]
    project_names_sql_list = ", ".join(quoted_project_names)
    
    # Construct the SQL query
    sql_query = f"SELECT SUM(Amount) FROM Funding WHERE Project_Name IN ({project_names_sql_list});"
    
    print("__RESULT__:")
    print(json.dumps({"sql_query": sql_query}))
else:
    print("__RESULT__:")
    print(json.dumps({"sql_query": "SELECT 0;"})) # Return 0 if no projects found"""

env_args = {'var_function-call-4922019997739677456': ['civic_docs'], 'var_function-call-788512929960335419': 'file_storage/function-call-788512929960335419.json', 'var_function-call-9254905820928177274': [], 'var_function-call-6587616414360749789': [], 'var_function-call-3446571632783907127': [], 'var_function-call-2261813058681952031': [], 'var_function-call-8822505650285935510': [], 'var_function-call-8392476062244336283': [], 'var_function-call-11102447910259671137': ['Funding'], 'var_function-call-13676724116295004975': []}

exec(code, env_args)
