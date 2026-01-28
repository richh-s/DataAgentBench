code = """import json, re, pandas as pd
from pathlib import Path

# Load full funding data
funding_path = var_call_pcCKnIwA0MIfHYDglrVnja1l
with open(funding_path, 'r') as f:
    funding = json.load(f)

# Load civic docs (preview is enough to get project snippets containing FEMA/emergency keywords)
docs_path = var_call_4GM5kThvR4yC0Aza7y2ommBA
with open(docs_path, 'r') as f:
    docs = json.load(f)

# For this task, project topic/status are not explicitly structured; we'll approximate by
# identifying project names from funding that relate to FEMA/emergency based on name keywords.

fund_df = pd.DataFrame(funding)

# Filter projects where name suggests FEMA/emergency
mask = fund_df['Project_Name'].str.contains('FEMA', case=False, na=False) | \
       fund_df['Project_Name'].str.contains('emergency', case=False, na=False)
rel = fund_df[mask].copy()

# Try to infer status heuristically from civic_docs text: design / completed / not started
# Simple heuristic: search for project name near status words.

status_keywords = {
    'design': ['in design', 'design phase', 'design:', 'complete design', 'finalize the design', 'preliminary design'],
    'completed': ['construction was completed', 'project was completed', 'construction completed', 'completed,', 'notice of completion filed'],
    'not started': ['not started', 'identified in', 'will include', 'will consist of', 'project description']
}

def infer_status(name, texts):
    name_pattern = re.escape(name)
    for doc in texts:
        text = doc['text'].lower()
        if name.lower() in text:
            for status, kws in status_keywords.items():
                for kw in kws:
                    if kw in text:
                        return status
    return None

texts = docs
statuses = []
for _, row in rel.iterrows():
    status = infer_status(row['Project_Name'], texts)
    statuses.append(status if status is not None else 'unknown')

rel['Status'] = statuses

result = rel[['Project_Name', 'Funding_Source', 'Amount', 'Status']].to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_pcCKnIwA0MIfHYDglrVnja1l': 'file_storage/call_pcCKnIwA0MIfHYDglrVnja1l.json', 'var_call_4GM5kThvR4yC0Aza7y2ommBA': 'file_storage/call_4GM5kThvR4yC0Aza7y2ommBA.json'}

exec(code, env_args)
