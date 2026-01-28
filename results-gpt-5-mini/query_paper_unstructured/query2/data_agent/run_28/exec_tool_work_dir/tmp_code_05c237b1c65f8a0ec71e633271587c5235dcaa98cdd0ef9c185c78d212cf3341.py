code = """import json
import pandas as pd

# Load the large citations result from file path stored in var_call_8TewsOi0jcGVe1hk4shl065W
with open(var_call_8TewsOi0jcGVe1hk4shl065W, 'r') as f:
    citations = json.load(f)

# Load the paper docs result (list of filenames) from var_call_gk7HXaThPOeG46kG9YdJcB7r
paper_docs = var_call_gk7HXaThPOeG46kG9YdJcB7r

# Extract titles (filename without .txt)
acm_titles = set()
for d in paper_docs:
    fn = d.get('filename', '')
    if fn.lower().endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    acm_titles.add(title)

# Filter citations for 2018 (already filtered in query) and for titles that are in ACM papers
citation_counts = []
for rec in citations:
    t = rec.get('title')
    cc = rec.get('citation_count')
    try:
        cc_int = int(cc)
    except Exception:
        try:
            cc_int = int(float(cc))
        except Exception:
            continue
    if t in acm_titles:
        citation_counts.append(cc_int)

if len(citation_counts) > 0:
    avg = sum(citation_counts) / len(citation_counts)
    avg_rounded = round(avg, 2)
else:
    avg_rounded = None

result = {
    'average_citation_count': avg_rounded,
    'num_acm_papers_cited_in_2018': len(citation_counts),
    'acm_titles_counted': sorted(list(acm_titles))
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_OcWPVYyQeU7FtLimBt4kVF0b': ['paper_docs'], 'var_call_eqeOrs7UkbdR9tasEpB1VI3P': ['Citations', 'sqlite_sequence'], 'var_call_8TewsOi0jcGVe1hk4shl065W': 'file_storage/call_8TewsOi0jcGVe1hk4shl065W.json', 'var_call_gk7HXaThPOeG46kG9YdJcB7r': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
