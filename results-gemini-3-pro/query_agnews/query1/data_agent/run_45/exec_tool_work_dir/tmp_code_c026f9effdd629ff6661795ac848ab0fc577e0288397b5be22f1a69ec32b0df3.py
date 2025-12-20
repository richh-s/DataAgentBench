code = """import json
import string
import re

# Load the articles from the file
file_path = locals()['var_function-call-18177868496750435891']
with open(file_path, 'r') as f:
    data = json.load(f)

# Define keywords
keywords = {
    "Business": {
        "business", "economy", "market", "stock", "trade", "profit", "loss", "dollar", "euro", "yen", "bank", 
        "company", "corp", "inc", "shares", "invest", "price", "oil", "gas", "energy", "sales", "revenue", 
        "deal", "merger", "acquisition", "ceo", "cfo", "wall st", "nasdaq", "dow", "index", "finance", "money",
        "inflation", "recession", "fed", "federal", "imf", "wto", "deficit", "surplus", "bond", "yield", "rates",
        "layoff", "jobs", "employment", "hiring", "manager", "executive", "firm", "industry", "sector", "retail",
        "consumer", "spending", "growth", "forecast", "quarter", "earnings", "dividend", "bankrupt", "debt", "loan",
        "credit", "tax", "budget", "cost", "cut", "audit", "account", "marketing", "advertising", "brand", "product",
        "service", "customer", "client", "workforce", "strike", "union", "negotiation", "agreement", "contract",
        "supply", "demand", "export", "import", "logistics", "shipping", "transport", "airline", "manufacturer"
    },
    "Sci/Tech": {
        "technology", "science", "computer", "internet", "software", "hardware", "web", "online", "digital", 
        "phone", "mobile", "wireless", "space", "nasa", "orbit", "robot", "virus", "worm", "microsoft", "google", 
        "apple", "intel", "linux", "windows", "browser", "server", "chip", "research", "study", "scientist", 
        "discovery", "astronomy", "biology", "physics", "tech", "gadget", "cyber", "hacker", "network", "data",
        "spam", "email", "search", "engine", "site", "website", "link", "blog", "user", "download", "upload",
        "file", "program", "code", "developer", "system", "application", "device", "screen", "monitor", "keyboard",
        "mouse", "laptop", "notebook", "pc", "mac", "ipod", "mp3", "dvd", "cd", "camera", "video", "audio",
        "satellite", "galaxy", "planet", "mars", "moon", "sun", "star", "telescope", "lab", "experiment", "drug",
        "medicine", "medical", "health", "disease", "cancer", "aids", "hiv", "gene", "dna", "cell", "stem", "clone",
        "it", "information" # Added IT
    },
    "World": {
        "world", "international", "politics", "government", "president", "prime", "minister", "official", 
        "election", "vote", "war", "peace", "treaty", "military", "army", "navy", "police", "attack", "bomb", 
        "blast", "terror", "killed", "injured", "dead", "iraq", "iran", "china", "russia", "us", "uk", "un", 
        "united", "nations", "eu", "european", "union", "protest", "court", "law", "judge", "security", "diplomat", "crisis",
        "israel", "palestine", "gaza", "afghanistan", "syria", "korea", "nuclear", "weapon", "parliament", "congress",
        "baghdad", "troops", "strike", "insurgent", "rebel", "militia", "kidnap", "hostage", "arrest", "jail", "prison",
        "rights", "human", "aid", "relief", "disaster", "storm", "hurricane", "flood", "earthquake", "tsunami",
        "fire", "accident", "crash", "plane", "train", "bus", "car", "suicide", "murder", "crime", "criminal"
    },
    "Sports": {
        "sport", "olympic", "olympics", "game", "match", "team", "player", "coach", "win", "lose", "draw", "score", "goal", 
        "touchdown", "homerun", "basket", "medal", "championship", "tournament", "league", "cup", "final", 
        "semi-final", "quarter-final", "playoff", "nba", "nfl", "mlb", "nhl", "fifa", "football", "baseball", 
        "basketball", "soccer", "tennis", "golf", "hockey", "racing", "driver", "f1", "nascar", "athens", 
        "games", "gold", "silver", "bronze", "record", "champion", "athlete", "squad", "club", "manager", "run",
        "stadium", "field", "court", "pitch", "wicket", "inning", "bat", "ball", "striker", "defender", "goalkeeper",
        "quarterback", "receiver", "umpire", "referee", "boxing", "wrestling", "cycling", "tour", "wimbledon",
        "open", "grand", "slam", "masters", "pga", "lpga", "formula", "super", "bowl", "world", "series", "stanley",
        "medals", "race", "winner", "loser", "season", "qualify", "qualifier", "standings", "rank", "ranking",
        "title", "bout", "lap", "pole", "position", "grid"
    }
}

sports_articles = []
punctuation_table = str.maketrans('', '', string.punctuation)

for article in data:
    title = article.get("title", "") or ""
    desc = article.get("description", "") or ""
    text = (title + " " + desc).lower()
    
    # Simple split and strip
    words = text.split()
    tokens = set(w.translate(punctuation_table) for w in words if w)
    
    scores = {cat: 0 for cat in keywords}
    for cat, kws in keywords.items():
        scores[cat] = len(tokens.intersection(kws))
    
    # Adjustments
    if "olympic" in tokens or "olympics" in tokens:
        scores["Sports"] += 5
    if "iraq" in tokens:
        scores["World"] += 5
    if "stocks" in tokens or "market" in tokens:
        scores["Business"] += 2
        
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] > 0:
        if best_cat == "Sports":
            sports_articles.append(article)

# Sort by description length descending
sports_articles.sort(key=lambda x: len(x.get("description", "") or ""), reverse=True)

# Get top 10
top_candidates = []
for sa in sports_articles[:10]:
    top_candidates.append({
        "title": sa["title"],
        "desc_len": len(sa.get("description", "") or ""),
        "desc_preview": (sa.get("description", "") or "")[:100]
    })

print("__RESULT__:")
print(json.dumps(top_candidates))"""

