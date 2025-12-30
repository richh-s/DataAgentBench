code = """import json
import re

# Load citations
with open(locals()['var_function-call-13891558846941465066'], 'r') as f:
    citations_data = json.load(f)

# Load papers
with open(locals()['var_function-call-2034945145714030572'], 'r') as f:
    papers_data = json.load(f)

# Create a map of title -> citation_count for 2020
citations_map = {}
for item in citations_data:
    try:
        citations_map[item['title']] = int(item['citation_count'])
    except ValueError:
        citations_map[item['title']] = 0

chi_papers = []
chi_titles = []

regex_chi_broad = re.compile(
    r"(CHI\s*['’]?\d{2})|"
    r"(CHI\s+20\d{2})|"
    r"(Conference on Human Factors in Computing Systems)|"
    r"(CHI\s+Conference)",
    re.IGNORECASE
)

for paper in papers_data:
    text = paper.get('text', '')
    snippet = text[:5000]
    if regex_chi_broad.search(snippet):
        title = paper.get('filename', '').replace('.txt', '')
        chi_papers.append(paper)
        chi_titles.append(title)

total_citations = 0
found_count = 0
missing_titles = []

for title in chi_titles:
    if title in citations_map:
        total_citations += citations_map[title]
        found_count += 1
    else:
        missing_titles.append(title)

# Check if missing titles are present in citations_map keys with different casing
# or if they are just missing.
closest_matches = {}
citation_titles = set(citations_map.keys())

for mt in missing_titles:
    # simple containment check
    matches = [ct for ct in citation_titles if mt.lower() == ct.lower()]
    closest_matches[mt] = matches

debug_info = {
    "missing_titles_count": len(missing_titles),
    "missing_titles_examples": missing_titles,
    "closest_matches": closest_matches,
    "total_citations": total_citations
}

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-3161297584091160815': ['paper_docs'], 'var_function-call-3161297584091160886': ['Citations', 'sqlite_sequence'], 'var_function-call-16261242641906617785': 'file_storage/function-call-16261242641906617785.json', 'var_function-call-4279784200820574316': 'file_storage/function-call-4279784200820574316.json', 'var_function-call-13891558846941465066': 'file_storage/function-call-13891558846941465066.json', 'var_function-call-14966924842371218906': 0, 'var_function-call-1697024040972225892': {'citations_records': 188, 'papers_records': 5, 'chi_papers_identified': 0, 'matched_citations': 0, 'missing_citations': 0, 'total_citations': 0, 'sample_chi_titles': [], 'sample_citation_titles': ['Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices']}, 'var_function-call-11152806908800462062': 'file_storage/function-call-11152806908800462062.json', 'var_function-call-11221914133525263453': {'citations_records': 188, 'papers_records': 5, 'chi_papers_identified': 1, 'matched_citations': 1, 'missing_citations': 0, 'total_citations': 16}, 'var_function-call-6467787862815691825': 'file_storage/function-call-6467787862815691825.json', 'var_function-call-2582102276087240876': {'citations_records': 188, 'papers_records': 99, 'chi_papers_identified': 3, 'matched_citations': 3, 'missing_citations': 0, 'total_citations': 61}, 'var_function-call-2034945145714030572': 'file_storage/function-call-2034945145714030572.json', 'var_function-call-14311731575243625681': {'citations_records': 188, 'papers_records': 99, 'chi_papers_identified': 3, 'matched_citations': 3, 'missing_citations': 0, 'total_citations': 61, 'non_chi_samples': [{'title': 'A Lived Informatics Model of Personal Informatics', 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN"}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'header_snippet': 'Fengjiao Peng'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support'}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'header_snippet': 'Barriers and Negative Nudges:'}]}, 'var_function-call-17580145524174762903': {'citations_records': 188, 'papers_records': 99, 'chi_papers_identified': 48, 'matched_citations': 38, 'missing_citations': 10, 'total_citations': 1900, 'sample_chi_titles': ['A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Barriers to Engagement with a Personal Informatics Productivity Tool']}}

exec(code, env_args)
