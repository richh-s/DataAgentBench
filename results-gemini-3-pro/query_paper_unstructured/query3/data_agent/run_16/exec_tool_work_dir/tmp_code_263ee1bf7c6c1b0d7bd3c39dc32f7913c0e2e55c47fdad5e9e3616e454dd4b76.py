code = """import json
import re

citations_key = 'var_function-call-14861443508322681236'
papers_key = 'var_function-call-1947762228881266501'

with open(locals()[papers_key], 'r') as f:
    papers_data = json.load(f)

debug_info = []

for i, paper in enumerate(papers_data[:20]):
    text = paper.get('text', '')
    header = text[:1000]
    years = re.findall(r'\b(20\d{2})\b', header)
    has_empirical = 'empirical' in text.lower()
    
    debug_info.append({
        "title": paper.get('filename'),
        "years_found": years,
        "has_empirical": has_empirical
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-13973424374790880036': 'file_storage/function-call-13973424374790880036.json', 'var_function-call-13973424374790878367': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-3366737603932088961': 'file_storage/function-call-3366737603932088961.json', 'var_function-call-8593920629685848414': {'count': 5, 'samples': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'year_extracted': None, 'contrib_context': 'contributions  through  survey  design  and  participant  interviews. \nWe  also  thank  Elena  Agapi'}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'year_extracted': None, 'contrib_context': 'contributions  in  this  paper:  1)  we \nidentify  problems  across  personal  informatics  tools,  '}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'year_extracted': None, 'contrib_context': None}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'year_extracted': None, 'contrib_context': 'contribution “I like drawing!” (UP4),  some  did not like \ndrawing: “I don’t like drawing things.” ('}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'year_extracted': None, 'contrib_context': 'contribution of this research is \na  system  designed  to  support  the  work  of  occupational \nthe'}]}, 'var_function-call-1947762228881266501': 'file_storage/function-call-1947762228881266501.json', 'var_function-call-14861443508322681236': 'file_storage/function-call-14861443508322681236.json', 'var_function-call-3974080567568237': []}

exec(code, env_args)
