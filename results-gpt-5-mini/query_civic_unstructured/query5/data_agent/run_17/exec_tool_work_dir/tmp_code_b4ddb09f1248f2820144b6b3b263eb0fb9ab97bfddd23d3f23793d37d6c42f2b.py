code = """import json, re
import pandas as pd

# Load previous tool results from files
with open(var_call_UrNkxgfEDQUkHzHV3SgjINdE, 'r') as f:
    funding = json.load(f)
with open(var_call_WWnm6BfhxtYtODlly3SuNxUq, 'r') as f:
    civic_docs = json.load(f)

# Create DataFrame for funding
fund_df = pd.DataFrame(funding)
# Ensure Amount is int
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Disaster-related keywords in project names
disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'woolsey']

# Identify candidate disaster funding rows
fund_df['name_lower'] = fund_df['Project_Name'].str.lower()
mask = fund_df['name_lower'].apply(lambda x: any(k in x for k in disaster_keywords))
candidates = fund_df[mask].copy()

# Helper to normalize project name (remove parenthetical suffixes)
def normalize_name(n):
    # remove parenthesis content
    n2 = re.sub(r"\(.*?\)", "", n)
    n2 = re.sub(r"[^a-z0-9 ]+", " ", n2.lower())
    n2 = re.sub(r"\s+", " ", n2).strip()
    return n2

# Build list of documents' text lower
docs = [d.get('text','').lower() for d in civic_docs]

results = []
for idx, row in candidates.iterrows():
    pname = row['Project_Name']
    norm = normalize_name(pname)
    found = False
    found_doc_idx = None
    for i, doc in enumerate(docs):
        if norm and norm in doc:
            # if name occurs in doc
            pos = doc.find(norm)
            window = doc[max(0,pos-200): pos+len(norm)+200]
            if '2022' in window or '2022' in doc:
                found = True
                found_doc_idx = i
                break
        else:
            # try matching first 4 words sequence
            words = norm.split()
            if len(words) >= 3:
                seq = ' '.join(words[:4])
                if seq in doc:
                    pos = doc.find(seq)
                    window = doc[max(0,pos-200): pos+len(seq)+200]
                    if '2022' in window or '2022' in doc:
                        found = True
                        found_doc_idx = i
                        break
    results.append({
        'Funding_ID': int(row['Funding_ID']),
        'Project_Name': pname,
        'Amount': int(row['Amount']),
        'matched_in_docs': found,
        'doc_index': found_doc_idx
    })

# Sum amounts for those matched (considered disaster projects that started in 2022)
matched_rows = [r for r in results if r['matched_in_docs']]
total = sum(r['Amount'] for r in matched_rows)

out = {
    'total_funding_disaster_projects_started_2022': total,
    'matched_projects': matched_rows
}

print("----BEGIN PRINT FORMAT----")
print("print(\"__RESULT__:\")")
print('print(' + json.dumps(json.dumps(out)) + ')')
print("----END PRINT FORMAT----")"""

env_args = {'var_call_BNTx3inRJ9mvy6tdqJp73Xt0': ['civic_docs'], 'var_call_FGTaRAxpfrovZAI178E1gFqS': ['Funding'], 'var_call_WWnm6BfhxtYtODlly3SuNxUq': 'file_storage/call_WWnm6BfhxtYtODlly3SuNxUq.json', 'var_call_UrNkxgfEDQUkHzHV3SgjINdE': 'file_storage/call_UrNkxgfEDQUkHzHV3SgjINdE.json'}

exec(code, env_args)
