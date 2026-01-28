code = """import json
import re

# Get file paths
papers_path = locals()['var_function-call-11129089221235827665']
citations_path = locals()['var_function-call-3385159612181082423']

# Load Citations
try:
    with open(citations_path, 'r') as f:
        citations_data = json.load(f)
    
    # Map title -> total citations (summing up all years for each title)
    citation_map = {}
    for row in citations_data:
        t = row['title']
        c = row['total_citations']
        # c is likely a string from the preview, check type.
        # But SQLite SUM returns a number usually, but let's be safe.
        try:
            val = int(c)
        except:
            val = 0
        citation_map[t] = citation_map.get(t, 0) + val
            
except Exception as e:
    print(f"Error loading citations: {e}")
    citation_map = {}

results = []

try:
    with open(papers_path, 'r') as f:
        papers = json.load(f)
        
    for doc in papers:
        text = doc.get('text', '')
        filename = doc.get('filename', '')
        title = filename.replace('.txt', '')
        
        # Extract Year (First 500 chars)
        header = text[:500]
        
        # Find 4 digit years 20xx
        matches_4d = re.findall(r'\b(20\d{2})\b', header)
        
        # Find 2 digit years 'xx
        matches_2d = re.findall(r"'(\d{2})\b", header)
        
        found_year = None
        
        # Prefer 4 digit years
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
        
        # Check Criteria
        is_after_2016 = (found_year is not None) and (found_year > 2016)
        is_empirical = "empirical" in text.lower()
        
        if is_after_2016 and is_empirical:
            # Check if title exists in citation map
            # The prompt says title matches filename without extension.
            # But keys in citation_map might be case sensitive?
            # SQLite is usually case sensitive for string comparison unless specified.
            # Filenames might have different casing?
            # Let's try exact match first.
            
            if title in citation_map:
                total = citation_map[title]
                results.append({"title": title, "total_citation_count": total})
            else:
                # Debugging: maybe case mismatch?
                # Try finding case-insensitive match
                # (Slow but safe for small list)
                for c_title, count in citation_map.items():
                    if c_title.lower() == title.lower():
                        results.append({"title": c_title, "total_citation_count": count})
                        break
    
except Exception as e:
    print(f"Error processing papers: {e}")

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-12008909793186569857': ['paper_docs'], 'var_function-call-12008909793186566274': 'file_storage/function-call-12008909793186566274.json', 'var_function-call-12008909793186566787': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-7300462932011158786': 'file_storage/function-call-7300462932011158786.json', 'var_function-call-3385159612181082423': 'file_storage/function-call-3385159612181082423.json', 'var_function-call-15182070709462479705': 'check_complete', 'var_function-call-17779314564341058459': [], 'var_function-call-14079571341064099093': {'error': "[Errno 2] No such file or directory: 'var_function-call-7300462932011158786.json'"}, 'var_function-call-1918080602887774637': {'year_counts': {}, 'empirical_count': 2, 'after_2016_count': 0, 'both_count': 0}, 'var_function-call-7311144611923919482': 'debug_done', 'var_function-call-1686346562381530303': {'total_papers': 5, 'header_repr': '"UBICOMP \'15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\\n\\nA Lived Informatics Model of Personal Informatics \\n\\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \\n1Computer Science & Engineering, 2Human Centered Design & Engineering \\nDUB Group, University of Washington \\n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \\n\\nABSTRACT \\nCurrent  models  of  how  people  use  personal  informatics \\nsystems are largely based in behavior change goals. They do \\nnot  adequately  characteriz"', 'matches_20xx': [], 'matches_short': []}, 'var_function-call-11129089221235827665': 'file_storage/function-call-11129089221235827665.json'}

exec(code, env_args)
