code = """import json

# Load citations
with open(locals()['var_function-call-161273639758194169'], 'r') as f:
    citations_2018 = json.load(f)

# Load ACM papers (full text)
with open(locals()['var_function-call-16529135263217238013'], 'r') as f:
    acm_papers_raw = json.load(f)

citation_map = {c['title']: int(c['citation_count']) for c in citations_2018}

acm_citations = []
matched_titles = []

for p in acm_papers_raw:
    filename = p.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    if title in citation_map:
        # Verify ACM is in the header/metadata (first 3000 chars)
        # or look for specific copyright phrases
        text = p.get('text', '')
        # Check first 3000 chars for "ACM"
        if 'ACM' in text[:3000]:
            acm_citations.append(citation_map[title])
            matched_titles.append(title)
        else:
            # Check if it has standard ACM copyright anywhere?
            # e.g. "Copyright" and "ACM" in same line?
            # If not in first 3000, it's likely a reference.
            pass

avg_citations = 0
if len(acm_citations) > 0:
    avg_citations = sum(acm_citations) / len(acm_citations)

print("__RESULT__:")
print(json.dumps({
    "average_citations": avg_citations,
    "count_acm_papers": len(acm_citations),
    "total_citations_2018": len(citation_map),
    "sample_matched": matched_titles[:5]
}))"""

env_args = {'var_function-call-161273639758194169': 'file_storage/function-call-161273639758194169.json', 'var_function-call-161273639758192992': 'file_storage/function-call-161273639758192992.json', 'var_function-call-13120840873059324966': {'count': 158, 'sample_titles': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Sundroid: Solar Radiation Awareness with Smartphones', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set']}, 'var_function-call-447886293380607187': 'file_storage/function-call-447886293380607187.json', 'var_function-call-7481131308563480348': 'file_storage/function-call-7481131308563480348.json', 'var_function-call-4266321762780779682': 'file_storage/function-call-4266321762780779682.json', 'var_function-call-7357971864467483261': {'average_citations': 50.0, 'count_acm_papers': 1, 'total_citations_2018_papers': 158}, 'var_function-call-6360412478228823276': {'matched_titles': ['A Lived Informatics Model of Personal Informatics'], 'unmatched_samples': [{'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The University of Melbourne, Australia \n2Queensland University of Technology, Brisbane, Australia \n3Department of Mechanical Engineering, The University of Melbourne, Australia \n4Augmented Human Lab, Singapor'}]}, 'var_function-call-15122311342007185200': 'file_storage/function-call-15122311342007185200.json', 'var_function-call-16529135263217238013': 'file_storage/function-call-16529135263217238013.json'}

exec(code, env_args)