env_args = {'var_function-call-17820231337409902993': [{'_id': '694486b6b33217ab0ded7866', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694486b6b33217ab0ded7867', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694486b6b33217ab0ded7868', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694486b6b33217ab0ded7869', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694486b6b33217ab0ded786a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11407415087239536050': [{'_id': '694486b6b33217ab0ded7866', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694486b6b33217ab0ded7867', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694486b6b33217ab0ded7868', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694486b6b33217ab0ded7869', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694486b6b33217ab0ded786a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-357563551933968648': {'total_articles': 5, 'sports_articles_count': 0, 'best_article_title': None, 'max_length': -1}, 'var_function-call-4127149747257172605': [{'cnt': '127600'}], 'var_function-call-18177868496750435891': 'file_storage/function-call-18177868496750435891.json', 'var_function-call-16215107973573645152': {'total_sports': 0, 'best_title': None, 'max_len': -1}, 'var_function-call-17906700582839264187': [{'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'tokens_sample': [], 'scores': {'Sports': 0}}, {'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'tokens_sample': [], 'scores': {'Sports': 0}}, {'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'tokens_sample': [], 'scores': {'Sports': 0}}, {'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'tokens_sample': [], 'scores': {'Sports': 0}}, {'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'tokens_sample': [], 'scores': {'Sports': 0}}, {'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'tokens_sample': [], 'scores': {'Sports': 0}}, {'title': 'Money Funds Fell in Latest Week (AP)', 'tokens_sample': [], 'scores': {'Sports': 0}}, {'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'tokens_sample': [], 'scores': {'Sports': 0}}, {'title': 'Safety Net (Forbes.com)', 'tokens_sample': [], 'scores': {'Sports': 0}}, {'title': 'Wall St. Bears Claw Back Into the Black', 'tokens_sample': [], 'scores': {'Sports': 0}}], 'var_function-call-12975595024783832541': {'article_keys': ['_id', 'title', 'description'], 'title_val': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'desc_val': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again.", 'text_preview': "wall st. bears claw back into the black (reuters) reuters - short-sellers, wall street's dwindling\\b", 'tokens_re_count': 0, 'tokens_split_sample': ['wall', 'st.', 'bears', 'claw', 'back']}, 'var_function-call-5760136518899201542': {'total_sports': 27027, 'best_title': 'Life in the IT fun house', 'max_len': 970}, 'var_function-call-3312601849063404755': {'_id': '694486b8b33217ab0def30fb', 'title': 'Life in the IT fun house', 'description': 'For IT professionals, working in IT during the past few years has been a frightening whiplash tour through a carnival fun house. In the foyer of this (not so fun) fun house -- known as the 2001 Room -- the gag is simple: A rug is pulled out from under those fortunate enough to be standing, while others tumble down a dark chute, passing flashing neon signs that read layoffs and consolidation. In the background, the cacophony of late-night conference calls to Bangalore blares over loudspeakers.&lt;p&gt;ADVERTISEMENT&lt;/p&gt;&lt;p&gt;&lt;img src="http://ad.doubleclick.net/ad/idg.us.ifw.general/sbcspotrssfeed;sz=1x1;ord=200301151450?" width="1" height="1" border="0"/&gt;&lt;a href="http://ad.doubleclick.net/clk;11714255;9651165;g?http://infoworld.com/spotlights/sbc/main.html?lpid0101035400730403idlp"&gt;SBC Datacomm White Paper&lt;/a&gt;&lt;br/&gt;Find out how Crate   Barrel expects to save \\$180,000 by moving to VoIP, compared to a traditional PBX.&lt;/p&gt;'}}

exec(code, env_args)
