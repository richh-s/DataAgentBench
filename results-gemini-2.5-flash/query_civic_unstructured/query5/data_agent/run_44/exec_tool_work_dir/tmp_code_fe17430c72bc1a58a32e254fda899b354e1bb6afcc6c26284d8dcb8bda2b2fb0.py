code = """import json
import re

def extract_project_info(text):
    projects = []
    # Find the start of "Disaster Recovery Projects" section
    disaster_section_start_match = re.search(r"Disaster Recovery Projects\n\n", text)

    if disaster_section_start_match:
        start_index = disaster_section_start_match.end()
        # Find the end of the "Disaster Recovery Projects" section
        # The section ends before another Capital Improvement Projects section or the end of the document
        end_section_match = re.search(r"\n\n(Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Capital Improvement Projects \(Design\))", text[start_index:])
        
        disaster_section_text = ""
        if end_section_match:
            disaster_section_text = text[start_index : start_index + end_section_match.start()]
        else: # If no other Capital Projects section follows, it's the rest of the document
            disaster_section_text = text[start_index:]

        # Regex to find project name and its schedule within the disaster section
        # Project name is in group 1, year is in group 2.
        project_pattern = re.compile(r"([A-Z][a-zA-Z0-9_ -]+ Project)(?:.*?)(?:Project Schedule:|Estimated Schedule:)(?:.*?)(?:Begin Construction|Advertise|Complete Design|Final Design):\s*(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)?\s*(2022)", re.DOTALL | re.IGNORECASE)

        for match in project_pattern.finditer(disaster_section_text):
            project_name = match.group(1).strip()
            start_year = match.group(2) # This will be '2022'

            projects.append({
                "Project_Name": project_name,
                "type": "disaster",
                "st": start_year
            })
    return projects

file_path = locals()['var_function-call-13890045868796138189']
with open(file_path, "r") as f:
    data = json.load(f)

all_projects = []
for doc in data["query_db_response"]["results"]:
    all_projects.extend(extract_project_info(doc["text"]))

disaster_projects_2022 = list(set([p["Project_Name"] for p in all_projects]))

print("__RESULT__:")
print(json.dumps(disaster_projects_2022))"""

env_args = {'var_function-call-13890045868796138189': 'file_storage/function-call-13890045868796138189.json'}

exec(code, env_args)
