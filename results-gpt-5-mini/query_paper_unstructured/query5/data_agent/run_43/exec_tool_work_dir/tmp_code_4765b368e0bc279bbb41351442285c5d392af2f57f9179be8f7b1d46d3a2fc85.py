code = """import json
# load citation query results from file path stored in var_call_oDXJStwJQPDvvNpR6CkeIDYv
with open(var_call_oDXJStwJQPDvvNpR6CkeIDYv, 'r') as f:
    citations = json.load(f)
# paper docs query results are in var_call_RV9ExjQXwNd40pgdDIxJPXO4
chi_docs = var_call_RV9ExjQXwNd40pgdDIxJPXO4
# extract titles (filename without .txt)
chi_titles = [d['filename'].rsplit('.', 1)[0] for d in chi_docs]
# build mapping from citation title to count (int)
mapping = {rec['title']: int(rec['citation_count']) for rec in citations}
# collect per-paper citation counts for CHI papers that were cited in 2020
per_paper = []
total = 0
for t in chi_titles:
    if t in mapping:
        c = mapping[t]
        per_paper.append({'title': t, 'citation_count': c})
        total += c
# prepare result
result = {'per_paper': per_paper, 'total_citations': total}
import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_oDXJStwJQPDvvNpR6CkeIDYv': 'file_storage/call_oDXJStwJQPDvvNpR6CkeIDYv.json', 'var_call_RV9ExjQXwNd40pgdDIxJPXO4': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
