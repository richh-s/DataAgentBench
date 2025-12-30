code = """import json
import re

# Load the full result from the file
with open(locals()['var_function-call-14735836657967561594'], 'r') as f:
    documents = json.load(f)

extracted_projects = []

for doc in documents:
    text = doc['text']
    lines = text.split('\n')

    current_section_type = None
    current_section_status = None
    
    project_name_pattern = re.compile(r"^([A-Z][A-Za-z0-9 &-,/]+?(?: Project)?(?: Phase \d)?)" # Project Name
                                      r"$") # End of line
    
    for i, line in enumerate(lines):
        line = line.strip()

        if "Capital Improvement Projects (Design)" in line:
            current_section_type = "capital"
            current_section_status = "design"
        elif "Capital Improvement Projects (Construction)" in line:
            current_section_type = "capital"
            current_section_status = "construction"
        elif "Capital Improvement Projects (Not Started)" in line:
            current_section_type = "capital"
            current_section_status = "not started"
        elif "Disaster Recovery Projects" in line:
            current_section_type = "disaster"
            current_section_status = "various" # Status will be more specific per project

        project_name_match = project_name_pattern.match(line)
        if project_name_match:
            project_name = project_name_match.group(1).strip()
            
            # Now look for details about this project in subsequent lines
            project_details_text = ""
            for j in range(i + 1, min(i + 10, len(lines))):
                if "(cid:190)" in lines[j] or "Page" in lines[j]: # Look for common markers that signify project details or end of section
                    project_details_text += lines[j].strip() + "\n"
                else:
                    break # Stop if we hit a line that doesn't look like a detail or end of section

            status = current_section_status
            if "is currently under construction" in project_details_text or "is currently out to bid" in project_details_text:
                status = "construction"
            elif "Construction was completed" in project_details_text or "Notice of completion filed" in project_details_text:
                status = "completed"
            elif "in the preliminary design phase" in project_details_text or "working with the consultant to finalize the design plans" in project_details_text:
                status = "design"
            elif "Awaiting final FEMA/CalOES approval" in project_details_text:
                status = "design" # Or 'pending approval'
            
            project_type = current_section_type
            if "Disaster Recovery Projects" in text[text.find(project_name):min(text.find(project_name) + 200, len(text))] and project_type != "disaster":
                 project_type = "disaster"
            elif "Capital Improvement Projects" in text[text.find(project_name):min(text.find(project_name) + 200, len(text))] and project_type != "capital":
                 project_type = "capital"

            topic_keywords = []
            if "emergency" in project_name.lower() or "emergency" in project_details_text.lower():
                topic_keywords.append("emergency")
            if "FEMA" in project_name or "FEMA" in project_details_text:
                topic_keywords.append("FEMA")
            if "storm drain" in project_name.lower() or "storm drain" in project_details_text.lower():
                topic_keywords.append("storm drain")
            if "fire" in project_name.lower() or "fire" in project_details_text.lower():
                topic_keywords.append("fire")
            if "drainage" in project_name.lower() or "drainage" in project_details_text.lower():
                topic_keywords.append("drainage")
            if "disaster" in project_name.lower() or "disaster" in project_details_text.lower():
                topic_keywords.append("disaster")
            if "warning" in project_name.lower() or "warning" in project_details_text.lower():
                topic_keywords.append("emergency warning")
            if "road" in project_name.lower() or "road" in project_details_text.lower():
                topic_keywords.append("road")

            topic = ", ".join(sorted(list(set(topic_keywords))))

            extracted_projects.append({
                "Project_Name": project_name,
                "topic": topic if topic else None,
                "type": project_type,
                "status": status
            })

# Filter for unique projects (name, type, status, topic)
unique_projects = []
seen_projects = set()

for project in extracted_projects:
    project_tuple = (project["Project_Name"], project["type"], project["status"], project["topic"])
    if project_tuple not in seen_projects:
        unique_projects.append(project)
        seen_projects.add(project_tuple)

# Further refine and filter for 'emergency' or 'FEMA' in topic
final_projects = []
for project in unique_projects:
    if project["topic"] and ("emergency" in project["topic"].lower() or "fema" in project["topic"].lower()):
        final_projects.append(project)

print("__RESULT__:")
print(json.dumps(final_projects))"""

env_args = {'var_function-call-15574106946328272683': ['civic_docs'], 'var_function-call-14735836657967561594': 'file_storage/function-call-14735836657967561594.json'}

exec(code, env_args)
