code = """import json
# var_call_PvmEIqK2AFrZXeTv6gK1yJpF contains the citation records for 2018 (from SQLite)
records = var_call_PvmEIqK2AFrZXeTv6gK1yJpF
counts = []
for r in records:
    v = r.get('citation_count')
    if v is None:
        continue
    try:
        c = int(v)
    except Exception:
        try:
            c = int(float(v))
        except Exception:
            continue
    counts.append(c)
if counts:
    avg = sum(counts) / len(counts)
else:
    avg = None
result = {"average_citation_count": avg, "paper_count": len(counts)}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WtmpuuaUZ5enAbf7oGZkDOXa': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_call_PvmEIqK2AFrZXeTv6gK1yJpF': [{'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '50'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': '87'}]}

exec(code, env_args)
