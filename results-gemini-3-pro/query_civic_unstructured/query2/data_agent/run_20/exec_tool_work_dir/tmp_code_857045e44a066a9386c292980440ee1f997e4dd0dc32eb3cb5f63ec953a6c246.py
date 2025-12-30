code = """import json
import re

# Load data
with open(locals()['var_function-call-11529138748773800259'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-6363168235283738913'], 'r') as f:
    funding_data = json.load(f)

# Create a lookup for funding
funding_lookup = {item['Project_Name'].strip(): float(item['Amount']) for item in funding_data}

matched_projects = []
debug_info = []

for doc in civic_docs:
    text = doc['text']
    # The text uses (cid:190) as a bullet for sections like Updates, Project Schedule.
    # We can split by this bullet to find chunks.
    # The Project Name is usually the last non-empty line before the FIRST bullet of a block.
    
    # Let's find all indices of the bullet
    bullet = "(cid:190)"
    parts = text.split(bullet)
    
    # parts[0] contains the first project name at the end.
    # parts[1] is the content for the first bullet (e.g. Updates).
    # parts[2] might be another bullet for the same project (e.g. Schedule) OR the start of a new project?
    # Wait, "Project Schedule" is also a bullet.
    # So a project has multiple bullets.
    # How do we know when a new project starts?
    # New project starts when we see a line that is NOT a bullet content.
    # Actually, the text structure in the preview:
    # Project Name
    # (cid:190) Updates: ...
    # (cid:190) Project Schedule: ...
    #
    # Next Project Name
    # (cid:190) Updates: ...
    
    # So between parts[i] and parts[i+1], there might be a project name if parts[i+1] starts a new project block.
    # But parts[i] ends with the content of the previous bullet.
    # Then there is some text (the new project name) then the next bullet (start of parts[i+1]).
    
    # So, for each part (starting from 1), the text BEFORE it (which is the end of previous part) contains the header.
    # BUT, if the previous part was just another bullet of the SAME project, the text between them is just newline or empty.
    
    # We need to distinguish between "End of bullet content -> New Project Name -> Next Bullet" 
    # and "End of bullet content -> Next Bullet (Same Project)".
    
    # Heuristic: If the text between bullets is just whitespace, it's the same project.
    # If there is text, that text is the new project name.
    
    # Exception: The very first project name is at the end of parts[0].
    
    # Let's iterate and group content by project.
    
    current_project = None
    if parts[0].strip():
        lines = parts[0].strip().split('\n')
        # Filter "Capital Improvement Projects..." headers
        lines = [l for l in lines if "Capital Improvement Projects" not in l and "Agenda Item" not in l and "Page" not in l]
        if lines:
            current_project = lines[-1].strip()
    
    projects_found = {} # Name -> combined text
    
    for i in range(1, len(parts)):
        # content of the current bullet
        # The split removed the bullet.
        # We check what 'type' of bullet it is (Updates, Schedule, etc)
        # matches " Updates:" or " Project Schedule:"
        
        # Identify the content and the trailing text which might be the next project name
        # The split consumes the bullet, so parts[i] starts with " Updates:..." or " Project Schedule:..."
        # But wait, if we split by bullet, the separator is gone.
        
        # We need to find where the NEXT bullet would have been.
        # Actually, let's look at the structure of parts[i].
        # It contains the text of the bullet point, AND potentially the name of the NEXT project at the end.
        
        chunk = parts[i]
        
        # Logic: The chunk continues until the next bullet.
        # But since we split by bullet, `chunk` IS the text between bullets.
        # It includes the content of the current bullet, and any text before the next bullet.
        # If there is a new project, it will be at the end of `chunk`.
        
        # Let's separate the "bullet content" from the "next project name".
        # We can look for double newlines or significant separation.
        # Or we can assume the Project Name is the last line.
        
        lines = chunk.strip().split('\n')
        # Clean lines
        lines = [l.strip() for l in lines if l.strip()]
        
        # If lines is empty, unlikely.
        
        # The start of the chunk tells us what section it is.
        # e.g. " Updates: ..."
        
        # We assign this chunk to the current_project.
        if current_project:
            if current_project not in projects_found:
                projects_found[current_project] = ""
            projects_found[current_project] += " " + chunk
            
        # Now determine if there is a next project name at the end.
        # How to distinguish "content" from "next header"?
        # Headers are usually capitalized words, no punctuation at end (except maybe parens).
        # And usually "Agenda Item" or "Page X of Y" appear between projects.
        
        # Let's look at the last few lines.
        # If we see "Agenda Item" or "Page", ignore them.
        
        candidate_next_project = None
        
        # Iterate backwards
        for line in reversed(lines):
            if "Agenda Item" in line or "Page " in line or "Capital Improvement Projects" in line:
                continue
            # If it's a date or "Updates:", it's part of content.
            if line.startswith("Updates:") or line.startswith("Project Schedule:") or line.startswith("Complete Design:") or line.startswith("Begin Construction:"):
                # Matches content, so no new project name here.
                break
                
            # If it looks like a project name (not a sentence, title case-ish)
            # This is heuristic.
            candidate_next_project = line
            break
            
        if candidate_next_project:
            # Check if this line is actually part of the content.
            # If the chunk was "Updates: ... construction completed November 2022", then "November 2022" is not a project name.
            # But the logic above split by bullet.
            # The bullet is `(cid:190)`.
            # So: `(cid:190) Updates: ... \n\n Next Project \n\n (cid:190)`
            # The split gives: `Updates: ... \n\n Next Project \n\n`
            # So the last line IS "Next Project".
            # Unless the content ends with a newline and no text?
            
            # Let's verify if candidate_next_project is likely a name.
            # If it contains "2022" or "2023" and is short, it might be a date? No, "2022 Annual Street Maintenance" is a name.
            # If it ends with punctuation like "." it's likely a sentence.
            if candidate_next_project.endswith('.'):
                pass # Sentence
            else:
                # Likely a project name
                current_project = candidate_next_project

    # Now we have a list of projects and their text.
    # Filter and check status.
    
    for proj_name, content in projects_found.items():
        # Check topic
        is_park = "park" in proj_name.lower()
        if not is_park:
            # Check for specific park names from funding DB if name match fails
            # But query asks for "park-related".
            # "Skate Park" matches. "Bluffs Park" matches.
            pass
            
        # Check completion in 2022
        # Look for "completed <Month> 2022" or "completed, <Month> 2022" in content
        # Or "Construction was completed <Month> 2022"
        # Content might be messy.
        
        is_completed_2022 = False
        if "2022" in content:
            # Regex for "completed ... 2022"
            # We want to avoid "Design completed 2022" if we want "Project completed".
            # The prompt says "completed in 2022". Usually means construction.
            # Text says: "Construction was completed November 2022"
            
            # Regex: `Construction (was )?completed,? \w+ 2022`
            if re.search(r'Construction (was )?completed,? [A-Za-z]+ 2022', content, re.IGNORECASE):
                is_completed_2022 = True
            elif re.search(r'Complete Construction: [A-Za-z]+ 2022', content, re.IGNORECASE):
                is_completed_2022 = True
            # Also check for date like "11/2022" if any?
            
        if is_park and is_completed_2022:
            matched_projects.append(proj_name)
            debug_info.append({"name": proj_name, "content_snippet": content[:100]})

# deduplicate matched projects
matched_projects = list(set(matched_projects))

# Calculate total funding
total_funding = 0
found_funding_projects = []

for proj in matched_projects:
    # Try exact match
    if proj in funding_lookup:
        total_funding += funding_lookup[proj]
        found_funding_projects.append(proj)
    else:
        # Try fuzzy match?
        # Maybe "Project Name (CalOES)" vs "Project Name"
        # The prompt says "Project names can be joined...".
        # Let's try to find if the project name is a substring of the funding name or vice versa.
        # Or check if any funding name starts with proj
        for f_name in funding_lookup:
            if f_name == proj: # Already checked
                continue
            # Check if one is contained in another
            if proj in f_name or f_name in proj:
                # We need to be careful. "Phase 1" vs "Phase 2".
                # "Bluffs Park Shade Structure"
                # If parsed name is "Bluffs Park Shade Structure", it matches.
                pass

print('__RESULT__:')
print(json.dumps({"matches": matched_projects, "total_funding": total_funding, "debug": debug_info}))"""

env_args = {'var_function-call-9104980258508522346': ['Funding'], 'var_function-call-9104980258508522899': ['civic_docs'], 'var_function-call-6363168235283738913': 'file_storage/function-call-6363168235283738913.json', 'var_function-call-6363168235283742026': 'file_storage/function-call-6363168235283742026.json', 'var_function-call-11529138748773800259': 'file_storage/function-call-11529138748773800259.json'}

exec(code, env_args)
