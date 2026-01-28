code = """import json
path = var_call_LwXl5B15tgLqZCcjdGVIbA3I
with open(path, 'r', encoding='utf-8') as f:
    citations = json.load(f)
# Convert citation_count to int
for c in citations:
    # some citation_count may be strings
    try:
        c['citation_count'] = int(c.get('citation_count', 0))
    except:
        c['citation_count'] = 0
# Load paper titles from previous result
paper_titles = var_call_M64vPShT9cYECxm0VrLgiFSo
# Identify citations for papers whose title is in paper_titles and domain mention 'food' in their paper text is not directly known here.
# But our initial Mongo query filtered documents whose text contained the word 'food', and var_call_M64vPSh... contains those filenames.
# So paper_titles are papers whose full text contains 'food' somewhere.
# We'll sum citation counts for citation records whose title matches any of these paper titles.
paper_title_set = set(paper_titles)
matched = [c for c in citations if c['title'] in paper_title_set]
# Sum citation_count
total = sum(c['citation_count'] for c in matched)
# Also prepare list of matched titles and their total counts
from collections import defaultdict
per_title = defaultdict(int)
for c in matched:
    per_title[c['title']] += c['citation_count']
result = {'total_citations_for_food_domain': total, 'per_title_counts': per_title}
# Convert per_title to regular dict
result['per_title_counts'] = dict(result['per_title_counts'])
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_FpTMMwOGOy6ZNUAgkfnMqrT5': 'file_storage/call_FpTMMwOGOy6ZNUAgkfnMqrT5.json', 'var_call_M64vPShT9cYECxm0VrLgiFSo': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game', 'Exploring the Value of Parent Tracked Baby Data in Interactions with Healthcare Professionals: A Data-Enabled Design Exploration', 'From Nobody Cares to Way to Go!: A Design Framework for Social Sharing in Personal Informatics', 'FutureSelf: What Happens When We Forecast Self-Trackers? Future Health Statuses?', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'Heed: Exploring the Design of Situated Self-Reporting Devices', 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics', 'Modeling Interdependent and Periodic Real-World Action Sequences', 'MoodLight: Exploring Personal and Social Implications of Ambient Display of Biosensor Data', 'No Longer Wearing: Investigating the Abandonment of Personal Health-tracking Technologies on Craigslist', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'Personal Tracking of Screen Time on Digital Devices', 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness', 'Quantified Self Meets Social Media: Sharing of Weight Updates on Twitter', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'QuittyLink: Using Smartphones for Personal Counseling to Help People Quit Smoking', 'Real-life Experiences with an Adaptive Light Bracelet', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Self-tracking Cultures: Towards a Sociology of Personal Informatics', 'SleepTight: Low-burden, Self-monitoring Technology for Capturing and Reflecting on Sleep Behaviors', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'Sundroid: Solar Radiation Awareness with Smartphones', "Supporting Coping with Parkinson's Disease Through Self Tracking", 'TastyBeats: Designing Palatable Representations of Physical Activity', "The 'Self' As Barrier for Self-Management Technologies in Healthcare?", 'The Power of Mobile Notifications to Increase Wellbeing Logging Behavior', 'Tiny Habits in the Giant Enterprise: Understanding the Dynamics of a Quantified Workplace', 'Understanding Animals: A Critical Challenge in ACI', 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'Visual ODLs: Co-Designing Patient-Generated Observations of Daily Living to Support Data-Driven Conversations in Pediatric Care', "We'Ve Bin Watching You: Designing for Reflection and Social Persuasion to Promote Sustainable Lifestyles", 'What Health Topics Older Adults Want to Track: A Participatory Design Study', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating', 'Why We Use and Abandon Smart Devices'], 'var_call_LwXl5B15tgLqZCcjdGVIbA3I': 'file_storage/call_LwXl5B15tgLqZCcjdGVIbA3I.json'}

exec(code, env_args)
