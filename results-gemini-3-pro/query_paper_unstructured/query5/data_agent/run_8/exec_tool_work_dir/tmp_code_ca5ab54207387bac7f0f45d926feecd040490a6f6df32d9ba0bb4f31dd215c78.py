code = """import json

with open(locals()['var_function-call-4961661729464848456'], 'r') as f:
    citations = json.load(f)
citation_map = {c['title']: int(c['citation_count']) for c in citations}

with open(locals()['var_function-call-14263536467630025147'], 'r') as f:
    papers = json.load(f)

headers = []
for paper in papers:
    title = paper.get('filename', '')[:-4]
    if title in citation_map:
        text = paper.get('text', '')
        header = text[:100].replace(chr(10), ' ').replace(chr(13), '')
        headers.append({"title": title, "header": header})

print("__RESULT__:")
print(json.dumps(headers[:10]))"""

env_args = {'var_function-call-4961661729464848456': 'file_storage/function-call-4961661729464848456.json', 'var_function-call-4306319526809017372': 188, 'var_function-call-9160616424066584020': 'file_storage/function-call-9160616424066584020.json', 'var_function-call-16237189493323066997': 5, 'var_function-call-14263536467630025147': 'file_storage/function-call-14263536467630025147.json', 'var_function-call-95742628409748684': 1551, 'var_function-call-6733428787577609903': 16, 'var_function-call-17501030019706782583': {'total': 16, 'papers': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 16}]}, 'var_function-call-5225444022116205832': [], 'var_function-call-14680094483701822161': [{'title': 'A Lived Informatics Model of Personal Informatics', 'match': 'CHI Year'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'match': 'CHI Year'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'match': 'Full Name'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'match': 'Full Name'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'match': 'Full Name'}]}

exec(code, env_args)
