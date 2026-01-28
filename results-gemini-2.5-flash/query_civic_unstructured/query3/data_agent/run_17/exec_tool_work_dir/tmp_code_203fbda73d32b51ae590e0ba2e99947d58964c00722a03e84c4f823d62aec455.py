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
    
    # Project name pattern to identify potential project names on a line.
    # Using a raw string for regex and carefully escaping single quotes for the outer string.
    project_name_pattern = re.compile(r"^[A-Z][A-Za-z0-9 &-,/\'\']+(?: Project)?(?: Phase \\d)?$")

    for i, line in enumerate(lines):
        line = line.strip()

        # Update current section type and status based on headers
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

        # Check if the line matches a project name pattern
        project_name_match = project_name_pattern.match(line)
        if project_name_match and not ("Page " in line) and not ("Agenda Item #" in line):
            project_name = project_name_match.group(0).strip()
            
            # Extract context for the project from subsequent lines
            project_context = ""
            # Look up to 10 lines ahead for project details to avoid capturing too much irrelevant text
            for j in range(i + 1, min(i + 10, len(lines))):
                next_line = lines[j].strip()
                # Stop if we encounter another potential project name, a new section, or specific markers
                if project_name_pattern.match(next_line) or \
                   "Capital Improvement Projects" in next_line or \
                   "Disaster Recovery Projects" in next_line or \
                   "To:" in next_line or "Subject:" in next_line or \
                   re.search(r"^\\(cid:\\d+\\)$", next_line) or \
                   "Page " in next_line or \
                   "Agenda Item #" in next_line:
                    break
                project_context += next_line + "\n"
            
            # Determine project status, prioritizing explicit mentions in context
            status = current_section_status
            if "is currently under construction" in project_context.lower() or "is currently out to bid" in project_context.lower():
                status = "construction"
            elif "construction was completed" in project_context.lower() or "notice of completion filed" in project_context.lower():
                status = "completed"
            elif "in the preliminary design phase" in project_context.lower() or "working with the consultant to finalize the design plans" in project_context.lower() or "awaiting final fema/caloes approval" in project_context.lower():
                status = "design"
            elif "project is delayed" in project_context.lower():
                status = "delayed"

            # Determine project type, prioritizing explicit mentions in context
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

# Filter for projects related to 'emergency' or 'FEMA' in topic
final_projects_from_docs = []
for project in unique_projects:
    if project["topic"] and ("emergency" in project["topic"].lower() or "fema" in project["topic"].lower()):
        final_projects_from_docs.append(project)

print("__RESULT__:")
print(json.dumps(final_projects_from_docs))"""

env_args = {'var_function-call-15574106946328272683': ['civic_docs'], 'var_function-call-14735836657967561594': 'file_storage/function-call-14735836657967561594.json'}

exec(code, env_args)
