code = """import json, re
# Load the docs that contained '2016'
path = var_call_SjDbXdlbTIlTwAv4YaezRHuq
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

candidates = []
for d in docs:
    text = d.get('text','')
    if not text:
        continue
    if not re.search(r'physical activity', text, re.I):
        continue
    # Look for '2016' near the top (first 1000 chars)
    head = text[:1000]
    if re.search(r'\b2016\b', head):
        filename = d.get('filename','')
        title = filename[:-4] if filename.lower().endswith('.txt') else filename
        candidates.append(title)

# Deduplicate and sort
candidates = sorted(list(dict.fromkeys(candidates)))

import json
print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_call_MaQoQdQ19RyHzpTiYGP6O6ye': 'file_storage/call_MaQoQdQ19RyHzpTiYGP6O6ye.json', 'var_call_OxHAjomhDAL727R6akib7nUG': [], 'var_call_SjDbXdlbTIlTwAv4YaezRHuq': 'file_storage/call_SjDbXdlbTIlTwAv4YaezRHuq.json', 'var_call_fVXhCX2dTWyXDOejIG8uZim5': [], 'var_call_ErSdE1tZujPBsbnNtv5ajzjU': 'file_storage/call_ErSdE1tZujPBsbnNtv5ajzjU.json', 'var_call_CpUB1TL8mrUh1RcxxtffXFYW': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Charting Design Preferences on Wellness Wearables', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Communicating Uncertainty in Fertility Prognosis', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'Modeling Interdependent and Periodic Real-World Action Sequences', "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'Understanding Animals: A Critical Challenge in ACI', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating']}

exec(code, env_args)
