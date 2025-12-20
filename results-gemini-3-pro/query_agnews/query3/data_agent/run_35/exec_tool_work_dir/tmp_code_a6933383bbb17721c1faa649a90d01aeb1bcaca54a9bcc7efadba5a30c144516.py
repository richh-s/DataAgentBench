code = """import json
import re

# Load metadata
metadata_key = 'var_function-call-3785327814520365478'
metadata_file = locals()[metadata_key]
with open(metadata_file, 'r') as f:
    metadata_list = json.load(f)

article_years = {}
for entry in metadata_list:
    aid = str(entry['article_id'])
    pub_date = entry['publication_date']
    year = int(pub_date.split('-')[0])
    article_years[aid] = year

# Load articles (larger file)
articles_key = 'var_function-call-2040390662769178937'
articles_file = locals()[articles_key]
with open(articles_file, 'r') as f:
    articles_list = json.load(f)

# Keywords
business_keywords = [
    'market', 'markets', 'stock', 'stocks', 'wall street', 'dow', 'nasdaq', 'nyse', 
    'economy', 'economic', 'financial', 'finance', 'business', 'invest', 'investment', 
    'investor', 'bank', 'banks', 'banking', 'interest rate', 'fed', 'federal reserve', 
    'inflation', 'dollar', 'euro', 'currency', 'trade', 'deficit', 'surplus', 'profit', 
    'profits', 'earnings', 'revenue', 'loss', 'losses', 'quarterly', 'share', 'shares', 
    'company', 'companies', 'corp', 'corporation', 'inc', 'merger', 'acquisition', 'deal', 
    'buyout', 'ipo', 'ceo', 'oil', 'crude', 'prices', 'barrel', 'gasoline', 'energy', 'imf', 'wto',
    'bonds', 'treasury', 'yield', 'loan', 'credit', 'mortgage', 'sales', 'retail', 'consumer'
]

scitech_keywords = [
    'technology', 'tech', 'science', 'computer', 'computers', 'software', 'hardware', 
    'internet', 'web', 'online', 'net', 'telecom', 'wireless', 'mobile', 'cellphone', 
    'phone', 'broadband', 'satellite', 'space', 'nasa', 'astronomy', 'biology', 'physics', 
    'research', 'microsoft', 'google', 'apple', 'ibm', 'intel', 'linux', 'windows', 'virus', 
    'hacker', 'spam', 'search engine', 'chip', 'processor', 'digital', 'electronic', 'gadget'
]

sports_keywords = [
    'sport', 'sports', 'baseball', 'basketball', 'football', 'soccer', 'hockey', 'tennis', 
    'golf', 'rugby', 'cricket', 'game', 'games', 'match', 'tournament', 'cup', 'league', 
    'team', 'teams', 'player', 'players', 'coach', 'champion', 'championship', 'olympics', 
    'olympic', 'medal', 'gold', 'score', 'win', 'won', 'loss', 'lost', 'victory', 'defeat', 
    'season', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'athlete', 'athletics'
]

world_keywords = [
    'world', 'international', 'politics', 'political', 'government', 'president', 'premier', 
    'minister', 'official', 'officials', 'election', 'vote', 'voters', 'campaign', 'war', 
    'military', 'army', 'troops', 'soldiers', 'peace', 'treaty', 'accord', 'un', 'united nations', 
    'iraq', 'iran', 'palestine', 'israel', 'afghanistan', 'syria', 'attack', 'bomb', 'blast', 
    'kill', 'killed', 'police', 'court', 'trial', 'judge', 'prison', 'protest', 'riot', 'crisis', 
    'disaster', 'parliament', 'senate', 'congress', 'law', 'legal'
]

def count_keywords(text, keywords):
    count = 0
    text_lower = text.lower()
    for kw in keywords:
        if ' ' in kw:
            if kw in text_lower:
                count += 1
        else:
            if re.search(r'\b' + re.escape(kw) + r'\b', text_lower):
                count += 1
    return count

yearly_counts = {y: 0 for y in range(2010, 2021)}
matched_count = 0

for article in articles_list:
    aid = str(article['article_id'])
    if aid in article_years:
        matched_count += 1
        year = article_years[aid]
        text = (article.get('title', '') + " " + article.get('description', ''))
        
        c_bus = count_keywords(text, business_keywords)
        c_sci = count_keywords(text, scitech_keywords)
        c_spo = count_keywords(text, sports_keywords)
        c_wor = count_keywords(text, world_keywords)
        
        scores = {'Business': c_bus, 'Sci/Tech': c_sci, 'Sports': c_spo, 'World': c_wor}
        max_score = max(scores.values())
        
        if max_score > 0:
            top_cats = [k for k, v in scores.items() if v == max_score]
            # Prioritize Business if tied
            if 'Business' in top_cats:
                category = 'Business'
            else:
                category = top_cats[0]
                
            if category == 'Business':
                yearly_counts[year] += 1

total_business = sum(yearly_counts.values())
num_years = 11
average = total_business / num_years

result = {
    "yearly_counts": yearly_counts,
    "average": average,
    "matched_count": matched_count,
    "total_metadata": len(article_years)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-3785327814520365478': 'file_storage/function-call-3785327814520365478.json', 'var_function-call-10425828837385434801': 14860, 'var_function-call-14030611635613635526': ['articles'], 'var_function-call-14105563126826159578': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8122656162104347158': 5, 'var_function-call-10461147015258945080': 'file_storage/function-call-10461147015258945080.json', 'var_function-call-16342635927272023977': {'yearly_counts': {'2010': 50, '2011': 68, '2012': 47, '2013': 61, '2014': 59, '2015': 55, '2016': 63, '2017': 62, '2018': 73, '2019': 51, '2020': 64}, 'average': 59.36363636363637}, 'var_function-call-14388110284107897755': {'yearly_counts': {'2010': 1, '2011': 4, '2012': 4, '2013': 6, '2014': 1, '2015': 1, '2016': 7, '2017': 3, '2018': 4, '2019': 3, '2020': 3}, 'average': 3.3636363636363638}, 'var_function-call-11446294870613741721': {'total_metadata': 14860, 'total_articles': 20000, 'matched': 2273}, 'var_function-call-2040390662769178937': 'file_storage/function-call-2040390662769178937.json'}

exec(code, env_args)
