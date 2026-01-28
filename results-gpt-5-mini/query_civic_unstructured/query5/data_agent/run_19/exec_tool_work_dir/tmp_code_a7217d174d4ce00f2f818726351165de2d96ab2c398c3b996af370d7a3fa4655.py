code = """import json
import re

# Load data from storage files
with open(var_call_mD9y0i63dbrypAHlXFPtUAw5, 'r') as f:
    funding = json.load(f)
with open(var_call_sj17PQZB4sXEfi3fXW9hqIQ9, 'r') as f:
    civic_docs = json.load(f)

# Helper to normalize project names (remove parenthetical suffixes and excess whitespace)
def normalize(name):
    # remove parenthetical groups like (FEMA Project)
    n = re.sub(r"\(.*?\)", "", name)
    n = re.sub(r"[^\w\s-]", " ", n)  # replace non-alphanumeric (keep -) with space
    n = re.sub(r"\s+", " ", n).strip()
    return n.lower()

# Disaster keywords
disaster_kw = ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'woolsey', 'fema/caloes', 'fema/caloes', 'cal o es']

included = []

for row in funding:
    pname = row.get('Project_Name','')
    pname_norm = normalize(pname)
    pname_lower = pname.lower()
    amount = row.get('Amount')
    try:
        amount_val = int(amount)
    except:
        try:
            amount_val = int(float(amount))
        except:
            amount_val = 0

    found_in_docs = False
    matched_with_2022 = False
    matched_as_disaster = False

    # Quick check: if project name itself contains disaster keyword
    for kw in disaster_kw:
        if kw in pname_lower:
            matched_as_disaster = True
            break

    # Quick check: if name contains '2022' and disaster keyword
    if '2022' in pname_lower and matched_as_disaster:
        # include
        included.append({'Funding_ID': row.get('Funding_ID'), 'Project_Name': pname, 'Amount': amount_val})
        continue

    # Search in civic documents for mentions
    for doc in civic_docs:
        text = doc.get('text','').lower()
        # try to find either the full name or normalized name
        idx = text.find(pname.lower())
        if idx == -1:
            idx = text.find(pname_norm)
        if idx == -1:
            # try partial match by words of normalized name (first 4 words)
            words = pname_norm.split()
            if len(words) > 0:
                partial = ' '.join(words[:4])
                idx = text.find(partial)
        if idx != -1:
            found_in_docs = True
            # window around match
            start = max(0, idx-300)
            end = min(len(text), idx+300)
            window = text[start:end]
            if '2022' in window:
                matched_with_2022 = True
            # detect disaster keywords in window
            for kw in disaster_kw:
                if kw in window:
                    matched_as_disaster = True
                    break
            # If found and matched both, we can stop searching docs for this project
            if matched_with_2022 and matched_as_disaster:
                break
    # Decide inclusion: must be disaster and have 2022 near mention
    if matched_as_disaster and matched_with_2022:
        included.append({'Funding_ID': row.get('Funding_ID'), 'Project_Name': pname, 'Amount': amount_val})

# Sum amounts
total = sum([r['Amount'] for r in included])

result = {'total_funding': total, 'included_projects': included}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WZl1jvDUI6slkJ9SBofzj7N9': ['civic_docs'], 'var_call_HgxQu3gaWj93u9T43ZMo70fy': ['Funding'], 'var_call_mD9y0i63dbrypAHlXFPtUAw5': 'file_storage/call_mD9y0i63dbrypAHlXFPtUAw5.json', 'var_call_sj17PQZB4sXEfi3fXW9hqIQ9': 'file_storage/call_sj17PQZB4sXEfi3fXW9hqIQ9.json'}

exec(code, env_args)
