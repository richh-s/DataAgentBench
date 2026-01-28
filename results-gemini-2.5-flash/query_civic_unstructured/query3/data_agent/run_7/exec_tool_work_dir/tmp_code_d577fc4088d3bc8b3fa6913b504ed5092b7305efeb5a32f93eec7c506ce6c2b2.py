code = """import json
import re

file_path = locals()['var_function-call-16784002980503323397']
with open(file_path, 'r') as f:
    docs_data = json.load(f)

extracted_projects = []

for doc in docs_data:
    text = doc['text']

    # Capital Improvement Projects (Design)
    design_projects_section = re.search(r"Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|Public Works Quarterly Update)", text, re.DOTALL)
    if design_projects_section:
        design_projects_text = design_projects_section.group(1)
        project_entries = re.findall(r"\n\n(.*?)\n\n\\(cid:190\\) Updates:", design_projects_text)
        for entry in project_entries:
            project_name = entry.strip()
            if "emergency" in project_name.lower() or "fema" in project_name.lower() or "disaster" in project_name.lower():
                extracted_projects.append({'Project_Name': project_name, 'Status': 'design', 'Topic': 'emergency/FEMA/disaster'})
        project_entries = re.findall(r"\n\n(.*?)\n\n\\(cid:190\\) Project Description:", design_projects_text)
        for entry in project_entries:
            project_name = entry.strip()
            if "emergency" in project_name.lower() or "fema" in project_name.lower() or "disaster" in project_name.lower():
                extracted_projects.append({'Project_Name': project_name, 'Status': 'design', 'Topic': 'emergency/FEMA/disaster'})

    # Capital Improvement Projects (Construction)
    construction_projects_section = re.search(r"Capital Improvement Projects \(Construction\)(.*?)(?=Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|Public Works Quarterly Update)", text, re.DOTALL)
    if construction_projects_section:
        construction_projects_text = construction_projects_section.group(1)
        project_entries = re.findall(r"\n\n(.*?)\n\n\\(cid:190\\) Updates:", construction_projects_text)
        for entry in project_entries:
            project_name = entry.strip()
            if "emergency" in project_name.lower() or "fema" in project_name.lower() or "disaster" in project_name.lower():
                extracted_projects.append({'Project_Name': project_name, 'Status': 'construction', 'Topic': 'emergency/FEMA/disaster'})
        project_entries = re.findall(r"\n\n(.*?)\n\n\\(cid:190\\) Project Description:", construction_projects_text)
        for entry in project_entries:
            project_name = entry.strip()
            if "emergency" in project_name.lower() or "fema" in project_name.lower() or "disaster" in project_name.lower():
                extracted_projects.append({'Project_Name': project_name, 'Status': 'construction', 'Topic': 'emergency/FEMA/disaster'})

    # Capital Improvement Projects (Not Started)
    not_started_projects_section = re.search(r"Capital Improvement Projects \(Not Started\)(.*?)(?=Disaster Recovery Projects|Public Works Quarterly Update)", text, re.DOTALL)
    if not_started_projects_section:
        not_started_projects_text = not_started_projects_section.group(1)
        project_entries = re.findall(r"\n\n(.*?)\n\n\\(cid:190\\) Project Description:", not_started_projects_text)
        for entry in project_entries:
            project_name = entry.strip()
            if "emergency" in project_name.lower() or "fema" in project_name.lower() or "disaster" in project_name.lower():
                extracted_projects.append({'Project_Name': project_name, 'Status': 'not started', 'Topic': 'emergency/FEMA/disaster'})
        project_entries = re.findall(r"\n\n(.*?)\n\n\\(cid:190\\) Updates:", not_started_projects_text)
        for entry in project_entries:
            project_name = entry.strip()
            if "emergency" in project_name.lower() or "fema" in project_name.lower() or "disaster" in project_name.lower():
                extracted_projects.append({'Project_Name': project_name, 'Status': 'not started', 'Topic': 'emergency/FEMA/disaster'})

    # Disaster Recovery Projects
    disaster_projects_section = re.search(r"Disaster Recovery Projects(.*?)(?=Public Works Quarterly Update)", text, re.DOTALL)
    if disaster_projects_section:
        disaster_projects_text = disaster_projects_section.group(1)
        project_entries = re.findall(r"\n\n(.*?)\n\n\\(cid:190\\) Updates:", disaster_projects_text)
        for entry in project_entries:
            project_name = entry.strip()
            if "emergency" in project_name.lower() or "fema" in project_name.lower() or "disaster" in project_name.lower():
                extracted_projects.append({'Project_Name': project_name, 'Status': 'disaster recovery', 'Topic': 'emergency/FEMA/disaster'})
        project_entries = re.findall(r"\n\n(.*?)\n\n\\(cid:190\\) Project Description:", disaster_projects_text)
        for entry in project_entries:
            project_name = entry.strip()
            if "emergency" in project_name.lower() or "fema" in project_name.lower() or "disaster" in project_name.lower():
                extracted_projects.append({'Project_Name': project_name, 'Status': 'disaster recovery', 'Topic': 'emergency/FEMA/disaster'})


    latigo_canyon_project_match = re.search(r"Latigo Canyon Road Retaining Wall Repair Project\n\n\\(cid:190\\) Updates:\n\n.*?Awaiting final FEMA/CalOES approval for scope modification", text, re.DOTALL)
    if latigo_canyon_project_match:
        extracted_projects.append({'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Status': 'design', 'Topic': 'FEMA'})

    outdoor_warning_signs_match = re.search(r"Outdoor Warning Signs\n\n\\(cid:190\\) Updates:\n\n.*?Project to be discussed during a joint Public Works and Public Safety\nCommission meeting for project direction due to concerns regarding\nsirens height and feedback from residents and the community.", text, re.DOTALL)
    if outdoor_warning_signs_match:
        extracted_projects.append({'Project_Name': 'Outdoor Warning Signs', 'Status': 'design', 'Topic': 'emergency warning'})

    city_traffic_signals_match = re.search(r"City Traffic Signals Backup Power\n\n\\(cid:190\\) Project Description: This project will include upgrading the backup power\nsystem to the City\u2019s traffic signals on Civic Center Way, Webb Way, Malibu\nCanyon Road, and Winter Canyon Road\n\n\\(cid:190\\) Updates: Project is in the preliminary design phase", text, re.DOTALL)
    if city_traffic_signals_match:
        extracted_projects.append({'Project_Name': 'City Traffic Signals Backup Power', 'Status': 'not started', 'Topic': 'emergency'})


print('__RESULT__:')
print(json.dumps(extracted_projects))"""

env_args = {'var_function-call-16784002980503323397': 'file_storage/function-call-16784002980503323397.json'}

exec(code, env_args)
