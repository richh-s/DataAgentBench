code = """import json, re, pandas as pd
from pathlib import Path

path = Path(var_call_JKEY4tGkAaybFY60KiTKbnbv)
articles = json.loads(path.read_text())
case_desc = 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.'

best_id = None
best_score = 0

case_words = set(re.findall(r"[a-zA-Z]+", case_desc.lower()))

for art in articles:
    text = ' '.join([art.get('title',''), art.get('summary',''), art.get('faq_answer__c','')])
    words = set(re.findall(r"[a-zA-Z]+", text.lower()))
    if not words:
        continue
    overlap = len(case_words & words)
    score = overlap / len(case_words)
    if score > best_score:
        best_score = score
        best_id = art.get('id')

threshold = 0.05
result = None if best_score < threshold else best_id

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_QmXpcUzPqAII1gvq02SM8DPB': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.'}], 'var_call_JKEY4tGkAaybFY60KiTKbnbv': 'file_storage/call_JKEY4tGkAaybFY60KiTKbnbv.json'}

exec(code, env_args)
