code = """import pandas as pd
import json
import re

# Load the civic documents data from storage
with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

disaster_projects_starting_2022_names = set()

# Define regex patterns as raw strings
PROJECT_NAME_HEURISTIC_PATTERN = re.compile(r"^[A-Z0-9][A-Za-z0-9\s&,-_\':/\.\(\)]+?$")
DISASTER_KEYWORDS_PATTERN = re.compile(r"FEMA|CalOES|CalJPIA|Disaster Recovery|Woolsey Fire|emergency|fire", re.IGNORECASE)
DATE_2022_PATTERN = re.compile(r"(?:Begin\sConstruction|Project\sSchedule:\sBegin\sConstruction|Construction\swas\scompleted|Completed):\s*(?P<Date_Info>\b2022\b(?:[-\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\s]\d{2})?)", re.IGNORECASE)

for doc in civic_docs_data:
    text = doc['text']
    lines = text.split('\n')
    
    current_project_name = None
    current_project_details_buffer = []

    for line in lines:
        stripped_line = line.strip()

        # Check if the line is a potential project name based on defined pattern and exclusions.
        is_potential_project_name = bool(PROJECT_NAME_HEURISTIC_PATTERN.match(stripped_line)) and \
                                  not stripped_line.startswith("(cid:") and \
                                  not stripped_line.startswith("Agenda Item") and \
                                  not stripped_line.startswith("Page ") and \
                                  len(stripped_line) > 5 # Filter out very short lines

        if is_potential_project_name:
            if current_project_name:
                # Process the previous project block
                full_project_context = current_project_name + ' ' + ' '.join(current_project_details_buffer)
                
                is_disaster = bool(DISASTER_KEYWORDS_PATTERN.search(full_project_context))
                
                if is_disaster:
                    date_match = DATE_2022_PATTERN.search(full_project_context)
                    if date_match:
                        disaster_projects_starting_2022_names.add(current_project_name)

            # Start a new project block
            current_project_name = stripped_line
            current_project_details_buffer = []
        elif current_project_name: # If still within a project block (after a project name).
            current_project_details_buffer.append(stripped_line)
    
    # After the loop, process the last buffered project block if any.
    if current_project_name:
        full_project_context = current_project_name + ' ' + ' '.join(current_project_details_buffer)
        
        is_disaster = bool(DISASTER_KEYWORDS_PATTERN.search(full_project_context))
        
        if is_disaster:
            date_match = DATE_2022_PATTERN.search(full_project_context)
            if date_match:
                disaster_projects_starting_2022_names.add(current_project_name)

# Convert the set of unique project names to a list
unique_disaster_projects_2022 = list(disaster_projects_starting_2022_names)

# Now, construct the SQL query to get funding for these projects
if unique_disaster_projects_2022:
    # Prepare project names for an SQL IN clause. Escape single quotes within names for SQL compatibility.
    quoted_project_names = [f"'{name.replace("'", "''")}'" for name in unique_disaster_projects_2022]
    project_names_sql_list = ", ".join(quoted_project_names)
    
    # Construct the SQL query
    sql_query = f"SELECT SUM(Amount) FROM Funding WHERE Project_Name IN ({project_names_sql_list});"
    
    print("__RESULT__:")
    print(json.dumps({"sql_query": sql_query}))
else:
    print("__RESULT__:")
    print(json.dumps({"sql_query": "SELECT 0;"})) # Return 0 if no projects found"""

env_args = {'var_function-call-4922019997739677456': ['civic_docs'], 'var_function-call-788512929960335419': 'file_storage/function-call-788512929960335419.json', 'var_function-call-9254905820928177274': [], 'var_function-call-6587616414360749789': [], 'var_function-call-3446571632783907127': [], 'var_function-call-2261813058681952031': [], 'var_function-call-8822505650285935510': [], 'var_function-call-8392476062244336283': [], 'var_function-call-11102447910259671137': ['Funding'], 'var_function-call-13676724116295004975': [], 'var_function-call-15594358079768116859': {'sql_query': 'SELECT 0;'}}

exec(code, env_args)
