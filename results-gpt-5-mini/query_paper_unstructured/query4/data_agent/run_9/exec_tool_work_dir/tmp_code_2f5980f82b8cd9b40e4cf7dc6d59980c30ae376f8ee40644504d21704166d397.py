code = """import json, re
# Load the MongoDB query result file (path stored in var_call_wu68Wi2dE8hOS7u3codhzXJz)
path = var_call_wu68Wi2dE8hOS7u3codhzXJz
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load citations query result list
citations = var_call_2ctNZPGYzC3Xjgnpsx49hFTE
cit_map = {rec['title']: int(rec['total_citations']) for rec in citations}

results = []
for d in docs:
    filename = d.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = d.get('text','')
    # ensure domain mention
    if not re.search(r'physical activity', text, re.I):
        continue
    # search for year in header (first 1000 chars)
    header = text[:1000]
    years = re.findall(r"\b(19\d{2}|20\d{2})\b", header)
    pub_year = None
    if years:
        # pick the first plausible year between 1990 and 2026
        for y in years:
            yint = int(y)
            if 1990 <= yint <= 2026:
                pub_year = yint
                break
    else:
        # fallback: search entire text for earliest plausible year
        years_all = re.findall(r"\b(19\d{2}|20\d{2})\b", text)
        for y in years_all:
            yint = int(y)
            if 1990 <= yint <= 2026:
                pub_year = yint
                break
    if pub_year == 2016:
        results.append({"title": title, "total_citations": cit_map.get(title)})

# dedupe
seen = set()
final = []
for r in results:
    if r['title'] not in seen:
        seen.add(r['title'])
        final.append(r)

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_9LUcJa07UacZD6oGJc9q86b9': 'file_storage/call_9LUcJa07UacZD6oGJc9q86b9.json', 'var_call_rxiPijACM8fM6xdYrma1UYHi': [], 'var_call_NDKCw76JURjoKqfcSWAerO58': 'file_storage/call_NDKCw76JURjoKqfcSWAerO58.json', 'var_call_XbZPXxjiSVAG8ZgkztPKNSs7': 'file_storage/call_XbZPXxjiSVAG8ZgkztPKNSs7.json', 'var_call_ATCj0mIO9HJiksVpmjUL81hx': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Charting Design Preferences on Wellness Wearables', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Communicating Uncertainty in Fertility Prognosis', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'Modeling Interdependent and Periodic Real-World Action Sequences', "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'Understanding Animals: A Critical Challenge in ACI', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating'], 'var_call_2ctNZPGYzC3Xjgnpsx49hFTE': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '265'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': '636'}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'total_citations': '271'}, {'title': 'Charting Design Preferences on Wellness Wearables', 'total_citations': '269'}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'total_citations': '466'}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'total_citations': '264'}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'total_citations': '467'}, {'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'total_citations': '153'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'total_citations': '259'}, {'title': 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'total_citations': '55'}, {'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'total_citations': '362'}, {'title': 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'total_citations': '276'}, {'title': 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'total_citations': '449'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'total_citations': '349'}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'total_citations': '133'}, {'title': 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication', 'total_citations': '306'}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'total_citations': '316'}, {'title': "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'total_citations': '272'}, {'title': 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'total_citations': '327'}, {'title': 'Modeling Interdependent and Periodic Real-World Action Sequences', 'total_citations': '296'}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'total_citations': '542'}, {'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'total_citations': '190'}, {'title': 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'total_citations': '268'}, {'title': 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model', 'total_citations': '139'}, {'title': 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'total_citations': '271'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'total_citations': '335'}, {'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'total_citations': '404'}, {'title': 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'total_citations': '434'}, {'title': 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'total_citations': '191'}, {'title': 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'total_citations': '358'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citations': '278'}, {'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'total_citations': '72'}, {'title': 'Understanding Animals: A Critical Challenge in ACI', 'total_citations': '161'}, {'title': 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating', 'total_citations': '143'}], 'var_call_GUrdiTt2q6fL0GNJifahzQB4': [], 'var_call_FZhzf6K22MEW89pCgMZtFDMW': [], 'var_call_wu68Wi2dE8hOS7u3codhzXJz': 'file_storage/call_wu68Wi2dE8hOS7u3codhzXJz.json'}

exec(code, env_args)
