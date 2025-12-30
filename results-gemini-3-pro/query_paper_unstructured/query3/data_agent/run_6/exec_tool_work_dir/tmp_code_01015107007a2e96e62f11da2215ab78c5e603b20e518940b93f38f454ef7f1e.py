code = """import json
import re

# Load papers
with open(locals()['var_function-call-9482827288994489608'], 'r') as f:
    papers = json.load(f)

# Test on first paper
p = papers[0]
text = p.get('text', '')
match = re.search(r'20\d\d', text[:500])
print("__RESULT__:")
print(json.dumps({
    "filename": p['filename'],
    "match": match.group(0) if match else None,
    "first_500": text[:500]
}))"""

env_args = {'var_function-call-16968373354653802012': 'file_storage/function-call-16968373354653802012.json', 'var_function-call-12820784951702258902': ['paper_docs'], 'var_function-call-12820784951702258801': [{'cid': '0', 'name': 'id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '1'}, {'cid': '1', 'name': 'title', 'type': 'TEXT', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'citation_count', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'citation_year', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-15186585176547387853': 'file_storage/function-call-15186585176547387853.json', 'var_function-call-9482827288994489608': 'file_storage/function-call-9482827288994489608.json', 'var_function-call-9482827288994490825': 'file_storage/function-call-9482827288994490825.json', 'var_function-call-9811688043533249505': [], 'var_function-call-6165134770704943783': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'year': None, 'is_empirical': False}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'year': None, 'is_empirical': False}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'year': None, 'is_empirical': True}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'year': None, 'is_empirical': True}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'year': None, 'is_empirical': False}]}

exec(code, env_args)
