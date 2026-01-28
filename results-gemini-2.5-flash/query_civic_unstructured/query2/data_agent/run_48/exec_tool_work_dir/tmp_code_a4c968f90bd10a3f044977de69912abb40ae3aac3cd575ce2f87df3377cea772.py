code = """import json
import re

def extract_project_info(text):
    projects = []
    # Split the document into sections based on project headings
    project_sections = re.split(r"\n\n(Capital Improvement Projects \(Design\)|Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects)\\n\\n", text)

    for i in range(1, len(project_sections), 2):
        section_title = project_sections[i].strip()
        section_content = project_sections[i+1]

        # Regex to find project names and their associated details
        # This regex looks for a project name followed by "(cid:190) Updates:", "(cid:190) Project Description:", or "(cid:190) Estimated Schedule:"
        # and captures the project name and the subsequent details until the next project or section end.
        # It also looks for "Completed Construction: <date>" or "Construction was completed <date>" for end dates and status.

        # First try to match sections with explicit "Updates" or "Project Description"
        matches = re.findall(r"(.*?)\n\n(?:\(cid:190\) Updates:|\(cid:190\) Project Description:|\(cid:190\) Estimated Schedule:)", section_content, re.DOTALL)

        # If no clear matches using the above, try to find project names and then extract info until next project or section end
        if not matches:
            matches = re.findall(r"([A-Za-z0-9][^\n]*?)\n\((?:cid:190|cid:131)\)", section_content, re.DOTALL)
            # This is a fallback, might need further refinement
            if not matches:
                continue

        # Refine extracting project info
        project_name = ""
        status = ""
        et = ""
        topic = ""

        # Simplified approach to extract project info from each identified section
        # This will need to be made more robust if the current regex is not sufficient

        # For each potential project match, try to extract details more precisely
        # Let's focus on "completed" status and "2022" for "et" for now.
        project_matches = re.finditer(r"([A-Za-z0-9][^\n]*?)(?:\n\n(?:\(cid:190\) Updates:|\(cid:190\) Project Description:|\(cid:190\) Estimated Schedule:)|$)", section_content, re.DOTALL)

        last_end = 0
        for match in project_matches:
            if match.start() > last_end:
                # This indicates text before the next explicit project description, could be a project name
                possible_project_name = section_content[last_end:match.start()].strip()
                if possible_project_name and not possible_project_name.startswith("(cid:"): # Filter out non-names
                    project_name = possible_project_name.split("\n")[0].strip()
                    details = section_content[last_end:match.start()]
                    # Extract status and et from details for this potential project
                    status_match = re.search(r"Construction was completed[, ]*([A-Za-z]+\s+\d{4})|Complete Construction: ([A-Za-z]+\s+\d{4})|Construction was completed, ([A-Za-z]+\s+\d{4})", details)
                    if status_match:
                        status = "completed"
                        et = status_match.group(1) or status_match.group(2) or status_match.group(3)
                        # Check for "park" topic based on project name or surrounding text
                        if "park" in project_name.lower():
                            topic = "park"
                        # If it's a capital project and has "park" in the name, it's a park project
                        if "Capital Improvement Projects" in section_title and "park" in project_name.lower():
                             topic = "park"

                        projects.append({"Project_Name": project_name, "topic": topic, "status": status, "et": et, "section_title": section_title})

            # Now process the explicitly matched project
            project_name_full = match.group(1).strip()
            project_name = project_name_full.split("\n")[0].strip()
            details = match.group(0).strip()

            status = ""
            et = ""
            topic = ""

            # Check for "completed" status
            if "completed" in details.lower():
                status = "completed"
                # Extract end date if status is completed and contains 2022
                et_match = re.search(r"Complete Construction: ([A-Za-z]+ \d{4})|Construction was completed[, ]*([A-Za-z]+ \d{4})", details)
                if et_match:
                    et = et_match.group(1) or et_match.group(2)

            # Check for "park" topic in the project name
            if "park" in project_name.lower():
                topic = "park"
            # Also check if it's a capital project and contains "park" in the name.
            if "Capital Improvement Projects" in section_title and "park" in project_name.lower():
                 topic = "park"

            if project_name and status == "completed" and et and "2022" in et:
                projects.append({"Project_Name": project_name, "topic": topic, "status": status, "et": et, "section_title": section_title})

            last_end = match.end()

    return projects


file_path = locals()['var_function-call-8555713923215723093']
with open(file_path, 'r') as f:
    civic_docs_data = json.load(f)

all_projects_info = []
for doc in civic_docs_data:
    extracted_projects = extract_project_info(doc['text'])
    all_projects_info.extend(extracted_projects)


# Filter projects based on the query: "park-related", "completed", "2022"
park_projects_2022 = [
    p for p in all_projects_info
    if p['topic'] == 'park' and p['status'] == 'completed' and '2022' in p['et']
]

# Extract unique project names to query funding database
park_project_names_2022 = list(set([p['Project_Name'] for p in park_projects_2022]))

print("__RESULT__:")
print(json.dumps(park_project_names_2022))"""

env_args = {'var_function-call-8555713923215723093': 'file_storage/function-call-8555713923215723093.json'}

exec(code, env_args)
