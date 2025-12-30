code = """import json
import re

# Load
with open(locals()['var_function-call-10751851316187988885'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_function-call-2019060603328784572'], 'r') as f:
    civic_docs = json.load(f)

# Sort
civic_docs.sort(key=lambda x: x['filename'], reverse=True) 
# Filenames: malibucity_agenda_03222023... -> 2023 is lexically last if format is YYYY? 
# No, format is MMDDYYYY. 03222023 vs 01262022. 
# 03222023 > 01262022. It works roughly, but 12312021 vs 01012022 -> 12 > 01. 
# Need proper date parsing.
def get_date(fname):
    # simple parse
    parts = re.findall(r'\d+', fname)
    for p in parts:
        if len(p) == 8: # MMDDYYYY
            return p[4:] + p[0:4] # YYYYMMDD
    return '00000000'

civic_docs.sort(key=lambda x: get_date(x['filename']), reverse=True)
latest_doc = civic_docs[0]
print("Latest: " + latest_doc['filename'])

text = latest_doc['text']

# Parse
start_marker = "Capital Improvement Projects (Design)"
idx = text.find(start_marker)
design_names = []

if idx != -1:
    section = text[idx + len(start_marker):]
    # Crop at next header
    end_idx = len(section)
    for h in ["Capital Improvement Projects (Construction)", "Disaster Recovery Projects", "Capital Improvement Projects (Not Started)"]:
        i = section.find(h)
        if i != -1 and i < end_idx:
            end_idx = i
    section = section[:end_idx]
    
    # Split by Updates
    # The text has "(cid:190) Updates:"
    # We will split by "Updates:"
    parts = section.split("Updates:")
    # First part has first name at end.
    # Middle parts have name at end.
    # Last part has no name (it is the content of the last project).
    
    for i in range(len(parts)-1):
        seg = parts[i]
        # Remove the bullet if present at end
        # The line is like "\n\n(cid:190) " or just "(cid:190) "
        # We want the line BEFORE the bullet line.
        
        lines = seg.split('\n')
        lines = [l.strip() for l in lines if l.strip()]
        
        # We need to find the project name.
        # It's usually the last line that doesn't look like a bullet.
        # The line immediately preceding "Updates:" usually contains "(cid:190)" or is empty.
        # Let's look at the last few non-empty lines.
        
        if not lines: continue
        
        # Check if last line is just the bullet
        if "(cid" in lines[-1]:
            lines.pop()
        
        if lines:
            candidate = lines[-1]
            # Page number filter
            if "Page " in candidate or "Agenda Item" in candidate:
                if len(lines) > 1:
                    candidate = lines[-2]
            
            # Clean candidate
            candidate = candidate.strip()
            if len(candidate) > 3: # min length
                design_names.append(candidate)

# Funding
funded = set()
for r in funding_data:
    try:
        if float(r['Amount']) > 50000:
            funded.add(r['Project_Name'].strip())
    except: pass

# Match
count = 0
matches = []
for dn in design_names:
    # Check exact
    if dn in funded:
        count += 1
        matches.append(dn)
    else:
        # Check fuzzy
        # Is funded name inside dn?
        found = False
        for fn in funded:
            if fn in dn or dn in fn:
                 # Check length
                 if len(fn) > 10 and len(dn) > 10:
                     count += 1
                     matches.append(dn + " ~= " + fn)
                     found = True
                     break
        if not found:
            print("No match: " + dn)

print("Matches found: " + str(count))
for m in matches:
    print(m)

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_function-call-10751851316187988885': 'file_storage/function-call-10751851316187988885.json', 'var_function-call-10751851316187990910': 'file_storage/function-call-10751851316187990910.json', 'var_function-call-1560571324400942804': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}], 'var_function-call-2019060603328784572': 'file_storage/function-call-2019060603328784572.json'}

exec(code, env_args)
