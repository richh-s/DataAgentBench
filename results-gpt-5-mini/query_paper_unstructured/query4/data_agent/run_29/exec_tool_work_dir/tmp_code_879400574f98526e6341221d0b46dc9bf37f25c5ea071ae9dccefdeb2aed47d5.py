code = """import json, os, re

# Load the occurrences result file
occ_path = var_call_GpC0v7yeKWOfhkjcenVg2AmO
with open(occ_path, 'r', encoding='utf-8') as f:
    occs = json.load(f)

# Load citations mapping
citations = var_call_40BzmFCtkmqBlfex3QhJccEU
cit_map = {rec['title']: int(rec['total_citations']) for rec in citations}

keywords = ['physical activity', 'physical', 'activity']
results = []
for rec in occs:
    fn = rec.get('filename','')
    count2016 = rec.get('count_2016',0)
    # check filename keywords
    fname_lower = fn.lower()
    if not any(k in fname_lower for k in keywords):
        # also check occurrences contexts for physical activity mention
        occs_list = rec.get('occurrences', [])
        found_pa = False
        for o in occs_list:
            if re.search(r'physical activity', o.get('context',''), re.IGNORECASE):
                found_pa = True
                break
        if not found_pa:
            continue
    # require a 2016 occurrence within first 2000 chars
    has_2016_header = False
    for o in rec.get('occurrences', []):
        if o.get('pos', 999999) < 2000 and '2016' in o.get('context',''):
            has_2016_header = True
            break
    # also accept if count2016>0 and filename or context suggests CHI/Ubicomp 2016
    if not has_2016_header:
        # look for 'chi' or 'ubicomp' with 2016 anywhere in file occurrences contexts
        for o in rec.get('occurrences', []):
            if re.search(r'CHI|UBICOMP|AH|IUI|DIS|CSCW', o.get('context',''), re.IGNORECASE) and '2016' in o.get('context',''):
                has_2016_header = True
                break
    if not has_2016_header:
        continue
    title = fn[:-4] if fn.endswith('.txt') else fn
    total = cit_map.get(title, 0)
    results.append({'title': title, 'total_citations': total})

# dedupe and sort by title
seen = set()
unique = []
for r in sorted(results, key=lambda x: x['title']):
    if r['title'] not in seen:
        seen.add(r['title'])
        unique.append(r)

print("__RESULT__:")
print(json.dumps(unique))"""

env_args = {'var_call_MMyKqAbaWyK4YDL1TloCDU5l': 'file_storage/call_MMyKqAbaWyK4YDL1TloCDU5l.json', 'var_call_2Ao7Cqo7BiMnFyxKdNNyYaWS': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Charting Design Preferences on Wellness Wearables', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Communicating Uncertainty in Fertility Prognosis', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'Modeling Interdependent and Periodic Real-World Action Sequences', "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'Understanding Animals: A Critical Challenge in ACI', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating'], 'var_call_40BzmFCtkmqBlfex3QhJccEU': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '265'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': '636'}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'total_citations': '271'}, {'title': 'Charting Design Preferences on Wellness Wearables', 'total_citations': '269'}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'total_citations': '466'}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'total_citations': '264'}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'total_citations': '467'}, {'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'total_citations': '153'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'total_citations': '259'}, {'title': 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'total_citations': '55'}, {'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'total_citations': '362'}, {'title': 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'total_citations': '276'}, {'title': 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'total_citations': '449'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'total_citations': '349'}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'total_citations': '133'}, {'title': 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication', 'total_citations': '306'}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'total_citations': '316'}, {'title': "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'total_citations': '272'}, {'title': 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'total_citations': '327'}, {'title': 'Modeling Interdependent and Periodic Real-World Action Sequences', 'total_citations': '296'}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'total_citations': '542'}, {'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'total_citations': '190'}, {'title': 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'total_citations': '268'}, {'title': 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model', 'total_citations': '139'}, {'title': 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'total_citations': '271'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'total_citations': '335'}, {'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'total_citations': '404'}, {'title': 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'total_citations': '434'}, {'title': 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'total_citations': '191'}, {'title': 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'total_citations': '358'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citations': '278'}, {'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'total_citations': '72'}, {'title': 'Understanding Animals: A Critical Challenge in ACI', 'total_citations': '161'}, {'title': 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating', 'total_citations': '143'}], 'var_call_jfmlt7Ql8pM0MQx0s5oHpL9q': [], 'var_call_Cju8hSFRLaJJ5CjoGSqRtAMg': [], 'var_call_Fem7JzGfiogNHhBOdIPWB0LL': [], 'var_call_GpC0v7yeKWOfhkjcenVg2AmO': 'file_storage/call_GpC0v7yeKWOfhkjcenVg2AmO.json'}

exec(code, env_args)
