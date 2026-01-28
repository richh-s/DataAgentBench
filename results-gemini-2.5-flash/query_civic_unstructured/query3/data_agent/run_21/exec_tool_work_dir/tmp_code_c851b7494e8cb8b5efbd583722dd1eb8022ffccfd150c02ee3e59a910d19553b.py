code = """import json
import re

with open(locals()['var_function-call-2241076992410809533'], 'r') as f:
    civic_docs = json.load(f)

projects_data = []

for doc in civic_docs:
    text = doc['text']
    # Regex to find project names and their updates/status.
    # We are looking for lines starting with a potential project name, followed by updates or schedule information.
    # The pattern (cid:190) Updates: is common for updates.
    # The pattern (cid:190) Project Schedule: is common for schedule.
    # We also look for lines containing "Capital Improvement Projects (Design)", "Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", and "Disaster Recovery Projects"

    # Capture Capital Improvement Projects
    capital_design_match = re.findall(r"Capital Improvement Projects \(Design\)\n\n(.*?)(?=\n\nCapital Improvement Projects \(Construction\)|\n\nDisaster Recovery Projects|\n\nCapital Improvement Projects \(Not Started\)|$)", text, re.DOTALL)
    if capital_design_match:
        design_projects_text = capital_design_match[0]
        design_projects = re.findall(r"(.+?)\n\n\(cid:190\) Updates:(.*?)(?=\n\n.+?\n\n\(cid:190\) Updates:|\n\n)", design_projects_text, re.DOTALL)
        for project_name, updates in design_projects:
            project_name = project_name.strip()
            if re.search(r"emergency|FEMA", project_name, re.IGNORECASE) or re.search(r"emergency|FEMA", updates, re.IGNORECASE):
                projects_data.append({"Project_Name": project_name, "status": "design", "topic": "emergency/FEMA"})

    capital_construction_match = re.findall(r"Capital Improvement Projects \(Construction\)\n\n(.*?)(?=\n\nCapital Improvement Projects \(Not Started\)|\n\nDisaster Recovery Projects|$)", text, re.DOTALL)
    if capital_construction_match:
        construction_projects_text = capital_construction_match[0]
        construction_projects = re.findall(r"(.+?)\n\n\(cid:190\) Updates:(.*?)(?=\n\n.+?\n\n\(cid:190\) Updates:|\n\n)", construction_projects_text, re.DOTALL)
        for project_name, updates in construction_projects:
            project_name = project_name.strip()
            if re.search(r"emergency|FEMA", project_name, re.IGNORECASE) or re.search(r"emergency|FEMA", updates, re.IGNORECASE):
                projects_data.append({"Project_Name": project_name, "status": "construction", "topic": "emergency/FEMA"})

    capital_not_started_match = re.findall(r"Capital Improvement Projects \(Not Started\)\n\n(.*?)(?=\n\nDisaster Recovery Projects|$)", text, re.DOTALL)
    if capital_not_started_match:
        not_started_projects_text = capital_not_started_match[0]
        not_started_projects = re.findall(r"(.+?)\n\n\(cid:190\) Project Description:(.*?)(?=\n\n.+?\n\n\(cid:190\) Project Description:|\n\n)", not_started_projects_text, re.DOTALL)
        for project_name, description in not_started_projects:
            project_name = project_name.strip()
            if re.search(r"emergency|FEMA", project_name, re.IGNORECASE) or re.search(r"emergency|FEMA", description, re.IGNORECASE):
                projects_data.append({"Project_Name": project_name, "status": "not started", "topic": "emergency/FEMA"})

    # Capture Disaster Recovery Projects
    disaster_projects_match = re.findall(r"Disaster Recovery Projects\n\n(.*?)(?=\n\nCapital Improvement Projects \(Design\)|\n\nCapital Improvement Projects \(Construction\)|\n\nCapital Improvement Projects \(Not Started\)|$)", text, re.DOTALL)
    if disaster_projects_match:
        disaster_projects_text = disaster_projects_match[0]
        disaster_projects = re.findall(r"(.+?)\n\n\(cid:190\) Updates:(.*?)(?=\n\n.+?\n\n\(cid:190\) Updates:|\n\n)", disaster_projects_text, re.DOTALL)
        for project_name, updates in disaster_projects:
            project_name = project_name.strip()
            if re.search(r"emergency|FEMA", project_name, re.IGNORECASE) or re.search(r"emergency|FEMA", updates, re.IGNORECASE) or "FEMA Project" in project_name or "CalOES Project" in project_name:
                # Attempt to determine a more specific status from the updates.
                status = "unknown"
                if re.search(r"completed", updates, re.IGNORECASE):
                    status = "completed"
                elif re.search(r"under construction", updates, re.IGNORECASE):
                    status = "construction"
                elif re.search(r"design", updates, re.IGNORECASE) or re.search(r"preliminary design", updates, re.IGNORECASE):
                    status = "design"
                elif re.search(r"not started", updates, re.IGNORECASE):
                    status = "not started"
                projects_data.append({"Project_Name": project_name, "status": status, "topic": "emergency/FEMA"})

    # Catch any other mentions of "emergency" or "FEMA" that might be standalone projects
    # This pattern looks for "Project Name" followed by "Updates" or "Schedule", then checks if "emergency" or "FEMA" is in the surrounding text.
    project_pattern = re.compile(r"([A-Z][a-zA-Z0-9'\- ]+? Project)(?=\n\n\(cid:190\) Updates:.*?emergency|FEMA|\(cid:190\) Project Schedule:.*?emergency|FEMA|\(cid:190\) Project Description:.*?emergency|FEMA)", re.DOTALL | re.IGNORECASE)
    for match in project_pattern.finditer(text):
        project_name = match.group(1).strip()
        # To determine status, we need to extract more context around the project.
        # This is more complex than the previous structured extractions, so we will primarily rely on the structured ones.
        # However, if we find a project name and then see "FEMA/CalOES approval" later, we can infer its a design phase.
        if "FEMA/CalOES approval" in text and project_name not in [p['Project_Name'] for p in projects_data]:
             projects_data.append({"Project_Name": project_name, "status": "design", "topic": "emergency/FEMA"})

    # Specifically look for "Outdoor Warning Signs" as it is explicitly related to emergency and has updates.
    outdoor_warning_signs_match = re.search(r"Outdoor Warning Signs\n\n\(cid:190\) Updates:(.*?)(?=\n\n.+?\n\n\(cid:190\) Updates:|\n\n)", text, re.DOTALL)
    if outdoor_warning_signs_match:
        updates = outdoor_warning_signs_match.group(1)
        if re.search(r"emergency", updates, re.IGNORECASE):
            # Attempt to determine a more specific status from the updates.
            status = "design" # Based on "project direction due to concerns regarding sirens height"
            projects_data.append({"Project_Name": "Outdoor Warning Signs", "status": status, "topic": "emergency"})
    
    # Specifically look for "Latigo Canyon Road Retaining Wall Repair Project"
    latigo_match = re.search(r"Latigo Canyon Road Retaining Wall Repair Project\n\n\(cid:190\) Updates:(.*?)(?=\n\n.+?\n\n\(cid:190\) Updates:|\n\n)", text, re.DOTALL)
    if latigo_match:
        updates = latigo_match.group(1)
        if "FEMA/CalOES approval" in updates:
            projects_data.append({"Project_Name": "Latigo Canyon Road Retaining Wall Repair Project", "status": "design", "topic": "FEMA"})

    # Specifically look for "City Traffic Signals Backup Power"
    traffic_signals_match = re.search(r"City Traffic Signals Backup Power\n\n\(cid:190\) Project Description:(.*?)\n\n\(cid:190\) Updates:(.*?)\n\n\(cid:190\) Project Schedule:(.*?)(?=\n\n.+?$)", text, re.DOTALL)
    if traffic_signals_match:
        description = traffic_signals_match.group(1)
        updates = traffic_signals_match.group(2)
        if re.search(r"emergency", description, re.IGNORECASE) or re.search(r"emergency", updates, re.IGNORECASE):
            projects_data.append({"Project_Name": "City Traffic Signals Backup Power", "status": "preliminary design", "topic": "emergency"})

# Remove duplicates
unique_projects = []
seen_projects = set()
for project in projects_data:
    if project['Project_Name'] not in seen_projects:
        unique_projects.append(project)
        seen_projects.add(project['Project_Name'])


print("__RESULT__:")
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-16338752333912652679': ['civic_docs'], 'var_function-call-2241076992410809533': 'file_storage/function-call-2241076992410809533.json'}

exec(code, env_args)
