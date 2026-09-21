# -*- coding: utf-8 -*-
"""Page registry: slug, metadata, target searches, body, internal links."""

import art_mystery as M
import art_christmas as C
import art_mahjong as J
import art_home as H

PAGES = [
    dict(slug="index.html", hub=True, og_type="website",
         h1="Notes from building printable party games",
         meta_title="A Maison Soirée Guides — party games, printed",
         desc="Free guides to hosting murder mystery parties, mahjong nights and adult advent "
              "calendars, written by the studio that draws the games. Plus a free four-player mystery.",
         targets=["a maison soiree", "printable party game guides"],
         body=H.HOME),

    dict(slug="guides.html", hub=True,
         h1="All guides",
         meta_title="All guides — murder mystery, advent and mahjong",
         desc="Ten long guides to hosting murder mystery parties, choosing guest numbers, printing "
              "the pack, running a mahjong night and reading a mahjong card.",
         targets=["party game guides"],
         body=H.GUIDES),

    dict(slug="free-murder-mystery-game.html", hub=True,
         h1="A free four-player murder mystery you can print tonight",
         meta_title="Free printable murder mystery game for 4 players (PDF)",
         desc="The Wet Half-Hour: a complete free four-player murder mystery. 11 printed documents, "
              "45 minutes, sealed answer in a separate file. No email needed. US Letter and A4 PDF.",
         targets=["free printable murder mystery game", "murder mystery for 4 players free",
                  "free murder mystery game pdf", "small murder mystery game 4 people"],
         about=["Murder mystery game", "Party game", "Printable"],
         faq=[("Is this free murder mystery game really complete?",
               "Yes. The Wet Half-Hour is a full four-player game: four suspect cards, eleven "
               "printed case documents, a guest sheet, a host sheet, accusation slips and a "
               "separate sealed answer file with the reveal and the fair-play audit."),
              ("Do I have to give an email address to download it?",
               "No. The PDFs are direct links on the page. There is no sign-up, no email capture "
               "and no account."),
              ("Can the person who prints it still play?",
               "Yes. The answer lives in a separate file behind a full-page STOP card, and nothing "
               "in the game file states who did it — the solution has to be assembled from the "
               "documents."),
              ("How long does it take?",
               "About 45 minutes of play plus roughly ten minutes to print and cut. It runs as "
               "three timed rounds of 12, 15 and 10 minutes, then a secret ballot."),
              ("Can we play it with three or five people?",
               "Yes. At three, leave out Dr Quill's card and read it aloud as a written statement; "
               "everything on it also appears on a document. At five, the extra person keeps time "
               "and reads out the ending.")],
         body=H.FREE,
         related=["how-to-host-a-murder-mystery-dinner-party.html",
                  "how-many-guests-murder-mystery-party.html",
                  "what-to-print-murder-mystery-party.html"]),

    dict(slug="how-to-host-a-murder-mystery-dinner-party.html",
         h1="How to host a murder mystery dinner party at home",
         meta_title="How to host a murder mystery dinner party at home",
         desc="A timetable, a print plan and the five decisions that make the evening work — "
              "including how to host a murder mystery party and still play it yourself.",
         targets=["how to host a murder mystery dinner party",
                  "how to host a murder mystery party at home",
                  "murder mystery dinner party tips", "murder mystery party host can play"],
         about=["Murder mystery game", "Dinner party", "Party planning"],
         faq=[("Can the host play in a murder mystery party?",
               "Only if the game is built for it: the host's reading must be one page, the clue "
               "envelopes must open on clock times rather than on the host's judgement, nothing "
               "must need adjudicating, and the reveal must be sealed and read out by a guest."),
              ("How long does a murder mystery dinner party take?",
               "Plan 90 to 120 minutes of game for 6 to 12 people, in three clue rounds with "
               "eating gaps between them. Set the envelope times as phone alarms before guests "
               "arrive."),
              ("What food works for a murder mystery dinner?",
               "A cold starter that is already plated, a main that reheats, and a pudding that "
               "lives in the fridge. The host should not disappear for twenty minutes mid-round.")],
         body=M.HOST,
         related=["how-many-guests-murder-mystery-party.html",
                  "what-goes-wrong-murder-mystery-party.html",
                  "what-to-print-murder-mystery-party.html",
                  "free-murder-mystery-game.html"]),

    dict(slug="how-many-guests-murder-mystery-party.html",
         h1="How many people do you need for a murder mystery party?",
         meta_title="How many people do you need for a murder mystery party?",
         desc="Four can work, 8 to 12 is the sweet spot and above 16 it becomes a different event. "
              "What changes at each size, and what breaks at the edge of a game's range.",
         targets=["how many people do you need for a murder mystery party",
                  "murder mystery party for 6 people", "murder mystery for large groups",
                  "minimum players murder mystery party"],
         about=["Murder mystery game", "Party planning"],
         faq=[("What is the minimum number of players for a murder mystery party?",
               "Four, and only if the documents carry the whole solution. With four players any "
               "game that distributes the answer across the guests breaks when one person goes "
               "quiet."),
              ("How many guests is best for a murder mystery party?",
               "Eight to twelve. At that size you can have suspects and separate witness roles, "
               "which is what makes the evening feel full without overloading anybody's reading."),
              ("Can you run a murder mystery for 30 or 40 people?",
               "Yes, but it needs a different structure: roles handed out at the door all evening, "
               "badges, a small core of suspects with a large edge of drop-in roles, evidence on a "
               "wall rather than a table, and an ending that fires on a clock.")],
         body=M.GUESTS,
         related=["how-to-host-a-murder-mystery-dinner-party.html",
                  "office-christmas-party-murder-mystery.html",
                  "free-murder-mystery-game.html"]),

    dict(slug="what-to-print-murder-mystery-party.html",
         h1="What you actually have to print for a murder mystery party (and how to cut it)",
         meta_title="What to print for a murder mystery party, and how to cut it",
         desc="The print list, paper and ink, the four printer settings that ruin a printable game, "
              "how to cut cards straight, and a one-sheet test that catches everything.",
         targets=["how to print a murder mystery party game",
                  "printable murder mystery what to print", "print murder mystery on cardstock",
                  "printable party game print settings"],
         about=["Printing", "Murder mystery game"],
         faq=[("Should I print a murder mystery game at 100% or fit to page?",
               "Always 100%, or 'Actual size'. Fit to page shrinks everything by about 4% and "
               "moves every cut line, which is why cards come out the wrong size."),
              ("How many pages is a printable murder mystery?",
               "For 6 to 12 guests, usually 30 to 45 sides. A game built for 16 to 40 people is a "
               "different order of magnitude — ours runs to about 141 pages, mostly badges and "
               "drop-in cards."),
              ("Do I need cardstock?",
               "Only for the character cards and any pocket cards, where 160 to 200 gsm is plenty. "
               "Evidence documents are meant to be handled and passed around on plain paper.")],
         body=M.PRINT,
         related=["how-to-host-a-murder-mystery-dinner-party.html",
                  "what-goes-wrong-murder-mystery-party.html",
                  "free-murder-mystery-game.html"]),

    dict(slug="what-goes-wrong-murder-mystery-party.html",
         h1="What goes wrong at murder mystery parties, and how to stop it",
         meta_title="What goes wrong at murder mystery parties (and how to stop it)",
         desc="Nine failure modes taken from real reviews — the host who cannot play, the answer "
              "on page one, type nobody can read, clues that lead nowhere — and the fix for each.",
         targets=["murder mystery party problems", "murder mystery party mistakes",
                  "how to make a murder mystery party better",
                  "murder mystery party not fun what to do"],
         about=["Murder mystery game", "Party planning"],
         faq=[("Why do murder mystery parties fall flat?",
               "Usually for structural reasons rather than story ones: the host knows the answer "
               "and cannot play, a guest has to perform in front of people they know, the clues do "
               "not connect to a provable solution, or the type is too small to read in the light "
               "the party actually has."),
              ("What if nobody solves the murder mystery?",
               "Assume it will happen and buy a game that plans for it: sealed hints that name "
               "nobody, and a reveal that fires on a clock time and works whether or not the room "
               "got there.")],
         body=M.WRONG,
         related=["how-to-host-a-murder-mystery-dinner-party.html",
                  "what-to-print-murder-mystery-party.html",
                  "free-murder-mystery-game.html"]),

    dict(slug="office-christmas-party-murder-mystery.html",
         h1="A murder mystery for the work Christmas party, without embarrassing anybody",
         meta_title="Work Christmas party murder mystery, without the HR problem",
         desc="The seven things a workplace murder mystery must not contain, the logistics of a "
              "room where people arrive across an hour, and what structural safety actually means.",
         targets=["work christmas party murder mystery",
                  "office murder mystery party game", "hr friendly office party game",
                  "corporate murder mystery for large groups",
                  "office christmas party game ideas for adults"],
         about=["Murder mystery game", "Office party", "Christmas party"],
         faq=[("Is a murder mystery appropriate for a work Christmas party?",
               "Yes, if it is chosen against a checklist rather than a theme: no affairs or "
               "romance, no card whose joke is on the holder, no protected characteristics near a "
               "motive, no real workplace grievances as plot, no drinking mechanic, no public "
               "accusations by name, and no performance requirement."),
              ("How do you run a murder mystery for 30 people at an office party?",
               "Hand roles out at the door for as long as people keep arriving, use badges with "
               "department marks, put the evidence on a wall instead of a table, take accusations "
               "as written secret ballots, and fire the ending on a clock time."),
              ("What if people arrive late or leave early?",
               "Choose a game where no single guest is load-bearing — every fact the solution "
               "depends on must also be printed on a document that stays on the wall.")],
         body=M.OFFICE_PARTY,
         related=["how-many-guests-murder-mystery-party.html",
                  "christmas-party-games-for-teens-and-adults.html",
                  "what-goes-wrong-murder-mystery-party.html"]),

    dict(slug="advent-calendar-ideas-for-adults.html",
         h1="Advent calendar ideas for adults that are not twenty-four small chocolates",
         meta_title="Advent calendar ideas for adults (not chocolate)",
         desc="Ten adult advent calendar formats, what each really costs in money and evenings, "
              "what the Etsy market actually looks like, and five rules for making one yourself.",
         targets=["advent calendar ideas for adults", "adult advent calendar printable",
                  "diy advent calendar for adults", "advent calendar that isn't chocolate",
                  "advent calendar ideas for husband or wife"],
         about=["Advent calendar", "Christmas", "Gift ideas"],
         faq=[("What can you put in an adult advent calendar instead of chocolate?",
               "The formats that actually get finished are the cumulative ones: a story told in "
               "instalments, a skill in 24 steps, 24 questions asked over breakfast, or one puzzle "
               "with 24 pieces of evidence. Anything where skipping a day costs nothing tends to "
               "be abandoned around the 9th."),
              ("How much does an adult advent calendar cost to make?",
               "A printable one costs paper, ink and 24 envelopes. Twenty-four spirit miniatures "
               "is comfortably a three-figure project, which is why twelve bottles with a note "
               "each is usually the better version."),
              ("When should I start making an advent calendar?",
               "Late October if it involves collecting things such as photographs or tickets. Two "
               "evenings in late November is enough for a printable one.")],
         body=C.ADVENT_IDEAS,
         related=["christmas-party-games-for-teens-and-adults.html",
                  "how-to-host-a-murder-mystery-dinner-party.html",
                  "free-murder-mystery-game.html"]),

    dict(slug="christmas-party-games-for-teens-and-adults.html",
         h1="Christmas party games for teens and adults in the same room",
         meta_title="Christmas party games for teens and adults together",
         desc="Eight games that work in a room spanning three generations, four to avoid, the "
              "trick for running each one, and how to give a teenager a job inside the game.",
         targets=["christmas party games for teens and adults",
                  "christmas party games for adults printable",
                  "christmas games for mixed ages", "family christmas games for teenagers"],
         about=["Party game", "Christmas", "Family games"],
         faq=[("What Christmas games work for teenagers and adults together?",
               "Games where nobody has to perform, where being loud does not win, and where you "
               "can join in twenty minutes late: a paper-led murder mystery, call-my-bluff with "
               "wrapped objects, guess-the-year scored by distance, a large shared crossword, and "
               "blind taste tests of supermarket brands."),
              ("What Christmas party games should you avoid with mixed ages?",
               "Anything where the forfeit is embarrassment, anything needing everybody's phone, "
               "physical minute-to-win-it games, and anything that requires players to lie."),
              ("How do you get a teenager to join in?",
               "Give them a job inside the game rather than outside it: opening the evidence "
               "envelopes on the clock, counting the ballots, or reading the ending aloud.")],
         body=C.TEEN_GAMES,
         related=["office-christmas-party-murder-mystery.html",
                  "advent-calendar-ideas-for-adults.html",
                  "free-murder-mystery-game.html"]),

    dict(slug="american-mahjong-for-beginners.html",
         h1="American mahjong for beginners: the whole game in one read",
         meta_title="American mahjong for beginners: the whole game in one read",
         desc="Tiles, deal, Charleston, the turn, calling discards, joker rules and settling up "
              "— American mahjong explained in the order you meet it, with four common mistakes.",
         targets=["american mahjong for beginners", "how to play american mahjong",
                  "american mahjong rules explained", "mahjong charleston rules",
                  "american mahjong joker rules"],
         about=["American mahjong", "Mahjong", "Tile game"],
         faq=[("How many tiles are in an American mahjong set?",
               "152: 108 suit tiles (dots, bams and craks, one to nine, four of each), 16 winds, "
               "12 dragons, 8 flowers and 8 jokers."),
              ("What is the Charleston in American mahjong?",
               "Three rounds of passing three tiles at a time. The first Charleston goes right, "
               "across, left and is always played; the second goes left, across, right and is "
               "optional. A joker is never passed in the Charleston."),
              ("Where can a joker be used in American mahjong?",
               "In any group of three or more — a pung, a kong or a quint. Never in a pair, "
               "never as a single tile, never in NEWS or in a year, and never in a hand the card "
               "marks as jokerless. A discarded joker is dead and cannot be claimed."),
              ("Can you call a discard for a pair?",
               "No. You may only claim a discard to complete a group of three or more, with one "
               "exception: the tile that completes your entire hand.")],
         body=J.BEGINNERS,
         related=["how-to-read-a-mahjong-card.html", "how-to-host-a-mahjong-night.html"]),

    dict(slug="how-to-read-a-mahjong-card.html",
         h1="How to read a mahjong card: the shorthand, decoded",
         meta_title="How to read a mahjong card: the shorthand, decoded",
         desc="Each line is fourteen tiles. What the repeated digits mean, what F, D, NEWS and 0 "
              "stand for, what the colours really tell you, and what X and C mean at the end.",
         targets=["how to read a mahjong card", "how to read the nmjl card",
                  "american mahjong card shorthand", "what does x and c mean on a mahjong card",
                  "mahjong card colours suits"],
         about=["American mahjong", "Mahjong"],
         faq=[("What do the colours on a mahjong card mean?",
               "Colour tells you whether groups share a suit, not which suit. Groups printed in "
               "the same colour must be the same suit; groups in different colours must be "
               "different suits. Which actual suit is your choice."),
              ("What do X and C mean on a mahjong card?",
               "X means the hand may be exposed, so you can call discards and lay groups face up. "
               "C means the hand must be concealed — you may expose nothing, and the only "
               "discard you may take is the one that completes the whole hand."),
              ("What does 0 mean on a mahjong card?",
               "A zero inside a year is played as the white dragon, usually called the soap. A "
               "year hand such as 2026 is four single tiles, so no jokers can be used in it."),
              ("How many tiles is each line on the card?",
               "Always fourteen. If your reading of a line does not add up to fourteen, you have "
               "misread it.")],
         body=J.READ_CARD,
         related=["american-mahjong-for-beginners.html", "how-to-host-a-mahjong-night.html"]),

    dict(slug="how-to-host-a-mahjong-night.html",
         h1="How to host a mahjong night",
         meta_title="How to host a mahjong night that people come back to",
         desc="Table, light, the six house rules to agree out loud, what to do with a fifth "
              "player, food that does not touch the tiles, and how to make it recur.",
         targets=["how to host a mahjong night", "mahjong night ideas",
                  "mahjong party for beginners", "what to serve at a mahjong night"],
         about=["American mahjong", "Party planning"],
         faq=[("How many people do you need for a mahjong night?",
               "Four play at a time. With five, one person sits out and scores each game, or you "
               "play two shorter games and swap at the halfway point. With eight, set up two "
               "tables."),
              ("What house rules should you agree before playing mahjong?",
               "Whether you are playing for money and what a hand is worth, whether a jokerless "
               "hand pays extra, whether pass-backs are allowed in the courtesy pass, which passes "
               "may be blind, what a dead hand does, and how much table talk is allowed."),
              ("What food works at a mahjong night?",
               "Anything that does not leave grease or powder on the tiles. Eat between games "
               "rather than during them, and take one proper twenty-minute break away from the "
               "table.")],
         body=J.NIGHT,
         related=["american-mahjong-for-beginners.html", "how-to-read-a-mahjong-card.html"]),
]
