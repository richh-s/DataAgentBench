code = """import json

# acm titles from previous execute_python call
acm = var_call_4tuzIwlaARVFI9kxJFNsoJYY
acm_titles = acm.get('acm_titles', [])

# Load citations query result from file path variable
citations_path = var_call_PwQJZI2Gp9yCogxKPf0S3GIo
with open(citations_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Filter citations for titles in acm_titles
matches = []
for rec in citations:
    title = rec.get('title')
    if title in acm_titles:
        # citation_count may be string
        try:
            count = int(rec.get('citation_count'))
        except Exception:
            try:
                count = int(float(rec.get('citation_count')))
            except Exception:
                count = None
        matches.append({'title': title, 'citation_count': count})

# Compute average
valid_counts = [r['citation_count'] for r in matches if r['citation_count'] is not None]
count = len(valid_counts)
if count > 0:
    total = sum(valid_counts)
    average = total / count
    average_rounded = round(average, 2)
else:
    total = 0
    average = None
    average_rounded = None

output = {
    'average_citation_count': average_rounded,
    'paper_count': count,
    'total_citations': total,
    'matches': matches
}

print('__RESULT__:')
print(json.dumps(output, ensure_ascii=False))"""

env_args = {'var_call_oum8fEP9La2Fq9G8QzYIelui': 'file_storage/call_oum8fEP9La2Fq9G8QzYIelui.json', 'var_call_4tuzIwlaARVFI9kxJFNsoJYY': {'acm_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Barriers to Engagement with a Personal Informatics Productivity Tool', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone', 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps', 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym', 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game', 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach', 'From Nobody Cares to Way to Go!: A Design Framework for Social Sharing in Personal Informatics', 'FutureSelf: What Happens When We Forecast Self-Trackers? Future Health Statuses?', 'Goal-oriented Visualizations of Activity Tracking: A Case Study with Engineering Students', 'How to Drive a London Bus: Measuring Performance in a Mobile and Remote Workplace', 'Intelligent Computing in Personal Informatics: Key Design Considerations', 'Live Interest Meter: Learning from Quantified Feedback in Mass Lectures', 'Lullaby: A Capture & Access System for Understanding the Sleep Environment', 'MoodLight: Exploring Personal and Social Implications of Ambient Display of Biosensor Data', 'No Forests Without Trees: Particulars and Patterns in Visualizing Personal Communication', 'No Longer Wearing: Investigating the Abandonment of Personal Health-tracking Technologies on Craigslist', 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness', 'Quantified Factory Worker: Designing a Worker Feedback Dashboard', 'Quantified Self Meets Social Media: Sharing of Weight Updates on Twitter', 'Real-life Experiences with an Adaptive Light Bracelet', 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'Reviewing Reflection: On the Use of Reflection in Interactive System Design', 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'Self-tracking Cultures: Towards a Sociology of Personal Informatics', 'Sitting in the Same Boat: A Case Study of a Combined Awareness System and Behaviour Change Technology', 'Social (Media) Jet Lag: How Usage of Social Technology Can Modulate and Reflect Circadian Rhythms', 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'Social Fabric Fitness: The Design and Evaluation of Wearable E-textile Displays to Support Group Running', 'Sundroid: Solar Radiation Awareness with Smartphones', 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'The Power of Mobile Notifications to Increase Wellbeing Logging Behavior', "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'Tiny Habits in the Giant Enterprise: Understanding the Dynamics of a Quantified Workplace', 'Turn to the Self in Human-Computer Interaction: Care of the Self in Negotiating the Human-Technology Relationship', 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'Understanding Physical Activity Through 3D Printed Material Artifacts', "We'Ve Bin Watching You: Designing for Reflection and Social Persuasion to Promote Sustainable Lifestyles", 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating', 'Why We Use and Abandon Smart Devices']}, 'var_call_PwQJZI2Gp9yCogxKPf0S3GIo': 'file_storage/call_PwQJZI2Gp9yCogxKPf0S3GIo.json'}

exec(code, env_args)
