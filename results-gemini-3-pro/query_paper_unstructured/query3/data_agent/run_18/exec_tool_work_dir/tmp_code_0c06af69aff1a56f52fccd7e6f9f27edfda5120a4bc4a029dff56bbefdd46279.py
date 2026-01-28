code = """import json
import re

# Load papers
with open(locals()['var_function-call-11547214803313997726'], 'r') as f:
    papers_data = json.load(f)

print("__RESULT__:")
target_titles = [
    "Everybody Knows What You're Doing: A Critical Design Approach to Personal Informatics", 
    "Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use",
    "Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym",
    "See Friendship, Sort of: How Conversation and Digital Traces Might Support Reflection on Friendships"
]

found_targets = []

for doc in papers_data:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    # Check if title is in targets
    # Case insensitive matching for safety
    if any(t.lower() == title.lower() for t in target_titles):
        # Extract Year
        year = None
        header_match = re.search(r"([A-Z]{2,})\s+'(\d{2})", text[:300])
        if header_match:
            y_short = int(header_match.group(2))
            if 0 <= y_short <= 30:
                year = 2000 + y_short
        if not year:
            copy_match = re.search(r'Copyright\s.*?(\d{4})', text[:3000], re.IGNORECASE)
            if copy_match:
                year = int(copy_match.group(1))
        if not year:
            year_match = re.search(r'\b(20\d\d)\b', text[:500])
            if year_match:
                year = int(year_match.group(1))
        
        # Check empirical
        has_empirical = "empirical" in text.lower()
        
        found_targets.append({
            "title": title,
            "extracted_year": year,
            "has_empirical": has_empirical,
            "text_preview": text[:200]
        })

print(json.dumps(found_targets))"""

env_args = {'var_function-call-15870197178321181346': 'file_storage/function-call-15870197178321181346.json', 'var_function-call-15870197178321180761': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-5877010014911458978': 'file_storage/function-call-5877010014911458978.json', 'var_function-call-15161005825129355678': 'file_storage/function-call-15161005825129355678.json', 'var_function-call-14023155913287027792': 'file_storage/function-call-14023155913287027792.json', 'var_function-call-14333893458989342011': [], 'var_function-call-16530110269305427312': [{'title': "Everybody Knows What You'Re Doing: A Critical Design Approach to Personal Informatics", 'total_citations': '694'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': '636'}, {'title': 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym', 'total_citations': '595'}, {'title': 'See Friendship, Sort of: How Conversation and Digital Traces Might Support Reflection on Friendships', 'total_citations': '593'}, {'title': 'Shifting Dynamics or Breaking Sacred Traditions?: The Role of Technology in Twelve-step Fellowships', 'total_citations': '587'}], 'var_function-call-11547214803313997726': 'file_storage/function-call-11547214803313997726.json', 'var_function-call-4200250418715985286': []}

exec(code, env_args)
