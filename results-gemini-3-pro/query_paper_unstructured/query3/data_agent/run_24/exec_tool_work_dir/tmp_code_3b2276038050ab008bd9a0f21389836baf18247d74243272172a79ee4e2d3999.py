code = """import json
import re
import pandas as pd

# Load citations
citations_file_path = locals()['var_function-call-8765785804266823925']
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

df = pd.DataFrame(citations_data)
df['citation_count'] = pd.to_numeric(df['citation_count'])
df['citation_year'] = pd.to_numeric(df['citation_year'])

# Group by title
# Calculate min citation year and total citations
grouped = df.groupby('title').agg({
    'citation_year': 'min',
    'citation_count': 'sum'
}).reset_index()

# Filter potential candidates based on citations starting > 2016
# Note: A paper published in 2016 could have citations in 2017.
# But if it has citations in 2016, it's definitely <= 2016.
# If min_citation_year > 2016, it implies no citations in 2016.
# This keeps 2017+ papers, and potentially 2016 papers with delayed citations.
candidates_df = grouped[grouped['citation_year'] > 2016]
candidate_titles = set(candidates_df['title'])
candidate_map = candidates_df.set_index('title')['citation_count'].to_dict()

# Load papers
papers_file_path = locals()['var_function-call-10316404265600385483']
with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

empirical_keywords = ["empirical", "user study", "participants", "interview", "experiment", "field study", "n="]

final_results = []

for paper in papers_data:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    if title not in candidate_titles:
        continue
        
    text = paper.get('text', '')
    header = text[:2000] # Check first 2000 chars for year
    
    # Check for publication year in header to filter out 2016 papers
    # Look for 2010-2016. If found, exclude.
    # Look for 2017-2025. If found, keep.
    # Regex for year
    years_found = re.findall(r'\b(20\d{2})\b', header)
    years_found = [int(y) for y in years_found]
    
    # Logic:
    # If any year <= 2016 is found in header, assume it's the pub year (or copyright) -> Exclude.
    # Unless there is ALSO a year > 2016? No, usually pub year is single.
    # Be careful of "Since 2010..."
    # But headers usually contain "Proceedings of ... 2015".
    
    has_old_year = any(y <= 2016 for y in years_found)
    has_new_year = any(y > 2016 for y in years_found)
    
    if has_old_year and not has_new_year:
        continue # It's likely <= 2016
    
    # If no year found, we rely on min_citation_year > 2016.
    # (Which we already filtered).
    
    # Check empirical
    text_lower = text.lower()
    is_empirical = any(k in text_lower for k in empirical_keywords)
    
    if is_empirical:
        final_results.append({
            "title": title,
            "total_citation_count": candidate_map[title]
        })

final_results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-2080358657401428239': 'file_storage/function-call-2080358657401428239.json', 'var_function-call-4922993133298785860': ['paper_docs'], 'var_function-call-4922993133298782503': ['Citations', 'sqlite_sequence'], 'var_function-call-15480292294165083401': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-10316404265600385483': 'file_storage/function-call-10316404265600385483.json', 'var_function-call-8350695654712224507': [{'count(*)': '1405'}], 'var_function-call-8765785804266825960': 'file_storage/function-call-8765785804266825960.json', 'var_function-call-8765785804266823925': 'file_storage/function-call-8765785804266823925.json', 'var_function-call-5730915488565907792': [], 'var_function-call-5254736183491458142': [{'title': 'A Lived Informatics Model of Personal Informatics', 'extracted_year': 0, 'is_empirical': False, 'in_citations': True}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'extracted_year': 0, 'is_empirical': False, 'in_citations': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'extracted_year': 0, 'is_empirical': True, 'in_citations': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'extracted_year': 0, 'is_empirical': True, 'in_citations': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'extracted_year': 0, 'is_empirical': False, 'in_citations': True}], 'var_function-call-15128375922083714200': {'text_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'years_found': ['2015']}, 'var_function-call-16820794468883058681': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'is_empirical': True, 'found_keywords': ['participants', 'interview', 'experiment']}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 0, 'is_empirical': True, 'found_keywords': ['participants', 'interview']}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 0, 'is_empirical': True, 'found_keywords': ['empirical', 'user study', 'participants', 'experiment']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 0, 'is_empirical': True, 'found_keywords': ['empirical', 'participants', 'interview', 'field study']}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 0, 'is_empirical': True, 'found_keywords': ['participants', 'interview']}], 'var_function-call-17302014328088869030': [{'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that use'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The University of Melbourne, Australia \n2Queensland University of Technology, Brisbane, Australia \n3Department of Mechanical Engineering, The University of Melbourne, Australia \n4Augmented Human Lab, Singapor'}]}

exec(code, env_args)
