code = """import json
import re

# Load the articles
with open(locals()['var_function-call-9674498384229145557'], 'r') as f:
    articles = json.load(f)

# Define keywords
categories = {
    "Sports": ["sport", "football", "baseball", "basketball", "soccer", "tennis", "golf", "olympics", "olympic", "medal", "gold", "silver", "bronze", "athens", "game", "match", "team", "league", "cup", "championship", "tournament", "coach", "athlete", "player", "score", "win", "loss", "victory", "defeat", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "racing", "f1", "nascar", "hockey", "cricket", "rugby", "boxing", "wrestling", "red sox", "yankees", "doping", "marathon", "sprint", "swimming", "gymnastics"],
    "Business": ["market", "stock", "price", "company", "corp", "inc", "ltd", "business", "economy", "trade", "profit", "loss", "dollar", "bank", "oil", "wto", "imf", "fed", "inflation", "ipo", "google", "shares", "investor", "fund", "revenue", "sales", "deal", "merger", "acquisition", "wall st", "nasdaq", "dow", "ceo", "cfo"],
    "Sci/Tech": ["technology", "science", "computer", "software", "internet", "web", "microsoft", "google", "intel", "ibm", "space", "nasa", "phone", "mobile", "chip", "virus", "hacker", "online", "network", "wireless", "broadband", "satellite", "robot", "gadget"],
    "World": ["world", "iraq", "president", "minister", "government", "war", "peace", "election", "un", "united nations", "eu", "europe", "asia", "africa", "country", "nuclear", "terror", "bomb", "military", "army", "police", "attack", "israel", "palestinian", "gaza", "baghdad", "iran", "korea", "china", "russia"]
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in categories}
    for cat, keywords in categories.items():
        for kw in keywords:
            # Simple word matching, checking word boundaries to avoid substrings like 'win' in 'winter'
            if re.search(r'\b' + re.escape(kw) + r'\b', text):
                scores[cat] += 1
    
    # Sort by score desc
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    best_cat, best_score = sorted_scores[0]
    
    # Check if best_score is 0 (unclassified)
    if best_score == 0:
        return "Unknown"
    return best_cat

sports_articles = []

for art in articles:
    text = (art.get('title', '') + " " + art.get('description', ''))
    cat = classify(text)
    if cat == "Sports":
        sports_articles.append(art)

# Find the one with the longest description
if not sports_articles:
    result = "No sports articles found."
else:
    longest_desc_article = max(sports_articles, key=lambda x: len(x.get('description', '')))
    result = {
        "title": longest_desc_article['title'],
        "description_length": len(longest_desc_article['description']),
        "description": longest_desc_article['description']
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17250944776855184585': ['articles'], 'var_function-call-17250944776855184316': ['authors', 'article_metadata'], 'var_function-call-13601084253976166638': [{'_id': '69446509b7cb91ea91dd468b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-13601084253976169751': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-2953041677624993579': [{'author_id': '0', 'name': 'Felicia Miles'}], 'var_function-call-175646378764434338': [{'_id': '69446509b7cb91ea91dd468b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446509b7cb91ea91dd468c', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446509b7cb91ea91dd468d', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446509b7cb91ea91dd468e', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446509b7cb91ea91dd468f', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-2720222771617662260': [{'_id': '69446509b7cb91ea91dd468b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446509b7cb91ea91dd468c', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446509b7cb91ea91dd468d', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446509b7cb91ea91dd468e', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446509b7cb91ea91dd468f', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-9674498384229145557': 'file_storage/function-call-9674498384229145557.json'}

exec(code, env_args)
