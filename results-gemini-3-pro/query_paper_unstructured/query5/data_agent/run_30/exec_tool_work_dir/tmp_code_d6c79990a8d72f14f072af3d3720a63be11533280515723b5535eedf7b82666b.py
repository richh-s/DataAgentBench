code = """import json
import re

with open(locals()['var_function-call-7711183651007727056'], 'r') as f:
    citations_data = json.load(f)

with open(locals()['var_function-call-15227609533641263682'], 'r') as f:
    paper_docs_data = json.load(f)

paper_map = {d['filename'].replace('.txt', ''): d['text'] for d in paper_docs_data if 'filename' in d}

total_citations = 0
chi_papers = []

for record in citations_data:
    title = record['title']
    if title in paper_map:
        text = paper_map[title]
        # Check first 3000 chars
        header = text[:3000]
        
        # Logic to identify CHI venue
        # 1. Look for "Conference on Human Factors in Computing Systems"
        # 2. Look for "CHI" followed by year (e.g. CHI '15, CHI 2015, CHI 20)
        # 3. Look for "CHI" in specific copyright strings like "Proceedings of the ... CHI"
        # 4. Use regex `\bCHI\b` but be careful of references. First 3000 chars usually safe from refs.
        
        is_chi = False
        if "Conference on Human Factors in Computing Systems" in header:
            is_chi = True
        elif re.search(r'\bCHI\b', header):
             # Check context if needed, but in header usually venue.
             # Avoid "Tai Chi" or similar if possible.
             # "Tai Chi" is rare in headers unless title.
             # If title contains "Tai Chi", we might have a false positive if we just search text.
             # But title is "Beyond Behavior...", so "CHI" in header is likely venue.
             is_chi = True
        
        if is_chi:
             count = int(record['citation_count'])
             total_citations += count
             chi_papers.append({"title": title, "count": count})

result = {
    "total_citations": total_citations,
    "chi_papers_count": len(chi_papers),
    "chi_papers_preview": chi_papers[:5]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-7711183651007727056': 'file_storage/function-call-7711183651007727056.json', 'var_function-call-4121090962908109712': 'file_storage/function-call-4121090962908109712.json', 'var_function-call-5326245820750148638': 16, 'var_function-call-17055580434800668848': {'total_citations': 0, 'chi_papers_count': 0, 'matched_titles_preview': []}, 'var_function-call-1860412936554148787': {'venue_counts': {'CHI': 0, 'Ubicomp': 0, 'CSCW': 0, 'Other': 4}, 'chi_citations': 0}, 'var_function-call-36950570922871518': {'num_citations': 188, 'num_docs': 5, 'intersection_count': 4, 'sample_cit_titles': ['Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"], 'sample_doc_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_function-call-15227609533641263682': 'file_storage/function-call-15227609533641263682.json', 'var_function-call-12382812125810194227': {'total_citations': 16, 'chi_papers_count': 1, 'total_docs_loaded': 99, 'matches_found': 68}, 'var_function-call-5026212127774461042': ['Sundroid: Solar Radiation Awareness with Smartphones∗Thomas Fahrni, Michael Kuhn, Philipp Sommer, Roger Wattenhofer, and Samuel WeltenComputer Engineering and Networks LaboratoryETH Zurich, Switzerlandﬁrstname.lastname@tik.ee.ethz.chABSTRACTWhile the sun is important for our health, overexpo', "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPANWhy We Use and Abandon Smart Devices Amanda Lazar University of Washington alaz@uw.edu Christian Koehler Carnegie Mellon University ckoehler@andrew.cmu.edu Theresa Jean Tanenbaum University of California, Irvine ttanen@uci.edu David H. N", 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App Bliss Altenhoff, Haley Vaigneur and Kelly Caine Department of Psychology, Department of Industrial Engineering, School of Computing Clemson University Clemson, United States {blissw, hvagine, caine} @clemson.edu ', 'I’ll Be Back: On the Multiple Lives of Usersof a Mobile Activity Tracking ApplicationZhiyuan LinStanford Universityzylin@cs.stanford.eduTim AlthoffStanford Universityalthoff@cs.stanford.eduJure LeskovecStanford Universityjure@cs.stanford.eduABSTRACTMobile health applications that tra', 'A Wee Bit More Interaction: Designing and Evaluating  an Overactive Bladder AppAna-Maria Salai  Heriot-Watt University  Edinburgh, UK  as152@hw.ac.uk Lynne Baillie  Heriot-Watt University  Edinburgh, UK  l.baillie@hw.ac.ukABSTRACT Overactive  Bladder  (OAB)  is  a  widespread  conditi'], 'var_function-call-17457589173953117732': {'total_citations': 1551, 'chi_papers_count': 29, 'chi_titles_preview': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'Heed: Exploring the Design of Situated Self-Reporting Devices', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis']}, 'var_function-call-9479490037383184003': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith  30  stakeholders  (9  medical  professionals  and  21  end-\nusers)  an  OAB  mobile  health  application  that  aims  to \nincrease  adherence  to  self-managed  treatment.  Our  results \nsupport previous research that visualizing progress, setting \ngoals, receiving reminders and feedback  increases  use.  We \ndiscovered  that  games  could  be  used  successfully  as  a \ndistraction technique for urge suppression. Contrary to the \ncurrent research direction, automatically calculated features \ncould  be  a  detriment  to  app \ninteraction.  Regarding \nevaluation,  we  found  that  designers  may  not  want  to  rely \nonly  on  questionnaires  when  assessing  the  success  of  a \ngame and its emotional impact on users. \n\nCCS CONCEPTS \n• Human-centered  computing  ~  User  studies;  Usability  Testing; \nField Studies \n\nKEYWORDS \nMobile  Health  Applications;  Assistive  Technology;  Co-Design; \nInterviews; Usability; Overactive Bladder \n\nACM Reference format: \n\nAna-Maria  Salai  and  Lynne  Baillie.  2019.  A  Wee  Bit  More  Interaction: \nDesigning  and  Evaluating  an  Overactive  Bladder  App.  In  2019  CHI \nConference on Human Factors in Computing Systems Proceedings (CHI 2019), \nMay 4–9, 2019, Glagsow, Scotland, UK. ACM,  NY,  NY,  USA.  Paper  703,  13 \npages. https://doi.org/10.1145/3290605.3300933 \n\nPermission to make digital or hard copies of all or part of this work for personal or \nclassroom use is granted without fee provided that copies are not made or distributed \nfor profit or commercial advantage and that copies bear this notice and the full citation \non the first page. Copyrights for components of this work owned by others than ACM \nmust  be  honored.  Abstracting  with  credit  is  permitted.  To  copy  otherwise,  or \nrepublish,  to  post  on  servers  or  to  redistribute  to  lists,  requires  prior  specific \npermission and/or a fee. Request permissions from permissions@acm.org). \nCHI 2019, May 4-9, 2019, Glasgow, Scotland, UK. \n© 2019 Copyright is held by the owner/author(s). Publication rights licensed to ACM. \nACM ISBN 978-1-4503-5970-2/19/05...$15.00. \nDOI: https://doi.org/10.1145/3290605.3300933 \n\n1  INTRODUCTION \nThe  number  of  people  suffering  from  Overactive  Bladder \n(OAB)  worldwide  is expected  to reach 20.1% by  the end of \n2018  [31].  The  condition \nincurs  high  direct  costs \n(treatment), indirect costs (low productivity) and intangible \ncosts  (quality  of  life)  [18].  OAB  is  a  treatable  condition  as \n7'}

exec(code, env_args)
