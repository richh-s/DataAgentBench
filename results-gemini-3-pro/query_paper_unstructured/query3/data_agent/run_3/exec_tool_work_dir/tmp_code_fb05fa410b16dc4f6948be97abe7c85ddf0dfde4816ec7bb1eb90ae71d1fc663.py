code = """import json
import re
import pandas as pd

# Load papers
with open(locals()['var_function-call-1637746451261953747'], 'r') as f:
    papers_data = json.load(f)

# Load citations
with open(locals()['var_function-call-1625983961919980937'], 'r') as f:
    citations_data = json.load(f)

citation_map = {}
for item in citations_data:
    try:
        count = int(item['total_citations'])
    except:
        count = 0
    citation_map[item['title']] = count

def get_year(text):
    header = text[:3000] # Increased range
    # Simple regex for 4 digits
    matches = re.findall(r'20[0-2][0-9]', header)
    valid_years = []
    for m in matches:
        y = int(m)
        if 2000 <= y <= 2024:
            valid_years.append(y)
    
    if valid_years:
        # Return the first one found
        return valid_years[0]
    
    # Fallback for '17 format
    matches_short = re.findall(r"'(\d{2})", header)
    for m in matches_short:
        y = 2000 + int(m)
        if 2000 <= y <= 2024:
            return y
    return None

results = []
for p in papers_data:
    title = p.get('filename', '').replace('.txt', '')
    text = p.get('text', '')
    
    year = get_year(text)
    is_empirical = "empirical" in text.lower()
    
    if year and year > 2016 and is_empirical:
        count = citation_map.get(title, 0)
        results.append({"title": title, "total_citation_count": count})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-1625983961919980332': 'file_storage/function-call-1625983961919980332.json', 'var_function-call-1625983961919980937': 'file_storage/function-call-1625983961919980937.json', 'var_function-call-603899956623293996': 'file_storage/function-call-603899956623293996.json', 'var_function-call-10661397933404745766': [], 'var_function-call-11800293491939370274': {'count': 5, 'years': [None, None, None, None, None], 'empirical_count': 2, 'gt_2016_count': 0}, 'var_function-call-1637746451261953747': 'file_storage/function-call-1637746451261953747.json', 'var_function-call-14546405968583665070': [{'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citation_count': 278}], 'var_function-call-16887723569607349610': 'file_storage/function-call-16887723569607349610.json', 'var_function-call-7560969263265466159': {'text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz"}, 'var_function-call-17972690823706818606': {'matches': [], 'valid_years': []}, 'var_function-call-5755365431532091131': {'repr': '"UBICOMP \'15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\\n\\nA Lived Informatics Model of Personal Informatics \\n\\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \\n1Computer Science & Engineering, 2Human Centered Design & Engineering \\nDUB Group, University of Washington \\n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \\n\\nABSTRACT \\nCurrent  models  of  how  people  use  personal  informatics \\nsystems are largely based in behavior change goals. They do \\nnot  adequately  characteriz"', 'find_2015': 29, 'surrounding': '–11, 2015, OSAK'}}

exec(code, env_args)
