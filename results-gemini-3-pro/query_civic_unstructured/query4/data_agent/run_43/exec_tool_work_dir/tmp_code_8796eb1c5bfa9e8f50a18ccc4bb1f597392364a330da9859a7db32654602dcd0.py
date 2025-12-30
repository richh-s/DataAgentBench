code = """import json
import pandas as pd
import re

# Load civic docs
civic_docs_path = locals()['var_function-call-12607651032579543164']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding
funding_path = locals()['var_function-call-5868675038188901918']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Helper for date check
def is_spring_2022(date_str):
    if not date_str:
        return False
    ds = date_str.lower().strip()
    if "spring 2022" in ds:
        return True
    if "2022" in ds:
        if "march" in ds or "april" in ds or "may" in ds:
            return True
        if "2022-03" in ds or "2022-04" in ds or "2022-05" in ds:
            return True
    return False

projects = []

for doc in civic_docs:
    text = doc['text']
    
    # We split by the bullet point marker "(cid:190)" which seems to start sections like Updates or Description
    # But we need the line *before* it as the project name.
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if next meaningful line starts with (cid:190) Updates or Description
        # Look ahead
        found_marker = False
        marker_type = ""
        
        # Scan next few lines (skip empty)
        next_idx = i + 1
        while next_idx < len(lines) and next_idx < i + 5:
            nl = lines[next_idx].strip()
            if nl.startswith("(cid:190) Updates") or nl.startswith("(cid:190) Project Description"):
                found_marker = True
                break
            if nl: # Found a non-empty line that isn't the marker, so the current line is probably not the project name immediately preceding the marker
                # Wait, the structure is:
                # Name
                # [Empty Lines]
                # Marker
                break
            next_idx += 1
            
        if found_marker:
            # Current line is likely a project name
            # Check if it's a header to ignore
            if "Capital Improvement Projects" in line:
                continue
                
            p_name = line
            
            # Now extract the block for this project
            # The block goes until the next project name or end of doc.
            # But simpler: scan forward for "Begin Construction:" until we hit another project name or end.
            # Actually, "Begin Construction" is usually within the next 20 lines.
            
            start_date = None
            
            # Scan forward from marker
            scan_idx = next_idx
            # We scan until we see another line that looks like a project name (which we detect by looking ahead for marker again)
            # Or just scan a fixed window or until next marker.
            
            while scan_idx < len(lines):
                sline = lines[scan_idx].strip()
                
                # Check for Start Date
                # Patterns: "Begin Construction:", "Start:", "Advertise:" (no), "Complete Design:" (no)
                match = re.search(r"Begin Construction[:\s]+(.*)", sline, re.IGNORECASE)
                if not match:
                     match = re.search(r"Start Date[:\s]+(.*)", sline, re.IGNORECASE)
                
                if match:
                    start_date = match.group(1).strip()
                    break
                
                # Stop if we hit a new project marker block (look ahead for marker)
                # But that's expensive. 
                # Let's just stop if we see "(cid:190) Updates" or "(cid:190) Project Description" again (start of next project's block? No, markers are INSIDE project blocks)
                # Wait, each project has ONE Updates and/or ONE Description section.
                # So if we see another "(cid:190) Updates" it's a new project.
                if scan_idx > next_idx and (sline.startswith("(cid:190) Updates") or sline.startswith("(cid:190) Project Description")):
                    break
                    
                scan_idx += 1
            
            projects.append({'name': p_name, 'start_date': start_date})

# Filter
matching_projects = []
for p in projects:
    if is_spring_2022(p['start_date']):
        matching_projects.append(p['name'])

unique_projects = list(set(matching_projects))

# Match funding
# Normalize
def normalize(s):
    return re.sub(r'\W+', '', s).lower()

funding_map = {normalize(row['Project_Name']): row['Amount'] for row in funding_data}
# Also keep original names for debug
funding_map_orig = {normalize(row['Project_Name']): row['Project_Name'] for row in funding_data}

total = 0
found_count = 0
matched_list = []

for p in unique_projects:
    n_p = normalize(p)
    if n_p in funding_map:
        total += funding_map[n_p]
        found_count += 1
        matched_list.append(p)
    else:
        # Try substring matching
        # "Birdview Avenue Improvements" vs "Birdview Avenue Improvements (CalOES Project)"
        best_match = None
        for k in funding_map:
            if n_p in k or k in n_p:
                # If one is contained in the other
                best_match = k
                break
        if best_match:
            total += funding_map[best_match]
            found_count += 1
            matched_list.append(f"{p} (matched {funding_map_orig[best_match]})")

print("__RESULT__:")
print(json.dumps({
    "count": found_count,
    "total_funding": total,
    "matched_projects": matched_list,
    "all_extracted_matches": [p for p in projects if is_spring_2022(p['start_date'])],
    "debug_projects": projects[:5]
}))"""

env_args = {'var_function-call-14853737414132312257': ['Funding'], 'var_function-call-14853737414132313422': 'file_storage/function-call-14853737414132313422.json', 'var_function-call-5868675038188901918': 'file_storage/function-call-5868675038188901918.json', 'var_function-call-12607651032579543164': 'file_storage/function-call-12607651032579543164.json'}

exec(code, env_args)
