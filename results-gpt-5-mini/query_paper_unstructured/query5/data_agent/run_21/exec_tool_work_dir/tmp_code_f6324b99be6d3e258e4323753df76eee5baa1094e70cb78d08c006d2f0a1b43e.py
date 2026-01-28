code = """import json
import pandas as pd

# Load citations result from file path stored in var_call_PoU0DZtw7CUBeQruiYOoOwKN
with open(var_call_PoU0DZtw7CUBeQruiYOoOwKN, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Load paper docs query result available in var_call_4fgDP7maQ3NhskclOIb63yc6
paper_docs = var_call_4fgDP7maQ3NhskclOIb63yc6

# Extract CHI titles from filenames (remove .txt)
chi_titles = set()
for doc in paper_docs:
    fn = doc.get('filename', '')
    if fn.lower().endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    chi_titles.add(title)

# Sum citation_count for citations where title is in chi_titles
total = 0
matched = []
for rec in citations:
    title = rec.get('title')
    # Some citation_count values are strings; convert safely
    try:
        cnt = int(rec.get('citation_count', 0))
    except Exception:
        try:
            cnt = int(float(rec.get('citation_count', 0)))
        except Exception:
            cnt = 0
    if title in chi_titles:
        total += cnt
        matched.append({'title': title, 'citation_count': cnt})

output = {'total_citations': total, 'matched_papers_count': len(matched), 'matched_papers': matched}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_PoU0DZtw7CUBeQruiYOoOwKN': 'file_storage/call_PoU0DZtw7CUBeQruiYOoOwKN.json', 'var_call_4fgDP7maQ3NhskclOIb63yc6': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
