code = """import json
import re

# Load the articles
file_path = locals()['var_function-call-1780775130450535914']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Keywords
categories = {
    "Sports": ["sport", "sports", "football", "soccer", "basketball", "baseball", "hockey", "tennis", "golf", "olympics", "olympic", "championship", "tournament", "league", "cup", "medal", "game", "games", "team", "teams", "player", "players", "coach", "athlete", "athletes", "score", "scores", "match", "matches", "race", "racing", "f1", "formula one", "nascar", "cricket", "rugby", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "wimbledon", "super bowl", "world series", "stanley cup", "marathon", "sprint", "swim", "gymnast", "boxing", "wrestling", "doping", "stadium", "yankees", "red sox", "lakers", "bulls", "real madrid", "manchester united", "arsenal", "chelsea", "liverpool", "barcelona", "milan", "juventus"],
    "World": ["war", "wars", "president", "minister", "iraq", "iran", "bush", "kerry", "election", "elections", "bomb", "bombs", "peace", "treaty", "military", "troops", "government", "un", "united nations", "eu", "europe", "china", "russia", "palestinian", "israel", "gaza", "baghdad", "afghanistan", "terror", "terrorism", "qaeda", "hurricane", "storm", "earthquake", "tsunami", "flood", "disaster", "hostage", "kidnap", "kill", "killed", "dead", "died", "police", "court", "judge", "legal", "law", "parliament", "congress", "senate", "democrat", "republican"],
    "Business": ["market", "markets", "stock", "stocks", "economy", "economic", "company", "companies", "deal", "deals", "price", "prices", "oil", "profit", "profits", "loss", "losses", "bank", "banks", "financial", "finance", "dollar", "euro", "trade", "deficit", "sales", "corp", "inc", "shares", "fed", "inflation", "growth", "invest", "investment", "revenue", "quarter", "wall st", "nasdaq", "dow", "ceo", "cfo", "merger", "acquisition", "bankrupt", "bankruptcy", "audit", "accounting"],
    "Sci/Tech": ["technology", "tech", "science", "computer", "computers", "software", "space", "nasa", "internet", "web", "online", "microsoft", "google", "apple", "intel", "linux", "virus", "worm", "patch", "phone", "mobile", "wireless", "digital", "camera", "chip", "server", "research", "study", "scientist", "drug", "drugs", "cancer", "disease", "health", "hospital", "medical", "patient", "patients", "doctor", "doctors", "treatment", "bacteria", "gene", "genome", "cell", "stem cell", "cloning", "robot", "ai", "artificial intelligence", "windows", "unix", "linux", "browser", "software", "hardware"]
}

def classify(title, description):
    text = (title + " " + description).lower()
    scores = {cat: 0 for cat in categories}
    for cat, keywords in categories.items():
        for word in keywords:
            if re.search(r'\b' + re.escape(word) + r'\b', text):
                scores[cat] += 1
    
    # Heuristics
    if re.search(r'\b(video game|console|nintendo|sony|xbox|playstation|doom|quake)\b', text):
        scores['Sci/Tech'] += 5
    
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return None, scores
    return best_cat, scores

sports_articles = []
for art in articles:
    cat, scores = classify(art.get('title', ''), art.get('description', ''))
    if cat == "Sports":
        sports_articles.append(art)

print(f"Total articles: {len(articles)}")
print(f"Sports articles found: {len(sports_articles)}")

if sports_articles:
    longest_sports_article = max(sports_articles, key=lambda x: len(x.get('description', '')))
    result = {
        "title": longest_sports_article['title'],
        "description": longest_sports_article['description'],
        "description_length": len(longest_sports_article['description']),
        "article_id": longest_sports_article['article_id']
    }
else:
    result = "No sports articles found."

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4590900096331911974': ['authors', 'article_metadata'], 'var_function-call-4590900096331911789': ['articles'], 'var_function-call-3211474583898576585': [{'_id': '69447ed1642a2800c36b09bf', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447ed1642a2800c36b09c0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447ed1642a2800c36b09c1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447ed1642a2800c36b09c2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447ed1642a2800c36b09c3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-452875463290003417': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-11291349327323491478': [{'_id': '69447ed1642a2800c36b09bf', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447ed1642a2800c36b09c0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447ed1642a2800c36b09c1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447ed1642a2800c36b09c2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447ed1642a2800c36b09c3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1606999567026856973': [{'_id': '69447ed1642a2800c36b09bf', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447ed1642a2800c36b09c0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447ed1642a2800c36b09c1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447ed1642a2800c36b09c2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447ed1642a2800c36b09c3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1721172400299206163': 5, 'var_function-call-1780775130450535914': 'file_storage/function-call-1780775130450535914.json', 'var_function-call-2248824272465795316': {'title': "Why Windows isn't Unix", 'description_length': 708, 'article_id': '183'}}

exec(code, env_args)
