code = """import json, re
# Load previous tool results from storage paths
citations_path = var_call_mYl1kRuKVMXm4FhezqDvAQh2
papers_path = var_call_WfQFa0WLNdLba5IpgTFTdudF

with open(citations_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(papers_path, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Build citation lookup by filename (filename includes .txt)
cit_by_file = {rec.get('filename'): rec.get('citation_count') for rec in citations if rec.get('filename')}

chi_papers = []
total = 0
for p in papers:
    filename = p.get('filename')
    text = p.get('text','')
    header = text[:400]
    # Detect CHI in header using word boundary or typical CHI patterns
    if re.search(r"\bCHI\b", header, re.I) or re.search(r"CHI\s?'?\d{2,4}", header, re.I) or re.search(r"Proceedings of the CHI", header, re.I):
        # Check if this paper has citations in 2020
        if filename in cit_by_file and cit_by_file[filename] is not None:
            cc = cit_by_file[filename]
            try:
                cc_int = int(cc)
            except:
                try:
                    cc_int = int(float(cc))
                except:
                    cc_int = 0
            chi_papers.append({'filename': filename, 'title': filename[:-4], 'citation_count': cc_int})
            total += cc_int

result = {'total_citations': total, 'num_chi_papers_cited_in_2020': len(chi_papers), 'papers': chi_papers}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_uhZdm0NT8ktOmC9xiiiVkh8g': 'file_storage/call_uhZdm0NT8ktOmC9xiiiVkh8g.json', 'var_call_mYl1kRuKVMXm4FhezqDvAQh2': 'file_storage/call_mYl1kRuKVMXm4FhezqDvAQh2.json', 'var_call_WfQFa0WLNdLba5IpgTFTdudF': 'file_storage/call_WfQFa0WLNdLba5IpgTFTdudF.json'}

exec(code, env_args)
