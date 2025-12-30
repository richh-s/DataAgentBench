code = """import json

# Food Papers is a list (direct result)
food_papers_data = locals()['var_function-call-13257791986397824615']

# Extract just the titles
food_titles = set([p['title'].strip() for p in food_papers_data])

# Citations is a file path
with open(locals()['var_function-call-9814510467799688242'], 'r') as f:
    citations_data = json.load(f)

total_citations = 0
matched_papers = set()

for row in citations_data:
    t = row.get('title', '').strip()
    if t in food_titles:
        count = row.get('citation_count', 0)
        try:
            count = int(count)
        except:
            count = 0
        total_citations += count
        matched_papers.add(t)

print('__RESULT__:')
print(json.dumps({
    "total_citations": total_citations,
    "matched_count": len(matched_papers),
    "food_titles_count": len(food_titles),
    "matched_titles": list(matched_papers)
}))"""

env_args = {'var_function-call-3709648201764099351': 'file_storage/function-call-3709648201764099351.json', 'var_function-call-12009379333761153785': 'file_storage/function-call-12009379333761153785.json', 'var_function-call-8395827407536305276': 'file_storage/function-call-8395827407536305276.json', 'var_function-call-12574282544977898815': [], 'var_function-call-11433524787453468215': [{'title': 'A Lived Informatics Model of Personal Informatics', 'snippet': 'r  tracking \nlocation  [24,30],  finances  [20],  food  [11],  weight  [19,25], \nand  physical  acti'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'snippet': 'projects  on  her  personal  behavior,  such  as \nfood  consumption  and  sneezes  (http://ellieharr'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'snippet': 'sist  of  avoiding  bladder  irritants \n(certain  food  and  drinks)  and  consuming  a  proper  amo'}], 'var_function-call-4825611475060270292': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'var_function-call-205188535857108763': 'file_storage/function-call-205188535857108763.json', 'var_function-call-2821502025567842666': [{'count(*)': '1405'}], 'var_function-call-13257791986397824615': [{'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'reason': 'Title'}, {'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'reason': 'Title'}, {'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'reason': 'Title'}, {'title': 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'reason': 'Keywords'}, {'title': 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'reason': 'Keywords'}, {'title': "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'reason': 'Keywords'}, {'title': 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'reason': 'Title'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity', 'reason': 'Keywords'}, {'title': 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating', 'reason': 'Keywords'}], 'var_function-call-9814510467799688242': 'file_storage/function-call-9814510467799688242.json'}

exec(code, env_args)
