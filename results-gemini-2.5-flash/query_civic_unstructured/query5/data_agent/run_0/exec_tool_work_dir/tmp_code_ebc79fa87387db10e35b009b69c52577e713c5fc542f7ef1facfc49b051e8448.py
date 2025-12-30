code = """import pandas as pd
import json
import re

# Load the civic documents data
with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

disaster_projects_2022_extracted = []

for doc in civic_docs_data:
    text = doc['text']

    # Regex to find project names and their schedules in the text.
    # It looks for a project name (captured as Project_Name), followed by
    # optional updates and then a schedule, where a date is extracted.
    # The 'Project_Name' is a capitalized line.
    # 'Details' captures the section containing Updates and Schedule.
    # All backslashes are explicitly escaped for the regex pattern within a Python string literal.
    project_schedule_pattern = re.compile(
        "^(?P<Project_Name>[A-Z][A-Za-z0-9\\s&,-_\'\\/.\\(\\)]+?)\\s*\\n" # Project Name line (e.g., "2022 Morning View Resurfacing & Storm Drain Improvements")
        "(?P<Details>" # Start capturing details
        "(?:\\(cid:\\d+?\\)\\sUpdates:[^\\n]*\\n(?:\\(cid:\\d+?\\)[^\\n]*\\n)*?)?" # Optional Updates section (e.g., "(cid:190) Updates:")
        "(?:\\(cid:\\d+?\\)\\s(?:Project|Estimated)\\sSchedule:[^\\n]*\\n(?:\\(cid:\\d+?\\)[^\\n]*\\n)*?)" # Required Schedule section (e.g., "(cid:190) Project Schedule:")
        ")", # End capturing details
        re.MULTILINE
    )

    for match in project_schedule_pattern.finditer(text):
        project_name = match.group("Project_Name").strip()
        details = match.group("Details").strip() # Extract details from the matched block

        is_disaster = False
        # Check for disaster keywords in the project name or its details.
        # The keywords are case-insensitive.
        if re.search(r"FEMA|CalOES|CalJPIA|Disaster Recovery", project_name + " " + details, re.IGNORECASE):
            is_disaster = True
        
        if is_disaster:
            start_date_2022 = None
            # Search for a 2022 date associated with construction start or completion within the details.
            # This regex looks for phrases like "Begin Construction:", "Construction was completed:", "Completed:"
            # followed by a date string that contains "2022".
            date_match = re.search(
                r"(?:Begin\\sConstruction|Construction\\swas\\scompleted|Completed):\\s*"
                r"(?P<Date_Info>\\b2022\\b(?:[-\\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\\s]\\d{2})?)",
                details, re.IGNORECASE
            )
            
            if date_match:
                start_date_2022 = date_match.group("Date_Info").strip()
                disaster_projects_2022_extracted.append({"Project_Name": project_name, "Start_Date": start_date_2022})

# Remove duplicates based on Project_Name and Start_Date for cleanliness.
final_projects_df = pd.DataFrame(disaster_projects_2022_extracted).drop_duplicates(subset=["Project_Name", "Start_Date"])
final_projects = final_projects_df.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(final_projects))"""

env_args = {'var_function-call-4922019997739677456': ['civic_docs'], 'var_function-call-788512929960335419': 'file_storage/function-call-788512929960335419.json', 'var_function-call-9254905820928177274': [], 'var_function-call-6587616414360749789': [], 'var_function-call-3446571632783907127': [], 'var_function-call-2261813058681952031': []}

exec(code, env_args)
