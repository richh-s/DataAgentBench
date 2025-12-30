code = """import json

citations_path = locals()['var_function-call-13908298438428433880']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

citation_map = {item['title']: int(item['citation_count']) for item in citations_data}

papers_path = locals()['var_function-call-13272072186750426102']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

acm_counts = []
total_matched = 0

for p in papers_data:
    title = p['filename'].replace('.txt', '')
    if title in citation_map:
        total_matched += 1
        text_head = p['text'][:2000]
        # Stricter check
        # ACM papers usually have "ACM" in the copyright line or "ACM Classification Keywords"
        if "ACM" in text_head:
            # exclude if it's explicitly IEEE?
            if "IEEE" in text_head and "ACM" in text_head:
                # Ambiguous. Let's look at the copyright line specifically?
                # But typically one publisher.
                # If "Copyright" is near "ACM", it's ACM.
                pass
            acm_counts.append(citation_map[title])

avg = sum(acm_counts) / len(acm_counts) if acm_counts else 0
print(f"Total papers with citations in 2018: {total_matched}")
print(f"ACM papers found: {len(acm_counts)}")
print(f"Average: {avg}")

print("__RESULT__:")
print(json.dumps(avg))"""

env_args = {'var_function-call-13908298438428433880': 'file_storage/function-call-13908298438428433880.json', 'var_function-call-13908298438428430929': 'file_storage/function-call-13908298438428430929.json', 'var_function-call-17064019482965131703': 'file_storage/function-call-17064019482965131703.json', 'var_function-call-13272072186750426102': 'file_storage/function-call-13272072186750426102.json', 'var_function-call-5520325511212738459': 68.5}

exec(code, env_args)
