code = """import json
import pandas as pd

# Load data from previous tool calls
with open(var_call_WYCdeCVJhHs5YIKTbm63A3Hd, 'r') as f:
    funding_data = json.load(f)
with open(var_call_zE9Ko6ZAcGG2jQOP9Y5R5mMf, 'r') as f:
    civic_docs = json.load(f)

# Create DataFrame for funding
fund_df = pd.DataFrame(funding_data)
# Ensure Amount is numeric
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce').fillna(0).astype(int)

# Extract potential project names that mention completion in 2022
extracted = set()
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if 'completed' in line.lower() and '2022' in line:
            # look upwards for a candidate project title
            j = i-1
            candidate = None
            while j >= 0:
                ln = lines[j].strip()
                lower_ln = ln.lower()
                if not ln:
                    j -= 1
                    continue
                # skip common header/footer/labels
                if any(token in lower_ln for token in ['updates', 'update', 'project schedule', 'agenda', 'page', 'item', 'prepared by', 'approved by', 'meeting date', 'discussion']):
                    j -= 1
                    continue
                # skip lines that look like bullets or metadata
                if lower_ln.startswith('(cid:') or lower_ln.endswith(':') and len(lower_ln.split())<6:
                    j -= 1
                    continue
                # candidate found
                candidate = ln
                break
            if candidate:
                extracted.add(candidate)

extracted_list = sorted(extracted)

# Define park-related keywords
park_keywords = ['park','playground','walkway','benches','paver','shade','playground','arbor','bluffs','plaza']

# Filter extracted names to park-related ones
park_extracted = [e for e in extracted_list if any(k in e.lower() for k in park_keywords)]

# Match funding entries by substring matching, ensuring park-related
matched_rows = []
for _, row in fund_df.iterrows():
    fname = row['Project_Name']
    fname_l = fname.lower()
    # check if funding row is park-related
    fund_is_park = any(k in fname_l for k in park_keywords)
    if not fund_is_park:
        continue
    # check match to any extracted park project name
    for ex in park_extracted:
        ex_l = ex.lower()
        if ex_l in fname_l or fname_l in ex_l:
            matched_rows.append({'Project_Name': fname, 'Amount': int(row['Amount'])})
            break

# Additionally, some projects might match via partial tokens (e.g., 'Point Dume Walkway' vs 'Point Dume Walkway Repairs')
# Try broader matching: split extracted tokens and check if most tokens in fname
for ex in park_extracted:
    ex_l = ex.lower()
    ex_tokens = [t for t in ex_l.replace('-',' ').split() if len(t)>3]
    for _, row in fund_df.iterrows():
        fname = row['Project_Name']
        fname_l = fname.lower()
        if any(m['Project_Name']==fname for m in matched_rows):
            continue
        fund_is_park = any(k in fname_l for k in park_keywords)
        if not fund_is_park:
            continue
        # count token overlap
        if ex_tokens and sum(1 for t in ex_tokens if t in fname_l) >= max(1, len(ex_tokens)//2):
            matched_rows.append({'Project_Name': fname, 'Amount': int(row['Amount'])})

# Deduplicate matched_rows by Project_Name
seen = set()
unique_matched = []
for r in matched_rows:
    if r['Project_Name'] not in seen:
        unique_matched.append(r)
        seen.add(r['Project_Name'])

# Sum total
total = sum(r['Amount'] for r in unique_matched)

result = {
    'total_funding': total,
    'matched_projects': unique_matched,
    'extracted_candidates': park_extracted
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WYCdeCVJhHs5YIKTbm63A3Hd': 'file_storage/call_WYCdeCVJhHs5YIKTbm63A3Hd.json', 'var_call_zE9Ko6ZAcGG2jQOP9Y5R5mMf': 'file_storage/call_zE9Ko6ZAcGG2jQOP9Y5R5mMf.json'}

exec(code, env_args)
