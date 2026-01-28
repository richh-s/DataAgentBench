code = """import json
import re
import pandas as pd

# Load data from storage file paths
funding_path = var_call_U60WqxOGdjsbcqS6PF9PWbjF
docs_path = var_call_8vBnfmWWXT7qozNkwSfsNVHc

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

funding_df = pd.DataFrame(funding)

# normalize funding_df columns
funding_df['Project_Name'] = funding_df['Project_Name'].astype(str)
funding_df['Funding_Source'] = funding_df['Funding_Source'].astype(str)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Prepare docs texts
for d in docs:
    d['text_low'] = d.get('text','').lower()

related = []

# helper for status extraction
def infer_status(context):
    c = context.lower()
    if any(x in c for x in ['construction was completed', 'completed', 'notice of completion', 'complete construction', 'complete design:']):
        return 'completed'
    if any(x in c for x in ['under construction', 'begin construction', 'begin construction:', 'begin construction', 'construction:']):
        return 'design'
    if any(x in c for x in ['complete design', 'design', 'plans are being finalized', 'finalizing the design', 'final design', 'complete design:']):
        return 'design'
    if any(x in c for x in ['not started', 'identified', 'awaiting', 'awaiting final', 'pending', 'to be discussed', 'preliminary design']):
        return 'not started'
    return None

# Determine related projects
for idx, row in funding_df.iterrows():
    pname = row['Project_Name']
    pname_low = pname.lower()
    is_related = False
    inferred_status = None

    # direct indicators in project name
    if 'fema' in pname_low or 'caloes' in pname_low or 'caloes' in pname_low or 'cal o es' in pname_low:
        is_related = True

    if any(k in pname_low for k in ['emergency', 'outdoor warning', 'sirens']):
        is_related = True

    # search docs for project mention; if doc also mentions fema or emergency, mark related
    for d in docs:
        txt = d['text_low']
        if pname_low in txt:
            # project mentioned in doc
            # if doc contains fema or emergency -> related
            if 'fema' in txt or 'emergency' in txt or 'caloes' in txt:
                is_related = True
            # attempt to infer status from nearby context
            idx_found = txt.find(pname_low)
            start = max(0, idx_found-400)
            end = min(len(txt), idx_found+800)
            context = txt[start:end]
            status = infer_status(context)
            if status:
                inferred_status = status
            # break not breaking: might find better status in other docs
    # If still not related but doc contains project name and project name includes keywords like 'outdoor warning', count it
    # Finalize
    if is_related:
        # if no inferred_status, try broader search across docs for project name contexts
        if inferred_status is None:
            for d in docs:
                txt = d['text_low']
                if pname_low in txt:
                    idx_found = txt.find(pname_low)
                    start = max(0, idx_found-400)
                    end = min(len(txt), idx_found+800)
                    context = txt[start:end]
                    status = infer_status(context)
                    if status:
                        inferred_status = status
                        break
        related.append({
            'Project_Name': row['Project_Name'],
            'Funding_Source': row['Funding_Source'],
            'Amount': int(row['Amount']),
            'Status': inferred_status if inferred_status is not None else ''
        })

# Additionally, find projects that appear in docs near emergency/FEMA mentions but funding may have different name match
# We'll search doc text for lines with project-like headings and extract names followed by keywords
# For simplicity, also include any funding rows where doc contains keywords and project name occurs in doc even if project name didn't include FEMA

# Deduplicate by Project_Name
unique = {}
for r in related:
    unique[r['Project_Name']] = r
res_list = list(unique.values())

# print result in required format
print("__RESULT__:")
print(json.dumps(res_list))"""

env_args = {'var_call_8vBnfmWWXT7qozNkwSfsNVHc': 'file_storage/call_8vBnfmWWXT7qozNkwSfsNVHc.json', 'var_call_U60WqxOGdjsbcqS6PF9PWbjF': 'file_storage/call_U60WqxOGdjsbcqS6PF9PWbjF.json'}

exec(code, env_args)
