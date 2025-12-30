code = """import json
import re

# Load data
with open('var_function-call-16455850891903614580.json', 'r') as f:
    civic_docs = json.load(f)
with open('var_function-call-16455850891903614945.json', 'r') as f:
    funding_records = json.load(f)

# Combine text from all docs (or just use the most comprehensive one)
# The docs seem to be agendas. They might contain duplicate info.
# We'll concatenate them but be careful about multiple matches.
# Actually, the agenda with the most recent date is likely the most accurate.
# Filename format: "malibucity_agenda_MMDDYYYY-ID.txt"
# Let's sort docs by date in filename and use the latest one for status.
def get_date_from_filename(fn):
    # malibucity_agenda_03222023-2060.txt
    match = re.search(r'agenda_(\d{8})', fn)
    if match:
        return match.group(1)
    return "00000000"

civic_docs.sort(key=lambda x: get_date_from_filename(x['filename']), reverse=True)
# Use the text from the latest document primarily, or check all if needed. 
# Let's inspect the text of the latest document to extract project info.
full_text = civic_docs[0]['text']

# Regex to find projects and their info
# Structure seems to be:
# Project Name
# (cid:190) ...
# ...
# (cid:131) Begin Construction: [Date]

# We also need to identify which section they are in ("Capital" or "Disaster").
# We will split the text by these headers.

sections = {
    "Capital": [],
    "Disaster": []
}

# Split text into lines
lines = full_text.split('\n')

current_section = None
current_project = None
project_data = {} # Name -> {section, start_date_str}

# Keywords to identify sections
# "Capital Improvement Projects"
# "Disaster Recovery Projects"
# "Capital Improvement Projects (Design)"
# "Capital Improvement Projects (Construction)"
# "Capital Improvement Projects (Not Started)"

# Regex for start date
# "Begin Construction: <Month> <Year>" or "<Season> <Year>"
date_pattern = re.compile(r'Begin Construction:\s*([A-Za-z0-9\s]+)', re.IGNORECASE)

# Iterate lines
for i, line in enumerate(lines):
    line = line.strip()
    if not line:
        continue
        
    # Detect Section
    if "Disaster Recovery Projects" in line:
        current_section = "Disaster"
        current_project = None
    elif "Capital Improvement Projects" in line:
        current_section = "Capital"
        current_project = None
        
    # Detect Project Name
    # Heuristic: A line that is not a bullet, not a header, and followed by a bullet line (Updates/Description)
    # The bullets in the text are special chars like (cid:190) which might show up as something else or unicode.
    # In the preview: "(cid:190)"
    # Let's look ahead.
    if i + 1 < len(lines):
        next_line = lines[i+1].strip()
        # Check if next line starts with a bullet indicator
        # Common bullet indicators in this text: "(cid:190)", "(cid:131)", or maybe unicode bullets.
        # Looking at preview: "(cid:190)" seems to be the main bullet for sections under a project.
        if next_line.startswith("(cid:190)") or next_line.startswith("Updates:") or next_line.startswith("Project Description:"):
            # This line is likely a project name
            # Exclude known headers
            if "Capital Improvement Projects" not in line and "Disaster Recovery Projects" not in line:
                current_project = line
                if current_project not in project_data:
                    project_data[current_project] = {"section": current_section, "dates": []}
                # If we are in a known section, update it (last wins or first wins?)
                # If we found it in Disaster section, mark as Disaster.
                if current_section:
                    project_data[current_project]["section"] = current_section

    # Extract Date
    if current_project:
        # Check for Begin Construction in this line
        m = date_pattern.search(line)
        if m:
            date_str = m.group(1).strip()
            project_data[current_project]["dates"].append(date_str)

# Also, we need to handle the case where "Disaster" projects are identified by name suffixes in the Funding table,
# even if they are not in the "Disaster" section of the text (though they likely are).

# Helper to normalize names for matching
def normalize(name):
    # Remove suffixes
    name = re.sub(r'\s*\((FEMA|CalOES|CalJPIA|Woolsey).*?\)', '', name, flags=re.IGNORECASE)
    # Remove "Project" if at end? No, "Project" might be part of name.
    return name.strip()

# Calculate Total Funding
total_funding = 0
disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Disaster"]

matched_projects = []

for record in funding_records:
    amt = float(record['Amount'])
    fname = record['Project_Name']
    
    # 1. Is it disaster-related?
    is_disaster = False
    
    # Check suffix/keywords
    if any(k in fname for k in disaster_keywords):
        is_disaster = True
    
    # Check text section
    # We need to match fname to project_data keys
    # Try exact match or normalized match
    norm_fname = normalize(fname)
    
    text_project_info = None
    
    # Try to find in extracted project_data
    # 1. Exact match
    if fname in project_data:
        text_project_info = project_data[fname]
    # 2. Normalized match (extracted keys might also need normalization?)
    # Actually, the text name is usually the base name.
    # So if fname is "X (FEMA)", norm is "X". If text has "X", we match.
    elif norm_fname in project_data:
        text_project_info = project_data[norm_fname]
    else:
        # Try to find a key in project_data that is a substring or vice versa
        # This can be risky.
        pass
        
    if text_project_info:
        if text_project_info['section'] == 'Disaster':
            is_disaster = True
            
    if not is_disaster:
        continue
        
    # 2. Did it start in 2022?
    # We need a start date from the text.
    # If we didn't find the project in text, we can't determine start date (unless it's in the name, which is rare).
    # Default to False if no date found.
    
    if text_project_info:
        dates = text_project_info['dates']
        # Check if any date contains "2022"
        # We specifically look for "Begin Construction: ... 2022"
        # The dates list contains the value after "Begin Construction:"
        started_2022 = False
        for d in dates:
            if "2022" in d:
                started_2022 = True
                break
        
        if started_2022:
            total_funding += amt
            matched_projects.append(fname)
            
print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matched_projects": matched_projects, "project_data_debug": list(project_data.keys())}))"""

env_args = {'var_function-call-16455850891903611214': ['civic_docs'], 'var_function-call-16455850891903614945': 'file_storage/function-call-16455850891903614945.json', 'var_function-call-16455850891903614580': 'file_storage/function-call-16455850891903614580.json'}

exec(code, env_args)
