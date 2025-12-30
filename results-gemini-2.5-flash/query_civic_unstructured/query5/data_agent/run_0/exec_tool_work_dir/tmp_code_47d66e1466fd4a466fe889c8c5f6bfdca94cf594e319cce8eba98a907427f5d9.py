code = """import pandas as pd
import json
import re

with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

disaster_projects_2022_extracted = []

for doc in civic_docs_data:
    text = doc['text']

    # Regex to capture a project block: Project Name followed by its details (updates, schedule, etc.)
    # It tries to find a capitalized line (potential project name) and then captures everything
    # until another similar capitalized line or a recognized section header, or end of text.
    project_block_pattern = re.compile(
        r"^(?P<Project_Name>[A-Z][A-Za-z0-9\s&,-_':\/.()]+?)$\n"  # Project Name (starts with capital, ends line)
        r"(?P<Details>(?:(?!^[A-Z][A-Za-z0-9\s&,-_':\/.()]+?$|^Agenda Item|^Page \d+ of \d+)[\s\S])*?)"
        , re.MULTILINE
    )

    for match in project_block_pattern.finditer(text):
        project_name = match.group("Project_Name").strip()
        details = match.group("Details").strip()

        is_disaster = False
        # Check for disaster keywords in the project name or its details
        if re.search(r"FEMA|CalOES|CalJPIA|Disaster Recovery Projects|Disaster Recovery", project_name + " " + details, re.IGNORECASE):
            is_disaster = True
        
        if is_disaster:
            start_date_2022 = None
            # Search for a 2022 date associated with construction start/completion within the details
            # This regex looks for phrases like "Begin Construction:", "Construction was completed:", "Completed:"
            # followed by a date string that contains "2022".
            date_match = re.search(
                r"(?:Begin\sConstruction|Construction\swas\scompleted|Completed):\s*"
                r"(?P<Date_Info>\b2022\b(?:[-\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\s]\d{2})?)",
                details, re.IGNORECASE
            )
            
            if date_match:
                start_date_2022 = date_match.group("Date_Info").strip()
                disaster_projects_2022_extracted.append({"Project_Name": project_name, "Start_Date": start_date_2022})

# Remove duplicates based on Project_Name
final_projects_df = pd.DataFrame(disaster_projects_2022_extracted).drop_duplicates(subset=["Project_Name"])
final_projects = final_projects_df.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(final_projects))"""

env_args = {'var_function-call-4922019997739677456': ['civic_docs'], 'var_function-call-788512929960335419': 'file_storage/function-call-788512929960335419.json', 'var_function-call-9254905820928177274': [], 'var_function-call-6587616414360749789': [], 'var_function-call-3446571632783907127': [], 'var_function-call-2261813058681952031': []}

exec(code, env_args)
