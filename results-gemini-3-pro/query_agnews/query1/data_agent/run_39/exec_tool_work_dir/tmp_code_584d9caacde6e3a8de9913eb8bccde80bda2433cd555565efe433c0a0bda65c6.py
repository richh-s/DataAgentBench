code = """import json

# Load data
file_path = locals()['var_function-call-16366185443636566609']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define keywords
# Using sets for faster lookup if single words, but for phrases need list
positive_keywords = [
    "olympic", "olympics", "medal", "athens", "phelps", "thorpe", "gymnastics", "swimming", 
    "football", "soccer", "basketball", "baseball", "hockey", "tennis", "golf", "cricket", "rugby",
    "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "pga", "atp", "wta", "nascar", "formula one", "f1",
    "red sox", "yankees", "mets", "dodgers", "giants", "lakers", "celtics", "bulls", "pistons", "spurs",
    "arsenal", "manchester", "liverpool", "chelsea", "real madrid", "barcelona", "ac milan", "juventus",
    "ferrari", "schumacher", "williams", "renault", "cycling", "armstrong", "doping", "athlete", 
    "tournament", "championship", "super bowl", "world cup", "davis cup", "ryder cup", "grand slam",
    "quarterback", "touchdown", "home run", "slam dunk", "goalie", "striker", "midfielder"
]

negative_keywords = [
    "stocks", "stock market", "wall st", "economy", "economic", "oil", "price", "prices", "company", "companies", 
    "corp", "profit", "profits", "earnings", "revenue", "loss", "losses", "share", "shares", "investor", "investment",
    "bank", "banking", "dollar", "euro", "yen", "currency", "trade", "deficit", "surplus", "gdp", "inflation",
    "iraq", "war", "military", "army", "troops", "bomb", "blast", "attack", "president", "bush", "kerry", "minister", 
    "election", "vote", "voters", "campaign", "party", "politics", "congress", "senate", "parliament", "un", "united nations",
    "microsoft", "google", "apple", "intel", "ibm", "software", "hardware", "internet", "web", "online", "search engine",
    "virus", "hacker", "technology", "science", "space", "nasa", "astronomer", "study", "research", "cell", "cancer"
]

sports_articles = []

for art in articles:
    text = (art.get('title', '') + " " + art.get('description', '')).lower()
    
    # Check positive
    p_score = 0
    for k in positive_keywords:
        if k in text:
            p_score += 1
            
    # Check negative
    n_score = 0
    for k in negative_keywords:
        if k in text:
            n_score += 1
            
    # Decision
    # Heuristic: significantly more sports terms or at least one strong sports term and low negative score
    # "Athens" alone might be enough if n_score is low.
    
    if p_score > 0 and p_score >= n_score:
        # Additional filter: if "company" or "stocks" appears, unlikely to be sports unless it's about a sports company (rare in news)
        # But allow "Giants" (team).
        
        # Let's verify lengths
        desc_len = len(art.get('description', ''))
        sports_articles.append({
            "title": art.get('title', ''),
            "description": art.get('description', ''),
            "len": desc_len,
            "p_score": p_score,
            "n_score": n_score
        })

# Sort by length descending
sports_articles.sort(key=lambda x: x['len'], reverse=True)

# Return top 5
print("__RESULT__:")
print(json.dumps(sports_articles[:5]))"""

env_args = {'var_function-call-15833744807724612077': [{'_id': '694481cbad2196511b261e49', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-3143975441130387556': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-11469297530681085735': ['authors', 'article_metadata'], 'var_function-call-5301725884931679165': ['articles'], 'var_function-call-9012431321503117105': [{'_id': '694481cbad2196511b261e49', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694481cbad2196511b261e4a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694481cbad2196511b261e4b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694481cbad2196511b261e4c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694481cbad2196511b261e4d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6879128558389348832': [{'_id': '694481cbad2196511b261e49', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694481cbad2196511b261e4a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694481cbad2196511b261e4b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694481cbad2196511b261e4c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694481cbad2196511b261e4d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-12762286513692276929': [], 'var_function-call-16365618101106747855': {'count': 5, 'first_5': [{'_id': '694481cbad2196511b261e49', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694481cbad2196511b261e4a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694481cbad2196511b261e4b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694481cbad2196511b261e4c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694481cbad2196511b261e4d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}, 'var_function-call-18118414036913127772': [{'_id': '694481cbad2196511b261e49', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694481cbad2196511b261e4a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694481cbad2196511b261e4b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694481cbad2196511b261e4c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694481cbad2196511b261e4d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-16366185443636566609': 'file_storage/function-call-16366185443636566609.json'}

exec(code, env_args)
