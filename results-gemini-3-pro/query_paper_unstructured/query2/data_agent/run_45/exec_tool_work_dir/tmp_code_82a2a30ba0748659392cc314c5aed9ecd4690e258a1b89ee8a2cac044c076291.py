code = """import json

with open(locals()['var_function-call-5858360374360622472'], 'r') as f:
    citations_list = json.load(f)
citation_titles = set(c['title'] for c in citations_list)

with open(locals()['var_function-call-13558657844956865301'], 'r') as f:
    papers_list = json.load(f)

# Deduplicate papers
unique_papers = {p['filename']: p for p in papers_list}

in_citations_count = 0
acm_in_citations_count = 0

for filename, p in unique_papers.items():
    title = filename.replace('.txt', '')
    if title in citation_titles:
        in_citations_count += 1
        if 'ACM' in p.get('text', '')[:5000]:
            acm_in_citations_count += 1

print("__RESULT__:")
print(json.dumps({"total_papers": len(unique_papers), "in_citations": in_citations_count, "acm_in_citations": acm_in_citations_count}))"""

env_args = {'var_function-call-5858360374360622472': 'file_storage/function-call-5858360374360622472.json', 'var_function-call-5858360374360624099': 'file_storage/function-call-5858360374360624099.json', 'var_function-call-8725325700366092565': 158, 'var_function-call-3027916622841632543': 'file_storage/function-call-3027916622841632543.json', 'var_function-call-17448438011554741318': 'file_storage/function-call-17448438011554741318.json', 'var_function-call-6936084591521727754': 67.8, 'var_function-call-3893205258143355360': 0, 'var_function-call-9991689489332659929': True, 'var_function-call-13779047879887923666': True, 'var_function-call-8236464070197401554': {'count': 5, 'avg': 67.8}, 'var_function-call-709801467346895870': ['A Lived Informatics Model of Personal Informatics', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use'], 'var_function-call-17697871091250765431': '', 'var_function-call-15344622579435763101': {'total': 5, 'empty': 0}, 'var_function-call-4606542608697530976': 'file_storage/function-call-4606542608697530976.json', 'var_function-call-8013404368822841914': 'file_storage/function-call-8013404368822841914.json', 'var_function-call-112453838044893986': 5, 'var_function-call-13558657844956865301': 'file_storage/function-call-13558657844956865301.json', 'var_function-call-1599459431005445606': {'count': 53, 'average': 59.75471698113208, 'titles': ['A Lived Informatics Model of Personal Informatics', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use']}, 'var_function-call-15833978865181483912': 59.75471698113208, 'var_function-call-5032261346159503189': 99, 'var_function-call-10293011181449104540': 0, 'var_function-call-10270261725302727365': ['Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt']}

exec(code, env_args)
