code = """import json
import collections

# Load the file
file_path = locals()['var_function-call-9779383998375679082']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define keywords
keywords = {
    "Sports": ["sport", "sports", "baseball", "basketball", "football", "soccer", "tennis", "golf", "hockey", "olympic", "olympics", "medal", "athlete", "championship", "tournament", "league", "team", "coach", "game", "match", "score", "win", "won", "loss", "lost", "victory", "defeat", "cup", "nfl", "nba", "mlb", "nhl", "fifa", "racing", "f1", "nascar", "rugby", "cricket", "boxing", "wrestling", "swimming", "track", "marathon", "stadium", "espn", "driver", "rider", "squad", "club"],
    "Business": ["market", "stock", "price", "company", "business", "economy", "trade", "profit", "bank", "dollar", "oil", "invest", "share", "finance", "corporate", "industry", "revenue", "sales", "ceo", "merger", "acquisition", "inflation", "rate", "fed", "reserve", "wall", "street", "dow", "nasdaq", "euro", "yen", "yuan"],
    "Sci/Tech": ["computer", "software", "technology", "internet", "web", "google", "microsoft", "apple", "linux", "virus", "security", "space", "nasa", "phone", "mobile", "digital", "online", "network", "science", "research", "lab", "processor", "chip", "intel", "amd", "server", "browser"],
    "World": ["president", "minister", "prime", "country", "war", "peace", "iraq", "israel", "palestine", "afghanistan", "iran", "un", "united", "nations", "government", "official", "election", "vote", "military", "army", "police", "blast", "attack", "kill", "die", "bomb", "explosion", "terror", "troops", "nuclear"]
}

sports_articles = []

for article in articles:
    text = (article.get('title', '') + " " + article.get('description', '')).lower()
    
    scores = {cat: 0 for cat in keywords}
    for cat, words in keywords.items():
        for word in words:
            # Simple substring match or word boundary match?
            # Substring might match "companies" for "pan".
            # Let's try to match whole words or check if word is in text tokens.
            # But simple check:
            if word in text:
                scores[cat] += 1
    
    # Determine category
    best_cat = None
    max_score = -1
    for cat, score in scores.items():
        if score > max_score:
            max_score = score
            best_cat = cat
        elif score == max_score:
            best_cat = "Tie" # Ambiguous
            
    if best_cat == "Sports" and max_score > 0:
        sports_articles.append(article)

# Find the one with max description length
longest_desc_article = None
max_len = -1

for article in sports_articles:
    desc_len = len(article.get('description', ''))
    if desc_len > max_len:
        max_len = desc_len
        longest_desc_article = article

result = {}
if longest_desc_article:
    result = {
        "title": longest_desc_article['title'],
        "description_length": max_len,
        "description_preview": longest_desc_article['description'][:50]
    }
else:
    result = {"error": "No sports articles found"}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-6833759783790572362': [{'_id': '694476c261590ca75deef375', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-6833759783790573323': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-17617418666776808318': ['articles'], 'var_function-call-17617418666776809305': ['authors', 'article_metadata'], 'var_function-call-824548603619282537': [{'_id': '694476c261590ca75deef375', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694476c261590ca75deef376', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694476c261590ca75deef377', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694476c261590ca75deef378', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694476c261590ca75deef379', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-18427185302018865351': [{'_id': '694476c261590ca75deef375', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694476c261590ca75deef376', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694476c261590ca75deef377', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694476c261590ca75deef378', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694476c261590ca75deef379', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4260440268981957139': 'file_storage/function-call-4260440268981957139.json', 'var_function-call-9779383998375679082': 'file_storage/function-call-9779383998375679082.json'}

exec(code, env_args)
