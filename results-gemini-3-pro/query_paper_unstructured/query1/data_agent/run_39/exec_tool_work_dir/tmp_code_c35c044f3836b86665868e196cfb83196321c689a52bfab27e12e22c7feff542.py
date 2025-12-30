code = """import json

with open(locals()['var_function-call-8131891965155681043'], 'r') as f:
    paper_docs = json.load(f)

titles = [p['filename'] for p in paper_docs]
print("__RESULT__:")
print(json.dumps({"count": len(titles), "titles": titles[:50]}))"""

env_args = {'var_function-call-8528399130518209876': ['paper_docs'], 'var_function-call-8528399130518209403': ['Citations', 'sqlite_sequence'], 'var_function-call-5911009850598284906': 'file_storage/function-call-5911009850598284906.json', 'var_function-call-5911009850598284323': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-8131891965155681043': 'file_storage/function-call-8131891965155681043.json', 'var_function-call-9545123832461402324': 'file_storage/function-call-9545123832461402324.json', 'var_function-call-16177678008665017919': {'food_papers_count': 0, 'food_papers_titles': [], 'total_citations': 0}, 'var_function-call-9443954233437372911': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'context': 'r  tracking  location  [24,30],  finances  [20],  food  [11],  weight  [19,25],  and  physical  acti'}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'context': 'projects  on  her  personal  behavior,  such  as  food  consumption  and  sneezes  (http://ellieharr'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'context': 'sist  of  avoiding  bladder  irritants  (certain  food  and  drinks)  and  consuming  a  proper  amo'}]}

exec(code, env_args)
