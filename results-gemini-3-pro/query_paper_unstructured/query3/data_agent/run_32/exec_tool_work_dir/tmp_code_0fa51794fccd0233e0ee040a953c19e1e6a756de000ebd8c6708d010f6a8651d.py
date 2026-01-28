code = """import json
import re

# Load citations
with open(locals()['var_function-call-2014635944571045995'], 'r') as f:
    citations_data = json.load(f)

# Map title to total citations
citation_map = {}
for item in citations_data:
    t = item['title']
    c = int(item['citation_count'])
    citation_map[t] = citation_map.get(t, 0) + c

# Load papers
with open(locals()['var_function-call-10027824828918319104'], 'r') as f:
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
    # Use loose regex to catch years
    years = re.findall(r'20[0-9]{2}', text)
    year_ints = []
    for y in years:
        iy = int(y)
        if 2000 <= iy <= 2029:
            year_ints.append(iy)
            
    if not year_ints:
        continue
        
    # Use max year as proxy for publication year (or at least validity)
    # If max year > 2016, we assume it's published > 2016
    max_year = max(year_ints)
    
    if max_year > 2016:
        if title in citation_map:
            results.append({
                "title": title,
                "total_citation_count": citation_map[title]
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-968771099639512082': 'file_storage/function-call-968771099639512082.json', 'var_function-call-10025871425113369306': 'file_storage/function-call-10025871425113369306.json', 'var_function-call-3133197345042129806': 'file_storage/function-call-3133197345042129806.json', 'var_function-call-14920944781988559493': [], 'var_function-call-6019348044447435505': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'found_years': ['2015'], 'is_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'found_years': [], 'is_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'found_years': [], 'is_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'found_years': [], 'is_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'found_years': [], 'is_empirical': False}], 'var_function-call-15545378135994931146': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-tracking data can motivate the user towards\nconstructive self-reﬂection. One powerful form of narrative\nthat engages audience across various culture and age groups\nis animated movies. We collected a week of self-reported\nmood and behavior data from each user and created in Unity a\npersonalized animation based on their data. We evaluated the\nimpact of their video in a randomized control trial with a non-\npersonalized animated video as control. We found that person-\nalized videos tend to be more e', 'var_function-call-5052993713147510280': [{'count(*)': '1405'}], 'var_function-call-2014635944571045995': 'file_storage/function-call-2014635944571045995.json', 'var_function-call-10117392936548536323': [], 'var_function-call-13462427966498492264': [], 'var_function-call-3668337247189973295': {'empirical_count': 2, 'recent_count': 0, 'match_count': 0, 'total_papers': 5, 'samples': []}, 'var_function-call-10027824828918319104': 'file_storage/function-call-10027824828918319104.json', 'var_function-call-49147365760216548': [], 'var_function-call-12523744160132439239': {'citation_db_max_citation_year': 0, 'sample_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'max_year': 0, 'is_empirical': False, 'in_citations': True}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'max_year': 0, 'is_empirical': False, 'in_citations': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'max_year': 0, 'is_empirical': True, 'in_citations': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'max_year': 0, 'is_empirical': True, 'in_citations': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'max_year': 0, 'is_empirical': False, 'in_citations': True}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'max_year': 0, 'is_empirical': True, 'in_citations': True}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'max_year': 0, 'is_empirical': False, 'in_citations': True}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'max_year': 0, 'is_empirical': False, 'in_citations': True}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'max_year': 0, 'is_empirical': False, 'in_citations': True}, {'title': 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone', 'max_year': 0, 'is_empirical': False, 'in_citations': True}, {'title': 'Charting Design Preferences on Wellness Wearables', 'max_year': 0, 'is_empirical': True, 'in_citations': True}, {'title': 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units', 'max_year': 0, 'is_empirical': False, 'in_citations': True}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'max_year': 0, 'is_empirical': True, 'in_citations': True}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'max_year': 0, 'is_empirical': True, 'in_citations': True}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'max_year': 0, 'is_empirical': True, 'in_citations': True}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'max_year': 0, 'is_empirical': True, 'in_citations': True}, {'title': 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps', 'max_year': 0, 'is_empirical': False, 'in_citations': True}, {'title': 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym', 'max_year': 0, 'is_empirical': False, 'in_citations': True}, {'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'max_year': 0, 'is_empirical': False, 'in_citations': True}, {'title': 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data', 'max_year': 0, 'is_empirical': False, 'in_citations': True}]}, 'var_function-call-17472719601007293343': {'preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'years_found': ['2015', '2015', '2015', '2015', '2015', '2015', '2015', '2015', '2014', '2013'], 'type_text': "<class 'str'>"}}

exec(code, env_args)
