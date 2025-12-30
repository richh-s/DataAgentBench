code = """import json

path_papers = globals()['var_function-call-17219668882805826907']
with open(path_papers, 'r') as f:
    papers = json.load(f)

res = {}
res['p2'] = papers[1]['text'][:300]
res['p4'] = papers[3]['text'][:300]

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_function-call-2278250218217025444': ['paper_docs'], 'var_function-call-2278250218217023235': ['Citations', 'sqlite_sequence'], 'var_function-call-2998795241881557550': 'file_storage/function-call-2998795241881557550.json', 'var_function-call-1711006908380685270': {'start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz", 'end': '\nInferring Meal Eating Activities in Real World Settings \nfrom Ambient Sounds: A Feasibility Study. IUI 2015, \n427-431. \n\n40.  Toscos, T., Faber, A., Connelly, K., and Upoma, A.M. \n\nEncouraging Physical Activity in Teens: Can \nTechnology Help Reduce Barriers to Physical Activity \nin Adolescent Girls? PervasiveHealth 2008, 218-221. \n41.  Whooley, M., Gray, K., Ploderer, B., and Gray, K. On \n\nthe Integration of Self-tracking Data amongst \nQuantified Self Members. HCI 2014, 151-160.  \n\n742\n\n \n \n \n\x0c', 'has_empirical': False, 'lines_contrib': ['contributions  through  survey  design  and  participant  interviews.']}, 'var_function-call-137540704590043028': 'file_storage/function-call-137540704590043028.json', 'var_function-call-13928865052096685953': 'file_storage/function-call-13928865052096685953.json', 'var_function-call-17219668882805826907': 'file_storage/function-call-17219668882805826907.json', 'var_function-call-16099994179568050611': [], 'var_function-call-13201249820402721104': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'year': 2015, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'year': None, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'year': None, 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'year': None, 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'year': None, 'has_empirical': False}], 'var_function-call-4194948760569301762': 'Done'}

exec(code, env_args)
