[![Build Status](https://travis-ci.org/martialblog/cheatsheet.svg?branch=master)](https://travis-ci.org/martialblog/cheatsheet) [![Coverage Status](https://coveralls.io/repos/github/martialblog/cheatsheet/badge.svg?branch=master)](https://coveralls.io/github/martialblog/cheatsheet?branch=master)

# Commandline Cheatsheets

Everybody likes cheatsheets. If you're like me and use lots of different tools but you can't remember all those cool shortcuts to impress your colleagues.

Sure, there are lots of PDFs out there with everything you need. But are you really gonna have an PDF reader next to your terminal to look up shortcuts? Come on, who are we kidding?

I'm trying to solve that problem by putting the cheatsheets where they belong. The terminal you're working in!

- Cheatsheets directly in your terminal
- Open-Format so you can customize/add/share
- Grep-able!

## Requirements

Nothing but good old Python (3.x), it's not rocketscience.

I also provided a Python 2.x version. However, main branch is 3.x.

## Setup
Clone this repository to ```~/cheat.d```. Like so:

```bash
git clone https://github.com/martialblog/cheatsheet.git ~/.cheat.d
```

For usability you can set an alias:

```bash
alias cheat="python3 ~/.cheat.d/cheat/cheat.py"
```

For Python 2:

```bash
alias cheat="python2 ~/.cheat.d/cheat/cheat.py2"
```

And away we go!

```bash
user@computer$ cheat git
```

![Cheat Screenshot](cheat-screenshot.png?raw=true "Cheat Screenshot")

To list all available cheatsheets:

```bash
user@computer$ cheat --list
```

### Custom cheatsheets

You can add custom cheatsheet that will be "gitgnored" by using the prexif **my-**



