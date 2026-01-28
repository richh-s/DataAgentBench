code = """import json
import re

with open(locals()['var_function-call-2014635944571045995'], 'r') as f:
    citations_data = json.load(f)

citation_map = {item['title']: True for item in citations_data}

with open(locals()['var_function-call-3133197345042129806'], 'r') as f:
    papers = json.load(f)

empirical_count = 0
recent_count = 0
match_count = 0

debug_samples = []

for p in papers:
    text = p.get('text', '')
    title = p.get('filename', '').replace('.txt', '')
    
    is_empirical = 'empirical' in text.lower()
    if is_empirical:
        empirical_count += 1
        
    years = re.findall(r'\b(20[0-2][0-9])\b', text)
    year_ints = [int(y) for y in years]
    max_year = max(year_ints) if year_ints else 0
    
    if max_year > 2016:
        recent_count += 1
        
    if is_empirical and max_year > 2016:
        if title in citation_map:
            match_count += 1
            debug_samples.append(title)
        else:
            # Maybe title mismatch?
            if len(debug_samples) < 5:
                debug_samples.append(f"MISSING: {title}")

print("__RESULT__:")
print(json.dumps({
    "empirical_count": empirical_count,
    "recent_count": recent_count,
    "match_count": match_count,
    "total_papers": len(papers),
    "samples": debug_samples
}))"""

env_args = {'var_function-call-968771099639512082': 'file_storage/function-call-968771099639512082.json', 'var_function-call-10025871425113369306': 'file_storage/function-call-10025871425113369306.json', 'var_function-call-3133197345042129806': 'file_storage/function-call-3133197345042129806.json', 'var_function-call-14920944781988559493': [], 'var_function-call-6019348044447435505': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'found_years': ['2015'], 'is_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'found_years': [], 'is_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'found_years': [], 'is_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'found_years': [], 'is_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'found_years': [], 'is_empirical': False}], 'var_function-call-15545378135994931146': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-tracking data can motivate the user towards\nconstructive self-reﬂection. One powerful form of narrative\nthat engages audience across various culture and age groups\nis animated movies. We collected a week of self-reported\nmood and behavior data from each user and created in Unity a\npersonalized animation based on their data. We evaluated the\nimpact of their video in a randomized control trial with a non-\npersonalized animated video as control. We found that person-\nalized videos tend to be more e', 'var_function-call-5052993713147510280': [{'count(*)': '1405'}], 'var_function-call-2014635944571045995': 'file_storage/function-call-2014635944571045995.json', 'var_function-call-10117392936548536323': [], 'var_function-call-13462427966498492264': []}

exec(code, env_args)
