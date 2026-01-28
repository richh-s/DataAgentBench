code = """import json
import re

citations_path = locals()['var_function-call-9421256355430255115']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Create map and also a list of lower-case titles for debugging
citation_map = {c['title']: c['citation_count'] for c in citations_data}
citation_titles_lower = {c['title'].lower(): c['title'] for c in citations_data}

papers_path = locals()['var_function-call-9421256355430255910']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

def determine_source(text):
    text_upper = text.upper()
    # Check for ACM patterns
    acm_score = 0
    if "ACM" in text_upper: acm_score += 1
    if "ASSOCIATION FOR COMPUTING MACHINERY" in text_upper: acm_score += 2
    if "COPYRIGHT" in text_upper and "ACM" in text_upper: acm_score += 3
    if "PERMISSION" in text_upper and "ACM" in text_upper: acm_score += 3
    if "ACM CLASSIFICATION" in text_upper: acm_score += 5
    
    # Check for IEEE patterns
    ieee_score = 0
    if "IEEE" in text_upper: ieee_score += 1
    if "INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS" in text_upper: ieee_score += 2
    if "COPYRIGHT" in text_upper and "IEEE" in text_upper: ieee_score += 3
    
    if acm_score > ieee_score:
        return "ACM"
    elif ieee_score > acm_score:
        return "IEEE"
    else:
        # Tie or both 0
        if acm_score > 0: return "ACM" # Default to ACM if ambiguous but present
        return "UNKNOWN"

results = []

for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    title = filename.replace('.txt', '')
    
    source = determine_source(text)
    
    citation_count = None
    if title in citation_map:
        citation_count = citation_map[title]
    else:
        # Try case insensitive match
        if title.lower() in citation_titles_lower:
            matched_title = citation_titles_lower[title.lower()]
            citation_count = citation_map[matched_title]
    
    results.append({
        "title": title,
        "source": source,
        "citation_count": citation_count
    })

# Check for "Stage-based" in citations if not found
stage_citations = [c['title'] for c in citations_data if "Stage" in c['title']]

print("__RESULT__:")
print(json.dumps({
    "paper_results": results,
    "stage_citations_in_db": stage_citations
}))"""

env_args = {'var_function-call-9421256355430255115': 'file_storage/function-call-9421256355430255115.json', 'var_function-call-9421256355430255910': 'file_storage/function-call-9421256355430255910.json', 'var_function-call-10114779790998248711': {'average_citations': 68.5, 'count': 2, 'found_titles_sample': ['A Lived Informatics Model of Personal Informatics', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_function-call-18319933992546683446': {'total_citations_2018': 158, 'total_papers': 5, 'matched_papers': 2, 'acm_identified': 1, 'ieee_identified': 0, 'unknown/mixed': 1, 'sample_acm': ['A Lived Informatics Model of Personal Informatics'], 'sample_ieee': [], 'sample_unknown': ['ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'sample_unmatched': ['A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App']}, 'var_function-call-14159721120098003439': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}]}

exec(code, env_args)
