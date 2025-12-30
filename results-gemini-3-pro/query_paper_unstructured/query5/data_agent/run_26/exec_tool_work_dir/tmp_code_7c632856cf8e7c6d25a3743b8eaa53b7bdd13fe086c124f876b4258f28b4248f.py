code = """import json

# Load filenames
with open(locals()['var_function-call-13985119328028857859'], 'r') as f:
    data = json.load(f)
    filenames_target = set(data['filenames'])

# Load docs
with open(locals()['var_function-call-5489290469044726866'], 'r') as f:
    docs = json.load(f)
    filenames_docs = set([d['filename'] for d in docs])

# Check intersection
intersection = filenames_target.intersection(filenames_docs)
print(f"Intersection size: {len(intersection)}")

# Check specific file
specific = "A Lived Informatics Model of Personal Informatics.txt"
print(f"'{specific}' in target: {specific in filenames_target}")
print(f"'{specific}' in docs: {specific in filenames_docs}")

print("__RESULT__:")
print(json.dumps({"intersection_size": len(intersection)}))"""

env_args = {'var_function-call-2890407691846929350': ['Citations', 'sqlite_sequence'], 'var_function-call-2890407691846929759': 'file_storage/function-call-2890407691846929759.json', 'var_function-call-1018587870991830331': 'file_storage/function-call-1018587870991830331.json', 'var_function-call-13985119328028857859': 'file_storage/function-call-13985119328028857859.json', 'var_function-call-6633830581226945890': 'file_storage/function-call-6633830581226945890.json', 'var_function-call-5489290469044726866': 'file_storage/function-call-5489290469044726866.json', 'var_function-call-15377808340814584921': {'count_filenames': 188}, 'var_function-call-2561381756646521997': 'file_storage/function-call-2561381756646521997.json', 'var_function-call-8942685034973119923': True, 'var_function-call-8055407897078059507': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt']}

exec(code, env_args)
