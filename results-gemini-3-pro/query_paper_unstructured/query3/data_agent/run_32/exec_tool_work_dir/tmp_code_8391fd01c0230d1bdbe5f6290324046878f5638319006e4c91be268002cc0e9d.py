code = """import json
import re

with open(locals()['var_function-call-2014635944571045995'], 'r') as f:
    citations_data = json.load(f)
citation_titles = set(item['title'] for item in citations_data)
citation_years = [int(item['citation_year']) for item in citations_data if 'citation_year' in item]
max_citation_year = max(citation_years) if citation_years else 0

with open(locals()['var_function-call-10027824828918319104'], 'r') as f:
    papers = json.load(f)

debug_list = []
matches_found = 0
recent_found = 0

for p in papers[:20]:
    title = p.get('filename', '').replace('.txt', '')
    text = p.get('text', '')
    years = re.findall(r'\b(20[0-2][0-9])\b', text)
    year_ints = [int(y) for y in years if 2000 <= int(y) <= 2029]
    max_year = max(year_ints) if year_ints else 0
    is_empirical = 'empirical' in text.lower()
    
    in_citations = title in citation_titles
    
    debug_list.append({
        "title": title,
        "max_year": max_year,
        "is_empirical": is_empirical,
        "in_citations": in_citations
    })

print("__RESULT__:")
print(json.dumps({
    "citation_db_max_citation_year": max_citation_year,
    "sample_papers": debug_list
}))"""

env_args = {'var_function-call-968771099639512082': 'file_storage/function-call-968771099639512082.json', 'var_function-call-10025871425113369306': 'file_storage/function-call-10025871425113369306.json', 'var_function-call-3133197345042129806': 'file_storage/function-call-3133197345042129806.json', 'var_function-call-14920944781988559493': [], 'var_function-call-6019348044447435505': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'found_years': ['2015'], 'is_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'found_years': [], 'is_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'found_years': [], 'is_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'found_years': [], 'is_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'found_years': [], 'is_empirical': False}], 'var_function-call-15545378135994931146': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-tracking data can motivate the user towards\nconstructive self-reﬂection. One powerful form of narrative\nthat engages audience across various culture and age groups\nis animated movies. We collected a week of self-reported\nmood and behavior data from each user and created in Unity a\npersonalized animation based on their data. We evaluated the\nimpact of their video in a randomized control trial with a non-\npersonalized animated video as control. We found that person-\nalized videos tend to be more e', 'var_function-call-5052993713147510280': [{'count(*)': '1405'}], 'var_function-call-2014635944571045995': 'file_storage/function-call-2014635944571045995.json', 'var_function-call-10117392936548536323': [], 'var_function-call-13462427966498492264': [], 'var_function-call-3668337247189973295': {'empirical_count': 2, 'recent_count': 0, 'match_count': 0, 'total_papers': 5, 'samples': []}, 'var_function-call-10027824828918319104': 'file_storage/function-call-10027824828918319104.json', 'var_function-call-49147365760216548': []}

exec(code, env_args)
