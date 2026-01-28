code = """import json
import re

def extract_paper_info(text_content, filename):
    title_match = re.search(r'\n\n([^\n]+)\n\n', text_content)
    title = title_match.group(1).strip() if title_match else filename.replace('.txt', '')

    year_match = re.search(r'\b(19|20)\d{2}\b', text_content)
    year = int(year_match.group(0)) if year_match else None

    domain_match = re.search(r'Domain[s]?:\s*(.*?)\n', text_content, re.IGNORECASE)
    domain = domain_match.group(1).strip() if domain_match else None

    if not domain:
        domain_match_abstract = re.search(r'abstract.*?self-trackers across a variety of domains, first by surveying.*?trackers of (.*?)(?:,| and) (.*?)(?:,| and) (.*?) and then by interviewing', text_content, re.IGNORECASE | re.DOTALL)
        if domain_match_abstract:
            domains_from_abstract = [d.strip().lower() for d in domain_match_abstract.groups() if d]
            domain = ', '.join(domains_from_abstract) if domains_from_abstract else None
    
    if not domain:
        domain_match_keywords = re.search(r'keywords:\n(.*?)\n', text_content, re.IGNORECASE | re.DOTALL)
        if domain_match_keywords:
            keywords_text = domain_match_keywords.group(1).strip()
            if "physical activity" in keywords_text.lower():
                domain = "physical activity"

    return {'title': title, 'year': year, 'domain': domain}

file_path = locals()['var_function-call-12002591806772645320']
with open(file_path, 'r') as f:
    papers_data = json.load(f)

filtered_papers = []
for paper in papers_data:
    paper_info = extract_paper_info(paper['text'], paper['filename'])
    if paper_info['year'] == 2016 and paper_info['domain'] and 'physical activity' in paper_info['domain'].lower():
        filtered_papers.append({'title': paper_info['title'], 'year': paper_info['year'], 'domain': paper_info['domain']})

print('__RESULT__:')
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-17798319154585505742': ['paper_docs'], 'var_function-call-12002591806772645320': 'file_storage/function-call-12002591806772645320.json'}

exec(code, env_args)
