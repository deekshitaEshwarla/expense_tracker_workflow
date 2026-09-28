CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    category TEXT NOT NULL , 
    spent_on TEXT NOT NULL DEFAULT (date('now', 'localtime')), 
    amount_paise INTEGER NOT NULL CHECK(amount_paise > 0)
    ) STRICT;

 CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    cat_name TEXT UNIQUE NOT NULL CHECK(cat_name == (lower(trim(cat_name))) AND cat_name != '')

 )  STRICT ;