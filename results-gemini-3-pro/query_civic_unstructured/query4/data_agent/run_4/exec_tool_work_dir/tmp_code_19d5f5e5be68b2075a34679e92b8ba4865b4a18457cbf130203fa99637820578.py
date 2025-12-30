code = """import json
import re
import pandas as pd

# Load civic docs
with open('var_function-call-1460894796141311373', 'r') as f:
    civic_docs = json.load(f)

# Load funding data
with open('var_function-call-16354438159657144766', 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

target_projects = set()

# Regex for start date
# We look for "Begin Construction: <Date>" or similar
# We want dates that match Spring 2022 (Spring 2022, March 2022, April 2022, May 2022)
spring_2022_patterns = [
    r"Spring 2022", r"Spring, 2022",
    r"March 2022", r"March, 2022",
    r"April 2022", r"April, 2022",
    r"May 2022", r"May, 2022",
    r"2022-Spring", r"2022-03", r"2022-04", r"2022-05"
]

def is_spring_2022(text_chunk):
    # Find "Begin Construction" line
    match = re.search(r"Begin Construction:\s*(.*)", text_chunk, re.IGNORECASE)
    if match:
        date_str = match.group(1).strip()
        # Check if matches Spring 2022
        for pat in spring_2022_patterns:
            if re.search(pat, date_str, re.IGNORECASE):
                return True
    
    # Also check "Advertise: <Date>"? No, "started" usually means construction.
    # What if "Start Date:"?
    match = re.search(r"Start Date:\s*(.*)", text_chunk, re.IGNORECASE)
    if match:
        date_str = match.group(1).strip()
        for pat in spring_2022_patterns:
            if re.search(pat, date_str, re.IGNORECASE):
                return True
                
    # Also check "Construction was completed <Date>"?
    # If it completed in Spring 2022, it started earlier.
    # But if "Begin Construction" is not found, maybe look for general mention?
    # No, stick to explicit start.
    
    return False

# Iterate over docs
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    # Simple parser:
    # Identify project blocks.
    # A project block usually starts with a name.
    # Markers for project details: "(cid:190) Updates:", "(cid:190) Project Description:", "(cid:190) Project Schedule:"
    # We can iterate lines. If we find a marker, the previous non-empty line is the name.
    
    # We'll collect (name, full_text_of_block) tuples
    # Actually, the block continues until the next project name.
    
    current_project = None
    current_block = []
    
    # First, let's identify all indices where a project starts.
    # A project starts at line i if line i+k (skipping empty lines) starts with "(cid:190) Updates" or similar.
    
    project_starts = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Check for marker
        if "(cid:190)" in line or "Updates:" in line or "Project Description:" in line:
            # Check if this line *is* a marker line
            if line.startswith("(cid:190)") or line.startswith("Updates:") or line.startswith("Project Description:"):
                # The project name should be before this.
                # Look back for non-empty line
                j = i - 1
                while j >= 0 and not lines[j].strip():
                    j -= 1
                if j >= 0:
                    project_name = lines[j].strip()
                    # Filter out section headers like "Capital Improvement Projects (Design)"
                    if "Capital Improvement Projects" not in project_name:
                         # Store the start index of the project (line j)
                         # But wait, we might have multiple markers for one project.
                         # E.g. Updates, then Schedule.
                         # We only want to capture the project name once.
                         # So if we already have a current project and this marker belongs to it?
                         # Usually headers are distinct.
                         # Let's assume a new project name implies a new project.
                         # But "Project Schedule" follows "Updates".
                         # So if "Project Schedule" marker appears, the previous line is usually NOT the project name, but the end of previous section?
                         # In sample:
                         # (cid:190) Updates:
                         # ...
                         # (cid:190) Project Schedule:
                         # So "Project Schedule" is preceded by text.
                         # "Updates" is preceded by Project Name.
                         # "Project Description" is preceded by Project Name.
                         
                         if "Updates" in line or "Project Description" in line:
                             # This is likely the start of a project block (header + description/updates)
                             project_starts.append((j, project_name))
        i += 1
        
    # Now extract blocks
    for k in range(len(project_starts)):
        start_idx, name = project_starts[k]
        end_idx = project_starts[k+1][0] if k + 1 < len(project_starts) else len(lines)
        
        block_lines = lines[start_idx:end_idx]
        block_text = "\n".join(block_lines)
        
        if is_spring_2022(block_text):
            target_projects.add(name)

# Now filter funding
# Check exact match first
matched = funding_df[funding_df['Project_Name'].isin(target_projects)]

# If matches are low, maybe try cleaning names (strip whitespace)
# Or check substring
found_names = matched['Project_Name'].tolist()

# Calculate
count = len(matched)
total_funding = matched['Amount'].astype(int).sum()

result = {
    "count": count,
    "total_funding": int(total_funding),
    "projects": found_names,
    "target_projects_debug": list(target_projects)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-5721682823366817575': 'file_storage/function-call-5721682823366817575.json', 'var_function-call-1460894796141311373': 'file_storage/function-call-1460894796141311373.json', 'var_function-call-16354438159657144766': 'file_storage/function-call-16354438159657144766.json'}

exec(code, env_args)
