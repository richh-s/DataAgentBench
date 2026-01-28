code = """import json
import re

with open(locals()['var_function-call-9078033601304703484'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-14412117665521453199'], 'r') as f:
    citations = json.load(f)

year_pattern = re.compile(r'\b(20\d{2})\b')

matches = []
year_counts = {}

for p in papers:
    text = p.get('text', '')
    title = p.get('filename', '').replace('.txt', '')
    
    # Extract year from first 1000 chars
    header = text[:1000]
    found_years = year_pattern.findall(header)
    
    # Heuristic: The first 20xx year in the header is usually the publication year
    # (e.g. "UbiComp '15, ... 2015 ...")
    year = None
    if found_years:
        year = found_years[0]
        # Sometimes the first year might be part of an address or something, 
        # but usually it's the conference year.
    
    if year:
        year_counts[year] = year_counts.get(year, 0) + 1
    
    # Check domain
    has_domain = "physical activity" in text.lower()
    
    if year == '2016' and has_domain:
        matches.append(title)

# Calculate citations
final_results = []
if matches:
    # Filter citations
    citation_sums = {}
    for c in citations:
        if c['title'] in matches:
            citation_sums[c['title']] = citation_sums.get(c['title'], 0) + int(c['citation_count'])
            
    for title in matches:
        final_results.append({
            "title": title,
            "total_citation_count": citation_sums.get(title, 0)
        })

print("__RESULT__:")
print(json.dumps({
    "year_distribution": year_counts,
    "matched_papers": final_results
}))"""

env_args = {'var_function-call-16010210468405756630': 'file_storage/function-call-16010210468405756630.json', 'var_function-call-16010210468405758491': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-10417048927437287642': 'file_storage/function-call-10417048927437287642.json', 'var_function-call-14412117665521451328': 'file_storage/function-call-14412117665521451328.json', 'var_function-call-14412117665521453199': 'file_storage/function-call-14412117665521453199.json', 'var_function-call-12849824086341018331': [], 'var_function-call-17112652123555691582': {'count_domain': 4, 'count_year_1000': 0, 'count_both': 0, 'samples': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'header': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}]}, 'var_function-call-4625275472682914253': 'file_storage/function-call-4625275472682914253.json', 'var_function-call-12064431117875718388': [], 'var_function-call-2165682570679964338': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash"}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'header': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowled'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'header': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The Univ'}], 'var_function-call-1845517626011091668': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'var_function-call-9078033601304703484': 'file_storage/function-call-9078033601304703484.json'}

exec(code, env_args)
