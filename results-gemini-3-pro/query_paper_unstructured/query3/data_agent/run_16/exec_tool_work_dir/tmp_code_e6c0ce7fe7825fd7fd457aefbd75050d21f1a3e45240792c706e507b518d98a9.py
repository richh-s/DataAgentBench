code = """import json
import re

citations_key = 'var_function-call-14861443508322681236'
papers_key = 'var_function-call-1947762228881266501'

with open(locals()[papers_key], 'r') as f:
    papers_data = json.load(f)

debug_info = []

for i, paper in enumerate(papers_data[:10]):
    text = paper.get('text', '')
    header = text[:200]
    
    # Simple regex for year
    years = re.findall(r'20[0-9]{2}', header)
    
    debug_info.append({
        "title": paper.get('filename'),
        "header_snippet": header, # Let's print raw header, might be messy but ok
        "years_found": years
    })

print("__RESULT__:")
# Use default=str to handle non-serializable, though here simple types
print(json.dumps(debug_info, default=str))"""

env_args = {'var_function-call-13973424374790880036': 'file_storage/function-call-13973424374790880036.json', 'var_function-call-13973424374790878367': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-3366737603932088961': 'file_storage/function-call-3366737603932088961.json', 'var_function-call-8593920629685848414': {'count': 5, 'samples': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'year_extracted': None, 'contrib_context': 'contributions  through  survey  design  and  participant  interviews. \nWe  also  thank  Elena  Agapi'}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'year_extracted': None, 'contrib_context': 'contributions  in  this  paper:  1)  we \nidentify  problems  across  personal  informatics  tools,  '}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'year_extracted': None, 'contrib_context': None}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'year_extracted': None, 'contrib_context': 'contribution “I like drawing!” (UP4),  some  did not like \ndrawing: “I don’t like drawing things.” ('}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'year_extracted': None, 'contrib_context': 'contribution of this research is \na  system  designed  to  support  the  work  of  occupational \nthe'}]}, 'var_function-call-1947762228881266501': 'file_storage/function-call-1947762228881266501.json', 'var_function-call-14861443508322681236': 'file_storage/function-call-14861443508322681236.json', 'var_function-call-3974080567568237': [], 'var_function-call-3100392970530816796': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'years_found': [], 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'years_found': [], 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years_found': [], 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years_found': [], 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'years_found': [], 'has_empirical': False}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt', 'years_found': [], 'has_empirical': True}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt', 'years_found': [], 'has_empirical': False}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt', 'years_found': [], 'has_empirical': False}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt", 'years_found': [], 'has_empirical': False}, {'title': 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone.txt', 'years_found': [], 'has_empirical': False}, {'title': 'Charting Design Preferences on Wellness Wearables.txt', 'years_found': [], 'has_empirical': True}, {'title': 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units.txt', 'years_found': [], 'has_empirical': False}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'years_found': [], 'has_empirical': True}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings.txt', 'years_found': [], 'has_empirical': True}, {'title': 'Communicating Uncertainty in Fertility Prognosis.txt', 'years_found': [], 'has_empirical': True}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'years_found': [], 'has_empirical': True}, {'title': 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps.txt', 'years_found': [], 'has_empirical': False}, {'title': 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym.txt', 'years_found': [], 'has_empirical': False}, {'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt', 'years_found': [], 'has_empirical': False}, {'title': 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data.txt', 'years_found': [], 'has_empirical': False}]}

exec(code, env_args)
