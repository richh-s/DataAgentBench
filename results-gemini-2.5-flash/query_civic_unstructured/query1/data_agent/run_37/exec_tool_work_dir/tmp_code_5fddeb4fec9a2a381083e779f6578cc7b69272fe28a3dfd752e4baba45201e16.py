code = """import json
import re

def extract_projects(text):
    projects = []
    # Define sections and their project types/statuses
    sections = {
        "Capital Improvement Projects (Design)": {"type": "capital", "status": "design"},
    }

    for section_title, project_info in sections.items():
        # Regex to find the specific section and capture its content until another section or end of document
        section_pattern = re.compile(rf"{re.escape(section_title)}(.*?)(?:Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|RECOMMENDED ACTION:|\\Z)", re.DOTALL)
        section_match = section_pattern.search(text)

        if section_match:
            section_content = section_match.group(1)
            # Now, within this content, find lines that are likely project names
            # Project names typically appear as standalone lines, not starting with bullets (cid:) or being page numbers/agenda items.
            # They are usually followed by updates or schedule info.
            project_line_pattern = re.compile(r"(?m)^\s*(?!\\(cid:\\d+\\)|Page \\d+|Agenda Item # \\d+\\\\\.[A-Z])([A-Za-z0-9][^\\n]*?)\s*$") # Match lines not starting with (cid: or Page/Agenda Item
            
            # Iterate through the content to identify project names more carefully
            lines = section_content.split('\n')
            current_project_name = []
            for i, line in enumerate(lines):
                stripped_line = line.strip()
                if not stripped_line: # Skip empty lines
                    continue
                
                # Heuristic: If the line indicates updates or schedule, the previous collected lines form a project name
                if re.search(r'\\(cid:\\d+\\) (?:Updates:|Project Schedule:|Estimated Schedule:)', stripped_line):
                    if current_project_name:
                        project_name = ' '.join(current_project_name).strip()
                        projects.append({"Project_Name": project_name, **project_info})
                        current_project_name = []
                    continue
                
                # Skip lines that are clearly not project names (bullets, page numbers, etc.)
                if stripped_line.startswith('(cid:') or stripped_line.startswith('Page') or stripped_line.startswith('Agenda Item'):
                    if current_project_name: # If we were building a name and hit a non-name line, finalize the name
                        project_name = ' '.join(current_project_name).strip()
                        projects.append({"Project_Name": project_name, **project_info})
                        current_project_name = []
                    continue
                
                # If the line doesn't contain typical project info (updates, schedule), consider it part of a project name
                current_project_name.append(stripped_line)
            
            # After the loop, if there are remaining parts, add the last project
            if current_project_name:
                project_name = ' '.join(current_project_name).strip()
                projects.append({"Project_Name": project_name, **project_info})

    return projects

file_path = locals()['var_function-call-16303420803371647737']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

all_projects = []
for doc in civic_docs:
    all_projects.extend(extract_projects(doc['text']))

# Remove duplicates and clean project names again
project_names_set = set()
clean_unique_projects = []
for p in all_projects:
    clean_name = re.sub(r'\\(cid:\\d+\\)', '', p["Project_Name"]).strip()
    # Further refinement to ensure project names are not just descriptions or partial sentences
    # This is a heuristic: project names are usually concise. Filter out very long strings that are likely descriptions.
    if 5 < len(clean_name) < 100 and clean_name.count(' ') < 15: # Arbitrary length and word count limits
        if clean_name not in project_names_set:
            project_names_set.add(clean_name)
            p["Project_Name"] = clean_name
            clean_unique_projects.append(p)

print("__RESULT__:")
print(json.dumps(clean_unique_projects))"""

env_args = {'var_function-call-841909728376098398': ['civic_docs'], 'var_function-call-16303420803371647737': 'file_storage/function-call-16303420803371647737.json', 'var_function-call-15519595974979010567': 'file_storage/function-call-15519595974979010567.json'}

exec(code, env_args)
