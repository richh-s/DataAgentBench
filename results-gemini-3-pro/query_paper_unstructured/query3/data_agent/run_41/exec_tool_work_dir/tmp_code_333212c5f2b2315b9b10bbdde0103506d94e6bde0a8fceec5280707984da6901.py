code = """import json
import re

# Access the file path from the variable
papers_path = locals()['var_function-call-7300462932011158786']

try:
    with open(papers_path, 'r') as f:
        papers = json.load(f)

    year_counts = {}
    empirical_count = 0
    after_2016_count = 0
    both_count = 0
    
    for doc in papers:
        text = doc.get('text', '')
        header = text[:1000]
        
        # Determine Year
        all_years = re.findall(r'\b(20\d{2})\b', header)
        
        found_year = None
        for y in all_years:
            iy = int(y)
            if 2000 <= iy <= 2025:
                found_year = iy
                break
        
        if not found_year:
            # check for '17 pattern
            short_years = re.findall(r"'(\d{2})\b", header)
            for y in short_years:
                iy = int("20" + y)
                if 2000 <= iy <= 2025:
                    found_year = iy
                    break

        # Stats
        if found_year:
            year_counts[found_year] = year_counts.get(found_year, 0) + 1
            if found_year > 2016:
                after_2016_count += 1
        
        is_empirical = "empirical" in text.lower()
        if is_empirical:
            empirical_count += 1
            
        if found_year and found_year > 2016 and is_empirical:
            both_count += 1

    print("__RESULT__:")
    result_stats = {
        "year_counts": year_counts,
        "empirical_count": empirical_count,
        "after_2016_count": after_2016_count,
        "both_count": both_count
    }
    print(json.dumps(result_stats))
    
except Exception as e:
    print("__RESULT__:")
    print(json.dumps({"error": str(e)}))"""

env_args = {'var_function-call-12008909793186569857': ['paper_docs'], 'var_function-call-12008909793186566274': 'file_storage/function-call-12008909793186566274.json', 'var_function-call-12008909793186566787': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-7300462932011158786': 'file_storage/function-call-7300462932011158786.json', 'var_function-call-3385159612181082423': 'file_storage/function-call-3385159612181082423.json', 'var_function-call-15182070709462479705': 'check_complete', 'var_function-call-17779314564341058459': [], 'var_function-call-14079571341064099093': {'error': "[Errno 2] No such file or directory: 'var_function-call-7300462932011158786.json'"}}

exec(code, env_args)
