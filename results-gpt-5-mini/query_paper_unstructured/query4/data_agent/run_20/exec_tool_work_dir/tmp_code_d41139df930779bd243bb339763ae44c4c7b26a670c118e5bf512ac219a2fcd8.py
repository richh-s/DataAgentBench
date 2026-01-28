code = """import json, re
from pathlib import Path
# Load Mongo query results from var_call_UGXRs02smPa8XIJInYASS4bD
p = Path(var_call_UGXRs02smPa8XIJInYASS4bD)
mongo_records = json.loads(p.read_text())
# Load SQL aggregation results from var_call_8SWMA4YmtDREDW1OHJG0A0cC
sql_records = var_call_8SWMA4YmtDREDW1OHJG0A0cC
# Build dict from SQL results for quick lookup
cit_dict = {r['title']: int(r['total_citations']) for r in sql_records}

results = []
for rec in mongo_records:
    filename = rec.get('filename','')
    text = rec.get('text','')
    if not filename or not text:
        continue
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    # domain check: contains 'physical activity'
    if 'physical activity' not in text.lower():
        continue
    # attempt to extract publication year from header area (first 1000 chars)
    header = text[:1000]
    years = re.findall(r"(20\d{2})", header)
    pub_year = None
    if years:
        # pick the first occurrence that is plausible (>=2000 and <=2024)
        for y in years:
            yi = int(y)
            if 2000 <= yi <= 2024:
                pub_year = yi
                break
    # if not found in header, search whole text for 'Published' lines
    if pub_year is None:
        years_all = re.findall(r"(20\d{2})", text)
        for y in years_all:
            yi = int(y)
            if 2000 <= yi <= 2024:
                pub_year = yi
                break
    if pub_year != 2016:
        continue
    total_citations = cit_dict.get(title, 0)
    results.append({"title": title, "total_citations": total_citations})
# sort by total_citations desc
results.sort(key=lambda x: x['total_citations'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_UGXRs02smPa8XIJInYASS4bD': 'file_storage/call_UGXRs02smPa8XIJInYASS4bD.json', 'var_call_TNRc3RP4L6ah2vnHGFP8aUOL': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Charting Design Preferences on Wellness Wearables', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Communicating Uncertainty in Fertility Prognosis', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'Modeling Interdependent and Periodic Real-World Action Sequences', "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'Understanding Animals: A Critical Challenge in ACI', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating'], 'var_call_8SWMA4YmtDREDW1OHJG0A0cC': [{'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': '636'}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'total_citations': '542'}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'total_citations': '467'}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'total_citations': '466'}, {'title': 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'total_citations': '449'}, {'title': 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'total_citations': '434'}, {'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'total_citations': '404'}, {'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'total_citations': '362'}, {'title': 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'total_citations': '358'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'total_citations': '349'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'total_citations': '335'}, {'title': 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'total_citations': '327'}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'total_citations': '316'}, {'title': 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication', 'total_citations': '306'}, {'title': 'Modeling Interdependent and Periodic Real-World Action Sequences', 'total_citations': '296'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citations': '278'}, {'title': 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'total_citations': '276'}, {'title': "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'total_citations': '272'}, {'title': 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'total_citations': '271'}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'total_citations': '271'}, {'title': 'Charting Design Preferences on Wellness Wearables', 'total_citations': '269'}, {'title': 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'total_citations': '268'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '265'}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'total_citations': '264'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'total_citations': '259'}, {'title': 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'total_citations': '191'}, {'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'total_citations': '190'}, {'title': 'Understanding Animals: A Critical Challenge in ACI', 'total_citations': '161'}, {'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'total_citations': '153'}, {'title': 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating', 'total_citations': '143'}, {'title': 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model', 'total_citations': '139'}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'total_citations': '133'}, {'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'total_citations': '72'}, {'title': 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'total_citations': '55'}]}

exec(code, env_args)
