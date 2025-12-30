code = """import pandas as pd
import json
import re

# Load the civic documents data
with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

disaster_projects_2022_extracted = []

for doc in civic_docs_data:
    text = doc['text']

    # This regex attempts to capture a project block by identifying a project name (capitalized line)
    # followed by its updates and schedule, which are often indicated by '(cid:xxx)' bullet points.
    # It's designed to be flexible with the content between project name and schedule.
    # We need to use raw strings for regex to handle backslashes correctly, and ensure proper Python string escaping.
    project_block_pattern = re.compile(
        r"^(?P<Project_Name>[A-Z][A-Za-z0-9\\s&,-_\':\\/.\\(\\)]+?)$\n" # Project Name line (starts with capital letter)
        r"(?P<Details>"
        r"(?:\\(cid:\\d+?\\)\\sUpdates:[^\\n]*\\n(?:\\(cid:\\d+?\\)[^\\n]*\\n)*?)?" # Optional Updates section
        r"(?:\\(cid:\\d+?\\)\\s(?:Project|Estimated)\\sSchedule:[^\\n]*\\n(?:\\(cid:\\d+?\\)[^\\n]*\\n)*?)"
        r")", # Required Schedule section
        re.MULTILINE
    )

    for match in project_block_pattern.finditer(text):
        project_name = match.group("Project_Name").strip()
        details = match.group("Details").strip()

        is_disaster = False
        # Check for disaster keywords in the project name or its details.
        # The keywords are case-insensitive.
        if re.search(r"FEMA|CalOES|CalJPIA|Disaster Recovery", project_name + " " + details, re.IGNORECASE):
            is_disaster = True
        
        if is_disaster:
            start_date_2022 = None
            # Search for a 2022 date associated with construction start or completion within the details.
            # The date pattern looks for "2022" followed by optional season/month and day/year info.
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
