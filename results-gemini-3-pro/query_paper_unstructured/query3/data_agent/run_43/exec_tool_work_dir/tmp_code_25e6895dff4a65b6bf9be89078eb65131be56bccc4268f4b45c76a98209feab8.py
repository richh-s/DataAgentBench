code = """import json
import re

papers_file_path = locals()['var_function-call-7962722088325461616']

with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

target_title = "A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt"
paper = next((p for p in papers_data if p['filename'] == target_title), None)

if paper:
    text = paper['text'][:500]
    print("__RESULT__:")
    print(json.dumps({"title": target_title, "excerpt": text}))
else:
    print("__RESULT__:")
    print(json.dumps({"error": "Paper not found"}))"""

env_args = {'var_function-call-6384673105004028122': 'file_storage/function-call-6384673105004028122.json', 'var_function-call-11545422835381902119': 'file_storage/function-call-11545422835381902119.json', 'var_function-call-6168559912964544783': 'file_storage/function-call-6168559912964544783.json', 'var_function-call-7962722088325461616': 'file_storage/function-call-7962722088325461616.json', 'var_function-call-14142976482211745521': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}], 'var_function-call-10867487212165787391': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'years_found': [], 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'years_found': [], 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years_found': [], 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years_found': [], 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'years_found': [], 'has_empirical': False}], 'var_function-call-879949833819789779': {'excerpt': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'years': ['2015']}}

exec(code, env_args)
