code = """import json, re
import pandas as pd

def load_maybe_path(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

docs = load_maybe_path(var_call_R9IgLCM12ettU72Jx9kIe7Oo)
cits = load_maybe_path(var_call_gUBeyYOL6Gmwdwug8MRO0GZQ)

cits_df = pd.DataFrame(cits)
if not cits_df.empty:
    cits_df['title'] = cits_df['title'].astype(str).str.strip()
    cits_df['title_norm'] = cits_df['title'].str.replace(r'^"|"$', '', regex=True)
    cits_df['total_citations'] = pd.to_numeric(cits_df['total_citations'], errors='coerce').fillna(0).astype(int)

# simple contains-based publication year detection in first page

def is_2016(text):
    if not text:
        return False
    head = text[:3000]
    pats = [r'CHI\s*2016', r'UbiComp\s*2016', r'UBICOMP\s*2016', r'CSCW\s*2016', r'DIS\s*2016', r'\b2016\b']
    if any(re.search(p, head, flags=re.I) for p in pats):
        # try to exclude if clearly another year in venue line (e.g., CHI 2018)
        if re.search(r'CHI\s*201[0-9]', head) and not re.search(r'CHI\s*2016', head):
            return False
        if re.search(r'UbiComp\s*201[0-9]', head, flags=re.I) and not re.search(r'UbiComp\s*2016', head, flags=re.I):
            return False
        return True
    return False


def is_physical_activity_domain(text):
    if not text:
        return False
    t=text.lower()
    if 'physical activity' in t:
        return True
    pa_terms = ['fitness tracker', 'activity tracker', 'step count', 'steps', 'exercise', 'workout', 'gym', 'running', 'walking', 'sedentary']
    return sum(1 for term in pa_terms if term in t) >= 2

rows=[]
for d in docs:
    title_norm = re.sub(r'\.txt$', '', d.get('filename','')).strip()
    text = d.get('text','') or ''
    if is_2016(text) and is_physical_activity_domain(text):
        rows.append({'title_norm': title_norm})

pa2016 = pd.DataFrame(rows).drop_duplicates()
if pa2016.empty:
    result=[]
else:
    out = pa2016.merge(cits_df[['title_norm','total_citations','title']], on='title_norm', how='left')
    out['title'] = out['title'].fillna(out['title_norm'])
    out['total_citations'] = out['total_citations'].fillna(0).astype(int)
    out = out[['title','total_citations']].drop_duplicates().sort_values(['total_citations','title'], ascending=[False, True])
    result = out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_R9IgLCM12ettU72Jx9kIe7Oo': 'file_storage/call_R9IgLCM12ettU72Jx9kIe7Oo.json', 'var_call_gUBeyYOL6Gmwdwug8MRO0GZQ': 'file_storage/call_gUBeyYOL6Gmwdwug8MRO0GZQ.json', 'var_call_9T85sfQncAHyEmWHKS7XU84O': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'Charting Design Preferences on Wellness Wearables.txt', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings.txt', 'Communicating Uncertainty in Fertility Prognosis.txt', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt', 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data.txt', 'Defining Adherence: Making Sense of Physical Activity Tracker Data.txt', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease.txt', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers.txt', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance.txt', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats.txt', 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game.txt', 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing.txt', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt', 'Exploring the Value of Parent Tracked Baby Data in Interactions with Healthcare Professionals: A Data-Enabled Design Exploration.txt', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal.txt', 'Heed: Exploring the Design of Situated Self-Reporting Devices.txt', 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication.txt', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application.txt", "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps.txt", 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics.txt', 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health.txt', 'Modeling Interdependent and Periodic Real-World Action Sequences.txt', "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure.txt", 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', 'Opportunities for Oral Health Monitoring Technologies Beyond the Dental Clinic.txt', 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations.txt', 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome.txt', 'Personal Tracking of Screen Time on Digital Devices.txt', 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model.txt', 'Quantified Factory Worker: Designing a Worker Feedback Dashboard.txt', 'Quantified Self Meets Social Media: Sharing of Weight Updates on Twitter.txt', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis.txt', 'Scaffolding for an OLM for Long-Term Physical Activity Goals.txt', 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video.txt', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace.txt', "Supporting Coping with Parkinson's Disease Through Self Tracking.txt", 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model.txt', 'Technologies for Everyday Life Reflection: Illustrating a Design Space.txt', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices.txt', "The 'Self' As Barrier for Self-Management Technologies in Healthcare?.txt", "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System.txt", 'TimeAware: Leveraging Framing Effects to Enhance Personal Productivity.txt', 'Trajectories of Engagement and Disengagement with a Story-Based Smoking Cessation App.txt']}

exec(code, env_args)
