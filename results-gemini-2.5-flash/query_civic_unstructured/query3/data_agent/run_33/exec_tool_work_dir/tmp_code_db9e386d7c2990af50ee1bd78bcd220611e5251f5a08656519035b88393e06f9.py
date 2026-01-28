code = """import json
import re

file_path = locals()['var_function-call-13262898608241461619']

with open(file_path, 'r') as f:
    data = json.load(f)

projects = []
for doc in data:
    text = doc['text']
    # Regex to find project names and their status or related keywords (like FEMA)
    # This regex is an attempt to capture project names which are often followed by their status or relevant keywords
    # I am looking for lines that describe projects and their status or type.
    # It's a heuristic approach and might need refinement based on actual text content.

    # Example patterns from the hint:
    # "Disaster Recovery Projects, often FEMA-funded or related to Woolsey Fire recovery"
    # "Disaster project names often include suffixes like \"(FEMA Project)\""

    # Looking for "Project Name (Update/Status/Type)"
    # Or just "Project Name" followed by some keywords
    
    # I will try to extract projects and their details based on common patterns found in the preview.
    # From the preview, project names are often followed by "(Updates: ...)", "(Project Schedule: ...)", "(Project Description: ...)"
    # Or they are listed under sections like "Capital Improvement Projects (Design)", "Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)"
    # I will focus on projects explicitly mentioning "FEMA", "CalOES", "Disaster Recovery" or "emergency" in the vicinity of their names or descriptions.

    # For projects under 'Capital Improvement Projects (Design)', 'Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)'
    # and also looking for keywords like 'FEMA', 'CalOES', 'emergency', 'disaster'

    # Pattern for "Project Name (Update/Schedule/Description)"
    project_pattern = r"(.+?)(?:\s*\\n\\n(cid:190) (?:Updates|Project Schedule|Project Description):.*?)?(?=\\n\\n(?:\\n\\n|\\nAgenda Item|\\nPage)|$)"
    # This pattern attempts to capture project names by looking for a line that starts with a project name,
    # and then optionally followed by update/schedule/description section.
    # It stops before another project or a new section in the document.

    # Revised pattern to capture projects more robustly, and their status if explicitly mentioned.
    # This pattern looks for lines that appear to be project names and then tries to extract status and topic from surrounding text.
    # I will simplify the extraction process by first identifying general sections and then projects within those sections.

    # Re-evaluating the document structure from the preview:
    # - Sections like "Capital Improvement Projects (Design)", "Disaster Recovery Projects"
    # - Projects listed within these sections, often followed by "(cid:190) Updates:", "(cid:190) Project Schedule:", etc.

    # Let's use a simpler approach: iterate through lines and look for project names,
    # then try to extract relevant information from the following lines.

    lines = text.split('\\n')
    current_section = ""
    for i, line in enumerate(lines):
        line = line.strip()

        if "Capital Improvement Projects (Design)" in line:
            current_section = "design"
            continue
        elif "Capital Improvement Projects (Construction)" in line:
            current_section = "completed" # Assuming construction implies completed or in progress
            continue
        elif "Capital Improvement Projects (Not Started)" in line:
            current_section = "not started"
            continue
        elif "Disaster Recovery Projects" in line:
            # Disaster Recovery Projects can be in various stages, need to look for specific status
            current_section = "disaster_recovery" # Special section for disaster projects
            continue

        # Look for Project Names, which are often followed by specific update/schedule markers
        if re.match(r"^[A-Z][a-zA-Z0-9\\s&,-]+$", line) and not line.startswith("Page") and not line.startswith("Agenda Item"):
            project_name = line.strip()
            # Now, try to extract status and topic based on the surrounding text
            project_status = None
            project_topic = []

            # Check for keywords related to 'emergency' or 'FEMA'
            if re.search(r"emergency|FEMA|CalOES|disaster", project_name, re.IGNORECASE):
                if "FEMA" in project_name:
                    project_topic.append("FEMA")
                if "emergency" in project_name:
                    project_topic.append("emergency")
                if "disaster" in project_name:
                    project_topic.append("disaster")
                if "CalOES" in project_name:
                    project_topic.append("CalOES")
                
                # Try to determine status
                # Look in the next few lines for status indicators
                for j in range(i + 1, min(i + 5, len(lines))):
                    next_line = lines[j].strip()
                    if "Updates:" in next_line:
                        if "under construction" in next_line:
                            project_status = "completed" # Assuming "under construction" leads to completion
                        elif "design" in next_line or "planning" in next_line:
                            project_status = "design"
                        elif "completed" in next_line:
                            project_status = "completed"
                        elif "awaiting final FEMA/CalOES approval" in next_line:
                            project_status = "design" # Still in a planning/approval stage
                        elif "not started" in next_line:
                            project_status = "not started"
                    if "Project Schedule:" in next_line:
                         if "Begin Construction: Fall 2023" in next_line:
                             project_status = "design"
                         elif "Complete Design: Summer 2023" in next_line:
                             project_status = "design"

                if current_section == "design" and project_status is None:
                    project_status = "design"
                elif current_section == "completed" and project_status is None:
                    project_status = "completed"
                elif current_section == "not started" and project_status is None:
                    project_status = "not started"
                
                # If project_status is still None, try to infer from project name or document context
                if project_status is None:
                    if "(FEMA Project)" in project_name or "(CalOES Project)" in project_name:
                        project_status = "design" # Assuming these suffixes suggest ongoing projects
                    elif "Repairs" in project_name or "Improvements" in project_name:
                        # These could be ongoing or completed. Need more context.
                        pass
                
                # For topics, also search in next few lines
                for k in range(i + 1, min(i + 10, len(lines))):
                    next_line_for_topic = lines[k].strip()
                    if re.search(r"emergency|FEMA|CalOES|disaster", next_line_for_topic, re.IGNORECASE):
                        if "FEMA" not in project_topic and "FEMA" in next_line_for_topic:
                            project_topic.append("FEMA")
                        if "emergency" not in project_topic and "emergency" in next_line_for_topic:
                            project_topic.append("emergency")
                        if "disaster" not in project_topic and "disaster" in next_line_for_topic:
                            project_topic.append("disaster")
                        if "CalOES" not in project_topic and "CalOES" in next_line_for_topic:
                            project_topic.append("CalOES")

                if project_status and project_topic: # Only add if we have some status and topic
                    projects.append({
                        "Project_Name": project_name,
                        "status": project_status,
                        "topic": ", ".join(project_topic)
                    })

# This is a basic extraction. A more robust NLP approach would be better for unstructured text.
# Given the constraints, I will try to manually refine this extraction logic based on the preview.

# Let's re-parse the data again, with a more targeted approach.
# Specifically, for Latigo Canyon Road Retaining Wall Repair Project: "(cid:131) Awaiting final FEMA/CalOES approval for scope modification" -> status: design, topic: FEMA, CalOES
# For Outdoor Warning Signs: "Project to be discussed... due to concerns regarding sirens height" -> status: design, topic: emergency warning (implicitly from context of "Outdoor Warning Signs")

extracted_projects = []
for doc in data:
    text = doc['text']
    # Split the text into sections or lines that might contain project information
    
    # Common project patterns:
    # 1. Project name followed by "(cid:190) Updates:", "(cid:190) Project Schedule:", "(cid:190) Project Description:"
    # 2. Project name inside a section, e.g., "Capital Improvement Projects (Design)"
    
    # Let's try to extract project names and their associated block of text
    # A project block starts with a potential project name and ends before another project name or a new section.
    
    # This regex attempts to find project names (typically capitalized words, possibly with numbers, ampersands)
    # followed by their details up until the next project name or end of relevant document section.
    # It looks for a sequence of lines that form a project block.
    
    # Refined pattern for project names and their descriptions/updates
    # This regex is an attempt to capture project names and the associated update/schedule/description text.
    # It assumes project names are on their own line or start a line, and updates/schedules follow with a specific marker.
    project_blocks = re.findall(r"([A-Z][a-zA-Z0-9\\s&,-]+(?:\\s*\\(FEMA Project\\)|\\s*\\(CalOES Project\\))?)(?:\\n\\n(?:\\(cid:190) (?:Updates|Project Schedule|Project Description):.*?))+?(?=\\n\\n[A-Z][a-zA-Z0-9\\s&,-]+(?:\\s*\\(FEMA Project\\)|\\s*\\(CalOES Project\\))?|\\nAgenda Item|\\nPage|$)", text, re.DOTALL)

    # The above regex is still complex for general extraction.
    # Let's simplify and iterate through lines, marking sections and extracting projects.
    
    lines = text.split('\\n')
    current_status_context = None # To hold status inferred from section headers
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Update status context based on section headers
        if "Capital Improvement Projects (Design)" in line:
            current_status_context = "design"
        elif "Capital Improvement Projects (Construction)" in line:
            current_status_context = "completed" # In construction or recently completed
        elif "Capital Improvement Projects (Not Started)" in line:
            current_status_context = "not started"
        # "Disaster Recovery Projects" implies a topic, not necessarily a status
        # but could influence topic extraction.

        # Heuristic: Identify a project name if it's a capitalized phrase on its own line,
        # followed by (cid:190) markers, and contains keywords like 'emergency' or 'FEMA'.
        if re.match(r"^[A-Z][a-zA-Z0-9\\s&,-]+$", line) and not line.startswith("Page") and not line.startswith("Agenda Item"):
            project_name_candidate = line
            
            # Check the next few lines for 'emergency' or 'FEMA' keywords and status
            relevant_text_around_project = ' '.join(lines[i:min(i+10, len(lines))]) # Look at next 10 lines
            
            if re.search(r"emergency|FEMA|CalOES|disaster", relevant_text_around_project, re.IGNORECASE):
                project_name = project_name_candidate.strip()
                status = current_status_context # Default to section status
                topic = []
                
                if re.search(r"FEMA", relevant_text_around_project, re.IGNORECASE):
                    topic.append("FEMA")
                if re.search(r"emergency", relevant_text_around_project, re.IGNORECASE):
                    topic.append("emergency")
                if re.search(r"disaster", relevant_text_around_project, re.IGNORECASE):
                    topic.append("disaster")
                if re.search(r"CalOES", relevant_text_around_analysis, re.IGNORECASE):
                    topic.append("CalOES") # Not exactly a topic but a related entity

                # Refine status based on specific keywords in the project block
                if "under construction" in relevant_text_around_project:
                    status = "completed"
                elif "design" in relevant_text_around_project:
                    status = "design"
                elif "awaiting final FEMA/CalOES approval" in relevant_text_around_project:
                    status = "design"
                elif "completed" in relevant_text_around_project:
                    status = "completed"
                elif "not started" in relevant_text_around_project:
                    status = "not started"
                
                # If a project name has (FEMA Project) or (CalOES Project), add it to topic
                if "(FEMA Project)" in project_name and "FEMA" not in topic:
                    topic.append("FEMA")
                if "(CalOES Project)" in project_name and "CalOES" not in topic:
                    topic.append("CalOES")
                
                # Special handling for "Outdoor Warning Signs"
                if "Outdoor Warning Signs" in project_name_candidate:
                    topic.append("emergency warning")
                    if status is None:
                        status = "design" # From the context in the preview, it's still under discussion/design
                
                # Ensure unique project names for the final output, as the same project might be mentioned multiple times.
                # Use a set of project names to keep track.
                
                # Add if not already extracted or if new information is more complete
                project_found = False
                for existing_project in extracted_projects:
                    if existing_project['Project_Name'] == project_name:
                        project_found = True
                        # If existing status is less specific, update it
                        if (existing_project['status'] == None or existing_project['status'] == "unknown") and status is not None:
                            existing_project['status'] = status
                        # Combine topics, ensuring uniqueness
                        for t in topic:
                            if t not in existing_project['topic']:
                                existing_project['topic'].append(t)
                        break
                
                if not project_found and status and topic: # Only add if we have some status and topic
                     extracted_projects.append({
                        "Project_Name": project_name,
                        "status": status,
                        "topic": list(set(topic)) # Ensure unique topics
                    })

final_extracted_projects = []
# Post-processing to remove duplicates and refine topics/statuses
project_names_seen = set()
for p in extracted_projects:
    if p['Project_Name'] not in project_names_seen:
        final_extracted_projects.append(p)
        project_names_seen.add(p['Project_Name'])
    else:
        # If already seen, merge information (e.g., combine topics if new info adds more)
        for existing_p in final_extracted_projects:
            if existing_p['Project_Name'] == p['Project_Name']:
                # Update status if the new one is more specific
                if p['status'] is not None and (existing_p['status'] is None or existing_p['status'] == "unknown"):
                    existing_p['status'] = p['status']
                # Merge topics
                for t in p['topic']:
                    if t not in existing_p['topic']:
                        existing_p['topic'].append(t)
                break

# Convert topic list to comma-separated string for consistency
for p in final_extracted_projects:
    p['topic'] = ', '.join(p['topic'])

__RESULT__:")
print(json.dumps(final_extracted_projects))"""

env_args = {'var_function-call-13550203671448261431': ['civic_docs'], 'var_function-call-13262898608241461619': 'file_storage/function-call-13262898608241461619.json'}

exec(code, env_args)
