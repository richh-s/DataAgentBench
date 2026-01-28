code = """import json
import os

# Find the actual file from the first query
paper_query_result = locals().get('var_functions.query_db:2', '')
print(f"Paper query result path: {paper_query_result}")

if paper_query_result and os.path.exists(paper_query_result):
    with open(paper_query_result, 'r') as f:
        papers = json.load(f)
    
    # Extract titles for papers from 2016 in physical activity domain
    titles_2016_physical_activity = []
    for paper in papers:
        filename = paper.get('filename', '')
        title = filename.replace('.txt', '') if filename else ''
        text = paper.get('text', '')
        
        # Check if paper mentions 2016 and physical activity
        has_2016 = '2016' in text
        has_physical_activity = 'physical activity' in text.lower()
        
        if has_2016 and has_physical_activity and title:
            titles_2016_physical_activity.append(title)
    
    print(f"Found {len(titles_2016_physical_activity)} papers")
    
    # Save to a more accessible variable
    result = {
        'titles': titles_2016_physical_activity,
        'count': len(titles_2016_physical_activity)
    }
else:
    print("File not found")
    result = {'titles': [], 'count': 0}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'is_2016': True, 'has_physical_activity': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'is_2016': True, 'has_physical_activity': True}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'is_2016': True, 'has_physical_activity': True}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'is_2016': True, 'has_physical_activity': True}, {'title': 'Charting Design Preferences on Wellness Wearables', 'is_2016': True, 'has_physical_activity': True}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'is_2016': True, 'has_physical_activity': True}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'is_2016': True, 'has_physical_activity': True}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'is_2016': True, 'has_physical_activity': True}, {'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'is_2016': True, 'has_physical_activity': True}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'is_2016': True, 'has_physical_activity': True}], 'var_functions.execute_python:10': {'count': 35, 'titles': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Charting Design Preferences on Wellness Wearables', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Communicating Uncertainty in Fertility Prognosis', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'Modeling Interdependent and Periodic Real-World Action Sequences', "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'Understanding Animals: A Critical Challenge in ACI', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating']}, 'var_functions.list_db:12': ['Citations', 'sqlite_sequence'], 'var_functions.execute_python:14': {'titles_count': 35, 'titles': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Charting Design Preferences on Wellness Wearables', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Communicating Uncertainty in Fertility Prognosis', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Defining Adherence: Making Sense of Physical Activity Tracker Data']}, 'var_functions.execute_python:16': {'titles': [], 'count': 0}}

exec(code, env_args)
