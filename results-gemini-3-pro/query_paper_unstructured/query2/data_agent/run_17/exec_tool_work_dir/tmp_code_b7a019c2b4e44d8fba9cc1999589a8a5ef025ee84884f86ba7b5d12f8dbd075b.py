code = """import json

# Load citations
with open(locals()['var_function-call-161273639758194169'], 'r') as f:
    citations_2018 = json.load(f)
citation_titles = set(c['title'] for c in citations_2018)

# Load regex result
with open(locals()['var_function-call-16529135263217238013'], 'r') as f:
    regex_papers = json.load(f)
regex_filenames = set(p['filename'] for p in regex_papers)

# Load 2000 papers result
with open(locals()['var_function-call-17989801066274686341'], 'r') as f:
    all_papers_2000 = json.load(f)
all_filenames_2000 = set(p['filename'] for p in all_papers_2000)

# Check overlap
matched_regex = 0
matched_2000 = 0
found_titles_regex = []
found_titles_2000 = []

target = "Why We Use and Abandon Smart Devices"
is_target_in_regex = (target + ".txt") in regex_filenames
is_target_in_2000 = (target + ".txt") in all_filenames_2000

for title in citation_titles:
    fname = title + ".txt"
    if fname in regex_filenames:
        matched_regex += 1
        found_titles_regex.append(title)
    if fname in all_filenames_2000:
        matched_2000 += 1
        found_titles_2000.append(title)

print("__RESULT__:")
print(json.dumps({
    "citations_count": len(citation_titles),
    "regex_match_count": matched_regex,
    "all_2000_match_count": matched_2000,
    "target_in_regex": is_target_in_regex,
    "target_in_2000": is_target_in_2000,
    "total_regex_papers": len(regex_papers),
    "total_2000_papers": len(all_papers_2000)
}))"""

env_args = {'var_function-call-161273639758194169': 'file_storage/function-call-161273639758194169.json', 'var_function-call-161273639758192992': 'file_storage/function-call-161273639758192992.json', 'var_function-call-13120840873059324966': {'count': 158, 'sample_titles': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Sundroid: Solar Radiation Awareness with Smartphones', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set']}, 'var_function-call-447886293380607187': 'file_storage/function-call-447886293380607187.json', 'var_function-call-7481131308563480348': 'file_storage/function-call-7481131308563480348.json', 'var_function-call-4266321762780779682': 'file_storage/function-call-4266321762780779682.json', 'var_function-call-7357971864467483261': {'average_citations': 50.0, 'count_acm_papers': 1, 'total_citations_2018_papers': 158}, 'var_function-call-6360412478228823276': {'matched_titles': ['A Lived Informatics Model of Personal Informatics'], 'unmatched_samples': [{'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The University of Melbourne, Australia \n2Queensland University of Technology, Brisbane, Australia \n3Department of Mechanical Engineering, The University of Melbourne, Australia \n4Augmented Human Lab, Singapor'}]}, 'var_function-call-15122311342007185200': 'file_storage/function-call-15122311342007185200.json', 'var_function-call-16529135263217238013': 'file_storage/function-call-16529135263217238013.json', 'var_function-call-3005932884337927614': {'average_citations': 68.5, 'count_acm_papers': 2, 'total_citations_2018': 158, 'sample_matched': ['A Lived Informatics Model of Personal Informatics', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_function-call-12113278774783261809': 'file_storage/function-call-12113278774783261809.json', 'var_function-call-4990600512700917409': {'average_citation_count': 68.5, 'count_acm_papers': 2, 'total_citations_2018': 158, 'sample_acm_titles': ['A Lived Informatics Model of Personal Informatics', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_function-call-11681581142799115444': [], 'var_function-call-17609389995748567277': {'count': 5, 'sample_filenames': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt']}, 'var_function-call-17989801066274686341': 'file_storage/function-call-17989801066274686341.json'}

exec(code, env_args)
