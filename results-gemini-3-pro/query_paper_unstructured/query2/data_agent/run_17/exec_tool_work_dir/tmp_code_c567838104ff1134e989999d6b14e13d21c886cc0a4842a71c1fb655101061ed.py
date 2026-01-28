code = """import json

# Load citations
with open(locals()['var_function-call-161273639758194169'], 'r') as f:
    citations_2018 = json.load(f)
citation_map = {c['title']: int(c['citation_count']) for c in citations_2018}

# Load all papers
with open(locals()['var_function-call-12113278774783261809'], 'r') as f:
    all_papers = json.load(f)

acm_citations = []
acm_titles = []

for p in all_papers:
    filename = p.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    if title in citation_map:
        text = p.get('text', '')
        # Check for ACM
        # Use first 3000 chars to avoid references
        header_text = text[:3000]
        
        is_acm = False
        if "ACM" in header_text:
            is_acm = True
        
        # Double check for IEEE in copyright to avoid false positives?
        if "IEEE" in header_text and "Copyright" in header_text:
            # Check which one appears in copyright line
            # Simple heuristic: if ACM is present, likely ACM.
            pass
            
        if is_acm:
            acm_citations.append(citation_map[title])
            acm_titles.append(title)

# Calculate average
avg_citations = 0
if len(acm_citations) > 0:
    avg_citations = sum(acm_citations) / len(acm_citations)

print("__RESULT__:")
print(json.dumps({
    "average_citation_count": avg_citations,
    "count_acm_papers": len(acm_citations),
    "total_citations_2018": len(citation_map),
    "sample_acm_titles": acm_titles[:10]
}))"""

env_args = {'var_function-call-161273639758194169': 'file_storage/function-call-161273639758194169.json', 'var_function-call-161273639758192992': 'file_storage/function-call-161273639758192992.json', 'var_function-call-13120840873059324966': {'count': 158, 'sample_titles': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Sundroid: Solar Radiation Awareness with Smartphones', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set']}, 'var_function-call-447886293380607187': 'file_storage/function-call-447886293380607187.json', 'var_function-call-7481131308563480348': 'file_storage/function-call-7481131308563480348.json', 'var_function-call-4266321762780779682': 'file_storage/function-call-4266321762780779682.json', 'var_function-call-7357971864467483261': {'average_citations': 50.0, 'count_acm_papers': 1, 'total_citations_2018_papers': 158}, 'var_function-call-6360412478228823276': {'matched_titles': ['A Lived Informatics Model of Personal Informatics'], 'unmatched_samples': [{'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The University of Melbourne, Australia \n2Queensland University of Technology, Brisbane, Australia \n3Department of Mechanical Engineering, The University of Melbourne, Australia \n4Augmented Human Lab, Singapor'}]}, 'var_function-call-15122311342007185200': 'file_storage/function-call-15122311342007185200.json', 'var_function-call-16529135263217238013': 'file_storage/function-call-16529135263217238013.json', 'var_function-call-3005932884337927614': {'average_citations': 68.5, 'count_acm_papers': 2, 'total_citations_2018': 158, 'sample_matched': ['A Lived Informatics Model of Personal Informatics', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_function-call-12113278774783261809': 'file_storage/function-call-12113278774783261809.json'}

exec(code, env_args)
