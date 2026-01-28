code = """import json
import re

file_path = locals()['var_function-call-13210468559198728867']

with open(file_path, 'r') as f:
    data = json.load(f)

park_projects_completed_2022 = set()

completion_keywords = ["completed", "complete construction", "construction was completed", "notice of completion filed"]

for doc in data:
    text = doc['text']

    lines = text.split('\n')
    current_project_candidate = None
    context_lines = []

    for i, line in enumerate(lines):
        stripped_line = line.strip()

        is_potential_project_name = False
        # Using double quotes for the regex string to avoid issues with single quotes in Python's `code` argument
        if re.match(r"^[A-Z][a-zA-Z0-9\s,&-]+$", stripped_line) and len(stripped_line.split()) > 2:
            if not any(kw in stripped_line for kw in ["Public Works Commission", "Agenda Report", "RECOMMENDED ACTION", "DISCUSSION", "Capital Improvement Projects", "Disaster Recovery Projects", "Status Report", "Subject", "Item", "Prepared by", "Approved by", "Date prepared", "Meeting date", "Updates:", "Project Schedule:", "Project Description:", "Estimated Schedule:", "To:", "By:", "Page"]):
                 is_potential_project_name = True

        if is_potential_project_name:
            if current_project_candidate:
                full_context = " ".join(context_lines).lower()

                is_park_project = ("park" in current_project_candidate.lower() or "playground" in current_project_candidate.lower())

                is_completed = any(keyword in full_context for keyword in completion_keywords)

                # Check for 2022 more broadly in the context to cover variations like 'November 2022'
                is_2022 = re.search(r'2022', full_context)

                if is_park_project and is_completed and is_2022:
                    park_projects_completed_2022.add(current_project_candidate)

            current_project_candidate = stripped_line
            context_lines = []
        else:
            if current_project_candidate:
                context_lines.append(stripped_line)

    # Check the last project candidate after the loop finishes
    if current_project_candidate:
        full_context = " ".join(context_lines).lower()

        is_park_project = ("park" in current_project_candidate.lower() or "playground" in current_project_candidate.lower())

        is_completed = any(keyword in full_context for keyword in completion_keywords)

        is_2022 = re.search(r'2022', full_context)

        if is_park_project and is_completed and is_2022:
            park_projects_completed_2022.add(current_project_candidate)

result_project_names = list(park_projects_completed_2022)

print("__RESULT__:")
print(json.dumps(result_project_names))"""

env_args = {'var_function-call-13210468559198728867': 'file_storage/function-call-13210468559198728867.json', 'var_function-call-9401061401891132651': {'first_doc_filename': 'malibucity_agenda_03222023-2060.txt'}}

exec(code, env_args)
