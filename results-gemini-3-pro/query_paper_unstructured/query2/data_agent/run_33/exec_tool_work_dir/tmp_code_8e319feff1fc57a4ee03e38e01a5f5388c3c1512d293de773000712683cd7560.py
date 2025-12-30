code = """import json

citations_path = locals()['var_function-call-10128853651664279531']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Search for "Stage-based"
matches = [c for c in citations_data if "stage-based" in c['title'].lower()]

print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-10128853651664279531': 'file_storage/function-call-10128853651664279531.json', 'var_function-call-13767594165860701791': 'file_storage/function-call-13767594165860701791.json', 'var_function-call-447385373725122589': 'file_storage/function-call-447385373725122589.json', 'var_function-call-2153954921317662099': 'file_storage/function-call-2153954921317662099.json', 'var_function-call-2779362211671997774': {'matched_papers_count': 2, 'average_citations': 68.5}, 'var_function-call-18204126579925751486': {'count_citations_2018': 158, 'count_acm_papers_returned': 5, 'count_intersection': 2, 'sample_citation_titles': ['Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model', 'Problematising Upstream Technology Through Speculative Design: The Case of Quantified Cats and Dogs', 'Quantified Construction of Self: Numbers, Narratives and the Modern Individual', 'Supporting Learning by Considering Emotions: Tracking and Visualization a Case Study', 'Understanding the Cost of Driving Trips'], 'sample_acm_titles': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Stage-based Model of Personal Informatics Systems', 'A Lived Informatics Model of Personal Informatics', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_function-call-1895846447207820443': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-5330953167614813920': ['paper_docs'], 'var_function-call-8883199201736573988': {'matches': 2, 'average': 68.5, 'details': [['A Lived Informatics Model of Personal Informatics', 50], ['ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 87]]}}

exec(code, env_args)
