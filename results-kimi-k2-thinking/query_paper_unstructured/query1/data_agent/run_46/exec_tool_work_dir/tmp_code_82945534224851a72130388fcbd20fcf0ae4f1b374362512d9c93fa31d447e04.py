code = """import json

# Get the food titles from the previous result using locals()
food_result = locals()['var_functions.execute_python:20']
food_titles = food_result['food_titles']

# Get the citations file path from the query result
citations_path = locals()['var_functions.query_db:22']

# Read the citations data
with open(citations_path, 'r') as f:
    citations = json.load(f)

print('Total food papers: ' + str(len(food_titles)))
print('Total citation records: ' + str(len(citations)))

# Create a set of food titles for faster lookup (normalize case)
food_titles_set = set([title.lower() for title in food_titles])

# Find citations for food papers
citation_count_sum = 0
found_food_papers = set()

for citation in citations:
    citation_title = citation['title'].lower()
    
    # Check if this citation belongs to a food paper
    if citation_title in food_titles_set:
        count = int(citation['citation_count'])
        citation_count_sum += count
        found_food_papers.add(citation['title'])

print('Found citations for ' + str(len(found_food_papers)) + ' food papers')
print('Total citation count for food papers: ' + str(citation_count_sum))

output = {
    'total_citation_count': citation_count_sum
}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:20': {'food_papers_count': 36, 'food_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game', 'FutureSelf: What Happens When We Forecast Self-Trackers? Future Health Statuses?', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics', 'Modeling Interdependent and Periodic Real-World Action Sequences', 'No Longer Wearing: Investigating the Abandonment of Personal Health-tracking Technologies on Craigslist', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'Personal Tracking of Screen Time on Digital Devices', 'Quantified Self Meets Social Media: Sharing of Weight Updates on Twitter', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'SleepTight: Low-burden, Self-monitoring Technology for Capturing and Reflecting on Sleep Behaviors', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', "Supporting Coping with Parkinson's Disease Through Self Tracking", 'TastyBeats: Designing Palatable Representations of Physical Activity', 'The Power of Mobile Notifications to Increase Wellbeing Logging Behavior', 'Understanding Animals: A Critical Challenge in ACI', 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', "We'Ve Bin Watching You: Designing for Reflection and Social Persuasion to Promote Sustainable Lifestyles", 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
