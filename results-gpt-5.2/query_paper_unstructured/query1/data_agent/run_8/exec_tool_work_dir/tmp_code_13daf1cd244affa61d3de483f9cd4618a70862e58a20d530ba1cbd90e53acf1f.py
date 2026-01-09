code = """import json
import pandas as pd
import re

cit_path = var_call_OIH4ZkLpKsdNZP0Jje4SjSma
with open(cit_path,'r',encoding='utf-8') as f:
    cit=json.load(f)
df_cit=pd.DataFrame(cit)
df_cit['total_citations']=pd.to_numeric(df_cit['total_citations'],errors='coerce').fillna(0).astype(int)

# food-domain approximation using keyword 'food' in paper fulltext

docs_path = var_call_cK1DMFbC05HgX1efYgTXBowY
with open(docs_path,'r',encoding='utf-8') as f:
    docs=json.load(f)
df_docs=pd.DataFrame(docs)
df_docs['title']=df_docs['filename'].str.replace(r'\\.txt$','',regex=True)
pat=re.compile(r'\\bfood\\b', re.IGNORECASE)
df_docs['has_food']=df_docs['text'].apply(lambda t: bool(pat.search(t or '')))
food_titles=set(df_docs.loc[df_docs['has_food'],'title'])

result_total=int(df_cit[df_cit['title'].isin(food_titles)]['total_citations'].sum())

print('__RESULT__:')
print(json.dumps({'total_citation_count_food_domain': result_total, 'papers_counted': len(food_titles)}))"""

env_args = {'var_call_OIH4ZkLpKsdNZP0Jje4SjSma': 'file_storage/call_OIH4ZkLpKsdNZP0Jje4SjSma.json', 'var_call_cK1DMFbC05HgX1efYgTXBowY': 'file_storage/call_cK1DMFbC05HgX1efYgTXBowY.json', 'var_call_ZEuF8mA9BPOUO7kbrArabAVw': {'total_citation_count_food_domain': 0}, 'var_call_DvjFD2WlKfbTLLMjOGAQewiZ': {'n_food_detected': 0, 'sample_titles': []}, 'var_call_kFnqBI4PoWRfGH2AVlnu7M4Z': {'n_food_keyword': 58, 'sample_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game', 'Exploring the Value of Parent Tracked Baby Data in Interactions with Healthcare Professionals: A Data-Enabled Design Exploration', 'From Nobody Cares to Way to Go!: A Design Framework for Social Sharing in Personal Informatics']}}

exec(code, env_args)
