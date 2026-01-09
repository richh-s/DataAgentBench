code = """import json
import pandas as pd

# titles deemed 2016+physical activity from previous step
pa2016_titles = set(var_call_3Nl3lNHA6RyozLd21jE6xT3c['titles'])

# load citations totals
path = var_call_Mm62QoWeB79CKaBrLJVPMxmE
with open(path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

cit_df = pd.DataFrame(cit)
# ensure numeric
cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

res = cit_df[cit_df['title'].isin(pa2016_titles)][['title','total_citations']].sort_values(['total_citations','title'], ascending=[False, True])

print('__RESULT__:')
print(res.to_json(orient='records'))"""

env_args = {'var_call_COmGVncUODl5zdBzJJcc7YJx': 'file_storage/call_COmGVncUODl5zdBzJJcc7YJx.json', 'var_call_uVaBQiXCLJw7TGNKKOOfZnPM': 'file_storage/call_uVaBQiXCLJw7TGNKKOOfZnPM.json', 'var_call_s7h3GUFNR9s82nNZARtKmwcW': {'titles': [], 'n_titles': 0}, 'var_call_dEvBFgBZgulgkPoXImZ1pn3R': 'file_storage/call_dEvBFgBZgulgkPoXImZ1pn3R.json', 'var_call_3Nl3lNHA6RyozLd21jE6xT3c': {'n_with_2016_in_text': 35, 'titles': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Charting Design Preferences on Wellness Wearables', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Communicating Uncertainty in Fertility Prognosis', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'Modeling Interdependent and Periodic Real-World Action Sequences', "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'Understanding Animals: A Critical Challenge in ACI', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating']}, 'var_call_Mm62QoWeB79CKaBrLJVPMxmE': 'file_storage/call_Mm62QoWeB79CKaBrLJVPMxmE.json'}

exec(code, env_args)
