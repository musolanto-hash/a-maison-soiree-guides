# -*- coding: utf-8 -*-
"""Homepage, guides index, and the free-game landing page."""

SHOP = "https://www.etsy.com/shop/AMaisonSoiree"
HOUR_CANDLE = "https://www.etsy.com/listing/4578182899/christmas-murder-mystery-party-game-for"
OFFICE = "https://www.etsy.com/listing/4578116117/office-murder-mystery-party-game-for-16"
ADVENT = "https://www.etsy.com/listing/4576808653/murder-mystery-advent-calendar-printable"
CHEAT = "https://www.etsy.com/listing/4578067667/mahjong-cheat-sheet-printable-american"
TRACKER = "https://www.etsy.com/listing/4578084694/mahjong-hand-tracker-printable-blank"

FREE = """
<h1>A free four-player murder mystery you can print tonight</h1>
<p class="lede"><strong>The Wet Half-Hour.</strong> Four suspects, eleven printed case documents,
forty-five minutes at a kitchen table. Nobody acts, nobody lies, and nobody knows who did it
&mdash; including whoever did it.</p>
<p class="meta">A complete game, free, no email address, no sign-up &middot; PDF, US Letter and A4</p>

<p>The Juniper Inn, Wren's Hollow, a wet Tuesday afternoon in November. A debt collector called
Edmund Rook goes down to the cellar at five past four to count the stock that secures the note on
the inn. At eight minutes to five the coal merchant tips a sack down the chute, comes round to the
hatch steps and finds him at the bottom of them with the door-weight beside him and his wallet
open.</p>
<p>Four people were in the building or the yard. All four of them are sitting at your table.</p>

<div class="box">
<p><strong>Download the game</strong> &mdash; 20 pages, and the answer is not in it.</p>
<p><a class="cta" href="files/the-wet-half-hour-USLetter.pdf">The game &middot; US Letter (PDF)</a>
<a class="cta" href="files/the-wet-half-hour-A4.pdf">The game &middot; A4 (PDF)</a></p>
<p><strong>Download the sealed answer</strong> &mdash; a separate file, behind a full-page STOP card.
Print it without opening it and put it in an envelope, and whoever printed the game can still
play.</p>
<p><a class="cta alt" href="files/the-wet-half-hour-answer-USLetter.pdf">The answer &middot; US Letter</a>
<a class="cta alt" href="files/the-wet-half-hour-answer-A4.pdf">The answer &middot; A4</a></p>
</div>

<h2>What is in it</h2>
<ul>
<li><strong>Four suspect cards</strong>, two to a page with a cut line. Every word on all four is
true.</li>
<li><strong>Eleven case documents</strong>: the constable's scene report, the village weather book,
the dead man's own list of the papers in his wallet, an inn day book, a press copy of a letter, a
telephone exchange ticket, a hotel manager's reply, two household books, a carrier's delivery
ticket, the constable's measurements, and his sheet on the yard and the hall stand.</li>
<li><strong>A one-page guest sheet</strong> and <strong>a one-page host sheet</strong> that contains
no spoilers at all, so the person who prints it is not excluded from playing.</li>
<li><strong>Accusation slips</strong>, four to a page, and a shared sheet the table fills in
together.</li>
<li><strong>A separate answer file</strong> with the reveal and a page showing exactly how it was
proved, chain by chain.</li>
</ul>

<h2>The rules it is built on</h2>
<p>These are the same five rules our paid games are built on, and this is the smallest honest
demonstration of them we could make:</p>
<ol>
<li><strong>Nothing is memorised.</strong> A card is a reference sheet you read off when somebody
asks you something.</li>
<li><strong>Nothing is read aloud in character.</strong> No accents, no costumes, no acting,
anywhere.</li>
<li><strong>Nobody lies.</strong> Every card is literally true. The misdirection comes from omission,
refusal and missing context, and "I don't remember" is printed on all four cards as a legal
answer.</li>
<li><strong>Nobody knows they are the culprit</strong>, including the culprit. So nobody can give it
away and nobody can be blamed for giving it away.</li>
<li><strong>The paper carries the whole solution.</strong> A player who talks to nobody can still
solve it by reading. The four of you are the fast route, not the only one &mdash; which is why the
game does not break if somebody has to leave at half past nine.</li>
</ol>

<h2>How to run it</h2>
<p>Print, cut two pages, deal the cards face down. Then three rounds on a timer: the scene (12
minutes), the papers (15), the measurements (10). Everybody writes a secret accusation and names
the one fact on paper they would hang it on. Then you open the answer.</p>
<p>It works at four. At three, leave out the doctor's card and read it aloud as a written statement
&mdash; everything on it is also on a document. At five, the extra person keeps the time and reads
out the ending, which is the best job at the table.</p>

<h2>Why we are giving away a whole game</h2>
<p>Because it is the only honest advertisement for the paid ones. You can read a listing that says
"fair play" and "the host can play too" and have no way of knowing whether either is true. Print
this, play it, and you will know exactly what we mean by both &mdash; including whether our idea of
fair matches yours.</p>
<p>There is no email capture here and nothing to sign up for. The PDF is a link on this page.</p>

<div class="box shop"><span class="k">If you want a longer one afterwards</span>
<p><a href="{HC}">The Hour Candle, $29</a> &mdash; a Christmas murder mystery for 6 to 12 guests,
90 to 120 minutes, 22 case documents instead of 11, seven suspects and five witnesses, built to the
same five rules.<br>
<a href="{OF}">The Golden Tin, $39</a> &mdash; the same machinery for a room of 16 to 40 at an
office holiday party, with an evidence wall instead of a table.<br>
<a href="{AD}">Until Breakfast, $24.99</a> &mdash; a 24-day murder mystery advent calendar, one
envelope a day from the 1st of December.</p></div>

<h2>The small print</h2>
<p>The PDFs are free for personal use: print them as many times as you like, for your own table,
your classroom, your office or your book club. Please do not resell them or put them behind a
paywall. If something is wrong with a file, the fault is ours and we would like to know.</p>
""".replace("{HC}", HOUR_CANDLE).replace("{OF}", OFFICE).replace("{AD}", ADVENT)


