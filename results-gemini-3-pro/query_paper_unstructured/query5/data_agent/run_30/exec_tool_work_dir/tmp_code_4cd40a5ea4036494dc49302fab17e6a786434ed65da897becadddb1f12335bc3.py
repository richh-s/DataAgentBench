code = """import json
import re

with open(locals()['var_function-call-7711183651007727056'], 'r') as f:
    citations_data = json.load(f)

with open(locals()['var_function-call-15227609533641263682'], 'r') as f:
    paper_docs_data = json.load(f)

paper_map = {d['filename'].replace('.txt', ''): d['text'] for d in paper_docs_data if 'filename' in d}

total_citations = 0
chi_papers_count = 0
chi_titles = []

for record in citations_data:
    title = record['title']
    if title in paper_map:
        text = paper_map[title]
        # Search WHOLE text for CHI
        # Use regex for whole word CHI, case sensitive
        # Also include the full name check
        if re.search(r'\bCHI\b', text) or "Conference on Human Factors in Computing Systems" in text:
             count = int(record['citation_count'])
             total_citations += count
             chi_papers_count += 1
             chi_titles.append(title)

result = {
    "total_citations": total_citations,
    "chi_papers_count": chi_papers_count,
    "chi_titles_preview": chi_titles[:5]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-7711183651007727056': 'file_storage/function-call-7711183651007727056.json', 'var_function-call-4121090962908109712': 'file_storage/function-call-4121090962908109712.json', 'var_function-call-5326245820750148638': 16, 'var_function-call-17055580434800668848': {'total_citations': 0, 'chi_papers_count': 0, 'matched_titles_preview': []}, 'var_function-call-1860412936554148787': {'venue_counts': {'CHI': 0, 'Ubicomp': 0, 'CSCW': 0, 'Other': 4}, 'chi_citations': 0}, 'var_function-call-36950570922871518': {'num_citations': 188, 'num_docs': 5, 'intersection_count': 4, 'sample_cit_titles': ['Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"], 'sample_doc_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_function-call-15227609533641263682': 'file_storage/function-call-15227609533641263682.json', 'var_function-call-12382812125810194227': {'total_citations': 16, 'chi_papers_count': 1, 'total_docs_loaded': 99, 'matches_found': 68}, 'var_function-call-5026212127774461042': ['Sundroid: Solar Radiation Awareness with Smartphones∗Thomas Fahrni, Michael Kuhn, Philipp Sommer, Roger Wattenhofer, and Samuel WeltenComputer Engineering and Networks LaboratoryETH Zurich, Switzerlandﬁrstname.lastname@tik.ee.ethz.chABSTRACTWhile the sun is important for our health, overexpo', "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPANWhy We Use and Abandon Smart Devices Amanda Lazar University of Washington alaz@uw.edu Christian Koehler Carnegie Mellon University ckoehler@andrew.cmu.edu Theresa Jean Tanenbaum University of California, Irvine ttanen@uci.edu David H. N", 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App Bliss Altenhoff, Haley Vaigneur and Kelly Caine Department of Psychology, Department of Industrial Engineering, School of Computing Clemson University Clemson, United States {blissw, hvagine, caine} @clemson.edu ', 'I’ll Be Back: On the Multiple Lives of Usersof a Mobile Activity Tracking ApplicationZhiyuan LinStanford Universityzylin@cs.stanford.eduTim AlthoffStanford Universityalthoff@cs.stanford.eduJure LeskovecStanford Universityjure@cs.stanford.eduABSTRACTMobile health applications that tra', 'A Wee Bit More Interaction: Designing and Evaluating  an Overactive Bladder AppAna-Maria Salai  Heriot-Watt University  Edinburgh, UK  as152@hw.ac.uk Lynne Baillie  Heriot-Watt University  Edinburgh, UK  l.baillie@hw.ac.ukABSTRACT Overactive  Bladder  (OAB)  is  a  widespread  conditi']}

exec(code, env_args)
