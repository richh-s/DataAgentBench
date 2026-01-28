code = """import json
import re

# Access file paths from local variables
# The keys are 'var_function-call-2809487722948638107' and 'var_function-call-2809487722948637720'
funding_path = locals()['var_function-call-2809487722948638107']
civic_docs_path = locals()['var_function-call-2809487722948637720']

# Load data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Extract project names from funding database
project_names = set(item['Project_Name'] for item in funding_data)

# Sort by length descending to match longer names first
sorted_project_names = sorted(list(project_names), key=len, reverse=True)

# Regex to find dates indicating completion in 2022
# Looking for "completed" followed by "2022" within reasonable distance
# Or "Complete Construction: ... 2022"
date_regex = re.compile(r'(completed|complete construction|notice of completion).*?2022', re.IGNORECASE | re.DOTALL)

completed_2022_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    # Find indices of all project names in this text
    found_projects = []
    for name in sorted_project_names:
        start = 0
        while True:
            idx = text.find(name, start)
            if idx == -1:
                break
            found_projects.append((idx, name))
            start = idx + len(name)
            
    # Sort by appearance in text
    found_projects.sort(key=lambda x: x[0])
    
    # Iterate through found projects
    for i in range(len(found_projects)):
        start_idx, name = found_projects[i]
        # Define segment: from this project name to the next
        if i + 1 < len(found_projects):
            end_idx = found_projects[i+1][0]
        else:
            end_idx = len(text)
            
        segment = text[start_idx:end_idx]
        
        # Check if park-related
        # Check name first
        is_park = 'park' in name.lower() or 'playground' in name.lower() or 'recreation' in name.lower()
        
        # If not in name, check if "park" is in the text segment near the name
        # But be careful not to pick up other projects' keywords.
        # The segment is specific to this project.
        if not is_park:
            if 'park' in segment.lower():
                is_park = True
                
        if is_park:
            # Check for completion in 2022
            # Specific phrases from the preview:
            # "Construction was completed November 2022"
            # "Construction was completed, November 2022"
            # "Complete Construction: November 2022" (though usually "Summer 2023" in preview)
            
            if date_regex.search(segment):
                # Verify it's construction completion
                lower_seg = segment.lower()
                if "construction" in lower_seg and ("completed" in lower_seg or "complete" in lower_seg):
                     completed_2022_projects.add(name)

# Calculate total funding
total_funding = 0
found_details = []
for name in completed_2022_projects:
    # Get amount
    # Handle potential duplicates in funding DB (though Project_Name should be unique per project, Funding table might have multiple sources for one project)
    # The description says "Funding table contains funding records... Project_Name (str)".
    # A project might have multiple funding entries.
    records = [r for r in funding_data if r['Project_Name'] == name]
    project_total = 0
    for r in records:
        project_total += int(r['Amount'])
    
    if project_total > 0:
        total_funding += project_total
        found_details.append({"name": name, "amount": project_total})

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": found_details}))"""

env_args = {'var_function-call-2809487722948638107': 'file_storage/function-call-2809487722948638107.json', 'var_function-call-2809487722948637720': 'file_storage/function-call-2809487722948637720.json'}

exec(code, env_args)
