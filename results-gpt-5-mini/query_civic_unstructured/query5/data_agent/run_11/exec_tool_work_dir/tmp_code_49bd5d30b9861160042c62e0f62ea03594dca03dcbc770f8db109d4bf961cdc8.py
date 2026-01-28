code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_GyEWcq2K5rnx7ZJmvsg1YkqM, 'r') as f:
    funding_records = json.load(f)

with open(var_call_HOf3aqJTez2ROSUvCScSDjs7, 'r') as f:
    civic_docs = json.load(f)

# Create DataFrame for funding
fund_df = pd.DataFrame(funding_records)
# Ensure Amount is int
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Disaster-related keywords
disaster_keywords = ['fema', 'caloes', 'caljpia', 'fema/caloes', 'fema/caloes', 'fema project', 'caloes project', 'caljpia', 'disaster', 'fire', 'woolsey', 'emergency']

matched_rows = []

# For each funding record, determine if it's disaster-related and if it started in 2022 according to civic docs
for idx, row in fund_df.iterrows():
    pname = row['Project_Name']
    pname_lower = pname.lower()

    # Candidate if funding name itself contains disaster keywords
    is_disaster_by_name = any(k in pname_lower for k in disaster_keywords)

    # Prepare name variants: original and without parenthetical suffix
    variants = [pname]
    no_paren = re.sub(r"\s*\([^)]*\)\s*$", '', pname).strip()
    if no_paren and no_paren != pname:
        variants.append(no_paren)

    started_2022 = False
    detected_disaster_in_doc = False

    # Search each civic doc for occurrences
    for doc in civic_docs:
        text = doc.get('text','')
        text_lower = text.lower()
        for var in variants:
            if not var:
                continue
            # find occurrences case-insensitive
            for m in re.finditer(re.escape(var), text, flags=re.IGNORECASE):
                start = m.start()
                end = m.end()
                window = text[max(0, start-500): min(len(text), end+500)]
                window_lower = window.lower()
                # check disaster indicators near occurrence
                if any(k in window_lower for k in disaster_keywords) or is_disaster_by_name:
                    detected_disaster_in_doc = True
                # check if '2022' in window
                if '2022' in window:
                    started_2022 = True
                # early exit if both found
                if detected_disaster_in_doc and started_2022:
                    break
            if detected_disaster_in_doc and started_2022:
                break
        if detected_disaster_in_doc and started_2022:
            break

    # Also allow disaster_by_name even if not present in civic docs; but we need start date in docs
    # So require started_2022 True and (detected_disaster_in_doc or is_disaster_by_name)
    if started_2022 and (detected_disaster_in_doc or is_disaster_by_name):
        matched_rows.append({'Project_Name': pname, 'Amount': int(row['Amount'])})

# Compute total
total = sum(r['Amount'] for r in matched_rows)

# Prepare result
result = {
    'total': total,
    'matched_projects': matched_rows
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_CAyxg5KXpRvlWH8pMBudSuR0': ['civic_docs'], 'var_call_QUCB4v2RmRAloKnfPuxYTjQM': ['Funding'], 'var_call_HOf3aqJTez2ROSUvCScSDjs7': 'file_storage/call_HOf3aqJTez2ROSUvCScSDjs7.json', 'var_call_GyEWcq2K5rnx7ZJmvsg1YkqM': 'file_storage/call_GyEWcq2K5rnx7ZJmvsg1YkqM.json'}

exec(code, env_args)
