code = """import json
import re

path = locals()['var_function-call-454889790813745050']
with open(path, 'r') as f:
    docs = json.load(f)

extracted = []
for doc in docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Year
    year = None
    matches = re.findall(r'20[12]\d', text[:1000]) 
    # looking for 201x or 202x
    if matches:
        year = int(matches[0])
        
    # Empirical
    # Check if 'empirical' is in the text
    is_empirical = False
    if 'empirical' in text.lower():
        is_empirical = True
        
    extracted.append({"title": title, "year": year, "is_empirical": is_empirical})

print("__RESULT__:")
print(json.dumps(extracted))"""

env_args = {'var_function-call-454889790813745050': 'file_storage/function-call-454889790813745050.json', 'var_function-call-2725923968047008507': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-7236080537222007473': {'start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz", 'end': '\nInferring Meal Eating Activities in Real World Settings \nfrom Ambient Sounds: A Feasibility Study. IUI 2015, \n427-431. \n\n40.  Toscos, T., Faber, A., Connelly, K., and Upoma, A.M. \n\nEncouraging Physical Activity in Teens: Can \nTechnology Help Reduce Barriers to Physical Activity \nin Adolescent Girls? PervasiveHealth 2008, 218-221. \n41.  Whooley, M., Gray, K., Ploderer, B., and Gray, K. On \n\nthe Integration of Self-tracking Data amongst \nQuantified Self Members. HCI 2014, 151-160.  \n\n742\n\n \n \n \n\x0c'}, 'var_function-call-13029464252544165405': 'file_storage/function-call-13029464252544165405.json', 'var_function-call-7875787986985144672': 'Success', 'var_function-call-14039091801293034967': ['2015', 'None', 'None', 'None', 'None'], 'var_function-call-5957332521816669202': [{'y': '2015', 'emp': False, 'head': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA"}, {'y': 'None', 'emp': False, 'head': 'A Stage-Based Model of Personal Informatics System'}, {'y': 'None', 'emp': True, 'head': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpe'}, {'y': 'None', 'emp': True, 'head': 'A Wee Bit More Interaction: Designing and Evaluati'}, {'y': 'None', 'emp': False, 'head': 'ArmSleeve: a Patient Monitoring System to Support '}]}

exec(code, env_args)
