code = """import json
import re
import pandas as pd

# Load previous results
with open(locals()['var_function-call-4190880947126154290'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-2571507213258603600'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)

# Regex for Spring 2022
spring_2022_regex = re.compile(r'(Spring|March|April|May|Mar|Apr)\s*,?\s*2022', re.IGNORECASE)

found_projects = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this line is a project name
        # Heuristic: The next line starts with (cid:190) or similar marker
        # Looking at preview: "(cid:190) Updates:"
        # Also handling potential variations if any.
        
        is_project_header = False
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if next_line.startswith("(cid:190)") or next_line.startswith("Updates:") or next_line.startswith("Project Description:"):
                # But wait, sometimes there are blank lines.
                # In the preview: 
                # "2022 Morning View Resurfacing & Storm Drain Improvements"
                # ""
                # "(cid:190) Updates:"
                # So I should look ahead skipping blank lines.
                pass

    # Revised loop with index
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Determine if 'line' is a project name
        # Look ahead for "(cid:190)" or markers
        # The marker might be separated by empty lines
        j = i + 1
        is_proj = False
        while j < len(lines) and j < i + 5: # Look ahead a few lines
            nl = lines[j].strip()
            if not nl:
                j += 1
                continue
            if nl.startswith("(cid:190)") or "Updates:" in nl or "Project Description:" in nl:
                # Use a stronger check: usually "(cid:190)" is the bullet
                if "(cid:190)" in nl:
                    is_proj = True
                break
            else:
                # If we hit another text line that doesn't look like a marker, then the previous line wasn't a header?
                # Or maybe the marker is missing.
                # Let's rely on "(cid:190)" as it seems consistent in the preview.
                break
        
        if is_proj:
            current_project = line
            #print(f"DEBUG: Found Project: {current_project}")
            
            # Now scan for start date until next project
            # actually we continue the main loop, but we carry 'current_project' state
            # processing the block
            
            # We can scan the block here or just let the main loop continue and check lines
            # If we let the main loop continue, we need to know when the project block ends.
            # It ends when a new project starts.
            
            # Let's scan the block associated with this project immediately to avoid state confusion
            # The block ends at the next project header or end of file.
            # But finding the next header is the same logic.
            
            # So, simpler approach:
            # When a project is found, set it as 'current_project'
            # Check every line for dates if 'current_project' is set.
            pass
        
        if current_project:
            # Check for start date patterns
            # Pattern: "Begin Construction: <Date>"
            # Pattern: "Construction Start: <Date>"
            # Pattern: "Start: <Date>"
            
            # Normalize line
            l_lower = line.lower()
            
            # We are looking for "Begin Construction" or similar
            if "begin construction" in l_lower or "construction start" in l_lower or "construction began" in l_lower or "construction commenced" in l_lower:
                # Check if Spring 2022 is in this line
                if spring_2022_regex.search(line):
                    found_projects.add(current_project)
                    #print(f"DEBUG: Match Spring 2022 for {current_project}: {line}")
            
            # Also check for "Advertise" or "Design" if needed? No, question asks for "started".
            # Usually "started" == construction start for civic projects unless "design started".
            # But typically "project started" implies the main phase. 
            # Given the context of "Capital Improvement Projects", "Started" usually means Construction.
            # If the user meant "Design started", they would specify.
            # Also, "Projects started in Spring 2022" could mean the project *initiated* (Design).
            # Let's check the hints.
            # Hints: "Projects have three statuses: design, completed, not started".
            # Fields: "st: Start time/date".
            # If a project status is "design", its "start time" is when design started.
            # If "completed", start time is when it started (probably construction or design?).
            # Let's look for *any* start date that matches Spring 2022.
            # "Begin Construction: Spring 2022" is a strong signal.
            # "Design Start: Spring 2022" is also a start.
            
            # However, looking at the text:
            # "(cid:131) Complete Design: Summer 2023"
            # It doesn't list "Begin Design".
            # It lists "Advertise" (bidding).
            # "Begin Construction" is the most prominent start date.
            # I will assume "Started" means "Begin Construction" for construction projects.
            # But what if it's a "Design" project?
            # The text groups them: "Capital Improvement Projects (Design)".
            # These are in design phase.
            # If a project is in Design, did it "start"? Yes.
            # But usually the "Begin Construction" is the date listed.
            # If it's in Design, does it have a "Begin Design" date?
            # The preview shows: "(cid:131) Complete Design: ...". No "Begin Design".
            # Maybe "Advertise" is the start of the procurement for construction?
            
            # Let's stick to "Begin Construction" as the primary "Start" milestone for the physical project. 
            # If the question meant "Project Inception", it's harder to find.
            # "How many projects started..." usually refers to implementation.
            
            # Wait, let's look for any date labeled "Start" or "Begin".
            if "begin" in l_lower or "start" in l_lower:
                if spring_2022_regex.search(line):
                    found_projects.add(current_project)
                    #print(f"DEBUG: General Start Match for {current_project}: {line}")

        i += 1

# Clean project names
# Sometimes the extracted line has extra noise or is just the name.
# In the preview, names are clean: "2022 Morning View Resurfacing & Storm Drain Improvements"
# "PCH Median Improvements Project"
# But I should strip them.
cleaned_projects = {p.strip() for p in found_projects}

# Now filter funding
# The Project_Name in Funding might slightly differ (case, spacing).
# Let's normalize both sides (lowercase, strip).
funding_df['Project_Name_Clean'] = funding_df['Project_Name'].str.strip().str.lower()
cleaned_projects_lower = {p.lower() for p in cleaned_projects}

matched_funding = funding_df[funding_df['Project_Name_Clean'].isin(cleaned_projects_lower)]

# Calculate
count = len(matched_funding)
total_amount = matched_funding['Amount'].astype(float).sum()

print("__RESULT__:")
print(json.dumps({"count": count, "total_funding": total_amount, "projects": list(matched_funding['Project_Name'].unique())}))"""

env_args = {'var_function-call-2571507213258604103': ['civic_docs'], 'var_function-call-2571507213258603600': 'file_storage/function-call-2571507213258603600.json', 'var_function-call-4959924631149924151': 'file_storage/function-call-4959924631149924151.json', 'var_function-call-4190880947126154290': 'file_storage/function-call-4190880947126154290.json'}

exec(code, env_args)
