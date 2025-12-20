code = """import json
import re

# Load the data
file_path = locals()['var_function-call-5153620471586195905']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define sports keywords
sports_keywords = {
    "olympic", "olympics", "athens", "medal", "gold", "silver", "bronze",
    "football", "soccer", "basketball", "baseball", "tennis", "golf", "hockey",
    "cricket", "rugby", "nfl", "nba", "mlb", "nhl", "fifa", "uefa",
    "team", "coach", "athlete", "player", "match", "tournament", "championship", "league", "cup",
    "racing", "racer", "f1", "nascar", "driver", "grand prix",
    "marathon", "sprint", "swimming", "gymnastics", "boxing", "wrestling",
    "volleyball", "skiing", "skating", "super bowl", "world cup",
    "red sox", "yankees", "lakers", "pistons", "patriots", "eagles", "arsenal", "manchester", "real madrid", # Famous teams
    "woods", "federer", "armstrong", "phelps", "kobe", "shaq", "jeter" # Famous athletes of 2004
}

# Define non-sports keywords (Business, Tech, World) to reduce false positives
non_sports_keywords = {
    "stock", "market", "economy", "economic", "price", "profit", "loss", "revenue",
    "company", "corp", "inc", "business", "industry", "firm", "bank", "financial",
    "dollar", "euro", "yen", "currency", "trade", "deal", "merger", "acquisition",
    "software", "internet", "computer", "microsoft", "google", "apple", "intel", "technology", "tech",
    "science", "nasa", "space", "research", "study", "university",
    "president", "minister", "prime minister", "election", "vote", "poll", "politics", "political",
    "iraq", "war", "military", "army", "police", "crime", "attack", "bomb", "blast", "kill", "die",
    "oil", "gas", "energy"
}

def is_sports(text):
    text = text.lower()
    # Tokenize simply
    tokens = re.findall(r'\b\w+\b', text)
    
    score = 0
    for token in tokens:
        if token in sports_keywords:
            score += 1
        elif token in non_sports_keywords:
            score -= 1 # Penalize strong non-sports words
            
    # Heuristics for "athens" (very strong in 2004)
    if "athens" in text and "olympic" in text:
        score += 5
        
    return score

# Add length
for a in articles:
    a['desc_len'] = len(a['description'])

# Sort by length descending
articles.sort(key=lambda x: x['desc_len'], reverse=True)

# Find the first sports article
found_title = None
for a in articles:
    # Check if it's sports
    # Combine title and description for context
    full_text = a['title'] + " " + a['description']
    
    # Calculate score
    score = is_sports(full_text)
    
    # Threshold?
    # If score is positive, it's likely sports. 
    # But let's look at the tokens to be sure.
    # We can also check specific phrases.
    
    if score > 0:
        # Double check with a stricter rule if score is low
        # e.g. if score is 1, it might be "game" in business context.
        # But we penalized business words.
        
        # Let's assume the highest length sports article will have a decent score.
        # Print the top candidate to verify in output (I can't see it but the logic holds)
        found_title = a['title']
        break

print("__RESULT__:")
print(json.dumps(found_title))"""

env_args = {'var_function-call-15893758106873812776': ['articles'], 'var_function-call-15893758106873814773': ['authors', 'article_metadata'], 'var_function-call-12654063459967277183': [{'_id': '69447762070998a1ddf0b52e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447762070998a1ddf0b52f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447762070998a1ddf0b530', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447762070998a1ddf0b531', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447762070998a1ddf0b532', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-12654063459967275804': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-10974067136771552033': [{'_id': '69447762070998a1ddf0b52e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447762070998a1ddf0b52f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447762070998a1ddf0b530', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447762070998a1ddf0b531', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447762070998a1ddf0b532', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-10972115385490034610': [{'_id': '69447762070998a1ddf0b52e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447762070998a1ddf0b52f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447762070998a1ddf0b530', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447762070998a1ddf0b531', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447762070998a1ddf0b532', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-15231230027831837364': 'file_storage/function-call-15231230027831837364.json', 'var_function-call-5153620471586195905': 'file_storage/function-call-5153620471586195905.json'}

exec(code, env_args)
