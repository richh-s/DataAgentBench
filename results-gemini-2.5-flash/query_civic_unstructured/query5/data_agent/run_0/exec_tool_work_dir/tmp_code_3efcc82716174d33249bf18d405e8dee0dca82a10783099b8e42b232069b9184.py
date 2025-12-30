code = """import pandas as pd
import json
import re

# Load the civic documents data
with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

disaster_projects_starting_2022 = []

for doc in civic_docs_data:
    text = doc['text']

    # Iterate through each line to identify potential project names and their subsequent details.
    lines = text.split('\n')
    current_project_name = None
    current_project_details = []

    for line in lines:
        stripped_line = line.strip()
        
        # Heuristic to identify a new project name: capitalized, not a bullet, not a short header.
        # This assumes project names are typically on their own line and capitalized.
        # Regex: starts with a capital letter, contains alphanumeric, spaces, and specific punctuation.
        # Excludes lines starting with (cid: which are bullet points.
        if re.match(r"^[A-Z][A-Za-z0-9\s&,-_\':\/.()]+?$", stripped_line) and not stripped_line.startswith("(cid:"):
            if current_project_name:
                # Process the previous project's details before starting a new one
                full_details = " ".join(current_project_details)
                
                is_disaster = False
                # Check for disaster keywords in the project name or its collected details
                if re.search(r"FEMA|CalOES|CalJPIA|Disaster Recovery Projects|Disaster Recovery", current_project_name + " " + full_details, re.IGNORECASE):
                    is_disaster = True
                
                if is_disaster:
                    # Look for a 2022 start date within the details.
                    # This regex specifically looks for "Begin Construction" or similar phrases
                    # followed by a date containing "2022".
                    start_date_match = re.search(
                        r"(?:Begin\sConstruction|Project\sschedule:\sBegin\sconstruction):\s*"
                        r"(?P<Start_Date>\b2022\b(?:[-\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\s]\d{2})?)",
                        full_details, re.IGNORECASE
                    )
                    if start_date_match:
                        disaster_projects_starting_2022.append(current_project_name)

            # Start a new project: reset current_project_name and clear details
            current_project_name = stripped_line
            current_project_details = []
        elif current_project_name:
            # If it's not a new project name, add the line to the current project's details
            current_project_details.append(stripped_line)
    
    # After the loop, process the last project in the document (if any)
    if current_project_name:
        full_details = " ".join(current_project_details)
        
        is_disaster = False
        if re.search(r"FEMA|CalOES|CalJPIA|Disaster Recovery Projects|Disaster Recovery", current_project_name + " " + full_details, re.IGNORECASE):
            is_disaster = True
        
        if is_disaster:
            start_date_match = re.search(
                r"(?:Begin\sConstruction|Project\sschedule:\sBegin\sconstruction):\s*"
                r"(?P<Start_Date>\b2022\b(?:[-\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\s]\d{2})?)",
                full_details, re.IGNORECASE
            )
            if start_date_match:
                disaster_projects_starting_2022.append(current_project_name)

# Remove duplicate project names from the final list
unique_disaster_projects = list(set(disaster_projects_starting_2022))

print("__RESULT__:")
print(json.dumps(unique_disaster_projects))"""

env_args = {'var_function-call-4922019997739677456': ['civic_docs'], 'var_function-call-788512929960335419': 'file_storage/function-call-788512929960335419.json', 'var_function-call-9254905820928177274': [], 'var_function-call-6587616414360749789': [], 'var_function-call-3446571632783907127': [], 'var_function-call-2261813058681952031': [], 'var_function-call-8822505650285935510': []}

exec(code, env_args)
