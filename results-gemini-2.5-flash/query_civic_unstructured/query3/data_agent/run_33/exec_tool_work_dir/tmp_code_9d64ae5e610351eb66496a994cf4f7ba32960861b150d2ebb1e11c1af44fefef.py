code = """import json
import re

file_path = locals()['var_function-call-13262898608241461619']

with open(file_path, 'r') as f:
    data = json.load(f)

extracted_projects = []
project_names_seen = set()

for doc in data:
    text = doc['text']
    lines = text.split('\n') # Splitting by '\n' as text is already parsed JSON, not raw with \\n

    current_status_context = None

    for i, line in enumerate(lines):
        line = line.strip()

        # Update status context based on section headers
        if "Capital Improvement Projects (Design)" in line:
            current_status_context = "design"
            continue
        elif "Capital Improvement Projects (Construction)" in line:
            current_status_context = "completed"
            continue
        elif "Capital Improvement Projects (Not Started)" in line:
            current_status_context = "not started"
            continue
        elif "Disaster Recovery Projects" in line:
            # This is a section header, not a project name itself, but indicates relevant topics
            # Don't set current_status_context from this alone, look for explicit status later
            continue

        # Look for potential project names.
        # Project names are usually capitalized, possibly with numbers, &,-, and on their own line.
        # Avoid lines that are just "Page X of Y" or "Agenda Item # X.Y".
        # A simple heuristic for a project name: starts with a capital letter, contains letters/numbers/spaces/&/-, longer than 5 chars
        if re.search(r"^[A-Z][a-zA-Z0-9\s&,-]{5,}$", line) and not line.startswith("Page") and not line.startswith("Agenda Item"):
            project_name_candidate = line.strip()

            # Create a window of text around the project candidate to look for keywords and status.
            # Look up to 10 lines ahead and 2 lines behind for project details.
            # Max 12 lines for the window to prevent going too far.
            start_index = max(0, i - 2)
            end_index = min(len(lines), i + 10)
            relevant_text_window = ' '.join(lines[start_index:end_index]).lower()

            if re.search(r"emergency|fema|caloes|disaster", relevant_text_window):
                project_name = project_name_candidate
                status = current_status_context
                topic = []

                if re.search(r"fema", relevant_text_window):
                    topic.append("FEMA")
                if re.search(r"emergency", relevant_text_window):
                    topic.append("emergency")
                if re.search(r"disaster", relevant_text_window):
                    topic.append("disaster")
                if re.search(r"caloes", relevant_text_window):
                    topic.append("CalOES")
                
                # Refine status based on specific keywords in the relevant text window
                if "under construction" in relevant_text_window:
                    status = "completed"
                elif "design" in relevant_text_window or "preliminary design" in relevant_text_window:
                    status = "design"
                elif "awaiting final fema/caloes approval" in relevant_text_window:
                    status = "design"
                elif "completed" in relevant_text_window:
                    status = "completed"
                elif "not started" in relevant_text_window:
                    status = "not started"
                
                # Special handling for "Outdoor Warning Signs"
                if "Outdoor Warning Signs" in project_name:
                    if "emergency warning" not in topic: # Add if not already there
                        topic.append("emergency warning")
                    if status is None:
                        status = "design" # Inferred from context in the preview

                # If status is still None, try to infer from project name itself if it contains clues
                if status is None:
                    if "(FEMA Project)" in project_name or "(CalOES Project)" in project_name:
                        status = "design" # Often means it's an ongoing, planned project

                # Only add if a valid status and at least one relevant topic is found
                if status is not None and len(topic) > 0:
                    if project_name not in project_names_seen:
                        extracted_projects.append({
                            "Project_Name": project_name,
                            "status": status,
                            "topic": topic
                        })
                        project_names_seen.add(project_name)
                    else:
                        # Merge information if project is seen again (e.g., combine topics)
                        for p in extracted_projects:
                            if p['Project_Name'] == project_name:
                                # Update status if new one is more specific (e.g., from None to design)
                                if status is not None and (p['status'] is None or (p['status'] == 'not started' and status == 'design') or (p['status'] == 'design' and status == 'completed')):
                                    p['status'] = status
                                # Merge topics
                                for t in topic:
                                    if t not in p['topic']:
                                        p['topic'].append(t)
                                break

# Convert topic list to comma-separated string for consistency and sort for canonical representation
for p in extracted_projects:
    p['topic'] = ', '.join(sorted(list(set(p['topic']))))

print("__RESULT__:")
print(json.dumps(extracted_projects))"""

env_args = {'var_function-call-13550203671448261431': ['civic_docs'], 'var_function-call-13262898608241461619': 'file_storage/function-call-13262898608241461619.json'}

exec(code, env_args)
