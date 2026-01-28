code = """import json

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str) and maybe_path_or_list.endswith('.json'):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

cit = load_records(var_call_TRpLmu1z1yAwlBlNZUz41qpT)
chi_files = load_records(var_call_4mI3GWtW7N1ssI9Ui4DuO3Ph)
chi_titles = set()
for r in chi_files:
    fn = r.get('filename','')
    if fn.lower().endswith('.txt'):
        chi_titles.add(fn[:-4])
    else:
        chi_titles.add(fn)

chi_total = 0
chi_papers = 0
per_paper = []
for r in cit:
    t = r.get('title')
    if t in chi_titles:
        chi_papers += 1
        c = int(r.get('citation_count') or 0)
        chi_total += c
        per_paper.append({"title": t, "citation_count_2020": c})

per_paper_sorted = sorted(per_paper, key=lambda x: (-x['citation_count_2020'], x['title']))

out = {"total_citations_2020_for_CHI_papers": chi_total, "num_CHI_papers_cited_in_2020": chi_papers, "per_paper_citations_2020": per_paper_sorted}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_TRpLmu1z1yAwlBlNZUz41qpT': 'file_storage/call_TRpLmu1z1yAwlBlNZUz41qpT.json', 'var_call_0xzxrpc7YvsO6yzcV7d1dOG8': 'file_storage/call_0xzxrpc7YvsO6yzcV7d1dOG8.json', 'var_call_fir9ov4PUWbvrSB6gVQLqz5q': {'total_citations_2020_for_CHI_papers': 0, 'num_CHI_papers_cited_in_2020': 0}, 'var_call_Iux4gB9TPS5C9eUH6HBrhbT4': {'total_citations_2020_for_CHI_papers': 0, 'num_CHI_papers_cited_in_2020': 0, 'num_docs_detected_as_CHI': 0}, 'var_call_ag0kxZFgI57C5riycScYcpDU': 'file_storage/call_ag0kxZFgI57C5riycScYcpDU.json', 'var_call_4mI3GWtW7N1ssI9Ui4DuO3Ph': [{'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt'}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt'}, {'filename': 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats.txt'}, {'filename': 'Exploring the Value of Parent Tracked Baby Data in Interactions with Healthcare Professionals: A Data-Enabled Design Exploration.txt'}, {'filename': 'FutureSelf: What Happens When We Forecast Self-Trackers? Future Health Statuses?.txt'}, {'filename': 'Personal Tracking of Screen Time on Digital Devices.txt'}, {'filename': 'Self-tracking Cultures: Towards a Sociology of Personal Informatics.txt'}, {'filename': 'Sitting in the Same Boat: A Case Study of a Combined Awareness System and Behaviour Change Technology.txt'}, {'filename': 'SleepTight: Low-burden, Self-monitoring Technology for Capturing and Reflecting on Sleep Behaviors.txt'}, {'filename': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices.txt'}, {'filename': 'The Power of Mobile Notifications to Increase Wellbeing Logging Behavior.txt'}, {'filename': 'TimeAware: Leveraging Framing Effects to Enhance Personal Productivity.txt'}, {'filename': 'Understanding Animals: A Critical Challenge in ACI.txt'}, {'filename': 'Understanding Physical Activity Through 3D Printed Material Artifacts.txt'}, {'filename': "When Fitness Trackers Don'T 'Fit': End-user Difficulties in the Assessment of Personal Tracking Device Accuracy.txt"}]}

exec(code, env_args)
