code = """import json, re
import pandas as pd

# load 2016 copyright docs
path = var_call_SRbWbCl15gJkaacw5c0zpXpb
with open(path,'r',encoding='utf-8') as f:
    docs=json.load(f)

# identify physical activity domain: contains 'physical activity' AND ('exercise' or 'activity tracker' or 'step' etc) OR venue is PA-related
pa=[]
for d in docs:
    text=d.get('text','') or ''
    if re.search(r'physical\s+activity', text, re.IGNORECASE):
        pa.append(d['filename'][:-4])

pa=sorted(set(pa))
print('__RESULT__:')
print(json.dumps({'n':len(pa),'titles':pa}))"""

env_args = {'var_call_EdI5tfxdG7NthR2A0PqHgMLO': 'file_storage/call_EdI5tfxdG7NthR2A0PqHgMLO.json', 'var_call_saVRj1ZwzmtyAiRdfptdqatS': 'file_storage/call_saVRj1ZwzmtyAiRdfptdqatS.json', 'var_call_pXsj2WWCsxISUEttDET8u11L': [], 'var_call_KoGnYhKD8RfOl2mYVNII5E8K': {'cand_count': 0, 'year_counts_top20': {'null': 68}, 'sample_pa_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone', 'Charting Design Preferences on Wellness Wearables', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'Communicating Uncertainty in Fertility Prognosis', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps', 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers']}, 'var_call_YkrjMPak7QxHgwZozXZKkYpW': 'file_storage/call_YkrjMPak7QxHgwZozXZKkYpW.json', 'var_call_QMalNElfmj5VR1o2KvIkKfcy': {'n_pa_docs_with_2016': 0, 'titles': []}, 'var_call_rDvrIshyma8K8M9la9gG4va2': 'file_storage/call_rDvrIshyma8K8M9la9gG4va2.json', 'var_call_SRbWbCl15gJkaacw5c0zpXpb': 'file_storage/call_SRbWbCl15gJkaacw5c0zpXpb.json'}

exec(code, env_args)
