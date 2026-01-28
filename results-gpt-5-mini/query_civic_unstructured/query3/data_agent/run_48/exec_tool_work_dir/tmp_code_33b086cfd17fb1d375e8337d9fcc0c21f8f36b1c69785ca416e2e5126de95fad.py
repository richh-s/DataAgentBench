code = """import json
import re
import pandas as pd

# Load the query results from storage variables
with open(var_call_doKwQqZMvpmPnawdjdbN3n3o, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_wBrhbjFYhMnA5OtJjyPFnbnZ, 'r') as f:
    funding = json.load(f)

funding_df = pd.DataFrame(funding)
# Ensure Amount is int
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Function to normalize names (remove parenthetical, punctuation, lower)
def normalize(name):
    if not isinstance(name, str):
        return ''
    s = re.sub(r"\(.*?\)", "", name)  # remove parenthetical
    s = s.replace('&', ' and ')
    s = re.sub(r"[^0-9a-zA-Z ]+", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()

# Extract project titles and map to statuses from civic_docs
status_map = {}
for doc in civic_docs:
    text = doc.get('text','')
    # Find headings and their positions
    headings = []
    for m in re.finditer(r"([A-Za-z ].{0,80}?\(Design\)|[A-Za-z ].{0,80}?\(Construction\)|[A-Za-z ].{0,80}?\(Not Started\)|Disaster Recovery Projects|Capital Improvement Projects \(Design\)|Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\))", text):
        headings.append((m.start(), m.group(0)))
    # If no explicit headings found, keep empty
    # Find project title patterns followed by Updates marker
    for m in re.finditer(r"([A-Z][A-Za-z0-9&'\- ,\./]{5,120}?)\n\n\(cid:\d+\) Updates:", text):
        title = m.group(1).strip()
        pos = m.start()
        # Find nearest heading before pos
        hstatus = 'unknown'
        prev_head = None
        for hpos, htext in headings:
            if hpos < pos:
                prev_head = htext
            else:
                break
        if prev_head:
            if '(Design)' in prev_head:
                hstatus = 'design'
            elif '(Construction)' in prev_head:
                # Map construction to completed per guidance
                hstatus = 'completed'
            elif '(Not Started)' in prev_head:
                hstatus = 'not started'
            elif 'Disaster Recovery' in prev_head:
                hstatus = 'unknown'
        norm = normalize(title)
        if norm:
            status_map[norm] = hstatus

# Also try to capture project titles that appear as headings themselves (lines followed by "Updates:" without cid)
for doc in civic_docs:
    text = doc.get('text','')
    for m in re.finditer(r"([A-Z][A-Za-z0-9&'\- ,\./]{5,120}?)\n\nUpdates:", text):
        title = m.group(1).strip()
        pos = m.start()
        # Determine heading as above
        hstatus = 'unknown'
        # Search for nearest common section headings
        prev_head = None
        for mh in re.finditer(r"Capital Improvement Projects \((Design|Construction|Not Started)\)|Disaster Recovery Projects", text):
            hpos = mh.start()
            if hpos < pos:
                prev_head = mh.group(0)
            else:
                break
        if prev_head:
            if 'Design' in prev_head:
                hstatus = 'design'
            elif 'Construction' in prev_head:
                hstatus = 'completed'
            elif 'Not Started' in prev_head:
                hstatus = 'not started'
        norm = normalize(title)
        if norm and norm not in status_map:
            status_map[norm] = hstatus

# Now prepare result: find funding records that are related to 'fema' or 'emergency' OR match civic projects
results = []
for _, row in funding_df.iterrows():
    pname = row['Project_Name']
    norm_p = normalize(pname)
    pname_l = pname.lower()
    include = False
    # Include if name contains fema or emergency
    if 'fema' in pname_l or 'emergency' in pname_l:
        include = True
    # Include if normalized name matches any civic project normalized name
    if norm_p in status_map:
        include = True
    if include:
        status = status_map.get(norm_p, 'unknown')
        results.append({
            'Project_Name': pname,
            'Funding_Source': row['Funding_Source'],
            'Amount': int(row['Amount']),
            'Status': status
        })

# Additionally, there might be civic projects related to FEMA whose funding record has slightly different name (without parenthetical)
# Try to match civic projects to funding rows by comparing normalized forms
civic_norms = set(status_map.keys())
for _, row in funding_df.iterrows():
    pname = row['Project_Name']
    norm_p = normalize(pname)
    if any(norm_p == cn or norm_p in cn or cn in norm_p for cn in civic_norms):
        # Already added above? check
        already = any(r['Project_Name']==pname for r in results)
        if not already:
            status = status_map.get(norm_p, 'unknown')
            # if not exact match, try to find matching civic key
            if status=='unknown':
                for cn in civic_norms:
                    if norm_p == cn or norm_p in cn or cn in norm_p:
                        status = status_map.get(cn,'unknown')
                        break
            results.append({
                'Project_Name': pname,
                'Funding_Source': row['Funding_Source'],
                'Amount': int(row['Amount']),
                'Status': status
            })

# Deduplicate by Project_Name keeping first
seen = set()
unique_results = []
for r in results:
    if r['Project_Name'] not in seen:
        unique_results.append(r)
        seen.add(r['Project_Name'])

# Sort results by Project_Name
unique_results = sorted(unique_results, key=lambda x: x['Project_Name'].lower())

# Print in required format as JSON
print("__RESULT__:")
print(json.dumps(unique_results))"""

env_args = {'var_call_doKwQqZMvpmPnawdjdbN3n3o': 'file_storage/call_doKwQqZMvpmPnawdjdbN3n3o.json', 'var_call_wBrhbjFYhMnA5OtJjyPFnbnZ': 'file_storage/call_wBrhbjFYhMnA5OtJjyPFnbnZ.json'}

exec(code, env_args)
