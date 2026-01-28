code = """import pandas as pd
import json
import re

with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

extracted_projects_info = []

# Regex to find lines that are likely project names. These are lines that
# start with an alphanumeric character and are not bullet points (cid:xxx).
# It should end at the end of the line.
project_name_candidate_pattern = re.compile(r"^[A-Za-z0-9\s&,-_\':\/.\(\)]+?$", re.MULTILINE)

for doc in civic_docs_data:
    text = doc['text']

    # Iterate through each potential project name line
    for name_match in re.finditer(project_name_candidate_pattern, text):
        project_name = name_match.group(0).strip()
        
        # Define a search window for schedule details after the project name
        search_start = name_match.end()
        search_end = min(search_start + 500, len(text)) # Look up to 500 characters after the project name
        search_window = text[search_start:search_end]

        is_disaster = False
        # Check for disaster keywords in the project name or the search window
        if re.search(r"FEMA|CalOES|CalJPIA|Disaster Recovery", project_name + " " + search_window, re.IGNORECASE):
            is_disaster = True
        
        start_date = None
        # Extract start date containing "2022" from the search_window
        # Need to escape backslashes correctly for regex in Python string literal
        start_date_match = re.search(
            r"(?:Begin\sConstruction|Advertise|Construction\swas\scompleted|Complete\sConstruction):?\s*"
            r"(?P<Date>\b(?:2022|2023|2024|Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)\b(?:[-\s]\d{2})?(?:[-\s]\d{4})?(?:[\s]\w+)?(?:-\d{2})?(?:[\s]\d{4})?(?:[\s]\d{2})?)",
            search_window
        )
        
        if start_date_match:
            date_str = start_date_match.group("Date")
            if "2022" in date_str:
                start_date = date_str

        if is_disaster and start_date:
            extracted_projects_info.append({"Project_Name": project_name, "Start_Date": start_date})

# Remove duplicates based on Project_Name
unique_disaster_projects_2022 = pd.DataFrame(extracted_projects_info).drop_duplicates(subset=['Project_Name']).to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(unique_disaster_projects_2022))"""

env_args = {'var_function-call-4922019997739677456': ['civic_docs'], 'var_function-call-788512929960335419': 'file_storage/function-call-788512929960335419.json', 'var_function-call-9254905820928177274': [], 'var_function-call-6587616414360749789': []}

exec(code, env_args)
