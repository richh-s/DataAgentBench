code = """import json

food_papers = locals()['var_function-call-9949952103803740931']
if isinstance(food_papers, str):
    food_papers = json.loads(food_papers)

# Escape single quotes for SQL
safe_titles = [t.replace("'", "''") for t in food_papers]

# Construct SQL
titles_str = ", ".join([f"'{t}'" for t in safe_titles])
query = f"SELECT SUM(citation_count) FROM Citations WHERE title IN ({titles_str});"

print("__RESULT__:")
print(query)"""

env_args = {'var_function-call-17948406739355176464': 'file_storage/function-call-17948406739355176464.json', 'var_function-call-1041647607165485382': ['Citations', 'sqlite_sequence'], 'var_function-call-1041647607165487633': 'file_storage/function-call-1041647607165487633.json', 'var_function-call-17075501722390720700': [], 'var_function-call-12172120259311764631': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'has_food': True, 'context': 'r  tracking  location  [24,30],  finances  [20],  food  [11],  weight  [19,25],  and  physical  acti'}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'has_food': True, 'context': 'projects  on  her  personal  behavior,  such  as  food  consumption  and  sneezes  (http://ellieharr'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'has_food': False, 'context': ''}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'has_food': True, 'context': 'sist  of  avoiding  bladder  irritants  (certain  food  and  drinks)  and  consuming  a  proper  amo'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'has_food': False, 'context': ''}], 'var_function-call-14126767165602297505': [], 'var_function-call-785007343650812713': [{'title': 'A Lived Informatics Model of Personal Informatics', 'count': 13}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'count': 13}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 1}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'count': 0}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'count': 0}], 'var_function-call-4541425889179395715': 'file_storage/function-call-4541425889179395715.json', 'var_function-call-9949952103803740931': ['Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'TastyBeats: Designing Palatable Representations of Physical Activity', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating']}

exec(code, env_args)
