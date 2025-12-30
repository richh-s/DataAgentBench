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
    
    # Refined project name pattern, carefully escaped
    project_name_pattern = re.compile(r"^[A-Z][A-Za-z0-9 &-,/\']+(?: Project)?(?: Phase \\d)?$")

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
            current_section_status = "various"

        project_name_match = project_name_pattern.match(line)
        if project_name_match and not ("Page " in line) and not ("Agenda Item #" in line):
            project_name = project_name_match.group(0).strip()
            
            project_context = ""
            # Look for project details in the next few lines
            for j in range(i + 1, min(i + 15, len(lines))):
                next_line = lines[j].strip()
                # Stop if we hit another project name or a new section header
                if project_name_pattern.match(next_line) or \
                   "Capital Improvement Projects" in next_line or \
                   "Disaster Recovery Projects" in next_line or \
                   re.match(r"^\(cid:\d+\)", next_line): # For (cid:xxx) which marks new sections often
                    break
                project_context += next_line + "\n"
            
            # Determine status from context, prioritizing explicit mentions
            status = current_section_status
            if "is currently under construction" in project_context.lower() or "is currently out to bid" in project_context.lower():
                status = "construction"
            elif "construction was completed" in project_context.lower() or "notice of completion filed" in project_context.lower():
                status = "completed"
            elif "in the preliminary design phase" in project_context.lower() or "working with the consultant to finalize the design plans" in project_context.lower() or "awaiting final fema/caloes approval" in project_context.lower():
                status = "design"
            elif "project is delayed" in project_context.lower():
                status = "delayed"

            # Determine type from context
            project_type = current_section_type
            if "disaster recovery projects" in project_context.lower() or "fema" in project_context.lower():
                project_type = "disaster"
            elif "capital improvement projects" in project_context.lower() and project_type != "disaster": # Avoid overwriting if already disaster
                project_type = "capital"

            # Determine topics from project name and context
            topic_keywords = []
            if "emergency" in project_name.lower() or "emergency" in project_context.lower():
                topic_keywords.append("emergency")
            if "FEMA" in project_name or "FEMA" in project_context:
                topic_keywords.append("FEMA")
            if "storm drain" in project_name.lower() or "storm drain" in project_context.lower():
                topic_keywords.append("storm drain")
            if "fire" in project_name.lower() or "fire" in project_context.lower():
                topic_keywords.append("fire")
            if "drainage" in project_name.lower() or "drainage" in project_context.lower():
                topic_keywords.append("drainage")
            if "disaster" in project_name.lower() or "disaster" in project_context.lower():
                topic_keywords.append("disaster")
            if "warning" in project_name.lower() or "warning" in project_context.lower():
                topic_keywords.append("emergency warning")
            if "road" in project_name.lower() or "road" in project_context.lower():
                topic_keywords.append("road")
            if "park" in project_name.lower() or "park" in project_context.lower():
                topic_keywords.append("park")

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
final_projects_from_docs = []
for project in unique_projects:
    if project["topic"] and ("emergency" in project["topic"].lower() or "fema" in project["topic"].lower()):
        final_projects_from_docs.append(project)

print("__RESULT__:")
print(json.dumps(final_projects_from_docs))"""

env_args = {'var_function-call-15574106946328272683': ['civic_docs'], 'var_function-call-14735836657967561594': 'file_storage/function-call-14735836657967561594.json'}

exec(code, env_args)
