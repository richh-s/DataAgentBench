code = """import json
import re

# Load the data
with open(locals()['var_function-call-18190371962378278332'], 'r') as f:
    data = json.load(f)

projects = []

for doc in data:
    text = doc['text']
    lines = text.split('\n')
    
    current_project_name = None
    current_project_text = []
    
    # Iterate and group lines into projects
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check for start of a project section via markers
        # Markers: (cid:190) Updates:, (cid:190) Project Description:, (cid:190) Project Schedule:
        # Actually usually the structure is:
        # PROJECT NAME
        # (cid:190) Updates: ...
        
        if "(cid:190)" in line and ("Updates" in line or "Project Description" in line or "Status" in line):
            # The line BEFORE this (ignoring empty lines/headers) is likely the Project Name.
            
            # Search backwards for the name
            name_candidate = None
            j = i - 1
            while j >= 0:
                prev = lines[j].strip()
                # Skip common headers or empty lines
                if not prev or "Page" in prev or "Agenda Item" in prev or "Capital Improvement" in prev:
                    j -= 1
                    continue
                name_candidate = prev
                break
            
            # If we found a name, and it's different from current, start new project
            if name_candidate:
                # If we were already collecting a project, save it
                if current_project_name and name_candidate != current_project_name:
                    projects.append({"name": current_project_name, "text": "\n".join(current_project_text)})
                    current_project_text = []
                
                current_project_name = name_candidate
        
        if current_project_name:
            current_project_text.append(line)
            
    # Append the last one
    if current_project_name:
        projects.append({"name": current_project_name, "text": "\n".join(current_project_text)})

# Filter
matching_projects = set() # Use set to avoid duplicates

for p in projects:
    name = p['name']
    text = p['text'].lower()
    
    # Clean name
    name_clean = name.strip()
    
    # 1. Check for 'park' related keywords in Name or Text
    # Keywords: park, playground, recreation, gardens, etc.
    # The user query specifies "park-related".
    is_park_related = False
    keywords = ["park", "playground", "recreation", "garden", "walkway"] 
    # Added "walkway" because of "Point Dume Walkway" and "Malibu Bluffs Park South Walkway" in the text
    # But "walkway" alone might be generic (e.g. road walkway). 
    # However, "Malibu Bluffs Park" has "park".
    # "Point Dume Walkway" -> Point Dume is a nature reserve. 
    # Let's stick to "park" and "playground" primarily, and maybe check context for others if needed.
    # The hint says: Common topics include: "park", ... "playground".
    
    if "park" in name_clean.lower() or "playground" in name_clean.lower():
        is_park_related = True
    elif "park" in text or "playground" in text:
        # If it's in the text, we must ensure it's describing the project type, not just a reference.
        # But given the unstructured nature, presence is a strong signal if the project name is ambiguous.
        # However, many road projects might mention "park" (e.g. "near the park").
        # Let's rely on Name mostly, or strong indicators.
        # "Bluffs Park Shade Structure" -> Name has Park.
        # "Trancas Canyon Park Playground" -> Name has Park/Playground.
        pass

    # Re-evaluating logic:
    # If the name doesn't have "park", but text does, is it a park project?
    # Example: "Broad Beach Road Water Quality Repair" -> might mention park? Unlikely to be a park project.
    # So searching in Name is safer.
    
    # Let's check the extracted names from the preview:
    # "Bluffs Park Shade Structure"
    # "Trancas Canyon Park Upper and Lower Slopes Repair"
    # "Permanent Skate Park"
    # "Malibu Bluffs Park South Walkway Repairs"
    # "Trancas Canyon Park Playground"
    
    # These all have "Park" in the name.
    # "Point Dume Walkway Repairs" -> Does not have "Park". But Point Dume is a park.
    # Let's check if "Point Dume" implies park.
    # If I miss it, I might undercount.
    # But "Point Dume" is a location.
    # Let's verify extracted projects later.
    
    if "park" in name_clean.lower() or "playground" in name_clean.lower():
        is_park_related = True
        
    # 2. Check status "completed" in 2022
    is_completed_2022 = False
    
    # Look for lines in text indicating completion
    # Common strings: "Construction was completed, November 2022", "Construction was completed November 2022"
    
    if "completed" in text and "2022" in text:
        # Regex to be more specific
        # Matches: completed followed by date in 2022
        # or: completed in 2022
        if re.search(r"completed.*2022", text):
            # Check if it is "design" or "construction"
            # If the text says "Complete Design: ... 2022", it's NOT completed project.
            # If it says "Construction was completed" or "Complete Construction: ... 2022", it IS completed.
            
            # Check for "design" in the matching line
            # We can split by lines and check the line with "completed" and "2022"
            for line in text.split('\n'):
                if "completed" in line and "2022" in line:
                    if "design" in line:
                        continue # Skip design completion
                    is_completed_2022 = True
                elif "complete construction" in line and "2022" in line:
                    is_completed_2022 = True

    if is_park_related and is_completed_2022:
        matching_projects.add(name_clean)

print("__RESULT__:")
print(json.dumps(list(matching_projects)))"""

env_args = {'var_function-call-18190371962378278332': 'file_storage/function-call-18190371962378278332.json'}

exec(code, env_args)
