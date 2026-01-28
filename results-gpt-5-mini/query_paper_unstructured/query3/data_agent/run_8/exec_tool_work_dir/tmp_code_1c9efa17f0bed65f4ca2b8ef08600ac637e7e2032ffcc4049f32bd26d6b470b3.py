code = """import json
# Use the stored variables directly
filtered = var_call_lEJInzax932x5taHTdC4a0CH
citations = var_call_AnIl5thRJLvxeAwpOU3TrsHv

# Create mapping
cit_map = {}
for c in citations:
    title = c.get('title')
    tc = c.get('total_citations', 0)
    try:
        cit_map[title] = int(tc)
    except:
        try:
            cit_map[title] = int(str(tc))
        except:
            cit_map[title] = 0

results = []
for r in filtered:
    t = r['title']
    year = r.get('year')
    cit = cit_map.get(t, 0)
    results.append({'title': t, 'year': year, 'total_citations': cit})

# sort by total_citations desc
results_sorted = sorted(results, key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(results_sorted))"""

env_args = {'var_call_V3l4c1FCV6d0XAEGwntcPIui': 'file_storage/call_V3l4c1FCV6d0XAEGwntcPIui.json', 'var_call_lEJInzax932x5taHTdC4a0CH': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'year': 2018}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'year': 2019}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'year': 2017}, {'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'year': 2018}, {'title': 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game', 'year': 2018}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'year': 2019}, {'title': 'Heed: Exploring the Design of Situated Self-Reporting Devices', 'year': 2018}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'year': 2018}, {'title': 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'year': 2017}, {'title': 'Modeling Interdependent and Periodic Real-World Action Sequences', 'year': 2018}, {'title': 'No Forests Without Trees: Particulars and Patterns in Visualizing Personal Communication', 'year': 2023}, {'title': 'No Longer Wearing: Investigating the Abandonment of Personal Health-tracking Technologies on Craigslist', 'year': 2024}], 'var_call_AnIl5thRJLvxeAwpOU3TrsHv': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '265'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'total_citations': '402'}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'total_citations': '264'}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'total_citations': '467'}, {'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'total_citations': '362'}, {'title': 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game', 'total_citations': '97'}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'total_citations': '133'}, {'title': 'Heed: Exploring the Design of Situated Self-Reporting Devices', 'total_citations': '153'}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'total_citations': '316'}, {'title': 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'total_citations': '327'}, {'title': 'Modeling Interdependent and Periodic Real-World Action Sequences', 'total_citations': '296'}, {'title': 'No Forests Without Trees: Particulars and Patterns in Visualizing Personal Communication', 'total_citations': '195'}, {'title': 'No Longer Wearing: Investigating the Abandonment of Personal Health-tracking Technologies on Craigslist', 'total_citations': '131'}]}

exec(code, env_args)
