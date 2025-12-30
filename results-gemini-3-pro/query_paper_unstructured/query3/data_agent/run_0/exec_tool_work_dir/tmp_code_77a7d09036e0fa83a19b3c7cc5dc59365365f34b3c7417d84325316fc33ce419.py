code = """import json
import re

file_path = locals()['var_function-call-4290533744407008086']
with open(file_path, 'r') as f:
    docs = json.load(f)

titles = []
debug = []

for doc in docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Try to find year
    # Search for specific years 2017-2024 to satisfy "after 2016"
    # We also check for 20xx in general to be sure.
    
    # We look in the first 2000 chars to be safe
    header = text[:2000]
    
    # Regex for 20xx
    matches = re.findall(r'20\d{2}', header)
    
    pub_year = 0
    if matches:
        # Convert to ints
        years = [int(m) for m in matches]
        # Filter 2000-2025
        years = [y for y in years if 2000 <= y <= 2025]
        if years:
            # Heuristic: the first year mentioned is often the publication year
            # (Venue 20xx, Copyright 20xx)
            # Sometimes the first year is a citation?
            # E.g. "Previous work (Smith 2010)..."
            # But usually the header comes first.
            pub_year = years[0]
            
            # Refinement: if the first year is < 2010 and there is a later year, maybe the first is a citation?
            # But "after 2016" means we are looking for 2017+.
            # If we extract 2010, it's filtered out.
            # If we extract 2018, we keep it.
            pass
            
    is_empirical = 'empirical' in text.lower()
    
    if pub_year > 2016 and is_empirical:
        titles.append(title)
        if len(debug) < 5:
            debug.append({"title": title, "year": pub_year, "empirical": True})

print(f"Total matching titles: {len(titles)}")
print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_function-call-1070528273488687685': ['paper_docs'], 'var_function-call-1070528273488689510': ['Citations', 'sqlite_sequence'], 'var_function-call-3440707792195880886': 'file_storage/function-call-3440707792195880886.json', 'var_function-call-4290533744407008086': 'file_storage/function-call-4290533744407008086.json', 'var_function-call-9474119233572840717': [], 'var_function-call-3308725518524162572': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'empirical': False}], 'var_function-call-11803891483283226719': {'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz"}}

exec(code, env_args)
