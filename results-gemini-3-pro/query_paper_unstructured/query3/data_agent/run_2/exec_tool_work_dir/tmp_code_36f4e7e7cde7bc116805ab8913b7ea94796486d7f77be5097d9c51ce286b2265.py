code = """import json
import re
import pandas as pd

# Load papers from the new file
with open(locals()['var_function-call-15266602489067932662'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-13580482470423784099'], 'r') as f:
    citations = json.load(f)

citations_df = pd.DataFrame(citations)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

results = []

venue_pattern = re.compile(r"(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*['\u2019]?\s*(\d{2,4})", re.IGNORECASE)
copyright_pattern = re.compile(r"Copyright\s+.*(20\d{2})", re.IGNORECASE)
simple_year_pattern = re.compile(r"20[0-2]\d")

for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p['text']
    
    # Use first 5000 characters
    header = text[:5000]
    
    pub_year = None
    
    # 1. Venue pattern
    v_match = venue_pattern.search(header)
    if v_match:
        y_str = v_match.group(2)
        if len(y_str) == 2:
            pub_year = 2000 + int(y_str)
        else:
            pub_year = int(y_str)
            
    # 2. Copyright pattern
    if not pub_year:
        c_match = copyright_pattern.search(header)
        if c_match:
            pub_year = int(c_match.group(1))
            
    # 3. Simple year pattern in first 500 chars (likely header)
    if not pub_year:
        s_match = simple_year_pattern.search(text[:500])
        if s_match:
            pub_year = int(s_match.group(0))
            
    is_empirical = "empirical" in text.lower()
    
    # Filter
    if pub_year and pub_year > 2016 and is_empirical:
        paper_cits = citations_df[citations_df['title'] == title]
        if not paper_cits.empty:
            total_cits = paper_cits['citation_count'].sum()
            results.append({
                "title": title,
                "total_citation_count": int(total_cits)
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-7886853940146991682': 'file_storage/function-call-7886853940146991682.json', 'var_function-call-14846085348849016055': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-13085037572156381968': 'file_storage/function-call-13085037572156381968.json', 'var_function-call-1254515193280365466': [{'COUNT(*)': '1405'}], 'var_function-call-13580482470423784099': 'file_storage/function-call-13580482470423784099.json', 'var_function-call-5769832818917747020': [], 'var_function-call-8243376314728765099': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'has_empirical': False, 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n"}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'has_empirical': False, 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Hum'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'has_empirical': True, 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Anima'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'has_empirical': True, 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n '}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'has_empirical': False, 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation '}], 'var_function-call-18154700937133714252': [], 'var_function-call-15004411282572223018': {'year_distribution': {'2015': 1}, 'empirical_count': 2, 'total_papers': 5}, 'var_function-call-5830780861978788181': 'file_storage/function-call-5830780861978788181.json', 'var_function-call-14906456097883813854': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citation_count': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citation_count': 266}], 'var_function-call-6890880714177623059': {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'extracted_year': '2018', 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-'}, 'var_function-call-8986036293657002392': {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total': 265, 'rows': [{'id': '147', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': 65, 'citation_year': '2019'}, {'id': '148', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': 98, 'citation_year': '2020'}, {'id': '149', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': 23, 'citation_year': '2021'}, {'id': '150', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': 65, 'citation_year': '2022'}, {'id': '151', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': 14, 'citation_year': '2023'}]}, 'var_function-call-9911775484962687700': 'file_storage/function-call-9911775484962687700.json', 'var_function-call-6775625562686225163': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citation_count': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citation_count': 266}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'total_citation_count': 402}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'total_citation_count': 264}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'total_citation_count': 467}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'total_citation_count': 133}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'total_citation_count': 316}, {'title': 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'total_citation_count': 327}, {'title': 'Modeling Interdependent and Periodic Real-World Action Sequences', 'total_citation_count': 296}, {'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'total_citation_count': 190}, {'title': 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'total_citation_count': 268}, {'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'total_citation_count': 404}, {'title': "Supporting Coping with Parkinson's Disease Through Self Tracking", 'total_citation_count': 191}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citation_count': 278}, {'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'total_citation_count': 72}, {'title': 'Trajectories of Engagement and Disengagement with a Story-Based Smoking Cessation App', 'total_citation_count': 48}, {'title': 'Turn to the Self in Human-Computer Interaction: Care of the Self in Negotiating the Human-Technology Relationship', 'total_citation_count': 235}, {'title': 'Understanding Animals: A Critical Challenge in ACI', 'total_citation_count': 161}, {'title': 'Understanding Personal Productivity: How Knowledge Workers Define, Evaluate, and Reflect on Their Productivity', 'total_citation_count': 306}], 'var_function-call-15266602489067932662': 'file_storage/function-call-15266602489067932662.json'}

exec(code, env_args)
