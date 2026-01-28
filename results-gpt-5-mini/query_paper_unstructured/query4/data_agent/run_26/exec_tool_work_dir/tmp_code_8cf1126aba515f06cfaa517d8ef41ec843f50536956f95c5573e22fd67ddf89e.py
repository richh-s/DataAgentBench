code = """import json
# Load the query_db result stored in var_call_IEfkiwmOYmNR3euHuSF3nzIO (path to .json)
path = var_call_IEfkiwmOYmNR3euHuSF3nzIO
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Find filenames where text contains '2016'
titles_2016 = []
for rec in records:
    text = rec.get('text','')
    if '2016' in text:
        fn = rec.get('filename','')
        if fn.lower().endswith('.txt'):
            title = fn[:-4]
        else:
            title = fn
        titles_2016.append(title)

# Deduplicate and sort
titles_2016 = sorted(list(dict.fromkeys(titles_2016)))

import json
print("__RESULT__:")
print(json.dumps(titles_2016))"""

env_args = {'var_call_0XeobP8S9S9H03nQ0uys1TyB': ['paper_docs'], 'var_call_gh3Ip498NY8P8aIkiyg7hopu': 'file_storage/call_gh3Ip498NY8P8aIkiyg7hopu.json', 'var_call_bxebMmu7ELNQuWBmsJOdLw7Z': ['Citations', 'sqlite_sequence'], 'var_call_Dxh6tWoqsMXrvYaZbiXeaaoF': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt"}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt'}, {'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt"}, {'filename': 'Communicating Uncertainty in Fertility Prognosis.txt'}, {'filename': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt'}, {'filename': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt'}, {'filename': 'Defining Adherence: Making Sense of Physical Activity Tracker Data.txt'}, {'filename': 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease.txt'}, {'filename': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers.txt'}, {'filename': 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance.txt'}, {'filename': 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats.txt'}, {'filename': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt'}, {'filename': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal.txt'}, {'filename': 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication.txt'}, {'filename': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application.txt"}, {'filename': "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps.txt"}, {'filename': 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health.txt'}, {'filename': 'Modeling Interdependent and Periodic Real-World Action Sequences.txt'}, {'filename': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure.txt"}, {'filename': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations.txt'}, {'filename': 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome.txt'}, {'filename': 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model.txt'}, {'filename': 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis.txt'}, {'filename': 'Scaffolding for an OLM for Long-Term Physical Activity Goals.txt'}, {'filename': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video.txt'}, {'filename': 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace.txt'}, {'filename': 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model.txt'}, {'filename': 'Technologies for Everyday Life Reflection: Illustrating a Design Space.txt'}, {'filename': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices.txt'}, {'filename': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System.txt"}, {'filename': 'Understanding Animals: A Critical Challenge in ACI.txt'}, {'filename': 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating.txt'}], 'var_call_IEfkiwmOYmNR3euHuSF3nzIO': 'file_storage/call_IEfkiwmOYmNR3euHuSF3nzIO.json'}

exec(code, env_args)
