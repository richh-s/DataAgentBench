code = """import json
import re

# Load the full result from the file
with open(locals()['var_function-call-14735836657967561594'], 'r') as f:
    documents = json.load(f)

extracted_projects = []

for doc in documents:
    text = doc['text']
    
    # Using a more robust regex to capture project name and its subsequent details block
    # This pattern looks for a Project Name line, followed by at least one "(cid:190) [Section]:"
    # and then captures all lines until another project name, section header, or end of document.
    project_block_pattern = re.compile(
        r"\n\n([A-Z][A-Za-z0-9 &-,/']+(?: Project)?(?: Phase \d)?)\n" # Project Name
        r"(\((?:cid:\d+\)) (?:Updates|Project Description|Estimated Schedule):\n(?:\((?:cid:\d+\)) [^\n]*\n)*)+" # Details Block
        , re.DOTALL
    )

    # Iterating through the whole document to find project blocks
    for match in project_block_pattern.finditer(text):
        project_name = match.group(1).strip()
        project_details_block = match.group(2) # This contains all the (cid:190) updates etc.

        # Determine section context (Capital or Disaster, Design/Construction/Not Started)
        # We need to find the closest preceding section header for each project
        # This is a bit tricky with regex alone, so we'll use string search relative to the project start.
        
        # Default values
        current_section_type = None
        current_section_status = None

        # Look for section headers before the current project match
        preceding_text = text[:match.start()]
        
        if "Capital Improvement Projects (Design)" in preceding_text:
            current_section_type = "capital"
            current_section_status = "design"
        elif "Capital Improvement Projects (Construction)" in preceding_text:
            current_section_type = "capital"
            current_section_status = "construction"
        elif "Capital Improvement Projects (Not Started)" in preceding_text:
            current_section_type = "capital"
            current_section_status = "not started"
        elif "Disaster Recovery Projects" in preceding_text:
            current_section_type = "disaster"
            current_section_status = "various" # Specific status will be determined from details

        # Determine project status, prioritizing explicit mentions within the project details block
        status = current_section_status
        if "is currently under construction" in project_details_block.lower() or "is currently out to bid" in project_details_block.lower():
            status = "construction"
        elif "construction was completed" in project_details_block.lower() or "notice of completion filed" in project_details_block.lower():
            status = "completed"
        elif "in the preliminary design phase" in project_details_block.lower() or "working with the consultant to finalize the design plans" in project_details_block.lower() or "awaiting final fema/caloes approval" in project_details_block.lower():
            status = "design"
        elif "project is delayed" in project_details_block.lower():
            status = "delayed"

        # Determine project type, prioritizing explicit mentions in context
        project_type = current_section_type
        if "disaster recovery projects" in project_details_block.lower() or "fema" in project_details_block.lower():
            project_type = "disaster"
        elif "capital improvement projects" in project_details_block.lower() and project_type != "disaster":
            project_type = "capital"

        # Determine topics from project name and details block
        topic_keywords = []
        if "emergency" in project_name.lower() or "emergency" in project_details_block.lower():
            topic_keywords.append("emergency")
        if "FEMA" in project_name or "FEMA" in project_details_block:
            topic_keywords.append("FEMA")
        if "storm drain" in project_name.lower() or "storm drain" in project_details_block.lower():
            topic_keywords.append("storm drain")
        if "fire" in project_name.lower() or "fire" in project_details_block.lower():
            topic_keywords.append("fire")
        if "drainage" in project_name.lower() or "drainage" in project_details_block.lower():
            topic_keywords.append("drainage")
        if "disaster" in project_name.lower() or "disaster" in project_details_block.lower():
            topic_keywords.append("disaster")
        if "warning" in project_name.lower() or "warning" in project_details_block.lower():
            topic_keywords.append("emergency warning")
        if "road" in project_name.lower() or "road" in project_details_block.lower():
            topic_keywords.append("road")
        if "park" in project_name.lower() or "park" in project_details_block.lower():
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
