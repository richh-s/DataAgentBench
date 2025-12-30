code = """import json
import re

# Load the full result from the file
with open(locals()['var_function-call-14735836657967561594'], 'r') as f:
    documents = json.load(f)

extracted_projects = []

for doc in documents:
    text = doc['text']

    # Regex to find project names and the section they belong to
    project_section_pattern = re.compile(
        r"(Capital Improvement Projects \(Design\)|Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects)" # Section header
        r"\n\n" # Two newlines
        r"((?:[A-Z][A-Za-z0-9 &-,/]+?(?: Project)?(?: Phase \d)?\n\\(cid:190) (?:Updates|Project Description|Estimated Schedule):\n(?:\\(cid:131) [^\\n]*\\n)*)*)" # Projects within the section
    )

    for section_match in project_section_pattern.finditer(text):
        section_title = section_match.group(1)
        projects_text_in_section = section_match.group(2)

        section_type = None
        section_status = None

        if "Capital Improvement Projects (Design)" in section_title:
            section_type = "capital"
            section_status = "design"
        elif "Capital Improvement Projects (Construction)" in section_title:
            section_type = "capital"
            section_status = "construction"
        elif "Capital Improvement Projects (Not Started)" in section_title:
            section_type = "capital"
            section_status = "not started"
        elif "Disaster Recovery Projects" in section_title:
            section_type = "disaster"
            section_status = "various" # To be determined per project

        # Now, extract individual projects from projects_text_in_section
        project_detail_pattern = re.compile(
            r"([A-Z][A-Za-z0-9 &-,/]+?(?: Project)?(?: Phase \d)?)" # Project Name
            r"\n\\(cid:190) (Updates|Project Description|Estimated Schedule):" # Followed by update/description
            r"(?:\n(?:\\(cid:131) [^\\n]*)*)" # Followed by bullet points (optional)
        )

        for project_match in project_detail_pattern.finditer(projects_text_in_section):
            project_name = project_match.group(1).strip()
            project_details_text = project_match.group(0) # Full match including name and details

            # Determine status
            status = section_status
            if "is currently under construction" in project_details_text or "is currently out to bid" in project_details_text:
                status = "construction"
            elif "Construction was completed" in project_details_text or "Notice of completion filed" in project_details_text:
                status = "completed"
            elif "in the preliminary design phase" in project_details_text or "working with the consultant to finalize the design plans" in project_details_text:
                status = "design"
            elif "Awaiting final FEMA/CalOES approval" in project_details_text:
                status = "design" # Or 'pending approval'

            # Determine type
            project_type = section_type
            if "Disaster Recovery Projects" in section_title:
                project_type = "disaster"

            # Determine topic
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
