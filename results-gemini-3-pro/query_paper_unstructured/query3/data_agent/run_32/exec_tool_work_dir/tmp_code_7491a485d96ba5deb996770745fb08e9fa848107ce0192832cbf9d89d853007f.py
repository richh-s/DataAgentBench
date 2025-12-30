code = """import json
import re

# Load citations
with open(locals()['var_function-call-2014635944571045995'], 'r') as f:
    citations_data = json.load(f)

citation_map = {}
for item in citations_data:
    t = item['title']
    c = int(item['citation_count'])
    citation_map[t] = citation_map.get(t, 0) + c

# Load papers
with open(locals()['var_function-call-10027824828918319104'], 'r') as f:
    papers = json.load(f)

results = []
debug_info = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    is_empirical = 'empirical' in text.lower()
    
    # Heuristic for year: max year mentioned in text
    years = re.findall(r'\b(20[0-2][0-9])\b', text)
    year_ints = [int(y) for y in years if 2000 <= int(y) <= 2029]
    max_year = max(year_ints) if year_ints else 0
    
    if is_empirical and max_year > 2016:
        if title in citation_map:
            results.append({
                "title": title,
                "total_citations": citation_map[title]
            })
        else:
            # Check for near match? No, prompt says exact match.
            pass

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-968771099639512082': 'file_storage/function-call-968771099639512082.json', 'var_function-call-10025871425113369306': 'file_storage/function-call-10025871425113369306.json', 'var_function-call-3133197345042129806': 'file_storage/function-call-3133197345042129806.json', 'var_function-call-14920944781988559493': [], 'var_function-call-6019348044447435505': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'found_years': ['2015'], 'is_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'found_years': [], 'is_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'found_years': [], 'is_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'found_years': [], 'is_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'found_years': [], 'is_empirical': False}], 'var_function-call-15545378135994931146': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-tracking data can motivate the user towards\nconstructive self-reﬂection. One powerful form of narrative\nthat engages audience across various culture and age groups\nis animated movies. We collected a week of self-reported\nmood and behavior data from each user and created in Unity a\npersonalized animation based on their data. We evaluated the\nimpact of their video in a randomized control trial with a non-\npersonalized animated video as control. We found that person-\nalized videos tend to be more e', 'var_function-call-5052993713147510280': [{'count(*)': '1405'}], 'var_function-call-2014635944571045995': 'file_storage/function-call-2014635944571045995.json', 'var_function-call-10117392936548536323': [], 'var_function-call-13462427966498492264': [], 'var_function-call-3668337247189973295': {'empirical_count': 2, 'recent_count': 0, 'match_count': 0, 'total_papers': 5, 'samples': []}, 'var_function-call-10027824828918319104': 'file_storage/function-call-10027824828918319104.json'}

exec(code, env_args)
