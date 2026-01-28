code = """import json

citations_path = locals()['var_function-call-12816615437608771062']
with open(citations_path, 'r') as f:
    citations = json.load(f)

papers_path = locals()['var_function-call-6011285741143756461']
with open(papers_path, 'r') as f:
    papers = json.load(f)

debug = {}
debug['total_papers'] = len(papers)
debug['filenames'] = [p['filename'] for p in papers]

keywords_to_check = ['food', 'diet', 'nutrition', 'eating', 'meal']
keyword_counts = {k: 0 for k in keywords_to_check}

for p in papers:
    text = p.get('text', '').lower()
    for k in keywords_to_check:
        if k in text:
            keyword_counts[k] += 1

debug['keyword_counts'] = keyword_counts

print("__RESULT__:")
print(json.dumps(debug))"""

env_args = {'var_function-call-1408029875395216778': 'file_storage/function-call-1408029875395216778.json', 'var_function-call-12816615437608771062': 'file_storage/function-call-12816615437608771062.json', 'var_function-call-6011285741143756461': 'file_storage/function-call-6011285741143756461.json', 'var_function-call-4970845110660497664': 0, 'var_function-call-11335810610248278387': 'debug done', 'var_function-call-9994269108278680187': {'paper_titles_sample': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection'], 'citation_titles_sample': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'], 'food_in_text_count': 3, 'examples_with_food_in_text': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'is_food_identified': False, 'keyword_extraction_snippet': 'Lived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Locat'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'is_food_identified': False, 'keyword_extraction_snippet': 'Personal informatics, collection, reflection, model, barriers'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'is_food_identified': False, 'keyword_extraction_snippet': 'N/A'}], 'identified_food_papers_count': 0}}

exec(code, env_args)
