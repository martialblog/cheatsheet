#Commandline Cheatsheets
Everybody likes cheatsheets. If you're like me and use lots of different tools but you can't remember all those cool shortcuts to impress your colleagues.

Sure, there are lots of PDFs out there with everything you need. But are you really gonna have an PDF reader next to your terminal to look up shortcuts? Come on, who are we kidding?

I'm trying to solve that problem by putting the cheatsheets where they belong. The terminal you're working in!

- Cheatsheets directly in your terminal
- Open-Format so you can customize/add/share
- Grep-able!

##Requirements
Nothing but good old Python. It's not rocketscience.

##Installation
To use, clone this repository to ```~/cheat.d```. Like so:

```git clone https://github.com/martialblog/cheatsheet.git ~/.cheat.d```

For usability you can set an alias:

```alias cheat="python3 ~/.cheat.d/cheat.py"```

For Python 2:

```alias cheat="python2 ~/.cheat.d/cheat.py2"```

And of you go!

```user@computer$ cheat git```

###Custom cheatsheets
You can add custom cheatsheet that will be "gitgnored" by using the prexif ```my-```

##TODO
- Sort output maybe? I just grep stuff.
- Add more cheatsheets! MORE!
- Tell my mom about it.
