code = """import json, re, pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json_maybe(var_call_trlvYy8PDsbZXfgwQ6Ly84KM)
cit = load_json_maybe(var_call_hcnHLgqGIlOnchZOmx6RhUpg)

df_cit = pd.DataFrame(cit)
if not df_cit.empty:
    df_cit['total_citations'] = df_cit['total_citations'].astype(int)

def extract_year(text):
    m = re.search(r"\bCHI'16\b|\bCHI\s*2016\b|\bUbiComp\s*2016\b|\bCSCW\s*2016\b", text)
    if m:
        return 2016
    m = re.search(r"\b(19|20)\d{2}\b", text)
    # too broad; prefer copyright year
    m2 = re.search(r"\u00a9\s*(20\d{2})", text)
    if m2:
        return int(m2.group(1))
    return None

def is_physical_activity(text):
    return re.search(r"(?i)\bphysical activity\b", text) is not None

rows=[]
for d in docs:
    title = re.sub(r"(?i)\\.txt$","", d.get('filename',''))
    text = d.get('text','')
    year = extract_year(text)
    if year==2016 and is_physical_activity(text):
        rows.append({'title': title})

df = pd.DataFrame(rows).drop_duplicates()
if df.empty:
    out=[]
else:
    df = df.merge(df_cit, on='title', how='left')
    df['total_citations'] = df['total_citations'].fillna(0).astype(int)
    df = df.sort_values(['total_citations','title'], ascending=[False, True])
    out = df.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ia5jYj489eBJUeMzScw2xf5n': [], 'var_call_hcnHLgqGIlOnchZOmx6RhUpg': 'file_storage/call_hcnHLgqGIlOnchZOmx6RhUpg.json', 'var_call_ncmzi9YMBC2QrkTRZHn0voEK': 'file_storage/call_ncmzi9YMBC2QrkTRZHn0voEK.json', 'var_call_PHHSEgK0SLhYTKz3Wts3AH9w': {'candidate_titles': ['Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'Charting Design Preferences on Wellness Wearables', 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach', 'Goal-oriented Visualizations of Activity Tracking: A Case Study with Engineering Students', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'Pass the Ball: Enforced Turn-Taking in Activity Tracking', 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness', 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'Social Fabric Fitness: The Design and Evaluation of Wearable E-textile Displays to Support Group Running', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'TastyBeats: Designing Palatable Representations of Physical Activity', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'Understanding Physical Activity Through 3D Printed Material Artifacts', "When Fitness Trackers Don'T 'Fit': End-user Difficulties in the Assessment of Personal Tracking Device Accuracy"], 'candidate_count': 23}, 'var_call_trlvYy8PDsbZXfgwQ6Ly84KM': 'file_storage/call_trlvYy8PDsbZXfgwQ6Ly84KM.json'}

exec(code, env_args)
