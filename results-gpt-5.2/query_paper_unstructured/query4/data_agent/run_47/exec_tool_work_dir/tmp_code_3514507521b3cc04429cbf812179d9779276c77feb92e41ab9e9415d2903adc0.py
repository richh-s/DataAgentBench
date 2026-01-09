code = """import json, re
import pandas as pd

path_docs = var_call_YkrjMPak7QxHgwZozXZKkYpW
with open(path_docs,'r',encoding='utf-8') as f:
    docs=json.load(f)

pa_docs=[d for d in docs if re.search(r'physical\s+activity', d.get('text',''), re.IGNORECASE)]

def pub_year(text):
    head=text[:5000]
    m=re.search(r"Copyright\s+(?:\d{4}\s*)?\u00a9\s*(19\d{2}|20\d{2})", head, re.IGNORECASE)
    if m:
        return int(m.group(1))
    m=re.search(r"\bCopyright\s*(19\d{2}|20\d{2})", head, re.IGNORECASE)
    if m:
        return int(m.group(1))
    m=re.search(r"\bCHI\s+(19\d{2}|20\d{2})\b", head)
    if m:
        return int(m.group(1))
    m=re.search(r"\bUbiComp\s+'?(\d{2})\b", head, re.IGNORECASE)
    if m:
        return 2000+int(m.group(1))
    m=re.search(r"\bUbiComp\s+(19\d{2}|20\d{2})\b", head, re.IGNORECASE)
    if m:
        return int(m.group(1))
    m=re.search(r"\bCSCW\s+(19\d{2}|20\d{2})\b", head)
    if m:
        return int(m.group(1))
    m=re.search(r"\bDIS\s+(19\d{2}|20\d{2})\b", head)
    if m:
        return int(m.group(1))
    years=[int(y) for y in re.findall(r"\b(19\d{2}|20\d{2})\b", head)]
    years=[y for y in years if 2000<=y<=2030]
    return years[0] if years else None

parsed=[]
for d in pa_docs:
    t=d['filename'][:-4]
    y=pub_year(d.get('text','') or '')
    parsed.append({'title':t,'pub_year':y})

df=pd.DataFrame(parsed)
res=df[df.pub_year==2016].sort_values('title')
print('__RESULT__:')
print(json.dumps({'n_pa_docs_with_2016':int(len(res)),'titles':res.to_dict(orient='records')}))"""

env_args = {'var_call_EdI5tfxdG7NthR2A0PqHgMLO': 'file_storage/call_EdI5tfxdG7NthR2A0PqHgMLO.json', 'var_call_saVRj1ZwzmtyAiRdfptdqatS': 'file_storage/call_saVRj1ZwzmtyAiRdfptdqatS.json', 'var_call_pXsj2WWCsxISUEttDET8u11L': [], 'var_call_KoGnYhKD8RfOl2mYVNII5E8K': {'cand_count': 0, 'year_counts_top20': {'null': 68}, 'sample_pa_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone', 'Charting Design Preferences on Wellness Wearables', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'Communicating Uncertainty in Fertility Prognosis', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps', 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers']}, 'var_call_YkrjMPak7QxHgwZozXZKkYpW': 'file_storage/call_YkrjMPak7QxHgwZozXZKkYpW.json'}

exec(code, env_args)
