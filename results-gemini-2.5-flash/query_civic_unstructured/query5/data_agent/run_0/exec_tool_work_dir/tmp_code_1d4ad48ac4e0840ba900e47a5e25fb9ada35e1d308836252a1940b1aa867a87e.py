code = """import pandas as pd
import json
import re

# Load the civic documents data
with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

disaster_projects_starting_2022_names = set()

for doc in civic_docs_data:
    text = doc['text']

    # Split the document into logical sections based on major headings.
    # This helps to scope the search for disaster-related projects.
    sections = re.split(r'(Capital Improvement Projects \(Design\)|Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects Status Report)', text)
    
    current_section_type = ""
    
    # Iterate through the split sections. Even-indexed elements are text, odd-indexed are delimiters.
    for i in range(len(sections)):
        section_content = sections[i]
        if i % 2 == 0: # This is a content part
            # If we are in a 'Disaster Recovery Projects' section or a similar one
            if "Disaster Recovery Projects" in current_section_type or re.search(r"FEMA|CalOES|CalJPIA", section_content, re.IGNORECASE):
                # Regex to find project names and their schedule within this section.
                # Project names are typically followed by (cid:190) Updates: or (cid:190) Project Schedule:
                # This regex captures the Project_Name and the block of text containing details and schedule.
                project_detail_pattern = re.compile(
                    r"^(?P<Project_Name>[A-Z][A-Za-z0-9\\s&,-_\':\\/.\\(\\)]+?)$\\n"  # Project Name line
                    r"(?P<Details>"
                    r"(?:\\(cid:\\d+?\\)\\sUpdates:[^\\n]*\\n(?:\\(cid:\\d+?\\)[^\\n]*\\n)*?)?" # Optional Updates section
                    r"(?:\\(cid:\\d+?\\)\\s(?:Project|Estimated)\\sSchedule:[^\\n]*\\n(?:\\(cid:\\d+?\\)[^\\n]*\\n)*?)"
                    r")", # Required Schedule section
                    re.MULTILINE
                )

                for match in project_detail_pattern.finditer(section_content):
                    project_name = match.group("Project_Name").strip()
                    details = match.group("Details").strip()

                    # Double-check for disaster keywords within this specific project's block.
                    if re.search(r"FEMA|CalOES|CalJPIA|Disaster Recovery", project_name + " " + details, re.IGNORECASE):
                        # Now check for '2022' in the schedule details, specifically for start/completion.
                        date_match = re.search(
                            r"(?:Begin\\sConstruction|Construction\\swas\\scompleted|Completed):\\s*"
                            r"(?P<Date_Info>\\b2022\\b(?:[-\\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\\s]\\d{2})?)",
                            details, re.IGNORECASE
                        )
                        if date_match:
                            disaster_projects_starting_2022_names.add(project_name)
        else: # This is a delimiter part, update the current_section_type
            current_section_type = section_content

# Convert the set to a list for JSON serialization
final_project_names = list(disaster_projects_starting_2022_names)

print("__RESULT__:")
print(json.dumps(final_project_names))"""

env_args = {'var_function-call-4922019997739677456': ['civic_docs'], 'var_function-call-788512929960335419': 'file_storage/function-call-788512929960335419.json', 'var_function-call-9254905820928177274': [], 'var_function-call-6587616414360749789': [], 'var_function-call-3446571632783907127': [], 'var_function-call-2261813058681952031': [], 'var_function-call-8822505650285935510': []}

exec(code, env_args)
