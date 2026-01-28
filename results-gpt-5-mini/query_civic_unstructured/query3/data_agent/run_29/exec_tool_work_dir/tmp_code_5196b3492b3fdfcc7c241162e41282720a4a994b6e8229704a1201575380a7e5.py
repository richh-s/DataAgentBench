code = """import json, re

# Load data from storage entries (file paths)
path_civic = var_call_jzhQseUHxKXVBNdaUVsP8c9e
path_funding = var_call_Utur5J9BLQ3n16jKLtshjCae

with open(path_funding, 'r') as f:
    funding = json.load(f)
with open(path_civic, 'r') as f:
    civic_docs = json.load(f)

# Normalize civic texts concatenated
combined_texts = "\n---DOC---\n".join([d.get('text','') for d in civic_docs])
combined_lower = combined_texts.lower()

results = []

def clean_name(n):
    # remove parenthetical suffixes and extra whitespace
    return re.sub(r"\s*\(.*?\)\s*", "", n).strip()

# status mapping function
def extract_status(snippet):
    s = snippet.lower()
    if 'under construction' in s or 'begin construction' in s or 'construction was' in s:
        return 'under construction'
    if 'complete design' in s or 'complete design:' in s or 'design phase' in s or 'design plans' in s or 'preliminary design' in s:
        return 'design'
    if 'completed' in s or 'notice of completion' in s or 'complete construction' in s:
        return 'completed'
    if 'not started' in s or 'identified' in s and 'not' in s:
        return 'not started'
    if 'awaiting' in s and 'fema' in s:
        return 'awaiting FEMA approval'
    # default: try to capture short status phrases
    m = re.search(r"\b(status|updates):?\s*([^\n\.]+)", snippet, re.IGNORECASE)
    if m:
        return m.group(2).strip()
    return None

for rec in funding:
    pname = rec.get('Project_Name','')
    pname_clean = clean_name(pname)
    lname = pname.lower()
    selected = False
    status = None

    # Criterion 1: funding project name itself mentions FEMA or emergency
    if 'fema' in lname or 'emergency' in lname:
        selected = True
        # try to find in civic docs for status
        idx = combined_lower.find(pname_clean.lower())
        if idx != -1:
            snippet = combined_texts[max(0, idx-200): idx+500]
            status = extract_status(snippet)
    else:
        # Criterion 2: project name appears in civic docs near 'fema' or 'emergency'
        if pname_clean and pname_clean.lower() in combined_lower:
            # find each occurrence and check surrounding text for fema/emergency
            for m in re.finditer(re.escape(pname_clean.lower()), combined_lower):
                start = max(0, m.start()-300)
                end = min(len(combined_lower), m.end()+300)
                window = combined_lower[start:end]
                if 'fema' in window or 'caloes' in window or 'caloes' in window or 'emergency' in window:
                    selected = True
                    snippet = combined_texts[start:end]
                    status = extract_status(snippet)
                    break

    if selected:
        # convert amount to int if possible
        amt = rec.get('Amount')
        try:
            amt_v = int(amt)
        except:
            try:
                amt_v = int(float(amt))
            except:
                amt_v = None
        results.append({
            'Project_Name': pname,
            'Funding_Source': rec.get('Funding_Source'),
            'Amount': amt_v,
            'Status': status
        })

# Remove duplicates by Project_Name keeping first
seen = set()
unique_results = []
for r in results:
    if r['Project_Name'] not in seen:
        unique_results.append(r)
        seen.add(r['Project_Name'])

output = unique_results

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_jzhQseUHxKXVBNdaUVsP8c9e': 'file_storage/call_jzhQseUHxKXVBNdaUVsP8c9e.json', 'var_call_Utur5J9BLQ3n16jKLtshjCae': 'file_storage/call_Utur5J9BLQ3n16jKLtshjCae.json'}

exec(code, env_args)
