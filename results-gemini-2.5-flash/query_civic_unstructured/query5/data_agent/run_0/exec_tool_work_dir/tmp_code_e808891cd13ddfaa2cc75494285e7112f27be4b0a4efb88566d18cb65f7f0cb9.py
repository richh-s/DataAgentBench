code = """import pandas as pd
import json
import re

# Load the civic documents data
with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

disaster_projects_starting_2022_names = []

for doc in civic_docs_data:
    text = doc['text']

    # Split the document into lines to process them individually and gather context.
    lines = text.split('\n')
    current_project_block = []
    # This flag helps to collect lines belonging to the same project after a project name is identified.
    is_in_project_block = False

    # Iterate through lines to identify project names and their associated details.
    for line_num, line in enumerate(lines):
        stripped_line = line.strip()

        # Heuristic to identify a potential project name:
        # - Starts with a capital letter or digit.
        # - Is not a bullet point (doesn't start with '(cid:').
        # - Is not a common document header/footer ('Agenda Item', 'Page').
        # - Seems like a title (not too short, or clearly just a number).
        is_potential_project_name = bool(re.match(r"^[A-Z0-9][A-Za-z0-9\\s&,-_\':\\/.\\(\\)]+?$", stripped_line)) and \
                                  not stripped_line.startswith("(cid:") and \
                                  not stripped_line.startswith("Agenda Item") and \
                                  not stripped_line.startswith("Page ") and \
                                  len(stripped_line) > 5 # Simple length check to filter out very short lines
        
        if is_potential_project_name:
            if is_in_project_block: # If we were already in a project block, process the previous one
                # Process the collected block
                full_project_text = "\n".join(current_project_block).strip()
                
                # Extract project name from the first line of the block
                extracted_project_name = current_project_block[0].strip()

                is_disaster = False
                if re.search(r"FEMA|CalOES|CalJPIA|Disaster Recovery", full_project_text, re.IGNORECASE):
                    is_disaster = True
                
                if is_disaster:
                    start_date_2022 = None
                    date_match = re.search(
                        r"(?:Begin\\sConstruction|Construction\\swas\\scompleted|Completed):\\s*"
                        r"(?P<Date_Info>\\b2022\\b(?:[-\\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\\s]\\d{2})?)",
                        full_project_text, re.IGNORECASE
                    )
                    if date_match:
                        start_date_2022 = date_match.group("Date_Info").strip()
                        disaster_projects_starting_2022_names.append(extracted_project_name)
            
            # Start a new project block
            current_project_block = [stripped_line]
            is_in_project_block = True
        elif is_in_project_block: # If still within a project block, add the line to it
            current_project_block.append(stripped_line)
    
    # After the loop, process the last project block if any
    if is_in_project_block and current_project_block:
        full_project_text = "\n".join(current_project_block).strip()
        extracted_project_name = current_project_block[0].strip()

        is_disaster = False
        if re.search(r"FEMA|CalOES|CalJPIA|Disaster Recovery", full_project_text, re.IGNORECASE):
            is_disaster = True
        
        if is_disaster:
            start_date_2022 = None
            date_match = re.search(
                r"(?:Begin\\sConstruction|Construction\\swas\\scompleted|Completed):\\s*"
                r"(?P<Date_Info>\\b2022\\b(?:[-\\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\\s]\\d{2})?)",
                full_project_text, re.IGNORECASE
            )
            if date_match:
                start_date_2022 = date_match.group("Date_Info").strip()
                disaster_projects_starting_2022_names.append(extracted_project_name)

# Remove duplicates from the final list of project names.
unique_disaster_projects_2022 = list(set(disaster_projects_starting_2022_names))

print("__RESULT__:")
print(json.dumps(unique_disaster_projects_2022))"""

env_args = {'var_function-call-4922019997739677456': ['civic_docs'], 'var_function-call-788512929960335419': 'file_storage/function-call-788512929960335419.json', 'var_function-call-9254905820928177274': [], 'var_function-call-6587616414360749789': [], 'var_function-call-3446571632783907127': [], 'var_function-call-2261813058681952031': [], 'var_function-call-8822505650285935510': []}

exec(code, env_args)
