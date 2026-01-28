code = """import json, re
citations_path = var_call_mYl1kRuKVMXm4FhezqDvAQh2
papers_path = var_call_WfQFa0WLNdLba5IpgTFTdudF
with open(citations_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(papers_path, 'r', encoding='utf-8') as f:
    papers = json.load(f)

cit_filenames = set([rec.get('filename') for rec in citations if rec.get('filename')])
paper_filenames = set([p.get('filename') for p in papers if p.get('filename')])
common = sorted(list(cit_filenames & paper_filenames))

# For up to first 50 common files, check if text contains 'CHI'
check = []
for fn in common[:50]:
    p = next((pp for pp in papers if pp.get('filename')==fn), None)
    text = p.get('text','') if p else ''
    contains_chi = bool(re.search(r"\bCHI\b", text, re.I))
    header = text[:400]
    check.append({'filename': fn, 'contains_CHI': contains_chi, 'header_preview': header})

result = {'num_citations_records': len(citations), 'num_paper_docs': len(papers), 'num_common_files': len(common), 'common_sample': check}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_uhZdm0NT8ktOmC9xiiiVkh8g': 'file_storage/call_uhZdm0NT8ktOmC9xiiiVkh8g.json', 'var_call_mYl1kRuKVMXm4FhezqDvAQh2': 'file_storage/call_mYl1kRuKVMXm4FhezqDvAQh2.json', 'var_call_WfQFa0WLNdLba5IpgTFTdudF': 'file_storage/call_WfQFa0WLNdLba5IpgTFTdudF.json', 'var_call_vlQijP8bd83XTxVsoLEo9tmU': {'total_citations': 0, 'num_chi_papers_cited_in_2020': 0, 'papers': []}, 'var_call_wvckEX0ED2SbA1OjLnjGveNA': {'total_citations': 0, 'num_chi_papers_cited_in_2020': 0, 'papers': []}}

exec(code, env_args)
