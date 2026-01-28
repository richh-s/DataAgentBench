code = """import json
import re

# Load the large results from storage paths
with open(var_call_cEjSafhmAnKntSnyaUtqqfNg, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_XWvwPaMMbPzQo4cjfNOb5t3k, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

# Normalize documents
docs = []
for d in civic_docs:
    text = d.get('text','')
    docs.append(text.lower())

# Prepare disaster keywords
disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'woolsey', 'federal assistance', 'federal assistance', 'federal']

matched_funding_ids = set()
matched_projects = []

for rec in funding_records:
    pname = rec.get('Project_Name','')
    pid = rec.get('Funding_ID')
    amount = rec.get('Amount')
    if amount is None:
        continue
    try:
        amt = int(amount)
    except:
        # skip non-numeric
        continue
    pname_l = pname.lower()

    found = False
    for doc_text in docs:
        pos = doc_text.find(pname_l)
        if pos != -1:
            # create a window around occurrence
            start = max(0, pos-200)
            end = pos + len(pname_l) + 500
            window = doc_text[start:end]
            # check for 2022 in window
            if '2022' in window:
                # check for disaster keywords in window or in project name
                is_disaster = any(k in window for k in disaster_keywords) or any(k in pname_l for k in disaster_keywords)
                if is_disaster:
                    matched_funding_ids.add(pid)
                    matched_projects.append({'Funding_ID': pid, 'Project_Name': pname, 'Amount': amt})
                    found = True
                    break
        # also try shorter name match: remove common suffixes like ' project', ' improvements', ' repairs', ' repair', ' phase 2', ' phase 1'
        # construct a simplified name
        simple = re.sub(r"\b(project|projects|improvements|improvement|repairs|repair|phase \d|phase)\b", '', pname_l)
        simple = re.sub(r'[^a-z0-9 ]',' ', simple).strip()
        if not found and simple and len(simple) > 6:
            if simple in doc_text:
                start = max(0, doc_text.find(simple)-200)
                end = doc_text.find(simple) + len(simple) + 500
                window = doc_text[start:end]
                if '2022' in window:
                    is_disaster = any(k in window for k in disaster_keywords) or any(k in simple for k in disaster_keywords)
                    if is_disaster:
                        matched_funding_ids.add(pid)
                        matched_projects.append({'Funding_ID': pid, 'Project_Name': pname, 'Amount': amt})
                        break

# Remove duplicates in matched_projects by Funding_ID
unique_projects = {}
for p in matched_projects:
    unique_projects[p['Funding_ID']] = p

unique_list = list(unique_projects.values())

total = sum(p['Amount'] for p in unique_list)

result = {
    'total_funding': total,
    'matching_projects': unique_list
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cEjSafhmAnKntSnyaUtqqfNg': 'file_storage/call_cEjSafhmAnKntSnyaUtqqfNg.json', 'var_call_XWvwPaMMbPzQo4cjfNOb5t3k': 'file_storage/call_XWvwPaMMbPzQo4cjfNOb5t3k.json'}

exec(code, env_args)
