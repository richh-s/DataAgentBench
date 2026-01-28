code = """import json
# Load stored query results
with open(var_call_O8fNiGy0hYX2JWmSnRw9hiIg, 'r') as f:
    funding = json.load(f)
with open(var_call_RDTPadJ0MEdOGRSFv71OoRd6, 'r') as f:
    civic_docs = json.load(f)

# Combine all civic texts
all_text = "\n".join([doc.get('text','') for doc in civic_docs])
all_text_l = all_text.lower()

results = []

for row in funding:
    proj = row.get('Project_Name','')
    proj_l = proj.lower()
    funding_source = row.get('Funding_Source')
    amount_raw = row.get('Amount')
    try:
        amount = int(amount_raw) if amount_raw is not None and str(amount_raw).isdigit() else amount_raw
    except:
        amount = amount_raw

    matched = False
    status = 'Unknown'

    # find indices for full name and base name (without parenthesis suffix)
    indices = []
    idx = all_text_l.find(proj_l)
    if idx != -1:
        indices.append(idx)
    base = proj.split('(')[0].strip().lower()
    if base and base != proj_l:
        idx2 = all_text_l.find(base)
        if idx2 != -1:
            indices.append(idx2)

    # If project name itself mentions fema or emergency, mark matched and try to locate base in text
    if ('fema' in proj_l) or ('emergency' in proj_l):
        matched = True
        if base:
            idxb = all_text_l.find(base)
            if idxb != -1:
                indices.append(idxb)

    # Check found indices for nearby keywords
    for i in indices:
        window = all_text_l[max(0, i-300): i+300]
        if ('fema' in window) or ('emergency' in window) or ('fema' in proj_l) or ('emergency' in proj_l):
            matched = True
            # determine status from window
            if any(k in window for k in ['preliminary design','in the preliminary design phase','finalizing the design','complete design','final design']):
                status = 'Design'
            elif any(k in window for k in ['construction was completed','complete construction','notice of completion','was completed']):
                status = 'Completed'
            elif any(k in window for k in ['not started','identified but not begun','not begun']):
                status = 'Not Started'
            elif any(k in window for k in ['currently under construction','begin construction','begin construction:']):
                status = 'Construction'
            else:
                # check preceding section header
                pre = all_text_l[max(0, i-1000): i]
                if 'capital improvement projects' in pre:
                    # crude check for (Design) or (Construction) markers
                    hdr = pre.split('capital improvement projects')[-1][:200]
                    if 'design' in hdr:
                        status = 'Design'
                    elif 'construction' in hdr:
                        status = 'Construction'
                    elif 'not started' in hdr:
                        status = 'Not Started'
                    else:
                        status = 'Unknown'
                else:
                    status = 'Unknown'
            break

    if matched:
        results.append({
            'Project_Name': proj,
            'Funding_Source': funding_source,
            'Amount': amount,
            'Status': status
        })

# Deduplicate by project name
seen = set()
unique = []
for r in results:
    key = r['Project_Name'].lower()
    if key in seen:
        continue
    seen.add(key)
    unique.append(r)

print("__RESULT__:")
print(json.dumps(unique))"""

env_args = {'var_call_RDTPadJ0MEdOGRSFv71OoRd6': 'file_storage/call_RDTPadJ0MEdOGRSFv71OoRd6.json', 'var_call_HpgQvXmAaa9rS2LPuJKiZVjk': ['Funding'], 'var_call_O8fNiGy0hYX2JWmSnRw9hiIg': 'file_storage/call_O8fNiGy0hYX2JWmSnRw9hiIg.json'}

exec(code, env_args)
