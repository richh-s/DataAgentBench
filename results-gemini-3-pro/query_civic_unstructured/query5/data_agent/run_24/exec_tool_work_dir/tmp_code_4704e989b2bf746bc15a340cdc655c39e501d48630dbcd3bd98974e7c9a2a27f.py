code = """import json
import re
import pandas as pd

# Load civic docs
with open(locals()['var_function-call-2498552123289550299'], 'r') as f:
    docs = json.load(f)

# Load funding data
funding_df = pd.DataFrame(json.load(open(locals()['var_function-call-4052442815910590834'])))

projects = []

for doc in docs:
    text = doc['text']
    # Split text into segments based on project headers which seem to precede "Updates:"
    # We look for lines that look like project titles.
    # Pattern: Title \n+ (bullet) Updates:
    # We'll use a regex to find the starts of projects.
    
    # Normalize text to handle special characters if necessary, but regex might handle it.
    # The bullet is (cid:190) which often maps to ¾ or just a special char.
    # Let's try to match "Updates:"
    
    # We can split by "\n\n" and look for blocks.
    # Or find all matches of `(.*?)\n+(?:\(cid:190\)|\u00be|¾) Updates:`
    
    # Let's inspect the text structure more closely by finding the indices of "Updates:"
    matches = list(re.finditer(r'([^\n]+)\n+(?:\(cid:190\)|\u00be|¾|●|•)?\s*Updates:', text))
    
    # If no matches with specific bullets, try just "Updates:"
    if not matches:
        matches = list(re.finditer(r'([^\n]+)\n+Updates:', text))

    # Now extract blocks
    for i in range(len(matches)):
        start_idx = matches[i].start()
        # The project name is captured in group 1
        name = matches[i].group(1).strip()
        
        # The content of this project goes until the next project starts or end of text
        content_start = matches[i].end()
        if i < len(matches) - 1:
            content_end = matches[i+1].start()
        else:
            content_end = len(text)
            
        content = text[content_start:content_end]
        
        # Extract dates
        # Look for "Begin Construction: <date>"
        begin_construction = re.search(r'Begin Construction:\s*(.*)', content, re.IGNORECASE)
        # Look for "Advertise: <date>"
        advertise = re.search(r'Advertise:\s*(.*)', content, re.IGNORECASE)
        # Look for "Complete Design: <date>"
        complete_design = re.search(r'Complete Design:\s*(.*)', content, re.IGNORECASE)
        
        st = None
        if begin_construction:
            st = begin_construction.group(1).strip()
        elif advertise:
            st = advertise.group(1).strip() # Fallback?
        elif complete_design:
            st = complete_design.group(1).strip() # Fallback?
            
        # Refine st: strictly start date. If the project is "Not Started", "Begin Construction" is the planned start.
        # If the project is "Construction", "Begin Construction" might be past.
        # We want projects that "started in 2022".
        # If "Begin Construction" says "Fall 2023", it started in 2023.
        # If "Begin Construction" says "November 2022", it started in 2022.
        
        # Also check for "Construction was completed ... 2022".
        # If it completed in 2022, it likely started in 2022 or 2021. 
        # But if the query is strict about "started in 2022", and we don't know the start date, maybe we shouldn't include it unless we have a start date.
        # But for "Bluffs Park Shade Structure", it says "Construction was completed November 2022".
        # It's a small project, might have started in 2022.
        
        # Let's extract keywords for topic/type
        keywords = []
        if "FEMA" in name.upper() or "FEMA" in content.upper():
            keywords.append("FEMA")
        if "CALOES" in name.upper() or "CALOES" in content.upper():
            keywords.append("CalOES")
        if "FIRE" in name.upper() or "FIRE" in content.upper():
            keywords.append("Fire")
        if "DISASTER" in name.upper() or "DISASTER" in content.upper():
            keywords.append("Disaster")
        
        project_type = "capital"
        if keywords:
            project_type = "disaster" # Heuristic
        
        # Also check if name has suffix
        if "(" in name and ("FEMA" in name or "CalOES" in name or "CalJPIA" in name):
            project_type = "disaster"

        projects.append({
            "Project_Name": name,
            "st": st,
            "content_preview": content[:100],
            "type": project_type,
            "filename": doc['filename']
        })

print("__RESULT__:")
print(json.dumps(projects))"""

env_args = {'var_function-call-2498552123289550299': 'file_storage/function-call-2498552123289550299.json', 'var_function-call-4052442815910590834': 'file_storage/function-call-4052442815910590834.json'}

exec(code, env_args)
