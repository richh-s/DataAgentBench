code = """import json
import pandas as pd
import re

# Load metadata
with open(locals()['var_function-call-11138479476113441497'], 'r') as f:
    metadata_list = json.load(f)

# Load articles
with open(locals()['var_function-call-3099874506033231906'], 'r') as f:
    articles_list = json.load(f)

# Convert articles to dict for fast lookup
articles_dict = {int(a['article_id']): a for a in articles_list}

# Keywords
keywords = {
    'Business': ['business', 'economy', 'market', 'stock', 'trade', 'finance', 'financial', 'invest', 'bank', 'money', 'dollar', 'euro', 'yen', 'currency', 'profit', 'loss', 'revenue', 'sales', 'price', 'cost', 'rate', 'tax', 'inflation', 'fed', 'treasury', 'bond', 'loan', 'credit', 'debt', 'ipo', 'share', 'dividend', 'dow', 'nasdaq', 'wall street', 'ceo', 'cfo', 'merger', 'acquisition', 'deal', 'oil', 'gas', 'energy', 'commodit', 'gold', 'silver', 'audit', 'accounting', 'recession', 'growth', 'budget', 'deficit', 'employment', 'jobless', 'retail', 'consumer', 'spending'],
    'Sports': ['sport', 'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis', 'golf', 'rugby', 'cricket', 'f1', 'formula 1', 'racing', 'athlete', 'player', 'team', 'coach', 'manager', 'game', 'match', 'tournament', 'cup', 'league', 'championship', 'olympic', 'medal', 'win', 'lose', 'draw', 'score', 'goal', 'touchdown', 'homerun', 'wicket', 'inning', 'penalty', 'referee', 'stadium', 'club', 'season', 'playoff', 'final', 'semi-final'],
    'Sci/Tech': ['technology', 'tech', 'science', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 'digital', 'mobile', 'phone', 'smartphone', 'app', 'application', 'network', 'wireless', 'broadband', 'server', 'data', 'database', 'cyber', 'virus', 'hacker', 'security', 'chip', 'processor', 'microsoft', 'google', 'apple', 'intel', 'ibm', 'linux', 'windows', 'browser', 'search engine', 'space', 'nasa', 'astronomy', 'biology', 'physics', 'chemistry', 'genetics', 'medical', 'drug', 'research', 'scientist', 'laboratory', 'robot', 'ai', 'artificial intelligence'],
    'World': ['world', 'international', 'politic', 'government', 'president', 'minister', 'premier', 'senate', 'parliament', 'congress', 'election', 'vote', 'campaign', 'candidate', 'war', 'peace', 'conflict', 'military', 'army', 'navy', 'air force', 'troops', 'soldier', 'rebel', 'terror', 'bomb', 'blast', 'attack', 'kill', 'die', 'injured', 'disaster', 'quake', 'flood', 'storm', 'hurricane', 'typhoon', 'tsunami', 'crash', 'accident', 'crime', 'police', 'court', 'judge', 'law', 'legal', 'treaty', 'agreement', 'negotiation', 'diplomat', 'un', 'united nations', 'eu', 'european union', 'nato']
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in keywords}
    for cat, kw_list in keywords.items():
        for kw in kw_list:
            # Simple substring match or word boundary? Word boundary is better but slower.
            # Using simple check for now.
            # To be more precise, let's tokenize or check boundaries if possible.
            # But simple check `kw in text` often works well enough for these tasks.
            # Let's count occurrences?
            scores[cat] += text.count(kw)
    
    # Return category with max score
    # If all 0, default to something? Or maybe "World" as general?
    if max(scores.values()) == 0:
        return 'Unknown'
    
    return max(scores, key=scores.get)

business_counts = {}
years = range(2010, 2021)
for y in years:
    business_counts[y] = 0

processed_count = 0
for meta in metadata_list:
    aid = int(meta['article_id'])
    pub_date = meta['publication_date'] # YYYY-MM-DD
    year = int(pub_date[:4])
    
    if aid in articles_dict:
        art = articles_dict[aid]
        text = (art.get('title', '') + " " + art.get('description', ''))
        category = classify(text)
        
        if category == 'Business':
            business_counts[year] += 1
        
        processed_count += 1

total_business = sum(business_counts.values())
average = total_business / len(years)

result = {
    "business_counts_per_year": business_counts,
    "average": average,
    "processed_count": processed_count
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-11138479476113441497': 'file_storage/function-call-11138479476113441497.json', 'var_function-call-12022955013043577644': {'count': 14860, 'min_id': 3, 'max_id': 127583}, 'var_function-call-11598675633361403098': [{'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}], 'var_function-call-16201598819874038362': 5, 'var_function-call-3099874506033231906': 'file_storage/function-call-3099874506033231906.json'}

exec(code, env_args)
