code = """import json
from pathlib import Path
# food titles list from previous Mongo processing
food_titles = var_call_O7cuQT9A5zbenU89ULi5FTQr
# citations data file path
citations_path = var_call_gsEez7lvjjITRWnfMCFQbwRt

# Load citations data (file path string)
with open(citations_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

total = 0
matched_titles = set()
for rec in citations:
    title = rec.get('title', '')
    # citation_count may be string
    try:
        cc = int(rec.get('citation_count', 0))
    except:
        try:
            cc = int(float(rec.get('citation_count', 0)))
        except:
            cc = 0
    if title in food_titles:
        total += cc
        matched_titles.add(title)

# For transparency include titles matched count (not required but fine to compute)
result = {"total_citations": total, "matched_papers_count": len(matched_titles)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_pQOfsy41GlIFD19RbO1TdKkn': ['paper_docs'], 'var_call_aAIpk8JudSUTsUKhmKgEWf3b': 'file_storage/call_aAIpk8JudSUTsUKhmKgEWf3b.json', 'var_call_O7cuQT9A5zbenU89ULi5FTQr': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game', 'Exploring the Value of Parent Tracked Baby Data in Interactions with Healthcare Professionals: A Data-Enabled Design Exploration', 'From Nobody Cares to Way to Go!: A Design Framework for Social Sharing in Personal Informatics', 'FutureSelf: What Happens When We Forecast Self-Trackers? Future Health Statuses?', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'Heed: Exploring the Design of Situated Self-Reporting Devices', 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics', 'Modeling Interdependent and Periodic Real-World Action Sequences', 'MoodLight: Exploring Personal and Social Implications of Ambient Display of Biosensor Data', 'No Longer Wearing: Investigating the Abandonment of Personal Health-tracking Technologies on Craigslist'], 'var_call_gsEez7lvjjITRWnfMCFQbwRt': 'file_storage/call_gsEez7lvjjITRWnfMCFQbwRt.json'}

exec(code, env_args)
