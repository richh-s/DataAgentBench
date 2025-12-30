code = """import json

extracted_papers = json.loads(locals()['var_function-call-16302803230894781381'])
titles = [paper['title'] for paper in extracted_papers]

# Prepare titles for SQL IN clause
titles_str = ', '.join([f"'{title.replace("'", "''")}'" for title in titles])

print('__RESULT__:')
print(json.dumps(titles_str))"""

env_args = {'var_function-call-13855130215716654146': ['paper_docs'], 'var_function-call-12833057213824030696': 'file_storage/function-call-12833057213824030696.json', 'var_function-call-10685984074466707249': [], 'var_function-call-16302803230894781381': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2016, 'domain': 'physical activity'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2016, 'domain': 'physical activity'}]}

exec(code, env_args)
