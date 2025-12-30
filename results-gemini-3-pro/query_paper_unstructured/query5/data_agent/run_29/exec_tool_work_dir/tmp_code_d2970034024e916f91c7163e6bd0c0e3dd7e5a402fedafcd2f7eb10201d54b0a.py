code = """import json

# Load citations
cit_file = locals()['var_function-call-6787168720447240942']
with open(cit_file, 'r') as f:
    citations = json.load(f)

# Get filenames
filenames = [c['title'] + ".txt" for c in citations]

# Print first 50
batch1 = filenames[:50]
print("__RESULT__:")
print(json.dumps(batch1))"""

env_args = {'var_function-call-6787168720447240942': 'file_storage/function-call-6787168720447240942.json', 'var_function-call-8317175203464136568': 'file_storage/function-call-8317175203464136568.json', 'var_function-call-11529890176534547758': 'file_storage/function-call-11529890176534547758.json', 'var_function-call-63839196414706902': {'count': 188, 'sample': {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65'}}, 'var_function-call-4721039501757598262': 'file_storage/function-call-4721039501757598262.json', 'var_function-call-4152211640730931800': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-8607789987885693285': 'file_storage/function-call-8607789987885693285.json', 'var_function-call-1079362033276818739': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-5587663968911552224': 'file_storage/function-call-5587663968911552224.json', 'var_function-call-15010692503854524086': 5}

exec(code, env_args)
