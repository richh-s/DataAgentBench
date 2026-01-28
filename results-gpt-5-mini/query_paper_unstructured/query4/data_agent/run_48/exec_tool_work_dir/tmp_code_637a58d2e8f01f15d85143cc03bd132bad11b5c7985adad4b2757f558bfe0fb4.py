code = """import json, re
import pandas as pd

path = var_call_4jFBOOfAseWZ7H5WmMJJsZhp
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# keywords for physical activity domain
keywords = ["physical activity", "activity tracker", "activity tracking", "activity trackers", "activity-tracking", "step-count", "step counting", "step-counting", "steps", "fitness", "activity tracking application", "activity tracking application", "physical-activity"]

# find rows containing any keyword and '2016'

def contains_keywords(text):
    if not isinstance(text, str):
        return False
    t = text.lower()
    for kw in keywords:
        if kw in t:
            return True
    return False

mask = df['text'].apply(lambda x: isinstance(x, str) and ('2016' in x)) & df['text'].apply(contains_keywords)
selected = df[mask].copy()
selected['title'] = selected['filename'].str.replace(r"\.txt$", "", regex=True)

titles = selected['title'].tolist()
print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_call_8nJIP2hXQsVJiZVHgzYfiNec': ['paper_docs'], 'var_call_Ajd1Nj4e2Sn19cAJuZZpi1yq': ['Citations', 'sqlite_sequence'], 'var_call_vlt0OfzQjc9VbBtSyVCg0NBi': [{'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a870', 'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}, {'_id': '694f5530284b10b11dc0a871', 'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt"}, {'_id': '694f5530284b10b11dc0a873', 'filename': 'Charting Design Preferences on Wellness Wearables.txt'}, {'_id': '694f5530284b10b11dc0a875', 'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt"}, {'_id': '694f5530284b10b11dc0a877', 'filename': 'Communicating Uncertainty in Fertility Prognosis.txt'}, {'_id': '694f5530284b10b11dc0a878', 'filename': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt'}, {'_id': '694f5530284b10b11dc0a87b', 'filename': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt'}, {'_id': '694f5530284b10b11dc0a87d', 'filename': 'Defining Adherence: Making Sense of Physical Activity Tracker Data.txt'}, {'_id': '694f5530284b10b11dc0a87f', 'filename': 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease.txt'}, {'_id': '694f5530284b10b11dc0a880', 'filename': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers.txt'}, {'_id': '694f5530284b10b11dc0a881', 'filename': 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance.txt'}, {'_id': '694f5530284b10b11dc0a882', 'filename': 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats.txt'}, {'_id': '694f5530284b10b11dc0a885', 'filename': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt'}, {'_id': '694f5530284b10b11dc0a88b', 'filename': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal.txt'}, {'_id': '694f5530284b10b11dc0a88d', 'filename': 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication.txt'}, {'_id': '694f5530284b10b11dc0a88f', 'filename': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application.txt"}, {'_id': '694f5530284b10b11dc0a891', 'filename': "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps.txt"}, {'_id': '694f5530284b10b11dc0a895', 'filename': 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health.txt'}, {'_id': '694f5530284b10b11dc0a896', 'filename': 'Modeling Interdependent and Periodic Real-World Action Sequences.txt'}, {'_id': '694f5530284b10b11dc0a897', 'filename': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure.txt"}, {'_id': '694f5530284b10b11dc0a89d', 'filename': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations.txt'}, {'_id': '694f5530284b10b11dc0a89f', 'filename': 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome.txt'}, {'_id': '694f5530284b10b11dc0a8a3', 'filename': 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model.txt'}, {'_id': '694f5530284b10b11dc0a8a6', 'filename': 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis.txt'}, {'_id': '694f5530284b10b11dc0a8ac', 'filename': 'Scaffolding for an OLM for Long-Term Physical Activity Goals.txt'}, {'_id': '694f5530284b10b11dc0a8b2', 'filename': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video.txt'}, {'_id': '694f5530284b10b11dc0a8b4', 'filename': 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace.txt'}, {'_id': '694f5530284b10b11dc0a8b7', 'filename': 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model.txt'}, {'_id': '694f5530284b10b11dc0a8b9', 'filename': 'Technologies for Everyday Life Reflection: Illustrating a Design Space.txt'}, {'_id': '694f5530284b10b11dc0a8ba', 'filename': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices.txt'}, {'_id': '694f5530284b10b11dc0a8bd', 'filename': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System.txt"}, {'_id': '694f5530284b10b11dc0a8c2', 'filename': 'Understanding Animals: A Critical Challenge in ACI.txt'}, {'_id': '694f5530284b10b11dc0a8ca', 'filename': 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating.txt'}], 'var_call_4jFBOOfAseWZ7H5WmMJJsZhp': 'file_storage/call_4jFBOOfAseWZ7H5WmMJJsZhp.json', 'var_call_Kr5LnzOJWcvqx19baKfoHneD': []}

exec(code, env_args)
