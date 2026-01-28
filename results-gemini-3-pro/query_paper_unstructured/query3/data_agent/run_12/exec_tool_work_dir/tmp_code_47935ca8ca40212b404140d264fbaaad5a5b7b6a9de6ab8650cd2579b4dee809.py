code = """import json

with open(locals()['var_function-call-2108981104477433395'], 'r') as f:
    citations = json.load(f)

title = "A Trip to the Moon: Personalized Animated Movies for Self-reflection"
count = 0
for c in citations:
    if c['title'] == title:
        count += int(c['citation_count'])

print("__RESULT__:")
print(count)"""

env_args = {'var_function-call-1840327009665407502': ['paper_docs'], 'var_function-call-12708107300142329': 'file_storage/function-call-12708107300142329.json', 'var_function-call-5269555748610322771': 'file_storage/function-call-5269555748610322771.json', 'var_function-call-17632845538165496708': 'file_storage/function-call-17632845538165496708.json', 'var_function-call-2108981104477433395': 'file_storage/function-call-2108981104477433395.json', 'var_function-call-1161743497919610502': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': 265, 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': 266, 'year': 2019}], 'var_function-call-3310395966876323144': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 2010, 'empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018, 'empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 2016, 'empirical': False}], 'var_function-call-10090108131181962656': [], 'var_function-call-12219777910720063817': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}

exec(code, env_args)
