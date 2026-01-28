code = """import pandas as pd
import json
import re

# Load the civic documents data
with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

disaster_projects_starting_2022_names = set()

# Define regex patterns as raw strings within the Python code.
PROJECT_BLOCK_PATTERN = r"(?P<Project_Name>[A-Z][A-Za-z0-9\s&,-_':/\.\(\)]+?)\n(?:\(cid:\d+?\)\sUpdates:[^\n]*\n(?:\(cid:\d+?\)[^\n]*\n)*?)?(?:\(cid:\d+?\)\sProject Description:[^\n]*\n(?:\(cid:\d+?\)[^\n]*\n)*?)?\(cid:\d+?\)\s(?:Project|Estimated)\sSchedule:[^\n]*\n(?P<Schedule_Details>(?:\(cid:\d+?\)[^\n]*\n)*?)"
DISASTER_KEYWORDS_PATTERN = r"FEMA|CalOES|CalJPIA|Disaster Recovery|Woolsey Fire|emergency|fire"
DATE_2022_PATTERN = r"(?:Begin\sConstruction|Construction\swas\scompleted|Completed):\s*(?P<Date_Info>\b2022\b(?:[-\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\s]\d{2})?)"

for doc in civic_docs_data:
    text = doc['text']

    # Find all project blocks using the defined pattern
    for match in re.finditer(PROJECT_BLOCK_PATTERN, text, re.MULTILINE):
        project_name = match.group("Project_Name").strip()
        schedule_details = match.group("Schedule_Details").strip()
        
        # Combine project name and schedule details for a comprehensive context search
        full_project_context = project_name + " " + schedule_details

        is_disaster = False
        if re.search(DISASTER_KEYWORDS_PATTERN, full_project_context, re.IGNORECASE):
            is_disaster = True
        
        if is_disaster:
            # Check for a 2022 start/completion date within the schedule details
            date_match = re.search(DATE_2022_PATTERN, schedule_details, re.IGNORECASE)
            if date_match:
                disaster_projects_starting_2022_names.add(project_name)

# Convert the set of unique project names to a list for JSON serialization.
unique_disaster_projects_2022 = list(disaster_projects_starting_2022_names)

# Now, query the funding database for these extracted project names.
if unique_disaster_projects_2022:
    # Prepare project names for an SQL IN clause. Escape single quotes in names for SQL.
    quoted_project_names = [f"'{name.replace("'", "''")}'" for name in unique_disaster_projects_2022]
    project_names_sql_list = ", ".join(quoted_project_names)
    
    # Construct the SQL query to sum funding for these projects.
    sql_query = f"SELECT SUM(Amount) FROM Funding WHERE Project_Name IN ({project_names_sql_list});"
    
    print('__RESULT__:')
    print(json.dumps({"sql_query": sql_query}))
else:
    print('__RESULT__:')
    print(json.dumps({"sql_query": "SELECT 0;"})) # Return 0 if no projects found"""

env_args = {'var_function-call-4922019997739677456': ['civic_docs'], 'var_function-call-788512929960335419': 'file_storage/function-call-788512929960335419.json', 'var_function-call-9254905820928177274': [], 'var_function-call-6587616414360749789': [], 'var_function-call-3446571632783907127': [], 'var_function-call-2261813058681952031': [], 'var_function-call-8822505650285935510': [], 'var_function-call-8392476062244336283': [], 'var_function-call-11102447910259671137': ['Funding']}

exec(code, env_args)
