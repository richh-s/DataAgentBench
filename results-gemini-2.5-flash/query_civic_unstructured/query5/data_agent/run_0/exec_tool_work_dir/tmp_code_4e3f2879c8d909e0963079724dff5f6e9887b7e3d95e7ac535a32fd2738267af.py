code = """import pandas as pd
import json
import re

# Read the full result from the file
with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

all_extracted_projects = []

# Redefine project_and_schedule_pattern using double quotes and full escaping for Python string literal.
# Any double quotes inside the regex must be escaped. (There are none currently.)
project_and_schedule_pattern = "(?P<Project_Name>[A-Za-z0-9\\s&,-_':\\/.()]+?)\\n(?:\\(cid:190\\)\\sUpdates:[^\\n]*\\n)*?(?:\\(cid:190\\)\\sProject Description:[^\\n]*\\n)*?\\(cid:190\\)\\s(?:Project|Estimated)\\sSchedule:\\n(?:(?:\\(cid:131\\)[^\\n]*\\n)*?)(?:\\(cid:131\\)\\s(?:Begin\\sConstruction|Advertise|Complete\\sDesign|Final\\sDesign|Construction\\swas\\scompleted|Complete\\sConstruction|Project\\sis\\sdelayed\\sdue\\sto\\sthe\\sCultural\\sResource\\sreview|City\\swill\\sbe\\sissuing\\sa\\sRFQ/P\\sfor\\sdesign\\sservices\\sin\\sthe\\ssummer\\sof\\s2023):\\s*)(?P<Start_Date>\\b(?:2022|2023|2024|Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)\\b(?:[-\\s]\\d{2})?(?:[-\\s]\\d{4})?(?:\\s\\w+)?(?:-\\d{2})?(?:\\s\\d{4})?(?:\\s\\d{2})?)?"


for doc in civic_docs_data:
    text = doc['text']
    
    # Check for general disaster keywords in the document text
    doc_is_disaster_related = bool(re.search(r"Disaster Recovery Projects|FEMA|CalOES|CalJPIA", text, re.IGNORECASE))

    for match in re.finditer(project_and_schedule_pattern, text, re.MULTILINE):
        project_name = match.group("Project_Name").strip()
        start_date_str = match.group("Start_Date") if match.group("Start_Date") else ""
        
        is_project_disaster_related = False
        
        # Check for disaster keywords in the immediate context of the project
        # Define a context window around the project match
        context_start = max(0, match.start() - 200) # Look back 200 characters
        context_end = min(len(text), match.end() + 200) # Look forward 200 characters
        project_specific_context = text[context_start:context_end]

        if re.search(r"FEMA|CalOES|CalJPIA|Disaster Recovery", project_specific_context, re.IGNORECASE):
            is_project_disaster_related = True
        
        if (is_project_disaster_related or doc_is_disaster_related) and "2022" in start_date_str:
            all_extracted_projects.append({"Project_Name": project_name, "Start_Date": start_date_str})

# Remove duplicates based on Project_Name
unique_disaster_projects_2022 = pd.DataFrame(all_extracted_projects).drop_duplicates(subset=["Project_Name"]).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(unique_disaster_projects_2022))"""

env_args = {'var_function-call-4922019997739677456': ['civic_docs'], 'var_function-call-788512929960335419': 'file_storage/function-call-788512929960335419.json'}

exec(code, env_args)
