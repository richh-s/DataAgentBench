code = """import json
import re

# Load funding data
with open(locals()['var_function-call-14713834321312381364'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-14713834321312381855'], 'r') as f:
    civic_docs = json.load(f)

# Combine all text from civic docs
full_text = "\n".join([doc.get('text', '') for doc in civic_docs])

# List of project names
project_names = [item['Project_Name'] for item in funding_data]

# Sort project names by length descending to avoid partial matches first (though finding all occurrences is better)
# But here we want to find where each project is discussed in the text.
# A project might appear multiple times. We should check all occurrences.

park_projects = []
total_funding = 0

# Helper to identify park projects by name
def is_park_project(name):
    keywords = ['park', 'playground', 'recreation', 'open space', 'skate']
    return any(k in name.lower() for k in keywords)

# We need to find the text segments for each project.
# Since searching for all project names in a huge text and splitting is complex, 
# let's iterate through each project and find its occurrences.
# We assume the update block follows the name.

matched_projects = []

for project in funding_data:
    p_name = project['Project_Name']
    p_amount = project['Amount']
    
    # Check if park related
    if not is_park_project(p_name):
        continue
        
    # Search in text
    # We look for the project name followed by some update text.
    # To avoid matching just the name in a list, we look for the context.
    # Based on preview, the format is "Project Name\n\n(cid:190) Updates:..."
    # So we search for Project Name, get the index, and look ahead.
    
    # Find all start indices
    starts = [m.start() for m in re.finditer(re.escape(p_name), full_text)]
    
    completed_2022 = False
    
    for start in starts:
        # Extract a chunk of text after the name (e.g., 500 chars)
        # The block usually ends when another project starts or a major header appears.
        # But 500 chars should be enough to capture the status updates shown in preview.
        chunk = full_text[start:start+1000]
        
        # Check for completion in 2022
        # Avoid "design completed" if possible, but "Construction was completed" is the key.
        # Patterns in preview:
        # "Construction was completed November 2022"
        # "Construction was completed, November 2022"
        # "Notice of completion filed January 2023" (implies completion before)
        
        # We look for "completed" and "2022" in the chunk.
        # But we must ensure it's not "Design completed".
        # The preview shows "Complete Design: Summer 2023".
        # So "Complete Design" is a schedule item, not status.
        # "Construction was completed" is a status.
        
        if re.search(r"construction\s+was\s+completed.*2022", chunk, re.IGNORECASE):
            completed_2022 = True
            break
        if re.search(r"project\s+.*completed.*2022", chunk, re.IGNORECASE):
            # Make sure it's not design
            if "design" not in chunk[chunk.lower().find("completed"):].lower().split('\n')[0]:
                 completed_2022 = True
                 break
        
        # Check for specific phrase "Construction was completed" and date in same line
        lines = chunk.split('\n')
        for line in lines:
            if "completed" in line.lower() and "2022" in line and "construction" in line.lower():
                completed_2022 = True
                break
            # Check for "completed" and "2022" without "construction" if strictly "completed" status
            if "completed" in line.lower() and "2022" in line:
                if "design" not in line.lower():
                    completed_2022 = True
                    break

    if completed_2022:
        matched_projects.append(project)
        total_funding += int(p_amount)

print("__RESULT__:")
print(json.dumps({"matched_projects": [p['Project_Name'] for p in matched_projects], "total_funding": total_funding}))"""

env_args = {'var_function-call-14713834321312381364': 'file_storage/function-call-14713834321312381364.json', 'var_function-call-14713834321312381855': 'file_storage/function-call-14713834321312381855.json'}

exec(code, env_args)
