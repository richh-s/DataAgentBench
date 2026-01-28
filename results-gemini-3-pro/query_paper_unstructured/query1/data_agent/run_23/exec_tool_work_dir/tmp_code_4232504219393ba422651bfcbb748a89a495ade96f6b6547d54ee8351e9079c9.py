code = """import json

papers_file = locals()['var_function-call-15343742255672942069']

with open(papers_file, 'r') as f:
    papers = json.load(f)

counts = []
for paper in papers:
    text = paper.get('text', '').lower()
    count = text.count('food')
    if count > 0:
        counts.append({"title": paper.get('filename'), "count": count})

counts.sort(key=lambda x: x['count'], reverse=True)

print("__RESULT__:")
print(json.dumps(counts[:10]))"""

env_args = {'var_function-call-9331785913232115953': 'file_storage/function-call-9331785913232115953.json', 'var_function-call-2738688620942147002': 'file_storage/function-call-2738688620942147002.json', 'var_function-call-2738688620942145205': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-15343742255672940442': 'file_storage/function-call-15343742255672940442.json', 'var_function-call-15343742255672942069': 'file_storage/function-call-15343742255672942069.json', 'var_function-call-1326459099851093110': {'food_papers_count': 0, 'food_paper_titles': [], 'total_citations': 0}, 'var_function-call-2047701024969481369': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'has_food_in_text': True, 'keyword_snippet': 'Author Keywords \nLived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location. \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation '}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'has_food_in_text': True, 'keyword_snippet': 'Author Keywords \nPersonal informatics, collection, reflection, model, barriers \n\nACM Classification Keywords \nH5.m.  Information  interfaces  and  presentation  (e.g.,  HCI): \nMiscellaneous.  \n\nGenera'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'has_food_in_text': False, 'keyword_snippet': 'Author Keywords\nPersonalization; animation; emotion; engagement; empathy;\nself-reﬂection.\n\nINTRODUCTION\nThe development of mobile phone technology and biological\nsensors is enabling individuals to sel'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'has_food_in_text': True, 'keyword_snippet': ''}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'has_food_in_text': False, 'keyword_snippet': 'Author Keywords \nWearable technology; dashboard; information visualization; \nstroke rehabilitation; occupational therapy  \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation '}], 'var_function-call-3581142459715585265': {'food_papers_count': 0, 'titles': [], 'total_citations': 0}}

exec(code, env_args)
