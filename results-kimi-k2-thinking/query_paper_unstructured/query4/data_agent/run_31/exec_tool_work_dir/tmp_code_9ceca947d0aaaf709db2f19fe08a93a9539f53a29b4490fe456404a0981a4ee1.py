code = """import json

# Get the full titles list from the previous execution
exec_result = locals().get('var_functions.execute_python:10', '')
if isinstance(exec_result, dict):
    titles_2016 = exec_result.get('titles', [])
else:
    # Try to read the result as a string and parse it
    exec_result_str = str(exec_result)
    # This might be a string representation, try to extract the JSON part
    import re
    json_match = re.search(r'\{.*\}', exec_result_str, re.DOTALL)
    if json_match:
        try:
            parsed = json.loads(json_match.group())
            titles_2016 = parsed.get('titles', [])
        except:
            titles_2016 = []
    else:
        titles_2016 = []

# Since we know from the previous result we had 35 papers
# Let's reference the file directly
result_path = locals().get('var_functions.execute_python:10', '')
if isinstance(result_path, str) and '.json' in result_path:
    # Actually this is a file path
    with open(result_path, 'r') as f:
        data = json.load(f)
    titles_2016 = data.get('titles', [])
else:
    # Try to get the file path from the storage
    # The actual result is stored in a file, let's find it
    import os
    # Look for the most recent result file
    temp_dir = '/tmp'
    files = [f for f in os.listdir(temp_dir) if f.startswith('paper_docs_database') and f.endswith('.json')]
    if files:
        latest_file = max([os.path.join(temp_dir, f) for f in files], key=os.path.getctime)
        with open(latest_file, 'r') as f:
            titles_2016 = json.load(f).get('titles', [])
    else:
        titles_2016 = []

print(f"Number of titles: {len(titles_2016)}")
print('__RESULT__:')
print(json.dumps({'titles': titles_2016, 'count': len(titles_2016)}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'is_2016': True, 'has_physical_activity': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'is_2016': True, 'has_physical_activity': True}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'is_2016': True, 'has_physical_activity': True}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'is_2016': True, 'has_physical_activity': True}, {'title': 'Charting Design Preferences on Wellness Wearables', 'is_2016': True, 'has_physical_activity': True}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'is_2016': True, 'has_physical_activity': True}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'is_2016': True, 'has_physical_activity': True}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'is_2016': True, 'has_physical_activity': True}, {'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'is_2016': True, 'has_physical_activity': True}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'is_2016': True, 'has_physical_activity': True}], 'var_functions.execute_python:10': {'count': 35, 'titles': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Charting Design Preferences on Wellness Wearables', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Communicating Uncertainty in Fertility Prognosis', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'Modeling Interdependent and Periodic Real-World Action Sequences', "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'Understanding Animals: A Critical Challenge in ACI', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating']}, 'var_functions.list_db:12': ['Citations', 'sqlite_sequence'], 'var_functions.execute_python:14': {'titles_count': 35, 'titles': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Charting Design Preferences on Wellness Wearables', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Communicating Uncertainty in Fertility Prognosis', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Defining Adherence: Making Sense of Physical Activity Tracker Data']}}

exec(code, env_args)
