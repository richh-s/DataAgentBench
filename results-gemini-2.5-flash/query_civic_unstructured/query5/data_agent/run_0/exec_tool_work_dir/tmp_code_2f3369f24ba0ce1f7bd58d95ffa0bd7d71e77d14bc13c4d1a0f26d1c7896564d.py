code = """import pandas as pd
import json
import re

# Load the civic documents data
with open(locals()['var_function-call-788512929960335419'], 'r') as f:
    civic_docs_data = json.load(f)

disaster_projects_starting_2022_names = []

for doc in civic_docs_data:
    text = doc['text']

    # Split the document into potential project blocks.
    # A new block is assumed to start with a capitalized line that is not a 'cid' bullet.
    # Use a non-capturing group for the delimiter to keep the delimiter in the split parts if needed.
    # This regex needs to be extremely careful with backslashes in Python string literals.
    # The previous `SyntaxError: unterminated string literal` might be from mixing quotes or improper escaping.
    # Using r"..." for raw strings helps with backslashes.
    project_blocks = re.split(
        r"\n(?=[A-Z][A-Za-z0-9\\s&,-_\':\\/.\\(\\)]+?\\n)", # Split by a new line followed by a capitalized line (potential project name)
        text
    )

    for block in project_blocks:
        # Each block should start with a project name on the first line, then details.
        lines = block.strip().split('\n')
        if not lines: # Skip empty blocks
            continue

        project_name_candidate = lines[0].strip()
        project_details = " ".join(lines[1:]).strip()

        # Filter out lines that are unlikely to be project names (e.g., very short, or headers like 'Agenda Item')
        if not re.match(r"^[A-Z][A-Za-z0-9\\s&,-_\':\\/.\\(\\)]+?$", project_name_candidate) or \
           project_name_candidate.startswith("Agenda Item") or project_name_candidate.startswith("Page"):
            continue

        is_disaster = False
        # Check for disaster keywords in the project name or its details (case-insensitive)
        if re.search(r"FEMA|CalOES|CalJPIA|Disaster Recovery", project_name_candidate + " " + project_details, re.IGNORECASE):
            is_disaster = True
        
        if is_disaster:
            # Search for a 2022 date associated with construction start/completion within the details.
            # This regex looks for phrases like "Begin Construction:", "Construction was completed:", "Completed:"
            # followed by a date string that explicitly contains "2022".
            date_match = re.search(
                r"(?:Begin\\sConstruction|Construction\\swas\\scompleted|Completed):\\s*"
                r"(?P<Date_Info>\\b2022\\b(?:[-\\s]?(?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December))?(?:[-\\s]\\d{2})?)",
                project_details, re.IGNORECASE
            )
            
            if date_match:
                # Found a disaster project that started/completed in 2022
                disaster_projects_starting_2022_names.append(project_name_candidate)

# Remove duplicates from the list of project names
unique_disaster_projects_2022 = list(set(disaster_projects_starting_2022_names))

print("__RESULT__:")
print(json.dumps(unique_disaster_projects_2022))"""

env_args = {'var_function-call-4922019997739677456': ['civic_docs'], 'var_function-call-788512929960335419': 'file_storage/function-call-788512929960335419.json', 'var_function-call-9254905820928177274': [], 'var_function-call-6587616414360749789': [], 'var_function-call-3446571632783907127': [], 'var_function-call-2261813058681952031': [], 'var_function-call-8822505650285935510': []}

exec(code, env_args)
