code = """import json
import re

# Load Funding Data
with open('var_function-call-17829266993034408002.json', 'r') as f:
    funding_data = json.load(f)

# Load Civic Docs Data
with open('var_function-call-17376844456995138725.json', 'r') as f:
    civic_data = json.load(f)

# Combine text from all civic docs
full_text = "\n".join([doc['text'] for doc in civic_data])

# Filter Park Projects from Funding Data
# We look for "Park" in the project name.
park_projects = {}
all_project_names = set()
for item in funding_data:
    p_name = item['Project_Name']
    all_project_names.add(p_name)
    if 'park' in p_name.lower():
        # Store amount. Handle duplicates?
        # Assuming Project_Name is unique or we sum them? 
        # The table has Funding_ID, so one project can have multiple funding sources.
        # We need the total funding for the project.
        if p_name not in park_projects:
            park_projects[p_name] = 0
        park_projects[p_name] += item['Amount']

# Function to check completion in 2022
completed_projects_2022 = []

for p_name in park_projects:
    # Find all occurrences of the project name in the text
    # We regex escape the name just in case
    # We look for the project name followed by some text until likely the next section or project
    # But since we don't know the exact structure, let's look for the project name 
    # and then look for "completed" and "2022" within a window (e.g., 500 chars)
    
    # Using finditer to get all occurrences
    matches = [m.start() for m in re.finditer(re.escape(p_name), full_text, re.IGNORECASE)]
    
    is_completed_2022 = False
    for start_idx in matches:
        # Define a window after the match
        # The text snippet should be enough to contain status updates
        window_size = 1000 
        snippet = full_text[start_idx:start_idx+window_size]
        
        # Check for completion keywords
        # Looking for "Construction was completed" or similar
        # And "2022"
        
        # Simplify: Check if "completed" and "2022" are in the snippet
        # BUT verify "completed" refers to status, not "design completed"
        # The preview showed: "Complete Design: Summer 2023" vs "Construction was completed... 2022"
        
        # Regex for completion
        # Pattern: "Construction (was )?completed" or "Project (was )?completed"
        # Or "Status: Completed"
        
        # Let's try to capture the date associated with completion
        # Pattern: "completed.*2022"
        
        # Case 1: "Construction was completed November 2022"
        # Case 2: "Construction was completed, November 2022"
        
        if re.search(r'Construction was completed.*2022', snippet, re.IGNORECASE):
            is_completed_2022 = True
            break
        
        # Also check for "Notice of completion filed.*2023" which implies 2022 completion usually?
        # No, let's stick to "completed ... 2022"
        
        # What if it says "completed in 2022"?
        
    if is_completed_2022:
        completed_projects_2022.append(p_name)

# Calculate total funding
total_funding = 0
for p_name in completed_projects_2022:
    total_funding += park_projects[p_name]

print("__RESULT__:")
print(json.dumps({
    "completed_park_projects": completed_projects_2022,
    "total_funding": total_funding,
    "park_projects_found": list(park_projects.keys())
}))"""

env_args = {'var_function-call-17376844456995135534': ['Funding'], 'var_function-call-17376844456995138725': 'file_storage/function-call-17376844456995138725.json', 'var_function-call-17829266993034408002': 'file_storage/function-call-17829266993034408002.json'}

exec(code, env_args)
