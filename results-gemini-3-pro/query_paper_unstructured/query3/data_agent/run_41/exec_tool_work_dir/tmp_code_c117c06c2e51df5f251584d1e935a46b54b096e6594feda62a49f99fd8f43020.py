code = """import json
import re

papers_path = locals()['var_function-call-11129089221235827665']
citations_path = locals()['var_function-call-3385159612181082423']

stats = {
    "papers_loaded": 0,
    "citations_loaded": 0,
    "after_2016_count": 0,
    "empirical_count": 0,
    "both_count": 0,
    "matched_title_count": 0,
    "sample_years": [],
    "sample_titles_after_2016": [],
    "sample_citation_titles": []
}

try:
    with open(citations_path, 'r') as f:
        citations_data = json.load(f)
    stats["citations_loaded"] = len(citations_data)
    citation_titles = {row['title'] for row in citations_data}
    stats["sample_citation_titles"] = list(citation_titles)[:5]

    with open(papers_path, 'r') as f:
        papers = json.load(f)
    stats["papers_loaded"] = len(papers)

    for doc in papers:
        text = doc.get('text', '')
        header = text[:500]
        
        matches_4d = re.findall(r'\b(20\d{2})\b', header)
        matches_2d = re.findall(r"'(\d{2})\b", header)
        
        found_year = None
        for y in matches_4d:
            iy = int(y)
            if 2000 <= iy <= 2025:
                found_year = iy
                break
        if not found_year:
            for y in matches_2d:
                iy = int("20" + y)
                if 2000 <= iy <= 2025:
                    found_year = iy
                    break
        
        if found_year:
            if len(stats["sample_years"]) < 10:
                stats["sample_years"].append(found_year)
            
            if found_year > 2016:
                stats["after_2016_count"] += 1
                if len(stats["sample_titles_after_2016"]) < 5:
                    stats["sample_titles_after_2016"].append(doc.get('filename'))
                
                is_empirical = "empirical" in text.lower()
                if is_empirical:
                    stats["empirical_count"] += 1
                    stats["both_count"] += 1
                    
                    title = doc.get('filename', '').replace('.txt', '')
                    if title in citation_titles:
                        stats["matched_title_count"] += 1

except Exception as e:
    stats["error"] = str(e)

print("__RESULT__:")
print(json.dumps(stats))"""

env_args = {'var_function-call-12008909793186569857': ['paper_docs'], 'var_function-call-12008909793186566274': 'file_storage/function-call-12008909793186566274.json', 'var_function-call-12008909793186566787': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-7300462932011158786': 'file_storage/function-call-7300462932011158786.json', 'var_function-call-3385159612181082423': 'file_storage/function-call-3385159612181082423.json', 'var_function-call-15182070709462479705': 'check_complete', 'var_function-call-17779314564341058459': [], 'var_function-call-14079571341064099093': {'error': "[Errno 2] No such file or directory: 'var_function-call-7300462932011158786.json'"}, 'var_function-call-1918080602887774637': {'year_counts': {}, 'empirical_count': 2, 'after_2016_count': 0, 'both_count': 0}, 'var_function-call-7311144611923919482': 'debug_done', 'var_function-call-1686346562381530303': {'total_papers': 5, 'header_repr': '"UBICOMP \'15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\\n\\nA Lived Informatics Model of Personal Informatics \\n\\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \\n1Computer Science & Engineering, 2Human Centered Design & Engineering \\nDUB Group, University of Washington \\n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \\n\\nABSTRACT \\nCurrent  models  of  how  people  use  personal  informatics \\nsystems are largely based in behavior change goals. They do \\nnot  adequately  characteriz"', 'matches_20xx': [], 'matches_short': []}, 'var_function-call-11129089221235827665': 'file_storage/function-call-11129089221235827665.json', 'var_function-call-8320219813278591190': []}

exec(code, env_args)
