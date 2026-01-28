code = """import json

# Load citations
with open(locals()['var_function-call-5858360374360622472'], 'r') as f:
    citations_list = json.load(f)

# Load papers (full fetch)
with open(locals()['var_function-call-13558657844956865301'], 'r') as f:
    papers_list = json.load(f)

citation_map = {}
for c in citations_list:
    try:
        count = int(c['citation_count'])
        citation_map[c['title']] = count
    except ValueError:
        continue

acm_citations = []
titles_found = []

for paper in papers_list:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check if this title is in citations
    if title in citation_map:
        # Check if published by ACM
        if 'ACM' in text[:5000]:
            acm_citations.append(citation_map[title])
            titles_found.append(title)

# Calculate average
if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
else:
    avg_citations = 0

print("__RESULT__:")
print(json.dumps({"count": len(acm_citations), "average": avg_citations, "titles": titles_found[:5]}))"""

env_args = {'var_function-call-5858360374360622472': 'file_storage/function-call-5858360374360622472.json', 'var_function-call-5858360374360624099': 'file_storage/function-call-5858360374360624099.json', 'var_function-call-8725325700366092565': 158, 'var_function-call-3027916622841632543': 'file_storage/function-call-3027916622841632543.json', 'var_function-call-17448438011554741318': 'file_storage/function-call-17448438011554741318.json', 'var_function-call-6936084591521727754': 67.8, 'var_function-call-3893205258143355360': 0, 'var_function-call-9991689489332659929': True, 'var_function-call-13779047879887923666': True, 'var_function-call-8236464070197401554': {'count': 5, 'avg': 67.8}, 'var_function-call-709801467346895870': ['A Lived Informatics Model of Personal Informatics', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use'], 'var_function-call-17697871091250765431': '', 'var_function-call-15344622579435763101': {'total': 5, 'empty': 0}, 'var_function-call-4606542608697530976': 'file_storage/function-call-4606542608697530976.json', 'var_function-call-8013404368822841914': 'file_storage/function-call-8013404368822841914.json', 'var_function-call-112453838044893986': 5, 'var_function-call-13558657844956865301': 'file_storage/function-call-13558657844956865301.json'}

exec(code, env_args)
