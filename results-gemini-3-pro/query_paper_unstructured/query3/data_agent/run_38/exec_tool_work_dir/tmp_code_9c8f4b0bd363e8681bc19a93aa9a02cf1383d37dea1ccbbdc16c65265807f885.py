code = """import json
import re

with open(locals()['var_function-call-10956757805883297717'], 'r') as f:
    papers = json.load(f)
    
with open(locals()['var_function-call-5688695509175081780'], 'r') as f:
    citations_data = json.load(f)

print("Debugging 'A Trip to the Moon'...")

# Find paper
paper = next((p for p in papers if "Trip to the Moon" in p['filename']), None)
if paper:
    fname = paper['filename']
    title_p = fname[:-4]
    text = paper['text']
    print(f"Found Paper: {fname}")
    print(f"  Title extracted: '{title_p}'")
    print(f"  Has 'empirical': {'empirical' in text.lower()}")
    print(f"  Has '2018': {'2018' in text}")
    
    # Check regex
    match = re.search(r'\b(201[7-9]|202[0-4])\b', text)
    print(f"  Regex Match: {match}")
else:
    print("Paper not found in docs.")

# Find citation
cit = next((c for c in citations_data if "Trip to the Moon" in c['title']), None)
if cit:
    title_c = cit['title']
    print(f"Found Citation: '{title_c}'")
    print(f"  Total Citations: {cit['total_citations']}")
    
    if paper:
        print(f"  Titles Match? {title_p == title_c}")
        if title_p != title_c:
            print(f"  Diff: P len {len(title_p)}, C len {len(title_c)}")
            print(f"  P: {[ord(c) for c in title_p]}")
            print(f"  C: {[ord(c) for c in title_c]}")
else:
    print("Citation not found.")

print("__RESULT__:")
print("[]")"""

env_args = {'var_function-call-5688695509175081780': 'file_storage/function-call-5688695509175081780.json', 'var_function-call-5688695509175080773': 'file_storage/function-call-5688695509175080773.json', 'var_function-call-10956757805883297717': 'file_storage/function-call-10956757805883297717.json', 'var_function-call-12897874429475959915': [], 'var_function-call-10123482125703570852': [], 'var_function-call-4464588429009855954': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'years_4d': [], 'venue_year_2d': '15', 'has_empirical': False, 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n"}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'years_4d': [], 'venue_year_2d': '15', 'has_empirical': False, 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Hum'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years_4d': [], 'venue_year_2d': None, 'has_empirical': True, 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Anima'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years_4d': [], 'venue_year_2d': None, 'has_empirical': True, 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n '}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'years_4d': [], 'venue_year_2d': None, 'has_empirical': False, 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation '}], 'var_function-call-12260434194863203705': [], 'var_function-call-14033479952836946442': [], 'var_function-call-4699397698012979875': {'sample_cit_titles': ['"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'A Lived Informatics Model of Personal Informatics'], 'sample_paper_titles': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'], 'papers': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'empirical': False, 'years_found': ['2015']}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'empirical': False, 'years_found': []}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'empirical': True, 'years_found': []}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'empirical': True, 'years_found': []}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'empirical': False, 'years_found': []}]}, 'var_function-call-15181580171572275167': []}

exec(code, env_args)
