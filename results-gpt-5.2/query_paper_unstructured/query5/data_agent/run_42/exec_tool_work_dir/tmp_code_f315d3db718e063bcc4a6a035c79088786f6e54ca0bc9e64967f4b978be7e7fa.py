code = """import json, pandas as pd, re

cit_path = var_call_hBMNtLT3jpsx8aDxz65hoYIP
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)

papers_path = var_call_B7Nd9ZV7ZXGO00IJwzlralmQ
with open(papers_path, 'r', encoding='utf-8') as f:
    papers = json.load(f)
df_p = pd.DataFrame(papers)
df_p['title'] = df_p['filename'].str.replace(r'\.txt$','', regex=True)

pat = re.compile(r"CHI\s*20\d{2}", re.I)

def is_chi(text):
    if not isinstance(text, str):
        return False
    return bool(pat.search(text[:20000]))

df_p['is_chi'] = df_p['text'].apply(is_chi)
chi_titles = set(df_p.loc[df_p['is_chi'], 'title'])

matched = df_cit[df_cit['title'].isin(chi_titles)]

out = {
    'total_citations_2020_for_CHI_papers': int(matched['citation_count'].sum()),
    'num_CHI_papers_cited_in_2020': int(matched['title'].nunique()),
    'num_CHI_papers_in_docs': int(df_p['is_chi'].sum())
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_hBMNtLT3jpsx8aDxz65hoYIP': 'file_storage/call_hBMNtLT3jpsx8aDxz65hoYIP.json', 'var_call_B7Nd9ZV7ZXGO00IJwzlralmQ': 'file_storage/call_B7Nd9ZV7ZXGO00IJwzlralmQ.json', 'var_call_dDvhD8Tl8825uM3qly4gYxpH': {'total_citations_2020_for_CHI_papers': 0, 'num_chi_papers_with_citations_in_2020': 0, 'num_citation_records_matched': 0}, 'var_call_UewTKYCOPDUwqVlGsi9JL9zk': 'file_storage/call_UewTKYCOPDUwqVlGsi9JL9zk.json', 'var_call_orCEe0SYk7MYRvGNjFPr46f4': {'total_citations_2020_for_CHI_papers': 0, 'num_chi_papers_with_citations_in_2020': 0, 'num_chi_papers_in_docs': 0}, 'var_call_CRBDIv3pi16k8kN7jLHyNGDv': {'sample_head': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash", 'contains_CHI_20_literal_count': 43, 'regex_CHI_20yy_count': 43, 'num_docs': 99}, 'var_call_VckDTpIJ3tGhm8ktZRwNK8EZ': {'total_citations_2020_for_CHI_papers': 0, 'num_CHI_papers_cited_in_2020': 0, 'num_CHI_papers_in_docs': 0}, 'var_call_jQIjRqHUQ8ALzDO17EKRdDCw': {'num_citation_titles_2020': 188, 'num_doc_titles': 99, 'overlap_count': 68, 'overlap_examples': ['A Lived Informatics Model of Personal Informatics', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Charting Design Preferences on Wellness Wearables', 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'Communicating Uncertainty in Fertility Prognosis', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data', 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers']}, 'var_call_uHsMLeCLP7iSwJ45PTYJFW4g': {'regex_count': 0, 'literal_CHI_2019_count': 8, 'literal_examples': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Communicating Uncertainty in Fertility Prognosis', 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data', 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', "Supporting Coping with Parkinson's Disease Through Self Tracking", 'Turn to the Self in Human-Computer Interaction: Care of the Self in Negotiating the Human-Technology Relationship', 'Understanding Personal Productivity: How Knowledge Workers Define, Evaluate, and Reflect on Their Productivity']}, 'var_call_lDUsCdSbWjys5hcRer60taQ9': {'count': 43, 'examples': [{'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'match': 'CHI 2010'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'match': 'CHI 2018'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'match': 'CHI 2019'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt', 'match': 'CHI 2015'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'match': 'CHI 2016'}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'match': 'CHI 2019'}, {'filename': 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone.txt', 'match': 'CHI 2015'}, {'filename': 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units.txt', 'match': 'CHI 2015'}, {'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'match': 'CHI 2016'}, {'filename': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings.txt', 'match': 'CHI 2018'}]}}

exec(code, env_args)
