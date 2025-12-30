code = """import pandas as pd
import json
import re

# Load the civic documents data
with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

disaster_projects_starting_2022_names = set()

# Define regex patterns using raw string literals for clarity and correct escaping.
PROJECT_NAME_LINE_PATTERN = r"^[A-Z][A-Za-z0-9\s&,-_\':/\.\(\)]+?$"
DISASTER_KEYWORDS_PATTERN = r"FEMA|CalOES|CalJPIA|Disaster Recovery|Woolsey Fire"
DATE_2022_PATTERN = r"(?:Begin\sConstruction|Project\sSchedule:\sBegin\sConstruction|Construction\swas\scompleted|Completed):\s*(?P<Date_Info>\b2022\b(?:[-\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\s]\d{2})?)"

for doc in civic_docs_data:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # Check if the line looks like a project name.
        if re.match(PROJECT_NAME_LINE_PATTERN, stripped_line) and \
           not stripped_line.startswith("(cid:") and \
           not stripped_line.startswith("Agenda Item") and \
           not stripped_line.startswith("Page ") and \
           len(stripped_line) > 5:

            project_name_candidate = stripped_line
            
            # Create a context window: the project name line itself and a few lines after it.
            # Adjust the window size as needed to capture relevant details.
            context_lines = lines[i : min(i + 10, len(lines))]
            project_context = " ".join(context_lines)

            # Check for disaster keywords in the project context.
            is_disaster = bool(re.search(DISASTER_KEYWORDS_PATTERN, project_context, re.IGNORECASE))
            
            if is_disaster:
                # Check for a 2022 start/completion date in the project context.
                date_match = re.search(DATE_2022_PATTERN, project_context, re.IGNORECASE)
                if date_match:
                    disaster_projects_starting_2022_names.add(project_name_candidate)

# Convert the set to a list for JSON serialization.
unique_disaster_projects_2022 = list(disaster_projects_starting_2022_names)

# Now, query the funding database for these extracted project names.
if unique_disaster_projects_2022:
    # Prepare project names for an SQL IN clause. Escape single quotes in names for SQL.
    quoted_project_names = [f"'{name.replace("'", "''")}'" for name in unique_disaster_projects_2022]
    project_names_sql_list = ", ".join(quoted_project_names)
    
    # Construct the SQL query to sum funding for these projects.
    sql_query = f"SELECT SUM(Amount) FROM Funding WHERE Project_Name IN ({project_names_sql_list});"
    
    print("__RESULT__:")
    print(json.dumps({"sql_query": sql_query}))
else:
    print("__RESULT__:")
    print(json.dumps({"sql_query": "SELECT 0;"})) # Return 0 if no projects found"""

env_args = {'var_function-call-4922019997739677456': ['civic_docs'], 'var_function-call-788512929960335419': 'file_storage/function-call-788512929960335419.json', 'var_function-call-9254905820928177274': [], 'var_function-call-6587616414360749789': [], 'var_function-call-3446571632783907127': [], 'var_function-call-2261813058681952031': [], 'var_function-call-8822505650285935510': [], 'var_function-call-8392476062244336283': [], 'var_function-call-11102447910259671137': ['Funding']}

exec(code, env_args)
