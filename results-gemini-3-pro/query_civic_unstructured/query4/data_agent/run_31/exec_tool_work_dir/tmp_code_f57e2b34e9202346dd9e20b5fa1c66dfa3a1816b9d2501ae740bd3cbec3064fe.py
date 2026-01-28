code = """import json
import re

# Load civic docs
with open(locals()['var_function-call-8587075472335102739'], 'r') as f:
    docs = json.load(f)

projects = []

def parse_date_season(date_str):
    date_str = date_str.lower().strip()
    if 'spring 2022' in date_str: return True
    if 'march 2022' in date_str or 'mar 2022' in date_str: return True
    if 'april 2022' in date_str or 'apr 2022' in date_str: return True
    if 'may 2022' in date_str: return True
    # check for month-year like 03-2022
    if re.search(r'(03|04|05)[-/]2022', date_str): return True
    return False

for doc in docs:
    text = doc['text']
    # Split by project blocks
    # A project usually starts with a name and then has (cid:190) Updates or Description
    # We can split by "(cid:190)" and look at the preceding lines for the name
    
    # Strategy: Find indices of "(cid:190)"
    # The lines before the first "(cid:190)" of a block is the title.
    # The block continues until the next title.
    
    # Better: Split by double newlines or clear headers?
    # Let's iterate line by line to build a state machine.
    
    lines = text.split('\n')
    current_project = {}
    current_buffer = [] # lines potentially containing project name
    
    # We need to capture the project name.
    # Pattern:
    # [Empty Lines]
    # Project Name (1-2 lines)
    # (cid:190) ...
    
    # Or Project Name
    # (cid:190) ...
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        if '(cid:190)' in line:
            # This line starts a section (Updates, Description, Schedule)
            # The previous lines in buffer (if any) might be the project name
            # But we might be already inside a project.
            
            # If current_project has no name, the buffer is the name
            if 'name' not in current_project:
                # Clean buffer
                # Filter out "Capital Improvement Projects..." headers if they are in buffer
                clean_buffer = [b for b in current_buffer if "Capital Improvement Projects" not in b and "Agenda" not in b and "Page " not in b]
                if clean_buffer:
                    name = " ".join(clean_buffer).strip()
                    current_project['name'] = name
                current_buffer = [] # reset buffer
            
            # Now identify the section
            section_type = "unknown"
            if "Updates" in line: section_type = "updates"
            elif "Schedule" in line: section_type = "schedule"
            elif "Description" in line: section_type = "description"
            
            # We are in a section. We need to read lines until the next header or empty block or next (cid:190)
            # Actually, just parse the line itself if it has content, and subsequent lines until next (cid:190)
            
            # If it is a Schedule section, look for Start/Begin
            if section_type == "schedule" or section_type == "updates": # Sometimes dates are in updates
                 # We need to continue reading lines until next (cid:190) or new project
                 pass
        
        else:
            # Not a section header
            # Could be content of a section, or a new project name
            # If we are effectively parsing a project, how do we know if we switched to a new one?
            # Usually new project name appears after a block of text, often separated by newlines.
            
            # Heuristic: If we hit a line that looks like a name (not starting with (cid:131) or bullet), add to buffer.
            # But if we already have a project name and we are processing sections, lines are content.
            # Wait, how to detect end of project?
            # End of project is usually followed by a new Project Name line, then (cid:190).
            
            pass
            
    # Let's try a regex approach to separate projects.
    # Projects seem to be chunks of text separated by headers or just spacing.
    # But "(cid:190)" is the key marker.
    # Find all occurrences of "(cid:190)" lines.
    # Group them by proximity?
    
    # Alternative:
    # 1. Find all lines with "(cid:190)".
    # 2. Group consecutive "(cid:190)" blocks into one project.
    # 3. The name is the text immediately preceding the first "(cid:190)" of the group.
    
    # Let's implement this.
    
    blocks = []
    # Find line indices with (cid:190)
    marker_indices = [idx for idx, l in enumerate(lines) if '(cid:190)' in l]
    
    if not marker_indices:
        continue
        
    # Group indices. If idx[j] - idx[j-1] is large, maybe different project?
    # No, a project can have long updates.
    # But a new project name must appear between them.
    # If the text between marker_indices[j-1] and marker_indices[j] contains a likely Title (short lines, no bullets), then it's a split.
    
    # Let's try to extract (Name, TextBlock) tuples.
    
    # Pass 1: Identify Project Starts.
    # A project start is identified by a name line followed shortly by a "(cid:190)" line.
    
    # Iterate lines. Keep a buffer of potential title lines.
    # When hitting "(cid:190)", the buffer becomes the title.
    # Then consume lines until a new Title is detected.
    # What defines a new Title?
    # - Non-empty
    # - Not starting with (cid:131)
    # - Not starting with Page, Agenda
    # - followed by (cid:190) eventually?
    
    # Let's try splitting by regex `(?=\n.*?\(cid:190\))` ? No, complex.
    
    # Let's simple iterate.
    potential_title_lines = []
    curr_proj_name = None
    curr_proj_text = ""
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
            
        if "(cid:190)" in stripped:
            if curr_proj_name is None:
                # We found the first section of a project.
                # The potential_title_lines must contain the name.
                # Filter noise
                valid_title_lines = [l for l in potential_title_lines if "Agenda" not in l and "Page" not in l and "Capital Improvement" not in l and "Public Works" not in l]
                if valid_title_lines:
                    curr_proj_name = " ".join(valid_title_lines).strip()
                else:
                    curr_proj_name = "Unknown Project"
                
                curr_proj_text += line + "\n"
                potential_title_lines = []
            else:
                # We are already in a project, and this is another section (e.g. Schedule after Updates)
                # Check if we should switch projects.
                # If potential_title_lines contains a likely name (non-empty), it might be a new project.
                # But inside a project, there are no "titles" between sections.
                # So if potential_title_lines is NOT empty, it implies there was text between the last section and this one that looks like a title?
                # But sections follow each other.
                # If there are lines between the last section content and this new (cid:190) line, were they content or a new title?
                
                # Heuristic: Section content usually starts with (cid:131) or has indentation.
                # Titles don't.
                
                # Check lines in potential_title_lines.
                # If they look like bullets `(cid:131)` or continuation, append to current text.
                # If they look like a standalone title (no bullets, shortish), start new project.
                
                is_new_project = False
                title_candidates = []
                content_candidates = []
                
                for pt in potential_title_lines:
                    if "(cid:131)" in pt or pt.startswith("Page") or pt.startswith("Agenda"):
                        content_candidates.append(pt)
                    else:
                        title_candidates.append(pt)
                
                # If we have title candidates that look legit (not just page numbers), assume new project
                # Refine: Titles are usually capitalized, short.
                real_titles = [t for t in title_candidates if len(t) > 3 and "Agenda" not in t]
                
                if real_titles:
                    # New Project
                    # Save old project
                    projects.append({'name': curr_proj_name, 'text': curr_proj_text})
                    
                    curr_proj_name = " ".join(real_titles).strip()
                    curr_proj_text = line + "\n" # Start text with current section header
                    potential_title_lines = []
                else:
                    # Continuation
                    curr_proj_text += "\n".join(potential_title_lines) + "\n" + line + "\n"
                    potential_title_lines = []
                    
        else:
            # Not a section start.
            # Add to potential_title_lines buffer.
            # But wait, if we are in a project, this line is likely content of the *current* section.
            # Unless it's the start of a new project (which we verify when we hit the *next* (cid:190)).
            potential_title_lines.append(stripped)
            
    # End of loop, save last project
    if curr_proj_name:
        projects.append({'name': curr_proj_name, 'text': curr_proj_text})

# Now extract dates from projects
results = []
for p in projects:
    name = p['name']
    text = p['text']
    
    # Look for "Begin Construction: <Date>" or "Start: <Date>"
    # Also "Advertise" might be relevant? No, "Started" usually implies construction or main phase.
    # The prompt asks "started in Spring 2022".
    # I will check for "Begin Construction", "Start Construction", "Construction Start".
    # If not found, look for general "Spring 2022" mentioned in Schedule.
    
    # Regex for start date
    # (cid:131) Begin Construction: Fall 2023
    start_match = re.search(r'(Begin Construction|Start Construction|Construction Start|Begin|Start)\s*[:\-]?\s*(.*)', text, re.IGNORECASE)
    
    # We might have multiple matches (lines). We want the one in the Schedule section?
    # Or just iterate all matches.
    
    matches = re.findall(r'(Begin Construction|Start Construction|Construction Start|Begin|Start)\s*[:\-]?\s*([A-Za-z0-9, ]+)', text, re.IGNORECASE)
    
    is_spring_2022 = False
    
    for label, date_str in matches:
        if parse_date_season(date_str):
            is_spring_2022 = True
            break
            
    if is_spring_2022:
        results.append(name)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-6062983773300407174': ['civic_docs'], 'var_function-call-8587075472335102739': 'file_storage/function-call-8587075472335102739.json', 'var_function-call-4603789047444994898': ['Funding'], 'var_function-call-8803859908455603463': 'file_storage/function-call-8803859908455603463.json'}

exec(code, env_args)
