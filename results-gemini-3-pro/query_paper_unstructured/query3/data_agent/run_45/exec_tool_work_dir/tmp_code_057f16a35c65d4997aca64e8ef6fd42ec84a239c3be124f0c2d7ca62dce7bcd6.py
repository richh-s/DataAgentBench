code = """import json
import re

with open(locals()['var_function-call-15772907393576741835'], 'r') as f:
    papers_data = json.load(f)

print("__RESULT__:")
info = []
for p in papers_data:
    header = p['text'][:500]
    # Simple regex
    matches = re.findall(r'20\d{2}', header)
    info.append({
        "title": p['filename'],
        "header_snippet": header.replace('\n', ' ')[:100],
        "matches": matches
    })
print(json.dumps(info))"""

env_args = {'var_function-call-11810081531988972241': ['paper_docs'], 'var_function-call-10291775221222249891': 'file_storage/function-call-10291775221222249891.json', 'var_function-call-15772907393576741835': 'file_storage/function-call-15772907393576741835.json', 'var_function-call-6342000761403970921': 'file_storage/function-call-6342000761403970921.json', 'var_function-call-809378135484135581': [], 'var_function-call-7140887120610556425': {'total_papers': 5, 'papers_with_empirical': 2, 'papers_post_2016': 0, 'matched_titles': 5, 'sample_years': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 0, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 0, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 0, 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 0, 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 0, 'has_empirical': False}]}}

exec(code, env_args)
