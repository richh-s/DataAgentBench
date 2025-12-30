code = """import json

citations_path = locals()['var_function-call-9421256355430255115']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

citation_titles = [c['title'] for c in citations_data]

keywords = ["Moon", "Overactive", "Bladder", "Stage-based", "Stage based", "Lived Informatics", "ArmSleeve"]

matches = {}
for k in keywords:
    matches[k] = [t for t in citation_titles if k.lower() in t.lower()]

print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-9421256355430255115': 'file_storage/function-call-9421256355430255115.json', 'var_function-call-9421256355430255910': 'file_storage/function-call-9421256355430255910.json', 'var_function-call-10114779790998248711': {'average_citations': 68.5, 'count': 2, 'found_titles_sample': ['A Lived Informatics Model of Personal Informatics', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_function-call-18319933992546683446': {'total_citations_2018': 158, 'total_papers': 5, 'matched_papers': 2, 'acm_identified': 1, 'ieee_identified': 0, 'unknown/mixed': 1, 'sample_acm': ['A Lived Informatics Model of Personal Informatics'], 'sample_ieee': [], 'sample_unknown': ['ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'sample_unmatched': ['A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App']}, 'var_function-call-14159721120098003439': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-16332201062364115446': {'paper_results': [{'title': 'A Lived Informatics Model of Personal Informatics', 'source': 'ACM', 'citation_count': '50'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'source': 'ACM', 'citation_count': None}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'source': 'ACM', 'citation_count': None}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'source': 'ACM', 'citation_count': None}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'source': 'ACM', 'citation_count': '87'}], 'stage_citations_in_db': ['Design Opportunities in Three Stages of Relationship Development Between Users and Self-Tracking Devices']}}

exec(code, env_args)
