code = """import json, re
import pandas as pd

# Load previous tool results from files
with open(var_call_UrNkxgfEDQUkHzHV3SgjINdE, 'r') as f:
    funding = json.load(f)
with open(var_call_WWnm6BfhxtYtODlly3SuNxUq, 'r') as f:
    civic_docs = json.load(f)

# Create DataFrame for funding
fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Disaster-related keywords in project names
keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'woolsey']
fund_df['name_lower'] = fund_df['Project_Name'].str.lower()

# Candidate rows where project name indicates disaster
candidates = fund_df[fund_df['name_lower'].apply(lambda x: any(k in x for k in keywords))].copy()

# Normalize function to remove parenthetical suffixes and punctuation
def normalize(n):
    n2 = re.sub(r"\(.*?\)", "", n)
    n2 = re.sub(r"[^a-z0-9 ]+", " ", n2.lower())
    n2 = re.sub(r"\s+", " ", n2).strip()
    return n2

docs = [d.get('text','').lower() for d in civic_docs]

matched = []
for _, row in candidates.iterrows():
    pname = row['Project_Name']
    amt = int(row['Amount'])
    norm = normalize(pname)
    is_matched = False
    for doc in docs:
        if norm and norm in doc:
            if '2022' in doc:
                is_matched = True
                break
        else:
            # try partial matching of first 4 words
            words = norm.split()
            if len(words) >= 3:
                seq = ' '.join(words[:4])
                if seq in doc and '2022' in doc:
                    is_matched = True
                    break
    matched.append({'Funding_ID': int(row['Funding_ID']), 'Project_Name': pname, 'Amount': amt, 'matched': is_matched})

matched_projects = [m for m in matched if m['matched']]
total = sum(m['Amount'] for m in matched_projects)

out = {'total_funding_disaster_projects_started_2022': total, 'matched_projects': matched_projects}

# Print in required format
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_BNTx3inRJ9mvy6tdqJp73Xt0': ['civic_docs'], 'var_call_FGTaRAxpfrovZAI178E1gFqS': ['Funding'], 'var_call_WWnm6BfhxtYtODlly3SuNxUq': 'file_storage/call_WWnm6BfhxtYtODlly3SuNxUq.json', 'var_call_UrNkxgfEDQUkHzHV3SgjINdE': 'file_storage/call_UrNkxgfEDQUkHzHV3SgjINdE.json'}

exec(code, env_args)
