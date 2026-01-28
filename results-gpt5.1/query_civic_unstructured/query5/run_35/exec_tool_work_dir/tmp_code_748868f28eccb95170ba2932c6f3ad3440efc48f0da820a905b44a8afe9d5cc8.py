code = """import re, json
from pathlib import Path

# Load full civic docs
path = Path(var_call_5vO74noyXoly1qnL8OEHJehK)
import pandas as pd
civic_docs = pd.read_json(path)
text = '\n'.join(civic_docs['text'].tolist())

# Heuristic: disaster projects are ones with FEMA/CalOES/CalJPIA or 'Fire' in name in funding table
funding = pd.DataFrame(var_call_mMUXk1pTX5O5J3Qe8YEp5RHX)

# Determine which funding projects are disaster-related: name contains 'FEMA', 'CalOES', 'CalJPIA', or 'Fire'
mask_disaster = funding['Project_Name'].str.contains('FEMA|CalOES|CalJPIA|Fire', case=False, regex=True)
funding_disaster = funding[mask_disaster].copy()

# Now we need those whose project start date is in 2022. Approximate by scanning civic text for project name near a 2022 date.
starts_2022 = []
for name in funding_disaster['Project_Name']:
    # escape regex specials
    pattern = re.escape(name[:40])  # use first 40 chars as identifier
    m = re.search(pattern + r'.{0,200}?20?22', text, flags=re.IGNORECASE|re.DOTALL)
    if m:
        starts_2022.append(True)
    else:
        # Also try just base name without parenthetical
        base = re.sub(r'\s*\(.*?\)', '', name).strip()
        pattern2 = re.escape(base[:40])
        m2 = re.search(pattern2 + r'.{0,200}?20?22', text, flags=re.IGNORECASE|re.DOTALL)
        starts_2022.append(bool(m2))

funding_disaster['start_2022'] = starts_2022

subset = funding_disaster[funding_disaster['start_2022']]
subset['Amount'] = subset['Amount'].astype(int)

total = int(subset['Amount'].sum())

result = {"total_disaster_funding_2022": total}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_5vO74noyXoly1qnL8OEHJehK': 'file_storage/call_5vO74noyXoly1qnL8OEHJehK.json', 'var_call_mMUXk1pTX5O5J3Qe8YEp5RHX': 'file_storage/call_mMUXk1pTX5O5J3Qe8YEp5RHX.json'}

exec(code, env_args)
