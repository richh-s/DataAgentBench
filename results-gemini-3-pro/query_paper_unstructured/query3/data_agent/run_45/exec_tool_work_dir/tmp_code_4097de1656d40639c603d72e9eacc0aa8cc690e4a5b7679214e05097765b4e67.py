code = """import json

with open(locals()['var_function-call-15772907393576741835'], 'r') as f:
    papers_data = json.load(f)

target_title = "A Wee Bit More Interaction"
target_text = ""
for p in papers_data:
    if target_title in p['filename']:
        target_text = p['text']
        break

print("__RESULT__:")
print(json.dumps(target_text[:1000]))"""

env_args = {'var_function-call-11810081531988972241': ['paper_docs'], 'var_function-call-10291775221222249891': 'file_storage/function-call-10291775221222249891.json', 'var_function-call-15772907393576741835': 'file_storage/function-call-15772907393576741835.json', 'var_function-call-6342000761403970921': 'file_storage/function-call-6342000761403970921.json', 'var_function-call-809378135484135581': [], 'var_function-call-7140887120610556425': {'total_papers': 5, 'papers_with_empirical': 2, 'papers_post_2016': 0, 'matched_titles': 5, 'sample_years': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 0, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 0, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 0, 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 0, 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 0, 'has_empirical': False}]}, 'var_function-call-14761232112250728850': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'post_2016_match': None, 'empirical': False}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'post_2016_match': None, 'empirical': False}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'post_2016_match': None, 'empirical': True}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'post_2016_match': None, 'empirical': True}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'post_2016_match': None, 'empirical': False}], 'var_function-call-10247718206001386956': [{'id': '47', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16', 'citation_year': '2020'}, {'id': '48', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '49', 'citation_year': '2021'}, {'id': '49', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '11', 'citation_year': '2022'}, {'id': '50', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '71', 'citation_year': '2023'}, {'id': '51', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '38', 'citation_year': '2024'}, {'id': '52', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '81', 'citation_year': '2025'}]}

exec(code, env_args)
