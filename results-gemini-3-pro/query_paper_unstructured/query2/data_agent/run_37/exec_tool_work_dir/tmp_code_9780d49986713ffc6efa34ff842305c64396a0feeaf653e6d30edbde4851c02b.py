code = """import json

citations_path = locals()['var_function-call-9421256355430255115']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)
citation_map = {item['title']: item['citation_count'] for item in citations_data}

papers_path = locals()['var_function-call-9421256355430255910']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

matched_count = 0
acm_count = 0
ieee_count = 0
unknown_count = 0

sample_acm = []
sample_ieee = []
sample_unknown = []
sample_unmatched_titles = []

for paper in papers_data:
    filename = paper.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4]
    
    if title in citation_map:
        matched_count += 1
        text = paper.get('text', '').upper()
        
        # Simplified detection for debugging
        is_acm = "ACM" in text or "ASSOCIATION FOR COMPUTING MACHINERY" in text
        is_ieee = "IEEE" in text
        
        if is_acm and not is_ieee:
            acm_count += 1
            if len(sample_acm) < 3: sample_acm.append(title)
        elif is_ieee and not is_acm:
            ieee_count += 1
            if len(sample_ieee) < 3: sample_ieee.append(title)
        else:
            unknown_count += 1
            if len(sample_unknown) < 3: sample_unknown.append(title)
            # Check why unknown
            # print(f"Unknown source for {title}: ACM={is_acm}, IEEE={is_ieee}")
    else:
        if len(sample_unmatched_titles) < 3: sample_unmatched_titles.append(title)

print("__RESULT__:")
print(json.dumps({
    "total_citations_2018": len(citation_map),
    "total_papers": len(papers_data),
    "matched_papers": matched_count,
    "acm_identified": acm_count,
    "ieee_identified": ieee_count,
    "unknown/mixed": unknown_count,
    "sample_acm": sample_acm,
    "sample_ieee": sample_ieee,
    "sample_unknown": sample_unknown,
    "sample_unmatched": sample_unmatched_titles
}))"""

env_args = {'var_function-call-9421256355430255115': 'file_storage/function-call-9421256355430255115.json', 'var_function-call-9421256355430255910': 'file_storage/function-call-9421256355430255910.json', 'var_function-call-10114779790998248711': {'average_citations': 68.5, 'count': 2, 'found_titles_sample': ['A Lived Informatics Model of Personal Informatics', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}}

exec(code, env_args)
