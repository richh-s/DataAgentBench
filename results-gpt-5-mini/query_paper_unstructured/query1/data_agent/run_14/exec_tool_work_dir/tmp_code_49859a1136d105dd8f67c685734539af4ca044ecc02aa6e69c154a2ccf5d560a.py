code = """import json
# Load citations query result
p = var_call_0FCL1WyTGnR526IwZKRTkLZt
with open(p, 'r', encoding='utf-8') as f:
    citations = json.load(f)
# Load list of titles from Mongo results
titles = var_call_ZPNA8Ho1WPzG3E8llhlcUZU3
# Filter citations to only those whose title is in titles list
# Convert citation_count to int
filtered = [ { 'title': c['title'], 'citation_count': int(c['citation_count']) } for c in citations if c['title'] in titles ]
# For debugging, compute counts
from collections import defaultdict
sum_by_title = defaultdict(int)
for c in filtered:
    sum_by_title[c['title']] += c['citation_count']
# Now, we need to determine which of these are in domain 'food'.
# We don't have explicit domain field; need to infer by title matching to known food-related keywords.
food_keywords = ['food','eat','meal','nutrition','diet','eatery','restaurant','hungry','calorie','calories','feeding','nutrition']
# Select titles that contain any food keyword (case-insensitive)
food_titles = []
for t in sum_by_title:
    low = t.lower()
    if any(kw in low for kw in food_keywords):
        food_titles.append(t)
# Sum citation counts for those titles
total = sum(sum_by_title[t] for t in food_titles)
result = {
    'food_titles': food_titles,
    'total_citation_count': total
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_tLa43TtWacLVmw6hQCvEOaoS': ['paper_docs'], 'var_call_tsvwQGwqYQamcPNiDCUWMjwf': 'file_storage/call_tsvwQGwqYQamcPNiDCUWMjwf.json', 'var_call_ZPNA8Ho1WPzG3E8llhlcUZU3': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game', 'Exploring the Value of Parent Tracked Baby Data in Interactions with Healthcare Professionals: A Data-Enabled Design Exploration', 'From Nobody Cares to Way to Go!: A Design Framework for Social Sharing in Personal Informatics', 'FutureSelf: What Happens When We Forecast Self-Trackers? Future Health Statuses?', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'Heed: Exploring the Design of Situated Self-Reporting Devices', 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics', 'Modeling Interdependent and Periodic Real-World Action Sequences', 'MoodLight: Exploring Personal and Social Implications of Ambient Display of Biosensor Data', 'No Longer Wearing: Investigating the Abandonment of Personal Health-tracking Technologies on Craigslist', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'Personal Tracking of Screen Time on Digital Devices', 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness', 'Quantified Self Meets Social Media: Sharing of Weight Updates on Twitter', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'QuittyLink: Using Smartphones for Personal Counseling to Help People Quit Smoking', 'Real-life Experiences with an Adaptive Light Bracelet', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Self-tracking Cultures: Towards a Sociology of Personal Informatics', 'SleepTight: Low-burden, Self-monitoring Technology for Capturing and Reflecting on Sleep Behaviors', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'Sundroid: Solar Radiation Awareness with Smartphones', "Supporting Coping with Parkinson's Disease Through Self Tracking", 'TastyBeats: Designing Palatable Representations of Physical Activity', "The 'Self' As Barrier for Self-Management Technologies in Healthcare?", 'The Power of Mobile Notifications to Increase Wellbeing Logging Behavior', 'Tiny Habits in the Giant Enterprise: Understanding the Dynamics of a Quantified Workplace', 'Understanding Animals: A Critical Challenge in ACI', 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'Visual ODLs: Co-Designing Patient-Generated Observations of Daily Living to Support Data-Driven Conversations in Pediatric Care', "We'Ve Bin Watching You: Designing for Reflection and Social Persuasion to Promote Sustainable Lifestyles", 'What Health Topics Older Adults Want to Track: A Participatory Design Study', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating', 'Why We Use and Abandon Smart Devices'], 'var_call_0FCL1WyTGnR526IwZKRTkLZt': 'file_storage/call_0FCL1WyTGnR526IwZKRTkLZt.json'}

exec(code, env_args)
