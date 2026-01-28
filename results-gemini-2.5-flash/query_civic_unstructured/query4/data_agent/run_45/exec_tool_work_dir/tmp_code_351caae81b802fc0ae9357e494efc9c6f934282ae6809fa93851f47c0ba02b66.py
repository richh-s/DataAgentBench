code = """import json
import re

file_path = locals()['var_function-call-8179248509000558122']
with open(file_path, 'r') as f:
    data = json.load(f)

spring_2022_projects = []

# A more robust regex to capture project names and their schedules.
# It looks for a potential project name line, followed by schedule header,
# and then a schedule detail line containing 'Spring 2022' or similar months.
# Using re.DOTALL to allow '.' to match newlines in the non-greedy parts.
project_schedule_pattern = re.compile(
    r'([A-Z][a-zA-Z0-9 &,/\.\(\)]{5,}[^\n]*?)\n'  # Project Name: Starts with Cap letter, min 5 chars, then any chars except newline, non-greedy
    r'(?:\s*\(cid:\d+\)[^\n]*\n)*?'              # Optional (cid) lines
    r'\s*(?:Project Schedule:|Estimated Schedule:)[^\n]*\n' # Schedule header
    r'(?:\s*\(cid:\d+\)[^\n]*\n)*?'              # Optional (cid) lines
    r'([^\n]*?(?:Spring|March|April|May)\s*2022[^\n]*)', # Schedule detail with Spring 2022
    re.IGNORECASE | re.DOTALL
)

known_non_projects = [
    "Capital Improvement Projects (Design)",
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects",
    "Public Works Commission",
    "Agenda Report",
    "Public Works",
    "Item",
    "Page",
    "Capital Improvement Program",
    "Agenda Item # 4.B.",
    "Table of Contents",
    "BACKGROUND",
    "FINDINGS",
    "FISCAL IMPACT",
    "ATTACHMENTS",
    "Project Description"
]

for doc in data:
    text_content = doc['text']
    for match in project_schedule_pattern.finditer(text_content):
        project_name = match.group(1).strip()
        
        # Filter out known headers that might be accidentally captured as project names
        if not any(header.lower() in project_name.lower() for header in known_non_projects) and len(project_name) > 5:
            spring_2022_projects.append(project_name)

# Remove duplicates
unique_spring_2022_projects = list(set(spring_2022_projects))

print("__RESULT__:")
print(json.dumps(unique_spring_2022_projects)))"""

env_args = {'var_function-call-8179248509000558122': 'file_storage/function-call-8179248509000558122.json'}

exec(code, env_args)
