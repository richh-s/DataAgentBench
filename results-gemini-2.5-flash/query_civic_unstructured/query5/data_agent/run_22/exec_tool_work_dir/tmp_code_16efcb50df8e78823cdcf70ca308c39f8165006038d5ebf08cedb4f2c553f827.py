code = """import json
import re

def extract_project_info(text):
    projects = []
    # Split the document into sections based on project titles or common headers
    # This is a heuristic approach, as the documents are unstructured.
    project_sections = re.split(r'\n\n(Capital Improvement Projects \(Design\)|Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|Project Schedule:|Estimated Schedule:|Malibu Bluffs Park South Walkway Repairs|PCH at Trancas Canyon Road Right Turn Lane|Permanent Skate Park|Trancas Canyon Park Upper and Lower Slopes Repair|Civic Center Water Treatment Facility Phase 2|Storm Drain Master Plan|Latigo Canyon Road Retaining Wall Repair Project|Clover Heights Storm Drainage Improvements|Westward Beach Road Drainage Improvements Project|Westward Beach Road Repair Project|PCH Median Improvements Project|2022 Morning View Resurfacing & Storm Drain Improvements|Outdoor Warning Signs|Trancas Canyon Park Playground|Malibu Canyon Road Traffic Study|Malibu Road Slope Repairs|Encinal Canyon Road Repairs|PCH Signal Synchronization System Improvements Project|Storm Drain Trash Screens Phase Two|Bluffs Park Shade Structure|Marie Canyon Green Streets|Broad Beach Road Water Quality Repair|Point Dume Walkway Repairs|PCH Median Improvements at Paradise Cove and Zuma Beach|PCH Crosswalk Improvements at Big Rock Drive and 20326 PCH|Kanan Dume Biofilter|City Traffic Signals Backup Power)\n\n', text)

    current_type = None
    for i, section in enumerate(project_sections):
        if "Capital Improvement Projects (Design)" in section:
            current_type = "capital"
            continue
        elif "Capital Improvement Projects (Construction)" in section:
            current_type = "capital"
            continue
        elif "Capital Improvement Projects (Not Started)" in section:
            current_type = "capital"
            continue
        elif "Disaster Recovery Projects" in section:
            current_type = "disaster"
            continue

        # Look for project names and their details within each section
        project_name_match = re.search(r'\n\n(.*?)\n\n\(cid:190\) Updates:', section, re.DOTALL)
        if project_name_match:
            project_name = project_name_match.group(1).strip()
            project_name = project_name.split('\n')[-1].strip() # Take the last line as project name
            # print(f"Processing project: {project_name}")

            topic_match = re.search(r'topic: (.*?)\n', section)
            topic = topic_match.group(1).strip() if topic_match else ""

            status_match = re.search(r'status: (.*?)\n', section)
            status = status_match.group(1).strip() if status_match else ""

            start_date_match = re.search(r'(Begin Construction|Advertise|Start Date):\s*(.*?)(?:\n|$)', section)
            start_date = start_date_match.group(2).strip() if start_date_match else ""

            end_date_match = re.search(r'(Complete Construction|End Date):\s*(.*?)(?:\n|$)', section)
            end_date = end_date_match.group(2).strip() if end_date_match else ""

            if current_type and project_name:
                projects.append({
                    "Project_Name": project_name,
                    "type": current_type,
                    "topic": topic,
                    "status": status,
                    "st": start_date,
                    "et": end_date
                })
        # Handle cases where "Project Schedule:" or "Estimated Schedule:" appears before the project name and updates
        else:
            project_name_match = re.search(r'(.*?)\n\n(?:\(cid:190\) Updates:|\(cid:190\) Project Schedule:|\(cid:190\) Estimated Schedule:)', section, re.DOTALL)
            if project_name_match:
                project_name = project_name_match.group(1).strip()
                project_name = project_name.split('\n')[-1].strip()  # Take the last line as project name
                # print(f"Processing project (alt): {project_name}")

                start_date_match = re.search(r'(Begin Construction|Advertise|Start Date):\s*(.*?)(?:\n|$)', section)
                start_date = start_date_match.group(2).strip() if start_date_match else ""

                if current_type and project_name:
                    projects.append({
                        "Project_Name": project_name,
                        "type": current_type,
                        "topic": "",  # Can't extract from this pattern
                        "status": "",  # Can't extract from this pattern
                        "st": start_date,
                        "et": ""
                    })

    return projects


with open(locals()['var_function-call-5915676293479369659'], 'r') as f:
    civic_docs = json.load(f)

all_projects = []
for doc in civic_docs:
    extracted_projects = extract_project_info(doc['text'])
    all_projects.extend(extracted_projects)


disaster_projects_2022 = []
for project in all_projects:
    if project['type'] == 'disaster' and '2022' in project['st']:
        disaster_projects_2022.append(project)

# Deduplicate projects based on Project_Name if necessary (assuming unique names)
deduplicated_projects = {}
for project in disaster_projects_2022:
    if project['Project_Name'] not in deduplicated_projects:
        deduplicated_projects[project['Project_Name']] = project


__RESULT__:
print(json.dumps(list(deduplicated_projects.values())))"""

env_args = {'var_function-call-9815844103134522859': ['civic_docs'], 'var_function-call-5915676293479369659': 'file_storage/function-call-5915676293479369659.json'}

exec(code, env_args)
