code = """import json

# Load metadata
with open(locals()['var_function-call-3090238535036356339'], 'r') as f:
    metadata_list = json.load(f)

# Load articles
with open(locals()['var_function-call-9655050446479882802'], 'r') as f:
    articles_list = json.load(f)

# Create lookup
articles_dict = {str(a['article_id']): a for a in articles_list}

# Merge
joined_data = []
for m in metadata_list:
    aid = str(m['article_id'])
    if aid in articles_dict:
        art = articles_dict[aid]
        joined_data.append({
            'region': m['region'],
            'title': art['title'],
            'description': art['description']
        })

# Keywords
keywords = {
    'World': ["govt", "government", "iraq", "syria", "iran", "israel", "palestin", "afghan", "pakistan", "china", "russia", "ukraine", "president", "minister", "prime minister", "official", "military", "army", "troop", "bomb", "kill", "dead", "death", "attack", "blast", "rebel", "force", "peace", "talk", "nuclear", "treaty", "united nations", "u.n.", "eu", "european union", "nato", "diplomat", "elect", "vote", "poll", "protest", "law", "court", "judge", "trial", "prison", "jail", "scandal", "security", "war", "crisis", "leader", "politic", "parliament", "congress", "senate", "democrat", "republican", "king", "queen", "prince", "terrorism", "terrorist", "strike", "police", "arrest", "charges", "ban", "rights", "human rights", "refugee", "migrant", "border", "crash", "disaster", "storm", "hurricane", "quake", "flood", "virus", "ebola", "flu", "outbreak", "vatican", "pope", "cuba", "north korea", "south korea", "venezuela", "brazil", "egypt", "libya", "nigeria", "korea"],
    'Sports': ["sport", "game", "match", "cup", "league", "team", "club", "coach", "manager", "player", "win", "won", "lose", "lost", "defeat", "score", "goal", "point", "medal", "olympic", "championship", "tournament", "final", "semi-final", "quarter-final", "round", "season", "baseball", "basketball", "football", "soccer", "tennis", "golf", "cricket", "rugby", "hockey", "racing", "driver", "athlete", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "nascar", "f1", "formula one", "grand prix", "wimbledon", "open", "series", "sox", "yankees", "mets", "bulls", "lakers", "knicks", "rangers", "giants", "eagles", "patriots", "red sox", "cubs", "cardinals"],
    'Business': ["business", "company", "corp", "inc", "ltd", "stock", "share", "market", "wall street", "dow", "nasdaq", "exchange", "trade", "economy", "economic", "bank", "financial", "finance", "money", "dollar", "euro", "yen", "currency", "profit", "loss", "earning", "revenue", "sale", "oil", "price", "cost", "deal", "merge", "acquire", "acquisition", "buyout", "ipo", "invest", "fed", "federal reserve", "ceo", "cfo", "chairman", "executive", "board", "shareholder", "investor", "fund", "equity", "bond", "rate", "inflation", "job", "unemployment", "hiring", "layoff", "cut", "retail", "store", "sale", "consumer", "spending", "growth", "recession", "gdp", "tax", "budget", "deficit", "debt", "loan", "mortgage", "housing", "real estate", "airlines", "auto", "gm", "ford", "toyota", "boeing", "airbus", "wal-mart", "mcdonald", "coke", "pepsi"],
    'Sci/Tech': ["science", "technology", "tech", "computer", "software", "hardware", "internet", "web", "online", "net", "cyber", "virus", "hacker", "microsoft", "google", "apple", "iphone", "ipod", "ipad", "mac", "intel", "ibm", "chip", "phone", "mobile", "wireless", "space", "nasa", "shuttle", "launch", "orbit", "planet", "moon", "star", "galaxy", "mars", "study", "research", "scientist", "researcher", "cancer", "drug", "health", "disease", "bacteria", "gene", "dna", "biology", "physics", "chemistry", "astronomy", "telescope", "robot", "artificial intelligence", "ai", "virtual", "digital", "data", "server", "cloud", "app", "browser", "search engine", "yahoo", "facebook", "twitter", "amazon", "ebay", "sony", "nintendo", "xbox", "playstation", "wii", "video game", "gamer", "gaming"]
}

# Adjust weights?
# "virus" is in World (Ebola etc) and Sci/Tech (computer virus).
# "oil" is in Business.
# "crash" is in World (plane crash) or Sci/Tech (software crash)? Usually World.
# "launch" -> Sci/Tech (rocket) or Business (product)?

def classify(title, description):
    text = (title + " " + description).lower()
    scores = {cat: 0 for cat in keywords}
    for cat, words in keywords.items():
        for w in words:
            if w in text:
                scores[cat] += 1
                
    # Tie breaking
    # If "oil" in text -> Business +2
    if "oil" in text: scores['Business'] += 2
    if "stock" in text: scores['Business'] += 2
    if "iraq" in text: scores['World'] += 2
    if "microsoft" in text: scores['Sci/Tech'] += 2
    if "game" in text and "video" not in text: scores['Sports'] += 1
    
    # Return category with max score
    m = max(scores.values())
    if m == 0: return "Unknown"
    
    # If multiple have max score?
    best = [k for k,v in scores.items() if v == m]
    # Priority: World > Sports > Business > Sci/Tech (arbitrary, but World is the target)
    if 'World' in best: return 'World'
    return best[0]

world_counts = {}

for item in joined_data:
    cat = classify(item['title'], item['description'])
    if cat == 'World':
        r = item['region']
        world_counts[r] = world_counts.get(r, 0) + 1

print("__RESULT__:")
print(json.dumps(world_counts))"""

env_args = {'var_function-call-3090238535036356339': 'file_storage/function-call-3090238535036356339.json', 'var_function-call-6809812975409689168': 'file_storage/function-call-6809812975409689168.json', 'var_function-call-18071088138891842561': [{'_id': '6944f33785bb2c4271f179ad', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944f33785bb2c4271f179ae', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944f33785bb2c4271f179af', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944f33785bb2c4271f179b0', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944f33785bb2c4271f179b1', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13503772162840934093': 6696, 'var_function-call-14230143626855137770': [{'_id': '6944f33785bb2c4271f179ad', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944f33785bb2c4271f179ae', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944f33785bb2c4271f179af', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944f33785bb2c4271f179b0', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944f33785bb2c4271f179b1', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8268891738577370634': {'counts': {}, 'uncategorized': 0, 'total_processed': 0}, 'var_function-call-9655050446479882802': 'file_storage/function-call-9655050446479882802.json'}

exec(code, env_args)
