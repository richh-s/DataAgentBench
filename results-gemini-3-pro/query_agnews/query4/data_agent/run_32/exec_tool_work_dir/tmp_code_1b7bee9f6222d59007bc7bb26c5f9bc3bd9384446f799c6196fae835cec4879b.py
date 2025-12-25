code = """import json
from collections import Counter

# Load metadata
with open(locals()['var_function-call-5900547977647289407'], 'r') as f:
    metadata_list = json.load(f)

# Load articles content
with open(locals()['var_function-call-12526826201360126982'], 'r') as f:
    content_list = json.load(f)

# Create map: article_id (str) -> region
# Filter metadata to valid articles only if needed, but here we iterate content?
# No, we iterate metadata (2015 articles) and look up content.
# Better to build a content map: article_id (str) -> text
content_map = {}
for item in content_list:
    content_map[str(item['article_id'])] = (item.get('title', '') + " " + item.get('description', '')).lower()

# Keywords
keywords = {
    "World": [
        "afghanistan", "africa", "arab", "attack", "baghdad", "blast", "bomb", "border", "britain", 
        "china", "court", "crisis", "diplomat", "earthquake", "egypt", "election", "europe", 
        "explosion", "force", "foreign", "france", "gaza", "germany", "government", "hostage", 
        "india", "international", "iran", "iraq", "israel", "japan", "killed", "korea", "law", 
        "leader", "libya", "military", "minister", "missile", "moscow", "nation", "nato", 
        "nuclear", "official", "pakistan", "palestine", "parliament", "peace", "police", "politics", 
        "president", "prime minister", "protest", "province", "putin", "rebel", "refugee", "region", 
        "russia", "security", "soldier", "state", "strike", "suicide", "syria", "taliban", "terror", 
        "troop", "turkey", "ukraine", "un", "united nations", "war", "weapon", "world", "yemen",
        "greek", "greece", "eurozone", "eu", "putin", "migrant"
    ],
    "Sports": [
        "baseball", "basketball", "champion", "coach", "cup", "defeat", "football", "game", "gold", 
        "golf", "hockey", "league", "medal", "mlb", "nascar", "nba", "nfl", "nhl", "olympic", 
        "player", "race", "score", "season", "soccer", "sport", "stadium", "team", "tennis", 
        "tournament", "victory", "win", "world cup"
    ],
    "Business": [
        "bank", "bond", "business", "buy", "ceo", "company", "corp", "deal", "dollar", "dow", 
        "earnings", "economy", "euro", "federal", "finance", "firm", "fund", "growth", "inc", 
        "industry", "invest", "job", "loss", "market", "merger", "money", "nasdaq", "oil", 
        "price", "profit", "quarter", "rate", "report", "revenue", "sale", "share", "stock", 
        "trade", "wall street", "initial public offering", "ipo"
    ],
    "Sci/Tech": [
        "android", "apple", "app", "astronomy", "biology", "browser", "cancer", "cell", "computer", 
        "device", "disease", "drug", "facebook", "galaxy", "gene", "google", "health", "internet", 
        "mars", "microsoft", "mission", "mobile", "moon", "nasa", "network", "online", "phone", 
        "planet", "research", "robot", "satellite", "science", "scientist", "server", "software", 
        "space", "study", "tech", "technology", "virus", "web", "windows", "wireless"
    ]
}

region_counts = Counter()
debug_samples = []
missing_content_count = 0

for meta in metadata_list:
    aid = str(meta['article_id'])
    if aid in content_map:
        text = content_map[aid]
        scores = {cat: 0 for cat in keywords}
        
        # Simple keyword counting
        for cat, words in keywords.items():
            for word in words:
                # Check for word boundaries roughly?
                # or just ' in '
                if word in text:
                    scores[cat] += 1
        
        # Determine category
        if max(scores.values()) > 0:
            best_cat = max(scores, key=scores.get)
            
            # Tie breaking? 
            # If World and Business tie (e.g. "China market"), what to do?
            # If World and Sports tie (e.g. "World Cup"), it's Sports.
            # "World" keyword is in World list. "World Cup" is in Sports list.
            # "World Cup" matches "world" (World) and "cup" (Sports) and "world cup" (Sports).
            # So Sports gets 2 points, World gets 1. Correct.
            
            if best_cat == 'World':
                region_counts[meta['region']] += 1
                if len(debug_samples) < 5:
                    debug_samples.append({"id": aid, "text": text[:100], "scores": scores, "region": meta['region']})
    else:
        missing_content_count += 1

print("__RESULT__:")
print(json.dumps({
    "region_counts": dict(region_counts), 
    "missing_content": missing_content_count,
    "debug_samples": debug_samples
}))"""

env_args = {'var_function-call-5900547977647289407': 'file_storage/function-call-5900547977647289407.json', 'var_function-call-8253439238580865499': {'count': 6696, 'sample_ids': [13, 18, 26, 51, 52]}, 'var_function-call-11413350339637926914': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6748392322076207893': {'counts': {}, 'debug': []}, 'var_function-call-11835655730956261158': {'common': 0}, 'var_function-call-12334258275261728907': {'common_int': 0}, 'var_function-call-762477354594242145': {'meta_count': 6696, 'content_count': 5, 'meta_min': 13, 'meta_max': 127570, 'content_min': 0, 'content_max': 4, 'meta_sample': [13, 18, 26, 51, 52], 'content_sample': [0, 1, 2, 3, 4], 'content_sample_raw': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}]}, 'var_function-call-17256143422197129974': [{'_id': '694510d0f346764387e32f39', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}], 'var_function-call-15580149888157125641': [{'_id': '694510d0f346764387e32f39', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '694510d0f346764387e32f3a', 'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'_id': '694510d0f346764387e32f3b', 'article_id': '15', 'title': 'Rescuing an Old Saver', 'description': "If you think you may need to help your elderly relatives with their finances, don't be shy about having the money talk -- soon."}, {'_id': '694510d0f346764387e32f3c', 'article_id': '16', 'title': 'Kids Rule for Back-to-School', 'description': 'The purchasing power of kids is a big part of why the back-to-school season has become such a huge marketing phenomenon.'}, {'_id': '694510d0f346764387e32f3d', 'article_id': '17', 'title': 'In a Down Market, Head Toward Value Funds', 'description': "There is little cause for celebration in the stock market these days, but investors in value-focused mutual funds have reason to feel a bit smug -- if only because they've lost less than the folks who stuck with growth."}], 'var_function-call-12526826201360126982': 'file_storage/function-call-12526826201360126982.json'}

exec(code, env_args)
