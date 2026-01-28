code = """import json, re
# Load the large result file containing paper docs
path = var_call_Z9XnWYjMIsiFgcN8UmmGrEv6
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)
# citation totals
citations = var_call_m3LsKCSBs4LPpvZlV3MPqL8Z
cit_map = {c['title']: int(c['total_citations']) for c in citations}

results = []

def extract_year(text):
    # Try Publication date
    m = re.search(r'Publication date:\s*([A-Za-z]+\s*)?(?P<y>19\d{2}|20\d{2})', text)
    if m:
        return int(m.group('y'))
    # ACM Reference Format line
    m = re.search(r'ACM Reference Format:.*?(?P<y>19\d{2}|20\d{2})', text)
    if m:
        return int(m.group('y'))
    # Look in first 400 chars for a year
    head = text[:400]
    m = re.search(r'(?P<y>19\d{2}|20\d{2})', head)
    if m:
        return int(m.group('y'))
    # fallback: first occurrence in whole text
    m = re.search(r'(?P<y>19\d{2}|20\d{2})', text)
    if m:
        return int(m.group('y'))
    return None

for d in docs:
    filename = d.get('filename','')
    if not filename.lower().endswith('.txt'):
        continue
    title = filename[:-4]
    text = d.get('text','')
    # ensure domain mention
    if 'physical activity' not in text.lower():
        continue
    year = extract_year(text)
    total_cit = cit_map.get(title)
    if year == 2016 and total_cit is not None:
        results.append({'title': title, 'total_citations': total_cit})

# Also, sometimes the filename might not match exactly due to punctuation; try to match by startswith or lower
if not results:
    # attempt fuzzy match for titles in citations where year==2016 in docs
    # build map of doc titles to year
    doc_year = {}
    for d in docs:
        fn = d.get('filename','')
        t = fn[:-4]
        y = extract_year(d.get('text',''))
        doc_year[t] = y
    for c in citations:
        t = c['title']
        # find docs whose title lower starts with t lower or vice versa
        for dt, y in doc_year.items():
            if y == 2016 and (dt.lower().startswith(t.lower()) or t.lower().startswith(dt.lower())):
                results.append({'title': dt, 'total_citations': int(c['total_citations'])})

# Prepare JSON serializable string
out = json.dumps(results)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_bu1sceJafwFXkty1F5bYH8fY': ['paper_docs'], 'var_call_3Le3gKXxzGlyMsWdCOO4H6fR': [{'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a870', 'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}, {'_id': '694f5530284b10b11dc0a871', 'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt"}, {'_id': '694f5530284b10b11dc0a873', 'filename': 'Charting Design Preferences on Wellness Wearables.txt'}, {'_id': '694f5530284b10b11dc0a875', 'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt"}, {'_id': '694f5530284b10b11dc0a877', 'filename': 'Communicating Uncertainty in Fertility Prognosis.txt'}, {'_id': '694f5530284b10b11dc0a878', 'filename': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt'}, {'_id': '694f5530284b10b11dc0a87b', 'filename': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt'}, {'_id': '694f5530284b10b11dc0a87d', 'filename': 'Defining Adherence: Making Sense of Physical Activity Tracker Data.txt'}, {'_id': '694f5530284b10b11dc0a87f', 'filename': 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease.txt'}, {'_id': '694f5530284b10b11dc0a880', 'filename': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers.txt'}, {'_id': '694f5530284b10b11dc0a881', 'filename': 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance.txt'}, {'_id': '694f5530284b10b11dc0a882', 'filename': 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats.txt'}, {'_id': '694f5530284b10b11dc0a885', 'filename': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt'}, {'_id': '694f5530284b10b11dc0a88b', 'filename': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal.txt'}, {'_id': '694f5530284b10b11dc0a88d', 'filename': 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication.txt'}, {'_id': '694f5530284b10b11dc0a88f', 'filename': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application.txt"}, {'_id': '694f5530284b10b11dc0a891', 'filename': "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps.txt"}, {'_id': '694f5530284b10b11dc0a895', 'filename': 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health.txt'}, {'_id': '694f5530284b10b11dc0a896', 'filename': 'Modeling Interdependent and Periodic Real-World Action Sequences.txt'}, {'_id': '694f5530284b10b11dc0a897', 'filename': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure.txt"}, {'_id': '694f5530284b10b11dc0a89d', 'filename': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations.txt'}, {'_id': '694f5530284b10b11dc0a89f', 'filename': 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome.txt'}, {'_id': '694f5530284b10b11dc0a8a3', 'filename': 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model.txt'}, {'_id': '694f5530284b10b11dc0a8a6', 'filename': 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis.txt'}, {'_id': '694f5530284b10b11dc0a8ac', 'filename': 'Scaffolding for an OLM for Long-Term Physical Activity Goals.txt'}, {'_id': '694f5530284b10b11dc0a8b2', 'filename': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video.txt'}, {'_id': '694f5530284b10b11dc0a8b4', 'filename': 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace.txt'}, {'_id': '694f5530284b10b11dc0a8b7', 'filename': 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model.txt'}, {'_id': '694f5530284b10b11dc0a8b9', 'filename': 'Technologies for Everyday Life Reflection: Illustrating a Design Space.txt'}, {'_id': '694f5530284b10b11dc0a8ba', 'filename': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices.txt'}, {'_id': '694f5530284b10b11dc0a8bd', 'filename': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System.txt"}, {'_id': '694f5530284b10b11dc0a8c2', 'filename': 'Understanding Animals: A Critical Challenge in ACI.txt'}, {'_id': '694f5530284b10b11dc0a8ca', 'filename': 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating.txt'}], 'var_call_r0S6BXXa3c7rZHZma5PacKXc': ['Defining Adherence: Making Sense of Physical Activity Tracker Data', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'], 'var_call_m3LsKCSBs4LPpvZlV3MPqL8Z': [{'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'total_citations': '259'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'total_citations': '349'}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'total_citations': '133'}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'total_citations': '316'}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'total_citations': '542'}, {'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'total_citations': '190'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'total_citations': '335'}, {'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'total_citations': '404'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citations': '278'}], 'var_call_Z9XnWYjMIsiFgcN8UmmGrEv6': 'file_storage/call_Z9XnWYjMIsiFgcN8UmmGrEv6.json'}

exec(code, env_args)
