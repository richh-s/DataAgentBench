code = """import json
import re

# Load the data
with open(locals()['var_function-call-15046969363982349672'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-6734558309770551932'], 'r') as f:
    funding_data = json.load(f)

projects = []

# Regex for bullet points
bullet_re = re.compile(r'^\(cid:\d+\)')

# Iterate over all docs
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    project_buffer = [] # lines belonging to current project
    
    # We need to identify project names. 
    # Heuristic: A line that looks like a title, followed eventually by "(cid:190)" lines.
    
    # Let's iterate and group lines by project
    # Identify indices where a new project likely starts
    
    # Better approach: Iterate line by line.
    # If a line seems to be a project name, start a new project entry.
    # What does a project name look like? 
    # It doesn't start with (cid:...), it's not "Updates:", it's not "Project Schedule:", not "Page ...".
    # And it's usually followed by a block starting with (cid:190).
    
    # Let's try to group the text into chunks starting with a potential title.
    
    idx = 0
    while idx < len(lines):
        line = lines[idx].strip()
        
        # Skip empty lines or page numbers
        if not line or line.startswith("Page ") or line.startswith("Agenda Item") or line == "Capital Improvement Projects (Design)" or line == "Capital Improvement Projects (Construction)" or line == "Capital Improvement Projects (Not Started)":
            idx += 1
            continue
            
        # Check if this line is a start of a project
        # A project name is usually followed by "(cid:190)" lines (Updates or Description)
        # Check ahead a few lines
        is_project_start = False
        for k in range(1, 10): # Look ahead
            if idx + k < len(lines):
                next_line = lines[idx+k].strip()
                if next_line.startswith("(cid:190)"):
                    is_project_start = True
                    break
                if next_line and not next_line.startswith("(cid:190)") and not next_line.startswith("(cid:131)"):
                    # Another text line, maybe the title spans two lines or it's not a title
                    # But usually titles are one line or the update starts immediately.
                    # Let's assume if we hit another text line before a bullet, the first one might not be the title OR title is multi-line.
                    # Simplified: if we find (cid:190) within a few lines, we assume the current line (and maybe intervening) is the title.
                    pass
        
        if is_project_start:
            # This line is likely the project Name
            p_name = line
            # Check if next lines are also part of name (until bullet)
            # Actually, let's just take this line as name for now, or concat if next line is not bullet.
            
            # Extract the block until the next project start
            # But "next project start" is hard to define without context.
            # simpler: consume until we hit a line that triggers `is_project_start` logic again?
            # No, that's recursive.
            
            # Let's just consume lines and associate with this project until we hit a line that looks like a NEW project (i.e. followed by cid:190)
            # OR end of text.
            
            # Start collecting text for this project
            p_text = ""
            current_idx = idx + 1
            while current_idx < len(lines):
                c_line = lines[current_idx].strip()
                
                # Check if c_line is start of new project
                # It must be text (not bullet) and followed by (cid:190)
                is_next_start = False
                if c_line and not c_line.startswith("(cid:") and not c_line.startswith("Page ") and not c_line.startswith("Agenda Item"):
                     # Look ahead for (cid:190)
                    for m in range(1, 10):
                        if current_idx + m < len(lines):
                            nl = lines[current_idx+m].strip()
                            if nl.startswith("(cid:190)"):
                                is_next_start = True
                                break
                            # If we hit another plain line before bullet, maybe it's still part of current text?
                            # This is fuzzy.
                            # Let's verify strict pattern: Project Name \n (cid:190) ...
                
                if is_next_start:
                    break
                
                p_text += "\n" + c_line
                current_idx += 1
            
            projects.append({
                "name": p_name,
                "text": p_text
            })
            idx = current_idx
        else:
            idx += 1

# Filter projects
matched_projects = []
for p in projects:
    name = p['name']
    text = p['text'].lower()
    name_lower = name.lower()
    
    # Check for "park" in name or text (topic)
    # Also check other park keywords? Prompt says "Common topics include: 'park'..."
    # Let's look for 'park' in name OR text.
    is_park = 'park' in name_lower or 'park' in text or 'playground' in text or 'recreation' in text
    
    # Check for completed in 2022
    # Phrases: "completed November 2022", "completed, November 2022", "completed in 2022"
    # Regex for completed + date
    # Status: "completed"
    
    # Let's normalize text for checking completion
    # Look for "completed" ... "2022"
    # But ensure they are close or in the same sentence.
    
    if is_park:
        # Check completion
        # Simple check: "completed" and "2022" in the same update block?
        # The text usually says: "(cid:190) Updates: Construction was completed November 2022"
        # Or "(cid:131) Construction was completed, November 2022"
        
        # Regex to find completion date
        # Pattern: completed.*2022
        if re.search(r'completed.*?2022', text, re.IGNORECASE):
            matched_projects.append(name)
        elif re.search(r'completion.*?2022', text, re.IGNORECASE):
             matched_projects.append(name)

# Normalize names for join
# Names in Funding table might match exactly or need trimming
funding_map = {item['Project_Name']: int(item['Amount']) for item in funding_data}

total_funding = 0
found_projects = []

for mp in matched_projects:
    # Try exact match
    if mp in funding_map:
        total_funding += funding_map[mp]
        found_projects.append(mp)
    else:
        # Try stripping or partial match?
        # The extraction might include trailing chars or might be slightly different.
        # Let's try to find best match?
        # For now, exact match after strip
        mp_clean = mp.strip()
        if mp_clean in funding_map:
            total_funding += funding_map[mp_clean]
            found_projects.append(mp_clean)

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": found_projects}))"""

env_args = {'var_function-call-6734558309770552995': 'file_storage/function-call-6734558309770552995.json', 'var_function-call-6734558309770551932': 'file_storage/function-call-6734558309770551932.json', 'var_function-call-15046969363982349672': 'file_storage/function-call-15046969363982349672.json'}

exec(code, env_args)
