code = """import json
import re

# Load
with open(locals()['var_function-call-10751851316187988885'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_function-call-2019060603328784572'], 'r') as f:
    civic_docs = json.load(f)

# Sort
def get_date(fname):
    parts = re.findall(r'\d+', fname)
    for p in parts:
        if len(p) == 8:
            return p[4:] + p[0:4]
    return '00000000'

civic_docs.sort(key=lambda x: get_date(x['filename']), reverse=True)
latest_doc = civic_docs[0]
text = latest_doc['text']

# Parse
start_marker = 'Capital Improvement Projects (Design)'
idx = text.find(start_marker)
design_names = []

if idx != -1:
    section = text[idx + len(start_marker):]
    end_idx = len(section)
    for h in ['Capital Improvement Projects (Construction)', 'Disaster Recovery Projects', 'Capital Improvement Projects (Not Started)']:
        i = section.find(h)
        if i != -1 and i < end_idx:
            end_idx = i
    section = section[:end_idx]
    
    # Regex extraction
    # Look for lines followed by (cid:190) Updates: or (cid:190) Project Description:
    # Note: (cid:190) might be encoded or just plain text. The preview showed it as plain text.
    # We use . matches anything except newline, but we want the line before.
    # Pattern: \n <Project Name> \n+ (cid:190) (Updates|Project Description):
    
    # We'll use a loose pattern
    # Find all occurrences of "(cid:190) Updates:" or "(cid:190) Project Description:"
    # and take the preceding non-empty line.
    
    delimiters = [r'\(cid:190\) Updates:', r'\(cid:190\) Project Description:']
    pattern = '|'.join(delimiters)
    
    # We iterate through the matches
    for m in re.finditer(pattern, section):
        start = m.start()
        # Look backwards from start
        # Skip whitespace/newlines
        i = start - 1
        while i >= 0 and section[i].isspace():
            i -= 1
        
        # Now read the line backwards
        if i >= 0:
            j = section.rfind('\n', 0, i+1)
            if j == -1: j = 0
            else: j += 1 # start of line
            
            line = section[j:i+1].strip()
            
            # Filter page numbers
            if 'Page ' in line or 'Agenda Item' in line:
                # Go back one more line
                i = j - 2 # before the newline
                while i >= 0 and section[i].isspace():
                    i -= 1
                if i >= 0:
                    j = section.rfind('\n', 0, i+1)
                    if j == -1: j = 0
                    else: j += 1
                    line = section[j:i+1].strip()
            
            if len(line) > 3:
                design_names.append(line)

# Funding
funded = {} # name -> amount
for r in funding_data:
    try:
        amt = float(r['Amount'])
        if amt > 50000:
            funded[r['Project_Name'].strip()] = amt
    except: pass

# Match
count = 0
matches = []
matched_design_names = set()

for dn in design_names:
    best_match = None
    
    # Exact
    if dn in funded:
        best_match = dn
    else:
        # Fuzzy
        # 1. Substring
        for fn in funded:
            if (fn in dn or dn in fn) and len(fn)>10 and len(dn)>10:
                best_match = fn
                break
        
        # 2. Token overlap (if no substring match)
        if not best_match:
            dn_tokens = set(re.findall(r'\w+', dn.lower()))
            for fn in funded:
                fn_tokens = set(re.findall(r'\w+', fn.lower()))
                # Ignore common words
                common = dn_tokens.intersection(fn_tokens)
                common.discard('project')
                common.discard('improvements')
                common.discard('repairs')
                common.discard('road') # maybe?
                
                if len(common) >= 3: # at least 3 distinctive words?
                    best_match = fn
                    break
                    
    if best_match:
        if dn not in matched_design_names: # avoid double counting the same extracted project? 
            # But what if multiple extracted map to same funded?
            # Or multiple funded map to same extracted?
            # We want number of *projects*. 
            # Assuming extracted names are unique projects.
            count += 1
            matches.append(f"{dn} -> {best_match}")
            matched_design_names.add(dn)
    else:
        print(f"No match: {dn}")

print(f"Total Matches: {count}")
for m in matches:
    print(m)

print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_function-call-10751851316187988885': 'file_storage/function-call-10751851316187988885.json', 'var_function-call-10751851316187990910': 'file_storage/function-call-10751851316187990910.json', 'var_function-call-1560571324400942804': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}], 'var_function-call-2019060603328784572': 'file_storage/function-call-2019060603328784572.json', 'var_function-call-8967049199834060110': 10}

exec(code, env_args)
