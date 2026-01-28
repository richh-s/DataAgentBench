code = """import json

# Get the 2016 papers list from the previous execution
paper_2016_list = locals()['var_functions.execute_python:12']

# Read the citation data from the file
citation_file = locals()['var_functions.query_db:14']
with open(citation_file, 'r') as f:
    citations = json.load(f)

# Create a dictionary to store total citations per paper title
citations_dict = {}
for citation in citations:
    title = citation['title']
    count = int(citation['citation_count'])
    
    if title not in citations_dict:
        citations_dict[title] = 0
    citations_dict[title] += count

# Filter for physical activity papers from 2016
physical_activity_papers = []

for paper in paper_2016_list:
    title = paper['title']
    text = paper.get('text', '')
    
    # Check if paper is in physical activity domain
    # Look for keywords related to physical activity
    physical_activity_keywords = [
        'physical activity',
        'activity tracker',
        'fitness',
        'exercise',
        'step counting',
        'sedentary behavior',
        'step-counting',
        'activity tracking'
    ]
    
    text_lower = text.lower()
    is_physical_activity = any(keyword in text_lower for keyword in physical_activity_keywords)
    
    if is_physical_activity:
        total_citations = citations_dict.get(title, 0)
        physical_activity_papers.append({
            'title': title,
            'total_citations': total_citations
        })

print('__RESULT__:')
print(json.dumps(physical_activity_papers, ensure_ascii=False, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:12': [{'_id': '694f5530284b10b11dc0a86b', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a86c', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a870', 'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a871', 'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'has_2016': True}, {'_id': '694f5530284b10b11dc0a873', 'title': 'Charting Design Preferences on Wellness Wearables', 'filename': 'Charting Design Preferences on Wellness Wearables.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a875', 'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'has_2016': True}, {'_id': '694f5530284b10b11dc0a877', 'title': 'Communicating Uncertainty in Fertility Prognosis', 'filename': 'Communicating Uncertainty in Fertility Prognosis.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a878', 'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'filename': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a87b', 'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'filename': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a87d', 'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'filename': 'Defining Adherence: Making Sense of Physical Activity Tracker Data.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a87f', 'title': 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'filename': 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a880', 'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'filename': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a881', 'title': 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'filename': 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a882', 'title': 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'filename': 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a885', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'filename': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a88b', 'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'filename': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a88d', 'title': 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication', 'filename': 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a88f', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'filename': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application.txt", 'has_2016': True}, {'_id': '694f5530284b10b11dc0a891', 'title': "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'filename': "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps.txt", 'has_2016': True}, {'_id': '694f5530284b10b11dc0a895', 'title': 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'filename': 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a896', 'title': 'Modeling Interdependent and Periodic Real-World Action Sequences', 'filename': 'Modeling Interdependent and Periodic Real-World Action Sequences.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a897', 'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'filename': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure.txt", 'has_2016': True}, {'_id': '694f5530284b10b11dc0a89d', 'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'filename': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a89f', 'title': 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'filename': 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a8a3', 'title': 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model', 'filename': 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a8a6', 'title': 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'filename': 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a8ac', 'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'filename': 'Scaffolding for an OLM for Long-Term Physical Activity Goals.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a8b2', 'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'filename': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a8b4', 'title': 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'filename': 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a8b7', 'title': 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'filename': 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a8b9', 'title': 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'filename': 'Technologies for Everyday Life Reflection: Illustrating a Design Space.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a8ba', 'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'filename': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a8bd', 'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'filename': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System.txt", 'has_2016': True}, {'_id': '694f5530284b10b11dc0a8c2', 'title': 'Understanding Animals: A Critical Challenge in ACI', 'filename': 'Understanding Animals: A Critical Challenge in ACI.txt', 'has_2016': True}, {'_id': '694f5530284b10b11dc0a8ca', 'title': 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating', 'filename': 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating.txt', 'has_2016': True}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
