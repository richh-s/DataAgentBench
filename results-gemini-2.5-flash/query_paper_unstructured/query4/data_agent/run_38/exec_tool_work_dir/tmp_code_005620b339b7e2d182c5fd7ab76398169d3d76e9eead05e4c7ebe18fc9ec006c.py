code = """import json
papers_2016_physical_activity = locals()['var_function-call-714282228086737627']
titles = [p['title'] for p in papers_2016_physical_activity]

print('__RESULT__:')
print(json.dumps(titles))"""

env_args = {'var_function-call-7385341935782596137': ['paper_docs'], 'var_function-call-15754045851250025291': ['Citations', 'sqlite_sequence'], 'var_function-call-7689240133367752773': 'file_storage/function-call-7689240133367752773.json', 'var_function-call-7978600574837803930': [], 'var_function-call-714282228086737627': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2016, 'domain': 'physical activity'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2016, 'domain': 'physical activity'}]}

exec(code, env_args)
