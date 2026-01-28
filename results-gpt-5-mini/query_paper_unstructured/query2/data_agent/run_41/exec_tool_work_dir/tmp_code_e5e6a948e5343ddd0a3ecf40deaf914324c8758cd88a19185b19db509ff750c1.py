code = """import json
from statistics import mean
# Load citations data from file path stored in var_call_2N3UiYD5P2T9axKCNxsaJHUD
citations_path = var_call_2N3UiYD5P2T9axKCNxsaJHUD
with open(citations_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)
# Build title -> citation_count mapping (int)
cit_map = {}
for rec in citations:
    title = rec.get('title')
    cc = rec.get('citation_count')
    try:
        cc_int = int(cc)
    except Exception:
        try:
            cc_int = int(float(cc))
        except Exception:
            continue
    if title:
        cit_map[title] = cc_int
# Get filenames from Mongo query result var_call_8vkhaVu1pkGIUfEvd5ODlci0
mongo_hits = var_call_8vkhaVu1pkGIUfEvd5ODlci0
filenames = [d.get('filename') for d in mongo_hits if 'filename' in d]
# Match
matched = []
for fn in filenames:
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    if title in cit_map:
        matched.append({'title': title, 'citation_count': cit_map[title]})
# Compute average
if matched:
    avg = mean([m['citation_count'] for m in matched])
    avg_val = avg
else:
    avg_val = None
# Prepare output
out = {'matched_count': len(matched), 'average_citation_count': avg_val, 'matched_records': matched}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_8vkhaVu1pkGIUfEvd5ODlci0': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_call_2N3UiYD5P2T9axKCNxsaJHUD': 'file_storage/call_2N3UiYD5P2T9axKCNxsaJHUD.json', 'var_call_Cx7lLwjtkpZiOunRsIkM9s6D': 'file_storage/call_Cx7lLwjtkpZiOunRsIkM9s6D.json'}

exec(code, env_args)
