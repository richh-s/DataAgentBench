code = """import json
import re

# Load funding names
with open(locals()['var_function-call-8803859908455603463'], 'r') as f:
    funding_data = json.load(f)

# Create a set of valid names for exact matching
valid_names = set(item['Project_Name'] for item in funding_data)

# Load civic docs
with open(locals()['var_function-call-8587075472335102739'], 'r') as f:
    docs = json.load(f)

identified_projects = []

for doc in docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_name = None
    buffer_lines = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        if "(cid:190)" in line:
            # Found a section start. The name is likely in buffer_lines.
            # Look backwards in buffer_lines for the name.
            # Name is likely the last non-empty line(s) before this marker.
            # But we might have accumulated a lot of text from previous section.
            
            # Heuristic: The name is usually 1-2 lines, Title Case, not starting with bullets.
            # And it appears after some empty space or previous section end.
            
            # Let's look at the last few lines of buffer.
            # Clean buffer: remove 'Page', 'Agenda' lines.
            
            candidates = []
            # We take the last 3 lines from buffer
            slice_lines = buffer_lines[-5:] if len(buffer_lines) > 5 else buffer_lines
            
            # Filter noise
            valid_slice = []
            for l in slice_lines:
                if "Agenda" in l or "Page " in l or "Public Works" in l or "Capital Improvement" in l:
                    continue
                valid_slice.append(l)
            
            # Join them? Or take the last one? Project names can be multi-line?
            # Usually single line in the preview.
            # "2022 Morning View Resurfacing & Storm Drain Improvements" -> 1 line.
            
            if valid_slice:
                # Try to match with valid_names
                # Try exact match of last line, or last 2 lines joined.
                candidate1 = valid_slice[-1]
                candidate2 = " ".join(valid_slice[-2:]) if len(valid_slice) >= 2 else ""
                
                found_name = None
                if candidate1 in valid_names:
                    found_name = candidate1
                elif candidate2 in valid_names:
                    found_name = candidate2
                else:
                    # If not in valid_names, maybe it's a new project or name mismatch.
                    # Assume it is the name if it looks like one.
                    # But if we rely on valid_names, we might miss some if text is slightly different.
                    # Let's assume candidate1 is the name.
                    found_name = candidate1
                
                # If we found a name different from current_name, we switch project.
                # Note: valid_slice[-1] might be just part of the previous section if we didn't detect end properly.
                # But headers usually stand out.
                
                # If valid_names check failed, we might be inside a project reading a sub-header?
                # But (cid:190) only starts sections like Updates, Schedule.
                # So every (cid:190) must belong to a project.
                # If we just switched to a new (cid:190) block and the text before it looks like a Title, it's a new project.
                # How to distinguish "Text from previous section" from "New Title"?
                # Previous section text is usually indented or bulleted. Titles are not.
                
                if found_name:
                    # Update current project
                    # If it's a new name, store the old one?
                    # We are storing on the fly.
                    # Wait, we need to associate the UPCOMING text (and date) with this name.
                    current_name = found_name
            
            # Reset buffer? No, we might be inside the project and buffer accumulates text?
            # Actually, once we hit (cid:190), we are entering a section.
            # We should parse the date from THIS line and subsequent lines.
            
            # We need to know which project we are in.
            # If we detected a new name, we are in that project.
            # If we didn't detect a name (e.g. valid_slice was empty or noise), we continue with previous name.
            
            buffer_lines = [] # Cleared because we processed the "header" candidates.
            
            # Now check for date in the current line (which contains (cid:190)) and following.
            # Actually, the line itself is usually just header "(cid:190) Updates:".
            # The content follows.
            
        else:
            buffer_lines.append(line)
            # Also, if we have a current_name, check this line for Dates.
            if current_name:
                # Check for "Begin Construction", etc.
                l_lower = line.lower()
                
                # Date parsing logic
                is_spring_2022 = False
                if 'spring 2022' in l_lower or 'march 2022' in l_lower or 'april 2022' in l_lower or 'may 2022' in l_lower:
                    is_spring_2022 = True
                
                if is_spring_2022:
                    # Check context
                    if 'begin construction' in l_lower or 'start' in l_lower or 'commence' in l_lower:
                        identified_projects.append(current_name)
                    # Handle "Advertise" if needed?
                    # "Advertise: Spring 2022" -> Project "starts" active phase?
                    # Let's include "Advertise" if it's the only thing? 
                    # But prompt says "projects started". Usually means start of work.
                    # I'll stick to "Begin Construction" or "Start".
                    # What if "Complete Design: Spring 2022"? That means it started design earlier.
                    # What if "Start Design: Spring 2022"?
                    if 'design' in l_lower and ('start' in l_lower or 'begin' in l_lower):
                         # "Begin Design: Spring 2022"
                         identified_projects.append(current_name)

# Deduplicate
unique_projects = list(set(identified_projects))

print("__RESULT__:")
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-6062983773300407174': ['civic_docs'], 'var_function-call-8587075472335102739': 'file_storage/function-call-8587075472335102739.json', 'var_function-call-4603789047444994898': ['Funding'], 'var_function-call-8803859908455603463': 'file_storage/function-call-8803859908455603463.json'}

exec(code, env_args)
