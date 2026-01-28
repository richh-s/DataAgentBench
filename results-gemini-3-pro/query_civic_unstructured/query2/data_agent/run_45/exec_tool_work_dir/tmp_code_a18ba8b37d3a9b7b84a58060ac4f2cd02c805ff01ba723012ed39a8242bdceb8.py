code = """import json
import re

# Load the data
with open(locals()['var_function-call-18190371962378278332'], 'r') as f:
    data = json.load(f)

projects = []

for doc in data:
    text = doc['text']
    # The text seems to separate projects by headers or spacing.
    # Looking at the sample:
    # Project Name is often followed by "(cid:190)" (which is a bullet point character, likely converted)
    # or just separate blocks.
    
    # Let's try to split by the bullet point `(cid:190)` or look for lines that look like headers.
    # But `(cid:190)` appears inside the project block too.
    
    # Alternative: The project name is usually a line before `(cid:190) Updates:` or `(cid:190) Project Description:`
    
    # Let's split by lines
    lines = text.split('\n')
    
    current_project = None
    project_buffer = []
    
    # Heuristic: A project name is a non-empty line followed shortly by a line containing "(cid:190) Updates" or "(cid:190) Project Description" or similar.
    # However, there might be blank lines.
    
    # We can use regex to find blocks.
    # Pattern: ^(.+?)\n+?\(cid:190\)\s*(Updates|Project Description|Status)
    
    # Let's try to identify project start points.
    # We can look for the pattern `(cid:190) Updates` or `(cid:190) Project Description` and take the preceding non-empty lines as the title.
    
    # It might be safer to parse the text block by looking for these markers.
    
    # Let's iterate through lines and track context.
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this line is a marker
        if "(cid:190)" in line and ("Updates" in line or "Project Description" in line):
            # The project name should be in the previous lines.
            # Look backwards for the first non-empty line that is not a page number or header.
            # Usually the project name is just above.
            
            # Look back
            j = i - 1
            while j >= 0:
                prev_line = lines[j].strip()
                if prev_line and "Page" not in prev_line and "Agenda Item" not in prev_line and "Capital Improvement Projects" not in prev_line:
                     # This is likely the project name.
                     # Sometimes the name spans two lines?
                     # For now assume one line or check if the line before that is also part of it.
                     break
                j -= 1
            
            if j >= 0:
                project_name = lines[j].strip()
                # Store the previous project if any
                if current_project:
                    projects.append(current_project)
                
                current_project = {
                    "name": project_name,
                    "text": ""
                }
        
        if current_project:
            current_project["text"] += line + "\n"
            
    if current_project:
        projects.append(current_project)

# Now filter projects
matching_projects = []

for p in projects:
    name = p['name']
    text = p['text'].lower()
    
    # Check topic "park"
    # "park" or "playground" or "recreation" etc.
    # User asked for "park-related".
    is_park = "park" in name.lower() or "park" in text or "playground" in name.lower() or "playground" in text
    
    # Check status completed in 2022
    # Look for "completed" and "2022" in the same sentence or proximity.
    # Or specifically "completed: ... 2022"
    # The text often says "Construction was completed November 2022" or "Complete Construction: April 2023"
    
    # Regex for completion
    # completed .* 2022
    # complete construction .* 2022
    
    # Be careful with "Complete Design: Summer 2022" - this is not project completion.
    # We want "Construction completed" or just "Completed" (if it implies the whole project).
    
    is_completed_2022 = False
    
    # Patterns to match completion in 2022
    # "Construction was completed, November 2022"
    # "Complete Construction: November 2022"
    
    if "construction" in text and "completed" in text and "2022" in text:
        # Check proximity or specific phrasing
        if re.search(r"completed.*2022", text) or re.search(r"complete construction.*2022", text):
            # Exclude "design"
            # But "Complete Design: Summer 2022" would match "completed.*2022" if we are not careful.
            # Wait, "Complete Design" vs "Complete Construction"
            
            # Let's look for specific "construction" or bare "completed"
            
            if re.search(r"construction.*completed.*2022", text) or re.search(r"completed.*construction.*2022", text):
                 is_completed_2022 = True
            elif re.search(r"completed\s+(?:in|on|,)?\s*(?:january|february|march|april|may|june|july|august|september|october|november|december)?\s*2022", text):
                 # e.g. "Construction was completed, November 2022"
                 # matches "completed, November 2022"
                 is_completed_2022 = True
            
            # Also exclude if it says "Complete Design" in the same line?
            # Let's check lines again within the text
            for line in text.split('\n'):
                 if "2022" in line and ("complete" in line or "completed" in line):
                      if "design" in line:
                           continue
                      if "construction" in line or "project" in line or "completed" in line:
                           # verify it is 2022
                           is_completed_2022 = True

    if is_park and is_completed_2022:
        matching_projects.append(name)

print("__RESULT__:")
print(json.dumps(matching_projects))"""

env_args = {'var_function-call-18190371962378278332': 'file_storage/function-call-18190371962378278332.json'}

exec(code, env_args)
