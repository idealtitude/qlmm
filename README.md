# QLMM

## Quick and Light Memos Manager

I'm often finding myself thinking "ho, I should write a memos for this command or that utility/tool/app"...
Actually, I have a folder containing many memo files, unclassified (only the title may help to describe the file content).

That's why I've decided to write an app (a command line tool, more precisely) to create/edit/delete/search and read memos.

I plan on using an sqlite database, with two tables (one for the memos categories, and the other for the memos (and maybe a third table for relations between tags (a field in the `memos` table) and memos)).

I'd like to include a very basic editor (a ncurse text field probably) for the description fields of each memo and each category.
