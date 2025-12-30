code = """import pandas as pd
import json
import re

# Load the civic documents data
with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

disaster_projects_starting_2022 = set()

for doc in civic_docs_data:
    text = doc['text']

    # Split the document into sections to isolate "Disaster Recovery Projects"
    # Use re.split with a non-capturing group to keep the delimiters in the result for context
    sections = re.split(r'(Disaster Recovery Projects)', text, flags=re.IGNORECASE)
    
    in_disaster_section = False
    
    for section_part in sections:
        if re.match(r'Disaster Recovery Projects', section_part, re.IGNORECASE):
            in_disaster_section = True
            continue
        
        if in_disaster_section:
            # Now, within this potential disaster section, find project names and their schedules.
            # Project names are usually on a line, followed by bulleted details.
            # Regex to find project names and capture their associated schedule block.
            project_schedule_pattern = re.compile(
                r"^(?P<Project_Name>[A-Z][A-Za-z0-9\\s&,-_\':/\\.\\(\\)]+?)$\n" # Project Name line
                r"(?P<Details>(?:\\(cid:\\d+?\\)[\\s\\S]*?)*?)" # Captures all (cid:xxx) lines that follow
                , re.MULTILINE
            )
            
            for match in project_schedule_pattern.finditer(section_part):
                project_name = match.group("Project_Name").strip()
                details = match.group("Details").strip()

                # Now check for 2022 start dates within these details.
                date_match = re.search(
                    r"(?:Begin\\sConstruction|Construction\\swas\\scompleted|Completed):\\s*"
                    r"(?P<Date_Info>\\b2022\\b(?:[-\\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\\s]\\d{2})?)",
                    details, re.IGNORECASE
                )
                
                if date_match:
                    disaster_projects_starting_2022.add(project_name)
        
        # Reset the flag if we encounter a new major section heading that is not 'Disaster Recovery Projects'
        if re.match(r'Capital Improvement Projects', section_part, re.IGNORECASE):
            in_disaster_section = False

# Also, separately check for disaster keywords like FEMA, CalOES, CalJPIA, or 'disaster' itself in the whole document
# for projects that might not be under a strict 'Disaster Recovery Projects' heading but are still disaster-related.
for doc in civic_docs_data:
    text = doc['text']
    
    # Regex to capture any potential project name and its surrounding context
    # This is a broad pattern to find any project with '2022' date and disaster keywords.
    broad_project_context_pattern = re.compile(
        r"(?P<Project_Name>[A-Z][A-Za-z0-9\\s&,-_\':/\\.\\(\\)]+?)\n" # Project Name
        r"(?P<Context>[\\s\\S]{0,500}?)"
        r"(?:Begin\\sConstruction|Construction\\swas\\scompleted|Completed):\\s*"
        r"(?P<Date_Info>\\b2022\\b(?:[-\\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\\s]\\d{2})?)"
        , re.IGNORECASE # Make the whole pattern case-insensitive for easier date matching
    )

    for match in broad_project_context_pattern.finditer(text):
        project_name = match.group("Project_Name").strip()
        context = match.group("Context").strip()
        date_info = match.group("Date_Info").strip()

        # Check if disaster keywords are in the project name or its context
        if re.search(r'FEMA|CalOES|CalJPIA|Disaster Recovery|Woolsey Fire|emergency|fire', project_name + " " + context, re.IGNORECASE):
            if "2022" in date_info: # Already ensured by DATE_2022_PATTERN but good to be explicit.
                disaster_projects_starting_2022.add(project_name)

# Convert the set of unique project names to a list
unique_disaster_projects_2022 = list(disaster_projects_starting_2022)

# Now, construct the SQL query to get funding for these projects
if unique_disaster_projects_2022:
    # Prepare project names for an SQL IN clause. Escape single quotes in names for SQL compatibility.
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
