code = """import json
import re

# Load funding data
with open(locals()['var_function-call-10318342191074584213'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-9654609134184919281'], 'r') as f:
    civic_docs = json.load(f)

# Filter funding for > 50,000
# Amount is string in preview, need to convert to int/float
high_funding_projects = {}
for item in funding_data:
    try:
        amount = float(item['Amount'])
        if amount > 50000:
            high_funding_projects[item['Project_Name']] = amount
    except ValueError:
        continue

capital_design_projects = set()

# Regex to find the Capital Design section
# We look for "Capital Improvement Projects (Design)" and capture until the next "Capital Improvement Projects (...)" or similar major header
# Based on preview, the next one is "Capital Improvement Projects (Construction)"
# There might be others.
# We can try to capture everything between "Capital Improvement Projects (Design)" and "Capital Improvement Projects (Construction)" or "Disaster Recovery Projects"
# or end of string if nothing else matches.

for doc in civic_docs:
    text = doc['text']
    
    # Locate start
    start_match = re.search(r'Capital Improvement Projects\s*\(\s*Design\s*\)', text, re.IGNORECASE)
    if not start_match:
        continue
    
    start_idx = start_match.end()
    
    # Locate end - look for next section header
    # Common headers in this structure seem to be "Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"
    # Or just the end.
    
    # Let's find the closest next header
    next_headers = [
        r'Capital Improvement Projects\s*\(\s*Construction\s*\)',
        r'Capital Improvement Projects\s*\(\s*Not Started\s*\)',
        r'Disaster Recovery Projects'
    ]
    
    end_idx = len(text)
    for header in next_headers:
        match = re.search(header, text[start_idx:], re.IGNORECASE)
        if match:
            # We want the earliest match
            current_end = start_idx + match.start()
            if current_end < end_idx:
                end_idx = current_end
                
    section_text = text[start_idx:end_idx]
    
    # Now parse projects from section_text
    # Projects seem to be separated by bullet points (cid:190) which are often represented as specific characters or just text.
    # In the preview JSON it was `(cid:190)`.
    # Let's assume the text in JSON has `(cid:190)` literal or the character.
    # The preview showed `(cid:190)`.
    
    # Split by `(cid:190)`
    # The project name should be at the end of the *previous* segment.
    # The first segment contains the first project name at its end.
    
    segments = section_text.split('(cid:190)')
    
    # The first segment (index 0) contains the first project name at the end.
    # Subsequent segments contain details. If a segment ends with text that doesn't look like a detail key (like "Updates:", "Schedule:"), it might be the start of next project?
    # Actually, the structure is:
    # Project Name
    # (cid:190) Updates: ...
    # (cid:190) Schedule: ...
    # 
    # Next Project Name
    # (cid:190) Updates: ...
    
    # So, `(cid:190)` starts a detail block.
    # If we split by `(cid:190)`, we get:
    # [ "Project 1 Name \n\n", " Updates: ... \n\n Project 2 Name \n\n", " Updates: ..." ]
    
    # So for segment `i`, the text *after* the last newline (or clean up) is likely the part of the previous detail, 
    # and the text *before* the first newline might be the key (Updates).
    # Wait, the project name is in the *preceding* chunk of the split.
    
    # Let's process segment 0. It should end with Project 1 Name.
    # Segment 1 starts with "Updates" (or similar) and ends with Project 2 Name.
    # ...
    # The last segment just ends with details.
    
    # Helper to clean and extract the last non-empty lines
    def extract_last_lines(s):
        lines = [line.strip() for line in s.split('\n') if line.strip()]
        if not lines:
            return None
        # The project name is usually the last line, or maybe last 2 if wrapped? 
        # Most project names in preview are 1 line.
        # But we need to be careful about page numbers or noise.
        # "Page 1 of 6"
        # "Agenda Item # 4.B."
        
        # Filter out noise lines
        clean_lines = []
        for line in reversed(lines):
            if "Page" in line and "of" in line: continue
            if "Agenda Item" in line: continue
            if "updates" in line.lower(): continue # Should be in next block usually
            clean_lines.append(line)
            if len(clean_lines) >= 1: break # Assume 1 line for now
            
        if clean_lines:
            return clean_lines[0] # Return the last valid line
        return None

    # First project name is in segments[0]
    p_name = extract_last_lines(segments[0])
    if p_name:
        capital_design_projects.add(p_name)
        
    # Other project names are at the end of segments[1:-1]
    for seg in segments[1:-1]:
        # The segment starts with the bullet content (e.g. " Updates: ...")
        # And ends with the next project name.
        p_name = extract_last_lines(seg)
        if p_name:
            capital_design_projects.add(p_name)

# Now compare with funding
count = 0
matches = []
for proj in capital_design_projects:
    # Try exact match first
    if proj in high_funding_projects:
        count += 1
        matches.append((proj, high_funding_projects[proj]))
    else:
        # Try stripping special chars or whitespace
        # Or simple fuzzy match? The prompt implies matching names.
        # Let's check if the project name from text is contained in DB name or vice versa?
        # "The Project_Name in the Funding SQLite table matches the project names that can be extracted"
        # This suggests they should match.
        pass

print("__RESULT__:")
print(json.dumps({"count": count, "matches": matches, "extracted_projects": list(capital_design_projects)}))"""

env_args = {'var_function-call-10318342191074584213': 'file_storage/function-call-10318342191074584213.json', 'var_function-call-9654609134184919281': 'file_storage/function-call-9654609134184919281.json'}

exec(code, env_args)
