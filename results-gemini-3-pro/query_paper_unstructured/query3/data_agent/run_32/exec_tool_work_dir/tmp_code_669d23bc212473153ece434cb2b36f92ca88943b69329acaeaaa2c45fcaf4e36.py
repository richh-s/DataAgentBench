code = """import json
import re

# Load citations
with open(locals()['var_function-call-2014635944571045995'], 'r') as f:
    citations_data = json.load(f)

# Create a map of title -> total_citations
citation_map = {}
for item in citations_data:
    t = item['title']
    c = int(item['citation_count'])
    citation_map[t] = citation_map.get(t, 0) + c

# Load papers
with open(locals()['var_function-call-3133197345042129806'], 'r') as f:
    papers = json.load(f)

results = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check empirical
    if 'empirical' not in text.lower():
        continue
        
    # Check year
    # Find all years in first 1000 chars
    years = re.findall(r'\b(20[0-9]{2})\b', text[:1000])
    
    # We want papers published AFTER 2016 (i.e. >= 2017)
    # If we find any year, we need to decide which one is the publication year.
    # Heuristic: The first year mentioned is often the publication year (header).
    # If the first year is >= 2017, we include it.
    
    if not years:
        # Try checking filename? No, filename has no year.
        continue
        
    # Take the first year found
    pub_year = int(years[0])
    
    if pub_year > 2016:
        # Check if we have citations for this title
        if title in citation_map:
            results.append({
                "title": title,
                "total_citations": citation_map[title]
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-968771099639512082': 'file_storage/function-call-968771099639512082.json', 'var_function-call-10025871425113369306': 'file_storage/function-call-10025871425113369306.json', 'var_function-call-3133197345042129806': 'file_storage/function-call-3133197345042129806.json', 'var_function-call-14920944781988559493': [], 'var_function-call-6019348044447435505': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'found_years': ['2015'], 'is_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'found_years': [], 'is_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'found_years': [], 'is_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'found_years': [], 'is_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'found_years': [], 'is_empirical': False}], 'var_function-call-15545378135994931146': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-tracking data can motivate the user towards\nconstructive self-reﬂection. One powerful form of narrative\nthat engages audience across various culture and age groups\nis animated movies. We collected a week of self-reported\nmood and behavior data from each user and created in Unity a\npersonalized animation based on their data. We evaluated the\nimpact of their video in a randomized control trial with a non-\npersonalized animated video as control. We found that person-\nalized videos tend to be more e', 'var_function-call-5052993713147510280': [{'count(*)': '1405'}], 'var_function-call-2014635944571045995': 'file_storage/function-call-2014635944571045995.json'}

exec(code, env_args)
