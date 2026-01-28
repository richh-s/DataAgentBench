code = """import json
import re

# Load citations
citations_key = 'var_function-call-14861443508322681236'
with open(locals()[citations_key], 'r') as f:
    citations_data = json.load(f)

# Aggregate citations by title
citation_counts = {}
for c in citations_data:
    t = c['title']
    count = int(c['citation_count'])
    citation_counts[t] = citation_counts.get(t, 0) + count

# Load papers
papers_key = 'var_function-call-1947762228881266501'
with open(locals()[papers_key], 'r') as f:
    papers_data = json.load(f)

results = []

for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    title = filename.replace('.txt', '')
    
    # Extract Year
    # Look in the first 1000 chars
    header = text[:1000]
    years = re.findall(r'\b(20\d{2})\b', header)
    
    pub_year = None
    if years:
        # Take the first year found? Or the most frequent? 
        # Usually the first one in the header is the publication year.
        # But sometimes there are other years (e.g. "since 2000").
        # Let's assume the first one is correct.
        pub_year = int(years[0])
    
    # Check if published after 2016
    if pub_year is None or pub_year <= 2016:
        continue
    
    # Check Contribution
    # Hint: "Fields like ... contribution may contain multiple values"
    # Hint: "use substring/contains matching"
    # I'll check if "empirical" is in the text.
    # To be safer, I'll check if "contribution" is mentioned near "empirical" or just "empirical" exists?
    # Given the unstructured nature and the hint, I'll check for "empirical" anywhere.
    # But wait, "empirical" is a common word. 
    # Maybe I should check if it's in the abstract or introduction?
    # Or maybe there is a hidden list?
    # Let's search for "empirical" (case insensitive).
    
    if 'empirical' in text.lower():
        # Get citation count
        total_citations = citation_counts.get(title, 0)
        results.append({
            "title": title,
            "citation_count": total_citations,
            "year": pub_year
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-13973424374790880036': 'file_storage/function-call-13973424374790880036.json', 'var_function-call-13973424374790878367': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-3366737603932088961': 'file_storage/function-call-3366737603932088961.json', 'var_function-call-8593920629685848414': {'count': 5, 'samples': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'year_extracted': None, 'contrib_context': 'contributions  through  survey  design  and  participant  interviews. \nWe  also  thank  Elena  Agapi'}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'year_extracted': None, 'contrib_context': 'contributions  in  this  paper:  1)  we \nidentify  problems  across  personal  informatics  tools,  '}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'year_extracted': None, 'contrib_context': None}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'year_extracted': None, 'contrib_context': 'contribution “I like drawing!” (UP4),  some  did not like \ndrawing: “I don’t like drawing things.” ('}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'year_extracted': None, 'contrib_context': 'contribution of this research is \na  system  designed  to  support  the  work  of  occupational \nthe'}]}, 'var_function-call-1947762228881266501': 'file_storage/function-call-1947762228881266501.json', 'var_function-call-14861443508322681236': 'file_storage/function-call-14861443508322681236.json'}

exec(code, env_args)
