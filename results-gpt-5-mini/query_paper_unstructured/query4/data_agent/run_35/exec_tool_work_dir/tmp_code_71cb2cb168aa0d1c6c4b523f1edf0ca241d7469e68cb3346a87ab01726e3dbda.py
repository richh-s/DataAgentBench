code = """import json, re

# Access previous tool results
titles_var = var_call_dOBpEqbGXDeBLSK8AFJbGC4V
citations_path = var_call_fy5Y1tRtOVUAGQkaMUotPUjQ

# Normalize titles_var to a Python list
if isinstance(titles_var, str):
    s = titles_var
    # Try to extract JSON array from the string
    m = re.search(r"\[.*\]", s, re.S)
    if m:
        titles = json.loads(m.group(0))
    else:
        try:
            titles = json.loads(s)
        except Exception:
            titles = []
else:
    titles = titles_var

# Load full citations result from file
with open(citations_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build mapping from cleaned title to total citations (int)
mapping = {}
for rec in citations:
    t = rec.get('title')
    if t is None:
        continue
    # Clean surrounding quotes if present
    t_clean = t.strip()
    if t_clean.startswith('"') and t_clean.endswith('"'):
        t_clean = t_clean[1:-1]
    # Also strip whitespace
    t_clean = t_clean.strip()
    # Convert citation count to int
    tc = rec.get('total_citations', 0)
    try:
        tc_int = int(tc)
    except Exception:
        try:
            tc_int = int(str(tc).strip())
        except:
            tc_int = 0
    mapping[t_clean] = tc_int

# Match and prepare results
results = []
for title in titles:
    # title likely already cleaned
    t_clean = title.strip()
    citations_count = mapping.get(t_clean)
    if citations_count is None:
        # try case-insensitive match
        for k, v in mapping.items():
            if k.lower() == t_clean.lower():
                citations_count = v
                break
    if citations_count is None:
        citations_count = 0
    results.append({"title": title, "total_citations": citations_count})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_t0eGZ0V7Vx2mFRtY6V1NTGeA': ['paper_docs'], 'var_call_nbkjSzhK5ThCLjNr4s2knSBh': 'file_storage/call_nbkjSzhK5ThCLjNr4s2knSBh.json', 'var_call_dOBpEqbGXDeBLSK8AFJbGC4V': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Charting Design Preferences on Wellness Wearables', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Communicating Uncertainty in Fertility Prognosis', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'Designing in the Dark: Eliciting Self-tracking Dimensions for Understanding Enigmatic Disease', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'How Information Sharing About Care Recipients by Family Caregivers Impacts Family Communication', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'Modeling Interdependent and Periodic Real-World Action Sequences', "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'Predicting Interruptibility for Manual Data Collection: A Cluster-based User Model', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'Supporting Meaningful Personal Fitness: The Tracker Goal Evolution Model', 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'Understanding Animals: A Critical Challenge in ACI', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating'], 'var_call_fy5Y1tRtOVUAGQkaMUotPUjQ': 'file_storage/call_fy5Y1tRtOVUAGQkaMUotPUjQ.json'}

exec(code, env_args)
