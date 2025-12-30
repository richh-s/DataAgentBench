code = """import json

with open(locals()['var_function-call-8395827407536305276'], 'r') as f:
    papers = json.load(f)

titles = [p.get('filename', '').replace('.txt', '') for p in papers]
print('__RESULT__:')
print(json.dumps(titles))"""

env_args = {'var_function-call-3709648201764099351': 'file_storage/function-call-3709648201764099351.json', 'var_function-call-12009379333761153785': 'file_storage/function-call-12009379333761153785.json', 'var_function-call-8395827407536305276': 'file_storage/function-call-8395827407536305276.json', 'var_function-call-12574282544977898815': [], 'var_function-call-11433524787453468215': [{'title': 'A Lived Informatics Model of Personal Informatics', 'snippet': 'r  tracking \nlocation  [24,30],  finances  [20],  food  [11],  weight  [19,25], \nand  physical  acti'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'snippet': 'projects  on  her  personal  behavior,  such  as \nfood  consumption  and  sneezes  (http://ellieharr'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'snippet': 'sist  of  avoiding  bladder  irritants \n(certain  food  and  drinks)  and  consuming  a  proper  amo'}]}

exec(code, env_args)
