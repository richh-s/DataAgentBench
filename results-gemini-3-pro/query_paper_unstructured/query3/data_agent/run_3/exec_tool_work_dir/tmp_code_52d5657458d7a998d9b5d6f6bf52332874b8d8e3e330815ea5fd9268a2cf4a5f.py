code = """import json
import re

with open(locals()['var_function-call-1637746451261953747'], 'r') as f:
    papers_data = json.load(f)

debug_res = {}

for p in papers_data:
    if "A Lived Informatics Model" in p['filename']:
        text = p['text']
        header = text[:2000]
        matches = re.findall(r'\b(20\d{2})\b', header)
        debug_res['matches'] = matches
        
        valid_years = []
        for m in matches:
            if 2000 <= int(m) <= 2025:
                valid_years.append(int(m))
        debug_res['valid_years'] = valid_years
        break

print("__RESULT__:")
print(json.dumps(debug_res))"""

env_args = {'var_function-call-1625983961919980332': 'file_storage/function-call-1625983961919980332.json', 'var_function-call-1625983961919980937': 'file_storage/function-call-1625983961919980937.json', 'var_function-call-603899956623293996': 'file_storage/function-call-603899956623293996.json', 'var_function-call-10661397933404745766': [], 'var_function-call-11800293491939370274': {'count': 5, 'years': [None, None, None, None, None], 'empirical_count': 2, 'gt_2016_count': 0}, 'var_function-call-1637746451261953747': 'file_storage/function-call-1637746451261953747.json', 'var_function-call-14546405968583665070': [{'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citation_count': 278}], 'var_function-call-16887723569607349610': 'file_storage/function-call-16887723569607349610.json', 'var_function-call-7560969263265466159': {'text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz"}}

exec(code, env_args)
