code = """import json, re, pandas as pd

# Load full civic docs
path_docs = var_call_O5EfH7EZdYFhberNDh3qxvUv
with open(path_docs, 'r') as f:
    docs = json.load(f)
texts = ' '.join(d['text'] for d in docs)

# Heuristic: disaster-related projects include '(FEMA', '(CalOES', '(CalJPIA' or words 'Disaster Recovery'
# For start year 2022, look for patterns like '2022' near project names.

# We'll approximate by assuming all disaster-type projects are those whose names in Funding contain FEMA/CalOES/CalJPIA,
# and then filter to those that in texts mention 2022 near their name.

funding = pd.DataFrame(var_call_LJd4H09XkUfEbHSFSvYSR73l)

# disaster-related funding rows by name pattern
disaster_mask = funding['Project_Name'].str.contains('\(FEMA', case=False, regex=False) | \
                funding['Project_Name'].str.contains('\(CalOES', case=False, regex=False) | \
                funding['Project_Name'].str.contains('\(CalJPIA', case=False, regex=False)

funding_disaster = funding[disaster_mask].copy()

# For each project, check if its base name appears near '2022' in docs text
def started_2022(name):
    base = re.sub(r"\s*\(.*?\)", "", name).strip()
    pattern = re.escape(base)
    for m in re.finditer(pattern, texts):
        window = texts[max(0, m.start()-50): m.end()+50]
        if '2022' in window:
            return True
    return False

funding_disaster['started_2022'] = funding_disaster['Project_Name'].apply(started_2022)

subset = funding_disaster[funding_disaster['started_2022']]
subset['Amount'] = subset['Amount'].astype(int)

total = int(subset['Amount'].sum())

result = json.dumps({"total_funding_started_2022_disaster_projects": total, "projects": subset[['Project_Name','Amount']].to_dict(orient='records')})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_O5EfH7EZdYFhberNDh3qxvUv': 'file_storage/call_O5EfH7EZdYFhberNDh3qxvUv.json', 'var_call_LJd4H09XkUfEbHSFSvYSR73l': 'file_storage/call_LJd4H09XkUfEbHSFSvYSR73l.json'}

exec(code, env_args)
