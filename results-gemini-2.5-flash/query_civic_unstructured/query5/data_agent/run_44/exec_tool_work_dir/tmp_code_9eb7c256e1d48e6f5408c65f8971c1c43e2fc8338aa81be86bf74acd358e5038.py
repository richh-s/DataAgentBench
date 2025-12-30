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

        # Now, within the disaster_section_text, find individual projects and their 2022 start dates
        # Project name pattern: Any line starting with a capital letter and ending with " Project"
        # Date pattern: Lines containing "Project Schedule:" or "Estimated Schedule:" followed by a line with "2022"
        
        # Split the section into potential project blocks based on project name pattern
        project_blocks = re.split(r"([A-Z][a-zA-Z0-9_ -]+ Project)", disaster_section_text)
        
        # Iterate through the blocks to find project names and their 2022 start dates
        # The split might result in empty strings or non-project text, so we need to be careful
        for i in range(1, len(project_blocks), 2): # Start from 1, step by 2 to get project name and its details
            project_name = project_blocks[i].strip()
            details_block = project_blocks[i+1] # This block contains details like schedule

            # Check if '2022' is present in the schedule details within this block
            if re.search(r"(?:Project Schedule:|Estimated Schedule:).*?(?:Begin Construction|Advertise|Complete Design|Final Design):.*?2022", details_block, re.DOTALL | re.IGNORECASE):
                projects.append({
                    "Project_Name": project_name,
                    "type": "disaster",
                    "st": "2022"
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
