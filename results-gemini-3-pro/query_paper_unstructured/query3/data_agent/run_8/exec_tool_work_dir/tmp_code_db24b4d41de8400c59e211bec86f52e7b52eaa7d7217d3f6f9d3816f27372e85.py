code = """import json
import re
from collections import Counter

# Load papers
with open(locals()['var_function-call-15080538060224287608'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-7203993170122994378'], 'r') as f:
    citations = json.load(f)

citation_sums = {}
for c in citations:
    t = c['title']
    count = int(c['citation_count'])
    citation_sums[t] = citation_sums.get(t, 0) + count

results = []

venue_pattern = re.compile(r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|MobileHCI|IMWUT|Proceedings|Conference)\s*.*?(20[0-2][0-9])', re.IGNORECASE)
copyright_pattern = re.compile(r'Copyright\s+(?:©|\(c\))?\s*(20[0-2][0-9])', re.IGNORECASE)
acm_pattern = re.compile(r'ACM\s*.*?(20[0-2][0-9])', re.IGNORECASE)

for p in papers:
    text = p['text']
    filename = p['filename']
    title = filename.replace('.txt', '')
    
    # Year Extraction
    found_years = []
    
    # Check headers/footers (start and end)
    # Combining first 2000 and last 2000 chars
    search_text = text[:2000] + "\n" + text[-2000:]
    
    # Pattern matching
    for m in venue_pattern.findall(search_text):
        found_years.append(int(m[1]))
    for m in copyright_pattern.findall(search_text):
        found_years.append(int(m))
    for m in acm_pattern.findall(search_text):
        found_years.append(int(m))
    
    # Simple regex for year if no specific pattern found, but only in header/footer
    if not found_years:
        simple_years = re.findall(r'20[0-2][0-9]', search_text)
        found_years.extend([int(y) for y in simple_years])

    # Determine year
    year = None
    if found_years:
        # Count frequency
        c = Counter(found_years)
        # Prefer years between 2010 and 2025
        valid_years = {y: count for y, count in c.items() if 2010 <= y <= 2025}
        if valid_years:
            year = max(valid_years, key=valid_years.get)
        else:
             # Just take the most common
             year = c.most_common(1)[0][0]
    
    # Fallback: if we still don't have a year, maybe look deeper?
    # Assuming the above covers most.
    
    # Contribution Extraction
    is_empirical = "empirical" in text.lower()
    
    if year and year > 2016 and is_empirical:
        total_c = citation_sums.get(title, 0)
        results.append({"title": title, "total_citation_count": total_c})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-1382832429316452546': ['paper_docs'], 'var_function-call-1382832429316454187': ['Citations', 'sqlite_sequence'], 'var_function-call-12576902616845472384': 'file_storage/function-call-12576902616845472384.json', 'var_function-call-9106356078782033053': 'file_storage/function-call-9106356078782033053.json', 'var_function-call-7203993170122994378': 'file_storage/function-call-7203993170122994378.json', 'var_function-call-9603352317542376889': [], 'var_function-call-10921488412089867487': {'total_papers': 5, 'sample_debug': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'is_empirical': False, 'in_citations': True}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'is_empirical': False, 'in_citations': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'is_empirical': True, 'in_citations': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'is_empirical': True, 'in_citations': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'is_empirical': False, 'in_citations': True}], 'stats': {'count_empirical': 2, 'count_year_found': 1, 'count_year_gt_2016': 0, 'count_matched_title': 5}}, 'var_function-call-15080538060224287608': 'file_storage/function-call-15080538060224287608.json', 'var_function-call-1845169715576085817': [], 'var_function-call-15525855107537648939': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'year': None}, {'title': 'Charting Design Preferences on Wellness Wearables', 'year': None}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'year': None}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'year': None}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'year': None}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'year': None}, {'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'year': None}, {'title': 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game', 'year': None}, {'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'year': None}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'year': 2016}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach', 'year': None}, {'title': 'From Nobody Cares to Way to Go!: A Design Framework for Social Sharing in Personal Informatics', 'year': None}, {'title': 'Goal-oriented Visualizations of Activity Tracking: A Case Study with Engineering Students', 'year': None}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'year': None}, {'title': 'Heed: Exploring the Design of Situated Self-Reporting Devices', 'year': None}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'year': None}, {'title': 'Intelligent Computing in Personal Informatics: Key Design Considerations', 'year': None}, {'title': 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics', 'year': None}], 'var_function-call-4381640419044326084': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith  30  stakeholders  (9  medical  professionals  and  21  end-\nusers)  an  OAB  mobile  health  application  that  aims  to \nincrease  adherence  to  self-managed  treatment.  Our  results \nsupport previous research that visualizing progress, setting \ngoals, receiving reminders and feedback  increases  use.  We \ndiscovered  that  games  could  be  used  successfully  as  a \ndistraction technique for urge suppression. Contrary to the \ncurrent research direction, automatically calculated features \n', 'var_function-call-3438152456902612955': ' and  Dawn  Skelton.  2012.  Senior \nto  Design  Enjoyable  Falls \n\nDesigners:  Empowering  Seniors \nRehabilitation Tools. In Proc. ACM CHI’12. \n\n[59]   Stephen Uzor and Lynne Baillie. 2018. Exploring the Communication \nof  Progress  in  Home-based  Falls  Rehabilitation  using  Exergame \nTechnologies.  Proceedings  of  the  ACM  on  Interactive,  Mobile, \nWearable and Ubiquitous Technologies.  \n\n[60]   Leena  Ventä, Minna  Isomursu, Aino  Ahtinen  and Shruti  Ramiah. \n2008. My Phone is a Part of My Soul – How People Bond with Their \nMobile Phones. In Proc. ACM MobileHCI’08. \n\n[61]   Lois M. Verbrugg 1980. Health diaries. Medical care 18.1: 73-95. \n[62]  Graham  Wilson  and  Stephen  A.  Brewster.  2017.  Multi-Moji: \nCombining  Thermal,  Vibrotactile  &  Visual  Stimuli  to  Expand  the \nAffective Range of Feedback. In Proc. CHI’17. \n\n[63]   2048, https://en.wikipedia.org/wiki/2048_(video_game) \n\nCHI 2019 Paper  CHI 2019, May 4–9, 2019, Glasgow, Scotland, UKPaper 703Page 14 \n \n \n \n \n\x0c'}

exec(code, env_args)
