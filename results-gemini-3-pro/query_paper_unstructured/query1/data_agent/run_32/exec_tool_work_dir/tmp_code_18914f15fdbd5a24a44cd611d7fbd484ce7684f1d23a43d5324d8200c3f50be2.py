code = """import json

with open(locals()['var_function-call-8647072041952310021'], 'r') as f:
    paper_docs = json.load(f)

with open(locals()['var_function-call-10209984453905818035'], 'r') as f:
    citations = json.load(f)

food_titles = set()

for doc in paper_docs:
    text = doc['text']
    title = doc['filename'].replace('.txt', '')
    
    # Check title
    if 'food' in title.lower():
        food_titles.add(title)
        continue
    
    # Check Keywords in first 5000 chars
    head = text[:5000]
    
    found_kw = False
    for kw_header in ["Author Keywords", "Keywords", "Index Terms", "General Terms"]:
        if kw_header in head:
            idx = head.find(kw_header)
            snippet = head[idx:idx+500]
            if 'food' in snippet.lower():
                food_titles.add(title)
                found_kw = True
                break
    
    if found_kw:
        continue

total_citations = 0
for cit in citations:
    if cit['title'] in food_titles:
        total_citations += int(cit['citation_count'])

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "food_papers": list(food_titles)}))"""

env_args = {'var_function-call-15020890105501723075': ['paper_docs'], 'var_function-call-15020890105501724646': ['Citations', 'sqlite_sequence'], 'var_function-call-10118985144780459012': 'file_storage/function-call-10118985144780459012.json', 'var_function-call-10118985144780458999': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-10209984453905821604': 'file_storage/function-call-10209984453905821604.json', 'var_function-call-10209984453905818035': 'file_storage/function-call-10209984453905818035.json', 'var_function-call-974932691459579436': {'total_citations': 0, 'food_papers': []}, 'var_function-call-7689676563908369420': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'snippet': 'r  tracking \nlocation  [24,30],  finances  [20],  food  [11],  weight  [19,25], \nand  physical  acti'}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'snippet': 'projects  on  her  personal  behavior,  such  as \nfood  consumption  and  sneezes  (http://ellieharr'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'snippet': 'sist  of  avoiding  bladder  irritants \n(certain  food  and  drinks)  and  consuming  a  proper  amo'}], 'var_function-call-3188381870738128970': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'var_function-call-18136910493045678336': 5, 'var_function-call-8647072041952310021': 'file_storage/function-call-8647072041952310021.json'}

exec(code, env_args)
