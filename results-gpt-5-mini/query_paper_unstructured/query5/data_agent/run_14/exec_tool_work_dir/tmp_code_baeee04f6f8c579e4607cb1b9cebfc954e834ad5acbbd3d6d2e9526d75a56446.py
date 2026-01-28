code = """import json
# Load citations from file path stored in var_call_f4utoUHbP7qtRLyirBuusos1
with open(var_call_f4utoUHbP7qtRLyirBuusos1, 'r') as f:
    citations = json.load(f)
# paper docs results are available in var_call_RNwClUdvqlhLk77qii3kcH2t
paper_docs = var_call_RNwClUdvqlhLk77qii3kcH2t
# Build set of titles from filenames (remove .txt)
chi_titles = [p['filename'][:-4] if p['filename'].lower().endswith('.txt') else p['filename'] for p in paper_docs]
# Match and collect citation counts
per_paper = []
total = 0
for t in chi_titles:
    matches = [c for c in citations if c.get('title') == t]
    if matches:
        # Sum citation_count across matches (should be one per title for 2020)
        cnt = sum(int(m.get('citation_count', 0)) for m in matches)
        per_paper.append({'title': t, 'citation_count_2020': cnt})
        total += cnt
# Prepare result
result = {'per_paper': per_paper, 'total_citations_2020': total}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_f4utoUHbP7qtRLyirBuusos1': 'file_storage/call_f4utoUHbP7qtRLyirBuusos1.json', 'var_call_nDKvFcijrA4BhDtp8wQZrV15': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_call_RNwClUdvqlhLk77qii3kcH2t': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
