code = """import json
import re

# Load the MongoDB documents
mongo_result = locals()['var_functions.query_db:0']

# If it's a file path, read the file
if isinstance(mongo_result, str) and mongo_result.endswith('.json'):
    with open(mongo_result, 'r') as f:
        papers = json.load(f)
else:
    papers = mongo_result

# Load the Citations data
citations_result = locals()['var_functions.query_db:8']

# If it's a file path, read the file
if isinstance(citations_result, str) and citations_result.endswith('.json'):
    with open(citations_result, 'r') as f:
        citations = json.load(f)
else:
    citations = citations_result

# Identify papers in food domain
food_domain_papers = set()
food_keywords = ['food', 'nutrition', 'eating', 'diet', 'meal', 'dietary']

for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    title = filename.replace('.txt', '') if filename else ''
    text_lower = text.lower()
    if any(keyword in text_lower for keyword in food_keywords):
        food_domain_papers.add(title)

# Sum up citations for food domain papers
total_citations = 0

for citation in citations:
    title = citation.get('title', '')
    citation_count = int(citation.get('citation_count', 0))
    if title in food_domain_papers:
        total_citations += citation_count

# Return the total citation count as result
result = str(total_citations)
print("__RESULT__:")
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:9': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps', 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data', 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game', 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Exploring the Value of Parent Tracked Baby Data in Interactions with Healthcare Professionals: A Data-Enabled Design Exploration', 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach', 'From Nobody Cares to Way to Go!: A Design Framework for Social Sharing in Personal Informatics', 'FutureSelf: What Happens When We Forecast Self-Trackers? Future Health Statuses?', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'Heed: Exploring the Design of Situated Self-Reporting Devices', 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication', 'How to Drive a London Bus: Measuring Performance in a Mobile and Remote Workplace', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'Intelligent Computing in Personal Informatics: Key Design Considerations', "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics', 'Live Interest Meter: Learning from Quantified Feedback in Mass Lectures', 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'Modeling Interdependent and Periodic Real-World Action Sequences', 'MoodLight: Exploring Personal and Social Implications of Ambient Display of Biosensor Data', 'No Forests Without Trees: Particulars and Patterns in Visualizing Personal Communication', 'No Longer Wearing: Investigating the Abandonment of Personal Health-tracking Technologies on Craigslist', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'Opportunities for Oral Health Monitoring Technologies Beyond the Dental Clinic', 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'Pass the Ball: Enforced Turn-Taking in Activity Tracking', 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'Personal Tracking of Screen Time on Digital Devices', 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness', 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model', 'Quantified Factory Worker: Designing a Worker Feedback Dashboard', 'Quantified Self Meets Social Media: Sharing of Weight Updates on Twitter', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'QuittyLink: Using Smartphones for Personal Counseling to Help People Quit Smoking', 'Real-life Experiences with an Adaptive Light Bracelet', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Reviewing Reflection: On the Use of Reflection in Interactive System Design', 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'Self-tracking Cultures: Towards a Sociology of Personal Informatics', 'Sitting in the Same Boat: A Case Study of a Combined Awareness System and Behaviour Change Technology', 'SleepTight: Low-burden, Self-monitoring Technology for Capturing and Reflecting on Sleep Behaviors', 'Social (Media) Jet Lag: How Usage of Social Technology Can Modulate and Reflect Circadian Rhythms', 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'Sundroid: Solar Radiation Awareness with Smartphones', "Supporting Coping with Parkinson's Disease Through Self Tracking", 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'TastyBeats: Designing Palatable Representations of Physical Activity', 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', "The 'Self' As Barrier for Self-Management Technologies in Healthcare?", 'The Power of Mobile Notifications to Increase Wellbeing Logging Behavior', "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'TimeAware: Leveraging Framing Effects to Enhance Personal Productivity', 'Tiny Habits in the Giant Enterprise: Understanding the Dynamics of a Quantified Workplace', 'Understanding Animals: A Critical Challenge in ACI', 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'Understanding Personal Productivity: How Knowledge Workers Define, Evaluate, and Reflect on Their Productivity', 'Understanding Physical Activity Through 3D Printed Material Artifacts', 'Visual ODLs: Co-Designing Patient-Generated Observations of Daily Living to Support Data-Driven Conversations in Pediatric Care', "We'Ve Bin Watching You: Designing for Reflection and Social Persuasion to Promote Sustainable Lifestyles", 'What Health Topics Older Adults Want to Track: A Participatory Design Study', "When Fitness Trackers Don'T 'Fit': End-user Difficulties in the Assessment of Personal Tracking Device Accuracy", 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating', 'Why We Use and Abandon Smart Devices'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
