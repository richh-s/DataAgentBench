code = """import json

paper_docs_path = locals()['var_function-call-15160889356619040949']

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

for doc in paper_docs:
    if "Trip to the Moon" in doc['filename']:
        print("__RESULT__:")
        print(json.dumps({"snippet": doc['text'][:500]}))
        break"""

env_args = {'var_function-call-15160889356619040949': 'file_storage/function-call-15160889356619040949.json', 'var_function-call-14370993471195573993': 'file_storage/function-call-14370993471195573993.json', 'var_function-call-3936278199097246076': [], 'var_function-call-845286639558883186': 'Done', 'var_function-call-9568601149975010194': {'total_docs': 5, 'count_year_found': 0, 'count_year_gt_2016': 0, 'count_empirical': 2, 'samples': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'extracted_year': None, 'is_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'extracted_year': None, 'is_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'extracted_year': None, 'is_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'extracted_year': None, 'is_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'extracted_year': None, 'is_empirical': False}]}, 'var_function-call-10596429833444850584': {'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz"}, 'var_function-call-5184517715911920305': {'matches': ['2015'], 'has_empirical': False, 'snippet_len': 68339}, 'var_function-call-2563683768028750558': 'file_storage/function-call-2563683768028750558.json', 'var_function-call-17415215317679155041': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': 266}], 'var_function-call-15842191870449935241': {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years': []}}

exec(code, env_args)
