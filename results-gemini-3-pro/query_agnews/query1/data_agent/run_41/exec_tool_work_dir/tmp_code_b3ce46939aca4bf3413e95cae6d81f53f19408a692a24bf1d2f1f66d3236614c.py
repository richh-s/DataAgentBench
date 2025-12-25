code = """import json

# Load the file
file_path = locals()['var_function-call-16498150637540614880']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define sports keywords
sports_keywords = [
    "olympic", "athens", "medal", "gold", "silver", "bronze", 
    "basketball", "nba", "baseball", "mlb", "football", "nfl", 
    "soccer", "premier league", "tennis", "wimbledon", "us open", 
    "golf", "pga", "hockey", "nhl", "cricket", "rugby", "f1", "nascar",
    "championship", "tournament", "world cup", "athlete", "stadium",
    "yankees", "red sox", "lakers", "spurs", "pistons", "armstrong", "phelps", "thorpe"
]

candidates = []

for art in articles:
    title = art.get('title', '')
    desc = art.get('description', '')
    text = (title + " " + desc).lower()
    
    # Check if any keyword is in text
    is_sport = False
    for kw in sports_keywords:
        # Simple containment check; for better accuracy, could use word boundaries
        if kw in text:
            # Filter out some false positives if necessary
            # e.g. "gold" might be in business (gold prices)
            if kw == "gold" or kw == "silver" or kw == "bronze":
                if "price" in text or "market" in text:
                    continue
            if kw == "medal" and "honor" in text: # Medal of honor?
                pass
                
            is_sport = True
            break
            
    if is_sport:
        candidates.append({
            "title": title,
            "desc_len": len(desc),
            "description": desc
        })

# Sort by description length descending
candidates.sort(key=lambda x: x['desc_len'], reverse=True)

# Print top 5 candidates to verify
print("__RESULT__:")
print(json.dumps(candidates[:5]))"""

env_args = {'var_function-call-4311503606640885860': ['articles'], 'var_function-call-14832231781823878473': [{'_id': '694483ba1f759e2c2778f8e2', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-15881672882449061525': ['authors', 'article_metadata'], 'var_function-call-9407118945008870673': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-1536730069265665031': [{'_id': '694483ba1f759e2c2778f8e2', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694483ba1f759e2c2778f8e3', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694483ba1f759e2c2778f8e4', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694483ba1f759e2c2778f8e5', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694483ba1f759e2c2778f8e6', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6936758391387168330': [{'_id': '694483ba1f759e2c2778f8e2', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694483ba1f759e2c2778f8e3', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694483ba1f759e2c2778f8e4', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694483ba1f759e2c2778f8e5', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694483ba1f759e2c2778f8e6', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-5455468116689382879': 5, 'var_function-call-16498150637540614880': 'file_storage/function-call-16498150637540614880.json'}

exec(code, env_args)
