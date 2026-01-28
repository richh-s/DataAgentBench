code = """import json

papers_from_mongo = locals()['var_function-call-16302803230894781381']
citations_from_sqlite = locals()['var_function-call-3536484868046147804']

citations_dict = {item['title']: item['total_citations'] for item in citations_from_sqlite}

final_results = []
for paper in papers_from_mongo:
    title = paper['title']
    if title in citations_dict:
        final_results.append({'title': title, 'total_citation_count': citations_dict[title]})

print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_function-call-13855130215716654146': ['paper_docs'], 'var_function-call-12833057213824030696': 'file_storage/function-call-12833057213824030696.json', 'var_function-call-10685984074466707249': [], 'var_function-call-16302803230894781381': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2016, 'domain': 'physical activity'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2016, 'domain': 'physical activity'}], 'var_function-call-16347787836677754787': "'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'", 'var_function-call-3536484868046147804': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '265'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}]}

exec(code, env_args)
