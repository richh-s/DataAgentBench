code = """import pandas as pd
import json
import re

with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

disaster_projects_2022_final = []

for doc in civic_docs_data:
    text = doc['text']

    # Find all possible project blocks (Project Name followed by indented details)
    # The pattern aims to capture a project name line and then all subsequent indented bullet points
    # until a new unindented line (which could be a new project name or a section heading).
    # This pattern needs to be carefully crafted to not be too greedy or too restrictive.
    project_block_pattern = re.compile(
        r"^(?P<Project_Name>[A-Z0-9][A-Za-z0-9\\s&,-_\':\\/.\\(\\)]+?)$\\n"  # Project name line
        r"(?P<Details>(?:\\(cid:\\d+?\\)[^\\n]*\\n)*?)" # Captures all (cid:xxx) lines that follow
        r"(?=(?:^[A-Z0-9]|^Agenda Item|Page \\d+ of \\d+)|$)", # Positive lookahead for next project/section or end of text
        re.MULTILINE
    )

    for block_match in project_block_pattern.finditer(text):
        project_name = block_match.group("Project_Name").strip()
        details = block_match.group("Details")

        is_disaster_project = False
        # Check for disaster keywords in the project name or its details
        if re.search(r"FEMA|CalOES|CalJPIA|Disaster Recovery Projects|Disaster Recovery", project_name + " " + details, re.IGNORECASE):
            is_disaster_project = True

        if is_disaster_project:
            start_date_2022 = None
            # Search for a 2022 date associated with construction start or completion within the details
            date_match = re.search(
                r"(?:Begin\\sConstruction|Construction\\swas\\scompleted|Completed):\\s*"
                r"(?P<Date_Info>\\b2022\\b(?:[-\\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\\s]\\d{2})?)",
                details, re.IGNORECASE
            )

            if date_match:
                start_date_2022 = date_match.group("Date_Info").strip()
                disaster_projects_2022_final.append({"Project_Name": project_name, "Start_Date": start_date_2022})

# Remove duplicates based on Project_Name and Start_Date
final_projects_df = pd.DataFrame(disaster_projects_2022_final).drop_duplicates(subset=["Project_Name", "Start_Date"])
final_projects = final_projects_df.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(final_projects))"""

env_args = {'var_function-call-4922019997739677456': ['civic_docs'], 'var_function-call-788512929960335419': 'file_storage/function-call-788512929960335419.json', 'var_function-call-9254905820928177274': [], 'var_function-call-6587616414360749789': [], 'var_function-call-3446571632783907127': []}

exec(code, env_args)
