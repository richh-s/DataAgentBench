code = """import json

# Load the file
file_path = locals()['var_function-call-9779383998375679082']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define keywords
keywords = {
    "Sports": ["sport", "baseball", "basketball", "football", "soccer", "tennis", "golf", "hockey", "olympic", "medal", "athlete", "championship", "tournament", "league", "team", "coach", "game", "match", "score", "win", "victory", "defeat", "cup", "nfl", "nba", "mlb", "nhl", "fifa", "racing", "f1", "nascar", "rugby", "cricket", "boxing", "wrestling", "swimming", "marathon", "stadium", "espn", "driver", "rider", "squad", "club", "athens"],
    "Business": ["market", "stock", "price", "company", "business", "economy", "trade", "profit", "bank", "dollar", "oil", "invest", "share", "finance", "corporate", "industry", "revenue", "sales", "ceo", "merger", "acquisition", "inflation", "rate", "fed", "reserve", "wall", "street", "dow", "nasdaq", "euro", "yen", "yuan"],
    "Sci/Tech": ["computer", "software", "technology", "internet", "web", "google", "microsoft", "apple", "linux", "virus", "security", "space", "nasa", "phone", "mobile", "digital", "online", "network", "science", "research", "lab", "processor", "chip", "intel", "amd", "server", "browser"],
    "World": ["president", "minister", "prime", "country", "war", "peace", "iraq", "israel", "palestine", "afghanistan", "iran", "un", "united nations", "government", "official", "election", "vote", "military", "army", "police", "blast", "attack", "kill", "die", "bomb", "explosion", "terror", "troops", "nuclear", "senate", "congress", "parliament", "democrat", "republican", "bush", "kerry", "candidate", "campaign", "poll", "voter", "party", "law", "court", "justice"]
}

sports_articles = []

for article in articles:
    text = (article.get('title', '') + " " + article.get('description', '')).lower()
    
    scores = {cat: 0 for cat in keywords}
    for cat, words in keywords.items():
        for word in words:
            if word in text:
                scores[cat] += 1
    
    # Determine category
    # If Sports has the highest score (strictly greater than others)
    # Check if Sports score is > 0
    if scores["Sports"] > 0:
        is_best = True
        for cat in scores:
            if cat != "Sports" and scores[cat] >= scores["Sports"]:
                is_best = False
                break
        if is_best:
            sports_articles.append(article)

# Sort by description length descending
sports_articles.sort(key=lambda x: len(x.get('description', '')), reverse=True)

top_3 = []
for art in sports_articles[:3]:
    top_3.append({
        "title": art['title'],
        "len": len(art['description']),
        "desc": art['description']
    })

print("__RESULT__:")
print(json.dumps(top_3))"""

env_args = {'var_function-call-6833759783790572362': [{'_id': '694476c261590ca75deef375', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-6833759783790573323': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-17617418666776808318': ['articles'], 'var_function-call-17617418666776809305': ['authors', 'article_metadata'], 'var_function-call-824548603619282537': [{'_id': '694476c261590ca75deef375', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694476c261590ca75deef376', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694476c261590ca75deef377', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694476c261590ca75deef378', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694476c261590ca75deef379', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-18427185302018865351': [{'_id': '694476c261590ca75deef375', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694476c261590ca75deef376', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694476c261590ca75deef377', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694476c261590ca75deef378', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694476c261590ca75deef379', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4260440268981957139': 'file_storage/function-call-4260440268981957139.json', 'var_function-call-9779383998375679082': 'file_storage/function-call-9779383998375679082.json', 'var_function-call-6585599168967989728': {'title': '2004 US Senate Outlook', 'description_length': 944, 'description_preview': 'With all the hoopla over Bush and Kerry, some of y'}}

exec(code, env_args)
