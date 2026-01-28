code = """import json
import re

# Load data
with open('var_function-call-16455850891903614580.json', 'r') as f:
    civic_docs = json.load(f)
with open('var_function-call-16455850891903614945.json', 'r') as f:
    funding_records = json.load(f)

# Sort docs by filename date
def get_date_from_filename(fn):
    match = re.search(r'agenda_(\d{8})', fn)
    if match:
        return match.group(1)
    return "00000000"

civic_docs.sort(key=lambda x: get_date_from_filename(x['filename']), reverse=True)
full_text = civic_docs[0]['text']

lines = full_text.split('\n')

project_data = {} # Name -> {section, start_dates: []}
current_section = "Unknown"
current_project = None

# Regex patterns
date_pattern = re.compile(r'Begin Construction:\s*(.*)', re.IGNORECASE)

for i, line in enumerate(lines):
    line_strip = line.strip()
    if not line_strip:
        continue
        
    # Section Detection
    if "Disaster Recovery Projects" in line_strip:
        current_section = "Disaster"
        current_project = None
        continue
    elif "Capital Improvement Projects" in line_strip:
        current_section = "Capital"
        current_project = None
        continue
        
    # Project Name Detection
    # Look ahead for a bullet line
    if i + 1 < len(lines):
        next_line = lines[i+1].strip()
        # The bullets in the preview were (cid:190).
        if next_line.startswith("(cid:190)") or next_line.startswith("Updates:"):
            # Exclude headers being mistaken as projects
            if "Projects" not in line_strip:
                current_project = line_strip
                if current_project not in project_data:
                    project_data[current_project] = {"section": current_section, "start_dates": []}
                # Update section if we are in a known one
                if current_section != "Unknown":
                    project_data[current_project]["section"] = current_section
    
    # Date Extraction
    if current_project:
        m = date_pattern.search(line_strip)
        if m:
            date_val = m.group(1).strip()
            project_data[current_project]["start_dates"].append(date_val)

# Normalization helper
def normalize(name):
    # Remove suffixes like (FEMA Project), (CalOES Project), etc.
    name = re.sub(r'\s*\(.*?\)$', '', name)
    return name.strip()

disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Disaster"]
total_funding = 0
matched_log = []

for record in funding_records:
    amt = record['Amount']
    # Handle amount if it's string
    if isinstance(amt, str):
        amt = float(amt)
        
    fname = record['Project_Name']
    
    # Check if Disaster Related
    is_disaster_name = any(k in fname for k in disaster_keywords)
    
    # Find in Text Data
    norm_fname = normalize(fname)
    
    # Match logic
    found_info = None
    if fname in project_data:
        found_info = project_data[fname]
    elif norm_fname in project_data:
        found_info = project_data[norm_fname]
    else:
        # Try simple matching
        for p_name in project_data:
            if norm_fname == normalize(p_name):
                found_info = project_data[p_name]
                break
    
    is_disaster_section = False
    if found_info and found_info['section'] == 'Disaster':
        is_disaster_section = True
        
    if not (is_disaster_name or is_disaster_section):
        continue
        
    # Check Start Date 2022
    started_2022 = False
    if found_info:
        for d in found_info['start_dates']:
            if "2022" in d:
                started_2022 = True
                break
    
    # If not found in text, we can't confirm start date, so we skip unless we assume something.
    # The prompt implies we need to read docs to get dates.
    
    if started_2022:
        total_funding += amt
        matched_log.append(fname)

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matched_projects": matched_log, "project_data_keys": list(project_data.keys())}))"""

env_args = {'var_function-call-16455850891903611214': ['civic_docs'], 'var_function-call-16455850891903614945': 'file_storage/function-call-16455850891903614945.json', 'var_function-call-16455850891903614580': 'file_storage/function-call-16455850891903614580.json'}

exec(code, env_args)