def _card(slug, title, blurb):
    return f'<li><a href="{slug}">{title}</a><p>{blurb}</p></li>'


GUIDE_LIST = "".join([
    _card("how-to-host-a-murder-mystery-dinner-party.html",
          "How to host a murder mystery dinner party at home",
          "The two decisions that make the evening: whether the host can play, and what happens "
          "when somebody arrives at nine. With a timetable and a week-before checklist."),
    _card("how-many-guests-murder-mystery-party.html",
          "How many people do you need for a murder mystery party?",
          "What actually changes at 4, at 8, at 12, at 16 and at 40 &mdash; and what quietly "
          "breaks when you are at the edge of a game's range."),
    _card("what-to-print-murder-mystery-party.html",
          "What you actually have to print, and how to cut it",
          "The print list, the paper, the ink, the four settings that ruin it, and the one-sheet "
          "test that catches everything."),
    _card("what-goes-wrong-murder-mystery-party.html",
          "What goes wrong at murder mystery parties",
          "Nine failure modes taken from real reviews of games that are still selling, and the "
          "design choice that prevents each one."),
    _card("office-christmas-party-murder-mystery.html",
          "A murder mystery for the work Christmas party",
          "The seven things a workplace game must not contain, the logistics nobody warns you "
          "about, and what structural safety looks like."),
    _card("advent-calendar-ideas-for-adults.html",
          "Advent calendar ideas for adults",
          "Ten formats that are not twenty-four small chocolates, what each really costs, and the "
          "design question that decides whether it survives past the 9th."),
    _card("christmas-party-games-for-teens-and-adults.html",
          "Christmas party games for teens and adults",
          "Eight that work in a room spanning three generations, four to avoid, and how to run "
          "the evening rather than just choose the game."),
    _card("american-mahjong-for-beginners.html",
          "American mahjong for beginners",
          "The tiles, the deal, the Charleston, the turn, the calls, the jokers and the settle-up, "
          "with the four mistakes beginners make marked as you go."),
    _card("how-to-read-a-mahjong-card.html",
          "How to read a mahjong card",
          "The shorthand decoded: the numbers, the letters, what the colours really mean, and the "
          "X and C at the end of the line."),
    _card("how-to-host-a-mahjong-night.html",
          "How to host a mahjong night",
          "Four players, three hours, and the six decisions that turn one evening into a "
          "fortnightly habit."),
])

GUIDES = """
<h1>All guides</h1>
<p class="lede">Ten long articles about hosting the kind of evening that needs printing out first.
Written from building the games, not from a keyword list.</p>
<p class="meta">Free to read &middot; no sign-up &middot; updated September 2026</p>
<h2>Murder mystery parties</h2>
<ul class="cards">%s</ul>
<h2>And a whole game, free</h2>
<p><a class="cta" href="free-murder-mystery-game.html">The Wet Half-Hour &mdash; a free four-player
murder mystery</a></p>
""" % GUIDE_LIST

HOME = """
<h1>Notes from building printable party games</h1>
<p class="lede">We draw murder mysteries, advent calendars and mahjong reference sheets, page by
page, and then read the reviews of everybody else's. These are the notes: how to host the evening,
what to print, what breaks, and what to check before you buy anything.</p>

<div class="box">
<p><strong>Start with the free one.</strong> <em>The Wet Half-Hour</em> is a complete four-player
murder mystery: four suspects, eleven printed documents, forty-five minutes. No email address, no
sign-up, and the answer is in a separate sealed file so whoever prints it can still play.</p>
<p><a class="cta" href="free-murder-mystery-game.html">Get the free game</a></p>
</div>

<h2>The guides</h2>
<ul class="cards">%s</ul>

<h2>Who writes this</h2>
<p>A Maison Soir&eacute;e is a small studio that makes printable party games. Everything on this
site comes out of building them: the legibility rules came from reading a year of one-star reviews
about type that could not be read by candlelight; the fair-play method came from auditing our own
Christmas mystery fact by fact, 58 rows, until every one of them was printed on a document rather
than living in somebody's head; the advice about hosts came from the discovery that "the host can
play too" is usually not true.</p>
<p>We try to be accurate about what we have and have not tested. Our games have been
<em>read-tested</em> &mdash; a fresh reader given only the player-facing files, asked to solve it,
and asked to score it &mdash; and that is a different thing from a room of twelve people with
plates in their hands. Where we have not done the room test, we say so, here and on the
listings.</p>
<p>If you want the finished products, they are on Etsy:
<a href="{SHOP}">the A Maison Soir&eacute;e shop</a>. Nothing is sold on this site.</p>
""" % GUIDE_LIST
HOME = HOME.replace("{SHOP}", SHOP)
