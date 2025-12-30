code = """import pandas as pd
import json
import re

with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

final_disaster_projects_2022 = []

for doc in civic_docs_data:
    text = doc['text']

    # This regex attempts to capture a project block by looking for a line that resembles a project name,
    # followed by an optional 'Updates' section, and then a 'Schedule' section. This structure seems common in the documents.
    project_schedule_block_pattern = re.compile(
        r"^(?P<Project_Name>[A-Z][A-Za-z0-9\s&,-_\':\/.()]+?)$\n" # Project Name, usually a capitalized line
        r"(?P<Details>"
        r"(?:\(cid:190\)\sUpdates:[^\n]*\n(?:\(cid:131\)[^\n]*\n)*?)?" # Optional Updates section and its bullet points
        r"(?:\(cid:190\)\s(?:Project|Estimated)\sSchedule:[^\n]*\n(?:\(cid:131\)[^\n]*\n)*?))", # Required Schedule section and its bullet points
        re.MULTILINE
    )

    for match in project_schedule_block_pattern.finditer(text):
        project_name = match.group("Project_Name").strip()
        details = match.group("Details").strip()

        is_disaster = False
        # Check for disaster keywords within the extracted project name and its details
        if re.search(r"FEMA|CalOES|CalJPIA|Disaster Recovery", project_name + " " + details, re.IGNORECASE):
            is_disaster = True
        
        if is_disaster:
            # Search for a 2022 date associated with 'Begin Construction', 'Construction was completed', or 'Completed' within the details
            start_date_2022 = None
            date_match = re.search(
                r"(?:Begin\sConstruction|Construction\swas\scompleted|Completed):\s*"
                r"(?P<Date_Info>\b2022\b(?:[-\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\s]\d{2})?)",
                details, re.IGNORECASE
            )
            
            if date_match:
                start_date_2022 = date_match.group("Date_Info").strip()
                final_disaster_projects_2022.append({"Project_Name": project_name, "Start_Date": start_date_2022})

# Remove duplicate projects based on their name and start date
final_projects_df = pd.DataFrame(final_disaster_projects_2022).drop_duplicates(subset=["Project_Name", "Start_Date"])
final_projects = final_projects_df.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(final_projects))"""

env_args = {'var_function-call-4922019997739677456': ['civic_docs'], 'var_function-call-788512929960335419': 'file_storage/function-call-788512929960335419.json', 'var_function-call-9254905820928177274': [], 'var_function-call-6587616414360749789': [], 'var_function-call-3446571632783907127': [], 'var_function-call-2261813058681952031': []}

exec(code, env_args)
