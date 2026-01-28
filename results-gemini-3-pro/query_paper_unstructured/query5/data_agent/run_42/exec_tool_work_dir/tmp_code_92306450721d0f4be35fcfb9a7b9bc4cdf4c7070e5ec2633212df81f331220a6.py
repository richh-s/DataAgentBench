code = """import json
import re

citations_path = locals()['var_function-call-9827945916294781673']
with open(citations_path, 'r') as f:
    citations = json.load(f)

citation_map = {}
for rec in citations:
    try:
        count = int(rec['citation_count'])
    except:
        count = 0
    citation_map[rec['title']] = count

papers_path = locals()['var_function-call-10964722236442380275']
with open(papers_path, 'r') as f:
    papers = json.load(f)

total_citations = 0
chi_papers_count = 0
matched_titles = []
chi_titles = []

for paper in papers:
    title = paper.get('filename', '').replace('.txt', '')
    if title in citation_map:
        matched_titles.append(title)
        text = paper.get('text', '')
        header_text = text[:3000]
        
        is_chi = False
        if "Conference on Human Factors in Computing Systems" in header_text:
            is_chi = True
        elif re.search(r"CHI\s+(20\d{2}|'\d{2})", header_text):
            is_chi = True
        elif re.search(r"Proceedings of the .*CHI", header_text, re.IGNORECASE):
            is_chi = True
        elif "CHI Conference" in header_text:
            is_chi = True
            
        if is_chi:
            total_citations += citation_map[title]
            chi_papers_count += 1
            chi_titles.append(title)

print("__RESULT__:")
print(json.dumps({
    "total_citations": total_citations,
    "chi_papers_count": chi_papers_count,
    "total_matched_titles": len(matched_titles),
    "total_papers_fetched": len(papers),
    "chi_titles": chi_titles
}))"""

env_args = {'var_function-call-9827945916294781673': 'file_storage/function-call-9827945916294781673.json', 'var_function-call-15113855768220925357': 'file_storage/function-call-15113855768220925357.json', 'var_function-call-14723286786793106195': {'total_citations': 16, 'paper_count': 1}, 'var_function-call-10777315937443816509': {'found_chi_count': 2, 'found_chi_titles': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'samples_others': [{'title': 'A Lived Informatics Model of Personal Informatics', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'header': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}], 'total_matched_papers': 4}, 'var_function-call-7885526825991231676': {'citations_count': 188, 'papers_count': 5, 'sample_citation_titles': ['Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"], 'sample_paper_filenames': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt']}, 'var_function-call-10964722236442380275': 'file_storage/function-call-10964722236442380275.json'}

exec(code, env_args)
