code = """import json, re
fp = var_call_rTQp7MxVakpeqHDYVds2V0FT
with open(fp, 'r', encoding='utf-8') as f:
    records = json.load(f)

matches = []
for r in records:
    fn = r.get('filename')
    if not fn:
        continue
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = r.get('text','')
    # domain check
    if re.search(r'physical activity', text, re.I):
        # try to find publication year in header (first 800 chars)
        header = text[:800]
        years = re.findall(r'\b(19|20)\d{2}\b', header)
        year = None
        if years:
            # re.findall above captured only first two digits, adjust: find full matches
            full_years = re.findall(r'\b(19\d{2}|20\d{2})\b', header)
            if full_years:
                year = int(full_years[0])
        else:
            full_years = re.findall(r'\b(19\d{2}|20\d{2})\b', text)
            if full_years:
                year = int(full_years[0])
        matches.append({'title': title, 'year': year})

# filter for year == 2016
titles_2016 = [m['title'] for m in matches if m['year'] == 2016]
# deduplicate
titles_2016 = list(dict.fromkeys(titles_2016))
import json as _json
print('__RESULT__:')
print(_json.dumps(titles_2016))"""

env_args = {'var_call_rTQp7MxVakpeqHDYVds2V0FT': 'file_storage/call_rTQp7MxVakpeqHDYVds2V0FT.json', 'var_call_Ar9123p89EIcfgrCL6x9kK0s': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Charting Design Preferences on Wellness Wearables', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Communicating Uncertainty in Fertility Prognosis', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'Modeling Interdependent and Periodic Real-World Action Sequences', "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'Understanding Animals: A Critical Challenge in ACI', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating']}

exec(code, env_args)
