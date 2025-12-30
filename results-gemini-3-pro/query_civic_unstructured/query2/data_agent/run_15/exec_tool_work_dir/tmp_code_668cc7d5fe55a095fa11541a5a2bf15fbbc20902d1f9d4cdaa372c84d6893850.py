code = """import json
import re

# Load Funding Data
with open(locals()['var_function-call-777734505766911732'], 'r') as f:
    funding_data = json.load(f)

# Create a dictionary for funding lookup: Name -> Amount
funding_map = {}
for entry in funding_data:
    # Normalize name slightly? (strip)
    name = entry['Project_Name'].strip()
    # Ensure amount is int
    amount = int(str(entry['Amount']))
    funding_map[name] = amount

# Load Civic Docs
with open(locals()['var_function-call-777734505766909915'], 'r') as f:
    civic_docs = json.load(f)

completed_park_projects = set()

# Helper to check if park related
def is_park_related(name, text):
    # Check name first
    name_lower = name.lower()
    if 'park' in name_lower or 'playground' in name_lower or 'recreation' in name_lower:
        return True
    # Check text
    # text_lower = text.lower()
    # if 'park' in text_lower:
    #     return True
    return False

# Helper to check if completed in 2022
def is_completed_2022(text):
    # Search for "completed" ... "2022"
    # Patterns: "Construction was completed November 2022", "Completed: March 2022"
    # "Notice of completion filed January 2023" (implies completion earlier, but we stick to explicit completion date)
    
    # Normalize text
    text_lower = text.lower()
    
    # Simple check: "completed" and "2022" in the same line or phrase?
    # Let's look for the word "completed" followed eventually by "2022" within reasonable distance?
    # Or strict regex
    
    # Pattern 1: completed [month] 2022
    if re.search(r'completed\W+(?:[a-z]+\W+)?2022', text_lower):
        return True
    
    # Pattern 2: completed in 2022
    if re.search(r'completed\s+in\s+2022', text_lower):
        return True
        
    return False

# Extract projects from docs
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Identify project start lines
    # Heuristic: Line i is a project name if Line i+1 starts with (cid:190) (unicode \u00be)
    # The preview shows: "(cid:190) Updates:"
    
    for i in range(len(lines) - 1):
        line = lines[i].strip()
        next_line = lines[i+1].strip()
        
        # Check for marker in next_line
        if next_line.startswith('(cid:190)') or next_line.startswith('\u00be'):
            project_name = line
            if not project_name: 
                # Sometimes the name might be on line i-1 if line i is empty
                if i > 0:
                    project_name = lines[i-1].strip()
            
            if not project_name:
                continue

            # Extract block
            # Block ends at next project name. 
            # But simpler: scan until next line followed by (cid:190), or end of doc.
            # We can just take the next N lines or search for the next marker.
            
            block_lines = []
            for j in range(i + 1, len(lines) - 1):
                block_line = lines[j].strip()
                block_next = lines[j+1].strip()
                if block_next.startswith('(cid:190)') or block_next.startswith('\u00be'):
                    # Found start of next project
                    break
                block_lines.append(lines[j])
            
            # Add the last few lines if we hit end
            # Actually, the inner loop captures up to the start of next.
            
            project_text = " ".join(block_lines)
            
            if is_park_related(project_name, project_text):
                if is_completed_2022(project_text):
                    completed_park_projects.add(project_name)

# Calculate funding
total_funding = 0
found_projects = []
missing_projects = []

for proj in completed_park_projects:
    if proj in funding_map:
        total_funding += funding_map[proj]
        found_projects.append((proj, funding_map[proj]))
    else:
        # Try fuzzy match or check if exists with slight variation
        # E.g. "Project Name" vs "Project Name (CalOES)"
        # The prompt says project names match.
        missing_projects.append(proj)

# Result
print("__RESULT__:")
print(json.dumps({
    "total_funding": total_funding,
    "completed_park_projects": list(completed_park_projects),
    "found_projects_details": found_projects,
    "missing_projects": missing_projects
}))"""

env_args = {'var_function-call-5669291864972532438': ['Funding'], 'var_function-call-5669291864972531351': ['civic_docs'], 'var_function-call-777734505766911732': 'file_storage/function-call-777734505766911732.json', 'var_function-call-777734505766909915': 'file_storage/function-call-777734505766909915.json'}

exec(code, env_args)
