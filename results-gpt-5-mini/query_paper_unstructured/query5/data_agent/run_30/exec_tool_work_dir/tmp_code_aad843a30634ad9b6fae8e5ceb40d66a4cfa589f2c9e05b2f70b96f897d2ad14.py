code = """import json, re
citations_path = var_call_mYl1kRuKVMXm4FhezqDvAQh2
papers_path = var_call_WfQFa0WLNdLba5IpgTFTdudF
with open(citations_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(papers_path, 'r', encoding='utf-8') as f:
    papers = json.load(f)
# Build mapping from filename to citation_count
cit_by_file = {rec.get('filename'): int(rec.get('citation_count')) if rec.get('citation_count') is not None and str(rec.get('citation_count')).isdigit() else int(float(rec.get('citation_count'))) if rec.get('citation_count') is not None else 0 for rec in citations}
chi_papers = []
total = 0
for p in papers:
    filename = p.get('filename')
    text = p.get('text','')
    if re.search(r"\bCHI\b", text, re.I):
        if filename in cit_by_file:
            cc = cit_by_file[filename]
            chi_papers.append({'title': filename[:-4], 'citation_count': cc})
            total += cc
# Remove duplicates (if any) by title
seen = set()
unique_papers = []
for pp in chi_papers:
    if pp['title'] not in seen:
        unique_papers.append(pp)
        seen.add(pp['title'])
result = {'total_citations': total, 'num_chi_papers_cited_in_2020': len(unique_papers), 'papers': unique_papers}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_uhZdm0NT8ktOmC9xiiiVkh8g': 'file_storage/call_uhZdm0NT8ktOmC9xiiiVkh8g.json', 'var_call_mYl1kRuKVMXm4FhezqDvAQh2': 'file_storage/call_mYl1kRuKVMXm4FhezqDvAQh2.json', 'var_call_WfQFa0WLNdLba5IpgTFTdudF': 'file_storage/call_WfQFa0WLNdLba5IpgTFTdudF.json', 'var_call_vlQijP8bd83XTxVsoLEo9tmU': {'total_citations': 0, 'num_chi_papers_cited_in_2020': 0, 'papers': []}}

exec(code, env_args)
