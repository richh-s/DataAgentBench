code = """import json
import re

with open(locals()['var_function-call-10956757805883297717'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-5688695509175081780'], 'r') as f:
    citations_data = json.load(f)

cit_map = {}
for c in citations_data:
    t = c['title']
    try:
        cnt = int(c['total_citations'])
    except:
        cnt = 0
    cit_map[t] = cnt

results = []

for p in papers:
    title = p['filename']
    if title.endswith('.txt'):
        title = title[:-4]
        
    text = p['text']
    
    # Combined search text (start and end)
    head = text[:2000]
    tail = text[-2000:]
    search_text = head + " " + tail
    
    # Years 2017-2024
    years_found = set()
    
    # 4-digit
    for m in re.finditer(r'\b(201[7-9]|202[0-4])\b', search_text):
        years_found.add(int(m.group(1)))
        
    # 2-digit with quote: '17, '18
    # Pattern: apostrophe then digits
    for m in re.finditer(r"'([1][7-9]|[2][0-4])\b", search_text):
        years_found.add(int("20" + m.group(1)))
        
    if not years_found:
        continue
        
    pub_year = max(years_found)
    
    # Check empirical
    # We check the WHOLE text for the word 'empirical'
    if 'empirical' in text.lower():
        if title in cit_map:
            results.append({
                "title": title,
                "total_citations": cit_map[title]
            })

results.sort(key=lambda x: x['total_citations'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5688695509175081780': 'file_storage/function-call-5688695509175081780.json', 'var_function-call-5688695509175080773': 'file_storage/function-call-5688695509175080773.json', 'var_function-call-10956757805883297717': 'file_storage/function-call-10956757805883297717.json', 'var_function-call-12897874429475959915': [], 'var_function-call-10123482125703570852': [], 'var_function-call-4464588429009855954': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'years_4d': [], 'venue_year_2d': '15', 'has_empirical': False, 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n"}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'years_4d': [], 'venue_year_2d': '15', 'has_empirical': False, 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Hum'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years_4d': [], 'venue_year_2d': None, 'has_empirical': True, 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Anima'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years_4d': [], 'venue_year_2d': None, 'has_empirical': True, 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n '}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'years_4d': [], 'venue_year_2d': None, 'has_empirical': False, 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation '}]}

exec(code, env_args)
