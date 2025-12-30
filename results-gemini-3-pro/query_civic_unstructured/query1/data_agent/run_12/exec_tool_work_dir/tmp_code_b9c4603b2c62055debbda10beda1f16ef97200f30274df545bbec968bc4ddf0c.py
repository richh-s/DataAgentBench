code = """import json
import re

# Load data
with open(locals()['var_function-call-10751851316187988885'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-2019060603328784572'], 'r') as f:
    civic_docs = json.load(f)

# 1. Identify the latest document
# Filenames have format malibucity_agenda_MMDDYYYY-...
def get_date_from_filename(fname):
    # regex for MMDDYYYY
    m = re.search(r'(\d{2})(\d{2})(\d{4})', fname)
    if m:
        return f"{m.group(3)}-{m.group(1)}-{m.group(2)}" # YYYY-MM-DD
    return "0000-00-00"

# Sort docs by date
civic_docs.sort(key=lambda x: get_date_from_filename(x['filename']), reverse=True)
latest_doc = civic_docs[0]
print(f"Latest doc: {latest_doc['filename']}")

text = latest_doc['text']

# 2. Extract Capital Projects (Design) section
# Find start
start_marker = "Capital Improvement Projects (Design)"
start_idx = text.find(start_marker)

if start_idx == -1:
    print("Could not find Capital Improvement Projects (Design) section")
    design_projects = []
else:
    # Find end - look for next section headers
    # Common headers seen: "Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"
    # We can just look for the next "Capital Improvement Projects (" or "Disaster Recovery Projects"
    sub_text = text[start_idx + len(start_marker):]
    
    # Find nearest next header
    next_headers = ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]
    end_idx = len(sub_text)
    for h in next_headers:
        idx = sub_text.find(h)
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    design_section = sub_text[:end_idx]
    
    # 3. Extract project names from the section
    # Pattern: Line ending with newline, followed by "(cid:190) Updates:"
    # Regex: capture group before \n\n(cid:190) Updates:
    # We need to be careful with newlines. The preview shows \n\n(cid:190) Updates:
    
    # Let's try to split by (cid:190) Updates: and look at the preceding lines.
    parts = design_section.split("(cid:190) Updates:")
    
    design_projects = []
    # The first part contains the first project name at the end.
    # Subsequent parts contain project info and then the next project name at the end, except the last part.
    
    # Actually, simpler:
    # The pattern seems to be: 
    # [Project Name]
    # (cid:190) Updates:
    
    # Let's iterate through parts (except the last one which doesn't have a following "Updates")
    for i in range(len(parts) - 1):
        # The project name is the last non-empty line of parts[i]
        # But parts[i] might contain the previous project's schedule etc.
        # We need to look at the text *immediately preceding* "(cid:190) Updates:"
        
        # Clean up whitespace
        segment = parts[i].strip()
        lines = segment.split('\n')
        # Filter empty lines
        lines = [l.strip() for l in lines if l.strip()]
        
        if lines:
            # The last line should be the project name
            p_name = lines[-1]
            
            # Clean up artifacts?
            # Sometimes there might be page numbers if it split across pages.
            # "Page 1 of 6\n\nAgenda Item # 4.B.\n\n..."
            # If the last line is a page number, we might need the one before.
            # Page numbers look like "Page X of Y" or "Agenda Item..."
            
            # Let's check the last few lines
            candidate = p_name
            # If candidate looks like "Agenda Item" or "Page", discard
            while (candidate.lower().startswith("page ") or candidate.lower().startswith("agenda item")) and len(lines) > 1:
                lines.pop()
                candidate = lines[-1]
            
            design_projects.append(candidate)

print("Extracted Design Projects:")
for p in design_projects:
    print(f" - {p}")

# 4. Filter by funding > 50,000
# Funding data is a list of dicts: {"Project_Name": "...", "Amount": "..."}
# Amounts are strings in the JSON, need to convert to int/float.
funded_projects = set()
for rec in funding_data:
    try:
        amt = float(rec['Amount'])
        if amt > 50000:
            funded_projects.add(rec['Project_Name'].strip())
    except:
        pass

print(f"\nFunded Projects (>50k): {len(funded_projects)}")

# 5. Count matches
count = 0
matches = []
for dp in design_projects:
    # Exact match?
    if dp in funded_projects:
        count += 1
        matches.append(dp)
    else:
        # Check for fuzzy match
        # Try checking if dp is in funded_projects (substring) or vice versa
        # Example: "Clover Heights Storm Drainage Improvements" vs "Clover Heights Storm Drain"
        # Let's check if any funded project name is a prefix or significantly contained in dp
        found = False
        for fp in funded_projects:
            # Check if one is substring of other
            if fp in dp or dp in fp:
                # Basic safety: length check to avoid matching "Project" to "Project X"
                if len(fp) > 10 and len(dp) > 10: 
                    count += 1
                    matches.append(f"{dp} (matched with {fp})")
                    found = True
                    break
        if not found:
            pass # print(f"No match for: {dp}")

print("\nMatches:")
for m in matches:
    print(m)

print("\n__RESULT__:")
print(json.dumps(str(count)))"""

env_args = {'var_function-call-10751851316187988885': 'file_storage/function-call-10751851316187988885.json', 'var_function-call-10751851316187990910': 'file_storage/function-call-10751851316187990910.json', 'var_function-call-1560571324400942804': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}], 'var_function-call-2019060603328784572': 'file_storage/function-call-2019060603328784572.json'}

exec(code, env_args)
