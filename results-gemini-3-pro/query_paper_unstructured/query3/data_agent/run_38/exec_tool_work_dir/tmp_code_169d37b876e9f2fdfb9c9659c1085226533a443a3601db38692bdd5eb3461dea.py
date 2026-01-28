code = """import json
import re

with open(locals()['var_function-call-10956757805883297717'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-5688695509175081780'], 'r') as f:
    citations_data = json.load(f)

print("Total Papers:", len(papers))
print("Total Citations:", len(citations_data))

print("--- Sample Citation Titles ---")
for c in citations_data[:5]:
    print(c['title'])

print("--- Sample Paper Titles ---")
for p in papers[:5]:
    print(p['filename'])

print("--- Year/Empirical Analysis (First 20) ---")
found_years = []
found_emp = 0
for p in papers[:20]:
    text = p['text']
    search_text = text[:1000] + " " + text[-1000:]
    
    ys = re.findall(r'\b(20\d\d)\b', search_text)
    ys_short = re.findall(r"'(\d\d)\b", search_text)
    
    has_emp = 'empirical' in text.lower()
    if has_emp: found_emp += 1
    
    if ys or ys_short:
        found_years.append((ys, ys_short))
        
print(f"Papers with 'empirical': {found_emp} / 20")
print(f"Years found sample: {found_years[:5]}")

print("__RESULT__:")
print("[]")"""

env_args = {'var_function-call-5688695509175081780': 'file_storage/function-call-5688695509175081780.json', 'var_function-call-5688695509175080773': 'file_storage/function-call-5688695509175080773.json', 'var_function-call-10956757805883297717': 'file_storage/function-call-10956757805883297717.json', 'var_function-call-12897874429475959915': [], 'var_function-call-10123482125703570852': [], 'var_function-call-4464588429009855954': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'years_4d': [], 'venue_year_2d': '15', 'has_empirical': False, 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n"}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'years_4d': [], 'venue_year_2d': '15', 'has_empirical': False, 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Hum'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years_4d': [], 'venue_year_2d': None, 'has_empirical': True, 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Anima'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years_4d': [], 'venue_year_2d': None, 'has_empirical': True, 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n '}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'years_4d': [], 'venue_year_2d': None, 'has_empirical': False, 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation '}], 'var_function-call-12260434194863203705': []}

exec(code, env_args)
