# -*- coding: utf-8 -*-
"""The Wet Half-Hour - all copy for the free four-player mini mystery.

House rules this game is built to (the same ones the paid games are built to):
  nothing is memorised, nothing is read aloud in character, nobody lies,
  every card is true, nobody knows they are the culprit, the paper carries
  the whole solution, and the answer ships in a separate file.
"""

TITLE = "The Wet Half-Hour"
SUB = "A murder mystery for exactly four players · 45 minutes · print and play"
BRAND = "A Maison Soirée"

# ----------------------------------------------------------------- cover
COVER = [
    ("p", "Four people. Eleven printed documents. Forty-five minutes at a kitchen table. "
          "One of the four of you killed Edmund Rook, and none of you knows which."),
    ("rule",),
    ("h", "What you need"),
    ("p", "A printer, a pair of scissors, four pencils and four people. Print pages 4 and 5 "
          "and cut out the four cards. Print the rest and keep it in three piles. That is the whole setup, "
          "and it takes about ten minutes."),
    ("h", "The five rules this game is built on"),
    ("li", "Nothing is memorised. Your card is a reference sheet you read off when somebody asks you something."),
    ("li", "Nothing is read aloud in character. No accents, no costumes, no acting, anywhere."),
    ("li", "Nobody lies. Every word on every card is true. What misleads you is what a card leaves out."),
    ("li", "Nobody knows they are the culprit — including the culprit. You will all find out together."),
    ("li", "The paper carries the whole solution. Every fact you need is printed on a document that sits on "
           "the table. The four of you are the fast route, not the only one."),
    ("rule",),
    ("p", "The answer is not in this file. It is in a second file called THE ANSWER. "
          "Do not open that one until the ballots are counted — whoever is hosting can play too, "
          "because nothing in these pages tells you who did it."),
]

# ----------------------------------------------------------------- how to play
HOWTO = [
    ("h", "The case"),
    ("p", "The Juniper Inn, in the village of Wren's Hollow. Tuesday the 4th of November, a wet afternoon. "
          "The inn is shut between lunch and six."),
    ("p", "In August a debt collector called Edmund Rook bought the mortgage on the inn from the bank, and "
          "has been coming for the money in person ever since. He came again this afternoon, at twenty to four. "
          "At five past four he went down the cellar stairs with a lamp to count the stock that secures the note."),
    ("p", "At eight minutes to five the coal merchant tipped a sack down the chute, came round to the hatch steps, "
          "and found Mr Rook at the bottom of them with the cellar door-weight beside him and his wallet open."),
    ("p", "Four people were in the building or the yard. All four of them are sitting at this table."),
    ("h", "How the evening runs"),
    ("li", "Deal the four cards face down and take one each without choosing. Read your own card. "
           "Do not read anybody else's, and do not hand it over."),
    ("li", "ROUND ONE (12 minutes). Put out documents C‑1, C‑2 and C‑3. Read them out loud, or pass them round. "
           "Then ask each other questions. You answer from your card. If the card does not cover it, the honest "
           "answer is “I don't remember”, and that is a legal answer printed on all four cards."),
    ("li", "ROUND TWO (15 minutes). Put out C‑4 to C‑9. These are the papers. This is the round where the "
           "why arrives, and it is the longest one."),
    ("li", "ROUND THREE (10 minutes). Put out C‑10 and C‑11. These are the measurements. If your table has been "
           "arguing well, this round ends the argument."),
    ("li", "THE BALLOT (5 minutes). Everyone fills in an accusation slip, including the person they think it is, "
           "and the one fact they would hang it on. Fold them. Then, and only then, open THE ANSWER."),
    ("h", "Two things worth knowing before you start"),
    ("p", "You may accuse yourself. People do, and they are sometimes right."),
    ("p", "There is no lie-detecting in this game, so there is nothing to adjudicate and nobody has to be a referee. "
          "You are not trying to catch somebody out. You are trying to work out which of four true stories has a "
          "hole in the middle of it."),
]

# ----------------------------------------------------------------- host page (spoiler free)
HOST = [
    ("p", "You can read every word of this page and still sit down and play. Nothing here says who did it, and "
          "nothing in the eleven documents says it either — the solution has to be assembled, which is why the "
          "host can hold a card like everybody else."),
    ("h", "Printing"),
    ("li", "Print at 100% “Actual size”, not “fit to page”. Every page in this file is laid out to fall inside "
           "both US Letter and A4 without scaling."),
    ("li", "Pages 4 and 5 are the four cards, two to a page. Cut along the dashed line."),
    ("li", "Everything prints legibly in black and white on the cheapest paper in the house. Nothing in this file "
           "is set smaller than 10 point and no text sits on top of a picture."),
    ("h", "Setting up, ten minutes"),
    ("li", "Make three piles: C‑1 to C‑3, C‑4 to C‑9, C‑10 and C‑11. Put the second and third out of sight."),
    ("li", "Four accusation slips and four pencils on the table."),
    ("li", "Put the sheet marked WHAT WE KNOW in the middle where everyone can write on it."),
    ("li", "Set a phone alarm for 12, then 15, then 10 minutes. The alarms run the evening, not you."),
    ("h", "The only four things you say out loud"),
    ("p", "Read these as yourself. There is no character for the host and nothing to perform."),
    ("cue", "AT THE START — “Edmund Rook came here this afternoon for money. At eight minutes to five he was "
            "found at the bottom of the cellar steps. The four of us were in the building. One of us did it, and "
            "the honest truth is that none of us knows which — that is how this one is built. Everything on your "
            "card is true. Nobody is lying to anybody tonight.”"),
    ("cue", "AT ROUND TWO — “These are the papers. The constable took them off Rook's desk in Aldersbury on "
            "Wednesday morning, so nobody in this room got to tidy them first.”"),
    ("cue", "AT ROUND THREE — “This is what the constable measured, and he says plainly that he is making no "
            "accusation. We are.”"),
    ("cue", "AT THE BALLOT — “Name somebody, and name the one thing on paper you would hang it on. You may name "
            "yourself. Fold it over. Nobody reads these until the end.”"),
    ("h", "The four questions you will actually be asked"),
    ("li", "“Can I lie?” No. Nobody in this game lies. If your card does not cover it, say you don't remember."),
    ("li", "“Am I allowed to show somebody my card?” No — but you may read any line of it out loud, and you may "
           "read the whole thing out loud if you want to."),
    ("li", "“What if I think it's me?” Say so. It may be. Write your own name on the ballot if you believe it."),
    ("li", "“What if we get it wrong?” Then you get it wrong. The reveal tells you which document you walked past."),
    ("h", "If you are three, or five"),
    ("p", "At three: leave out Dr Quill's card and read it aloud as a written statement instead — everything on it "
          "also appears on a document. At five: the fifth person takes the accusation slips, keeps the time, and "
          "reads out THE ANSWER at the end, which is the best job at the table."),
]

# ----------------------------------------------------------------- suspect cards
CARDS = [
    ("S1", "Mrs Harriet Pell", "52 · keeps the Juniper Inn", [
        "The inn was your mother's. In August a man called Edmund Rook bought the mortgage off the bank and "
        "started coming for the money in person, which the bank never did.",
        "You are clear of it. At the end of October you drew £412 out of the post office savings — every penny "
        "you had — and gave it to Mr Bram to carry to Rook. On the 2nd Mr Bram told you it was done.",
        "Rook came anyway this afternoon, at twenty to four, and would not say why. At four o'clock you told "
        "Mr Bram, in the hall, that Rook had gone down to count the barrels. At ten past you bolted the pantry "
        "stair door on your side, because the draught up that stair takes the flour off the table.",
        "You were alone in the kitchen from twenty past four until a quarter to five, with the yard door propped "
        "open for the steam. You did not go down to the cellar.",
    ]),
    ("S2", "Mr Silas Bram", "44 · bookkeeper, at the inn on Tuesdays", [
        "You keep the books for the Juniper, the garage, and the two farms at Hollow End.",
        "On the 31st of October Mrs Pell gave you £412 in notes, in the office, to carry to Mr Rook against the "
        "note. You wrote her a line for it. On the 2nd you told her it was settled and that the discharge would "
        "come by post.",
        "This afternoon you booked a trunk call from the front desk at eighteen minutes past four and cleared it "
        "at half past. It was to Aldersbury and it was about Mr Rook, and you would rather not repeat it in "
        "front of everybody.",
        "You went out into the yard once, after the call, to see whether the coal had come. You came back into "
        "the house by the front door, because the carter's horse was in the lane and it is a nervous animal.",
        "You did not speak to Mr Rook after three o'clock.",
    ]),
    ("S3", "Miss Nell Fisk", "19 · yard hand", [
        "You do the coal, the crates, the bottles and the horse. You have worked here since you were fifteen, "
        "and Mrs Pell taught you to read.",
        "You were in the yard all afternoon and your boots are still wet. The Birchfield cart came to the lane "
        "gate at twenty-six minutes past four, in the rain, and you signed for two crates and a sack. The carter "
        "stood under the gate until the rain went over, and you held the horse's head the whole time, because he "
        "will not stand for thunder.",
        "You knew Mr Rook by sight and you did not like him. In September he stopped you in the yard and asked "
        "you what the cellar held, and whether Mrs Pell kept the key on her.",
        "You did not go down the hatch today. You did not go into the house between four and five.",
    ]),
    ("S4", "Dr Ambrose Quill", "71 · retired physician, room 2 since March", [
        "You have lived in room 2 since March, and you would like to go on living in it.",
        "In September you asked Mr Rook, in the snug, what he would take for the freehold of the inn. He laughed "
        "at you and named a figure, and you wrote the figure down. You have not mentioned any of this to Mrs Pell.",
        "This afternoon you were in your chair by the window. The chambermaid took your linen out at a quarter "
        "past four and brought it back pressed at twenty to five, and you asked her the time.",
        "You heard the rain start and you heard it stop. Some time after it stopped, and before the girl came "
        "back with the linen, you heard somebody cross the yard below your window. Your window is at the back, "
        "over the coal hatch. You did not look out, because you were reading, and because people cross that yard "
        "all day.",
    ]),
]

CARD_FOOT = ("One of the four of you did it, and your card will not tell you which, because nobody knows. "
             "Everything here is true; nothing here is the whole evening. “I don't remember” is a legal answer.")

# ----------------------------------------------------------------- documents
# kind: "type" typed document, "hand" handwritten, "form" ruled form
DOCS = [
    dict(num="C-1", round=1, kind="type", full=True,
         head="WREN'S HOLLOW CONSTABULARY",
         title="Report of the scene",
         meta="Made by Constable A. Dorrit, 4 November, at the Juniper Inn. Timed from the kitchen clock, "
              "which the stationmaster checked against the station clock on Wednesday and found correct.",
         blocks=[
             ("p", "Called out at 4.55 p.m. by Mr J. Pryor, coal merchant. Arrived 5.02 p.m."),
             ("p", "THE BODY. Mr Edmund Rook, 58, of Aldersbury. Lying on the brick floor of the cellar at the "
                   "foot of the six steps that come down beside the coal chute, face down, feet towards the steps. "
                   "One blow to the back of the head. No other mark on him. Dr Quill, who lodges here, says one "
                   "blow and death within a minute or two of it, and that he could not put an hour to it closer "
                   "than the afternoon."),
             ("p", "THE WEAPON. The cellar door-weight, six pounds of iron on a cord, which hangs on a hook beside "
                   "the inner door and pulls it shut. It was on the floor a foot from his head. The cord is frayed "
                   "through where it has been pulled off its hook rather than lifted off."),
             ("p", "THE LAMP. A hurricane lamp, lit, standing upright on a barrel three feet from him, with oil in "
                   "it. Whoever was down there had light."),
             ("p", "THE TWO WAYS IN. (1) The pantry stair, through a door at the head of it. That door was bolted "
                   "on the pantry side. Mrs Pell shot the bolt at ten past four and drew it at five to five when "
                   "Mr Pryor shouted up from the yard; Mr Pryor was at the hatch and heard her draw it. (2) The "
                   "coal hatch in the yard, with six brick steps beside the chute. The hatch was open. It is never "
                   "locked."),
             ("p", "THE FLOOR. The cellar floor is dry brick and has been dry for a week. There is one line of "
                   "damp prints on it, coming down from the hatch steps to the body and going back to the hatch "
                   "steps. There are no damp prints anywhere else in the cellar and none at all on the pantry "
                   "stair. I have put the measurements of them on a separate sheet."),
             ("p", "THE WALLET. Open, beside his right hand. Four pockets in it. Three folded buff forms in it: "
                   "the note itself, the demand dated 1 November, and a receipt for £40 part payment dated "
                   "14 October. All three are folded with the printed side turned in. His clerk at Aldersbury "
                   "says he folds them the other way, printed side out, and has done for nine years, and that "
                   "Mr Rook never refolded anything in his life."),
             ("p", "His money was in his breast pocket and was not touched. £18 and some silver."),
         ]),

    dict(num="C-2", round=1, kind="form", full=False,
         head="WREN'S HOLLOW STATION HOUSE",
         title="Rainfall and weather book",
         meta="Kept hourly by the stationmaster. Entry for 4 November.",
         blocks=[
             ("p", "Fine and cold to 4.20 p.m. Rain, heavy, from 4.20 p.m. to 4.35 p.m., 0.31 in. Clear after, "
                   "no more rain that night."),
             ("note", "Note added by the stationmaster at the constable's request, 5 November: “The lane and the "
                      "yard behind the Juniper stood in water until about ten past five. The gutter at the "
                      "north-east corner of the inn comes down on the cobbles right by the coal hatch, and there "
                      "were two or three inches of water standing against that wall all evening. Anybody crossing "
                      "that corner after the rain went through it, whether they wanted to or not.”"),
         ]),

    dict(num="C-3", round=1, kind="type", full=False,
         head="E. ROOK, COLLECTIONS — ALDERSBURY",
         title="Flyleaf of the collecting book",
         meta="In Mr Rook's own hand. He wrote this list every morning. Taken from his desk by the constable, "
              "5 November.",
         blocks=[
             ("p", "4th Nov. Wren's Hollow, the Juniper. In the wallet, four papers, all buff, all folded in "
                   "three, and there is no telling one from another until you open it:"),
             ("list", ["1. The note.",
                       "2. The demand, 1 Nov.",
                       "3. Receipt, £40 on account, 14 Oct.",
                       "4. Letter to Mrs H. Pell. Sealed. To be put in her own hand and not left with anybody."]),
             ("note", "Three of the four were in the wallet when he was found. The fourth was not."),
         ]),

    dict(num="C-4", round=2, kind="hand", full=False,
         head="THE JUNIPER INN",
         title="The day book",
         meta="Mrs Pell's hand. Four entries, with a slip of paper pinned below the second.",
         blocks=[
             ("hand", "29 Oct — Mr Bram says the bank's man will take the whole in cash and be done with it. "
                      "Went to the post office savings and drew £412, being all of it."),
             ("hand", "31 Oct — Gave Mr Bram £412 in notes, in the office, to carry to Mr Rook at Aldersbury on "
                      "Friday. Mr Bram wrote me a line for it and I have pinned it here."),
             ("pin", "Received of Mrs H. Pell four hundred and twelve pounds, to be paid over to Mr E. Rook "
                     "against the Juniper note. — S. Bram, 31 October"),
             ("hand", "2 Nov — Mr Bram says it is done and the discharge will come by post."),
             ("hand", "3 Nov — No post. Asked Mr Bram again. He says Mr Rook is slow with paper."),
         ]),

    dict(num="C-5", round=2, kind="type", full=True,
         head="E. ROOK, COLLECTIONS — ALDERSBURY",
         title="Press copy of a letter",
         meta="Mr Rook kept a damp press copy of every letter he wrote. This is the copy of the letter he sealed "
              "and carried to Wren's Hollow on the 4th. Taken from the copy book on his desk, 5 November.",
         blocks=[
             ("p", "The Bell Hotel, Aldersbury. 3rd November."),
             ("p", "Madam,"),
             ("p", "I am obliged to write to you plainly, and I would rather do it on paper than across a table."),
             ("p", "You have twice said to me, and once in the hearing of my clerk, that four hundred and twelve "
                   "pounds was paid over to me on the 2nd of this month by Mr Bram on your behalf, and that a "
                   "discharge was to follow by post."),
             ("p", "No such sum has been paid to me. Not on the 2nd, not on any other day, not at this house and "
                   "not at my office. I have issued no discharge, because there was nothing to discharge. I hold "
                   "the note and I hold it unsatisfied, and the demand falls due on Friday."),
             ("p", "I do not say where your money is. I say only that it is not with me, and that you should ask "
                   "Mr Bram for it in front of a witness, and that you should do it this week."),
             ("p", "I shall be at the Inn on Tuesday afternoon. I will not send this by post. I will put it in "
                   "your hand myself and wait while you read it."),
             ("p", "Your obedient servant, EDMUND ROOK."),
             ("note", "Constable's note: Mrs Pell has never seen this letter. I read it to her on the Wednesday "
                      "and she had to sit down."),
         ]),

    dict(num="C-6", round=2, kind="form", full=False,
         head="POST OFFICE TELEPHONES — WREN'S HOLLOW EXCHANGE",
         title="Trunk call ticket",
         meta="One ticket is written for every trunk call and kept at the exchange for the quarter's accounts.",
         blocks=[
             ("kv", [("From", "Wren's Hollow 14 — the Juniper Inn, front desk"),
                     ("Booked by", "Mr S. Bram"),
                     ("To", "Aldersbury 227"),
                     ("Connected", "4.18 p.m."),
                     ("Cleared", "4.33 p.m."),
                     ("Chargeable", "15 minutes"),
                     ("Date", "4 November")]),
             ("note", "Operator's note: “The gentleman asked me to keep trying. I put him through at the second "
                      "attempt.”"),
         ]),

    dict(num="C-7", round=2, kind="type", full=False,
         head="THE BELL HOTEL, ALDERSBURY · TELEPHONE ALDERSBURY 227",
         title="Letter to the constable",
         meta="5 November. In answer to a letter from Constable Dorrit sent the same morning.",
         blocks=[
             ("p", "Sir — In answer to yours of this morning."),
             ("p", "Mr Edmund Rook has not stayed in this house since September, though he takes his letters here "
                   "and writes in our coffee room most Mondays, and everybody in Aldersbury knows it."),
             ("p", "No money was paid to Mr Rook in this house on the 2nd of November, or at any time this "
                   "autumn. I can be certain of that, because money paid to Mr Rook is handed in at our desk and "
                   "entered in the desk book against his name, and there is no entry."),
             ("p", "Yesterday, Tuesday, at about twenty past four, a gentleman telephoned from Wren's Hollow and "
                   "asked my desk clerk twice over whether Mr Rook had “settled up on Monday”, and then whether "
                   "there was “anything in the book at all” against his name. My clerk told him exactly what I "
                   "have told you. The gentleman rang off without leaving a name and did not ask for Mr Rook."),
             ("p", "Yours faithfully, J. MARCHMONT, Manager."),
         ]),

    dict(num="C-8", round=2, kind="hand", full=False,
         head="THE JUNIPER INN",
         title="Two household books",
         meta="The laundry round book, kept by Ivy Sallow, chambermaid. And the kitchen book, in Mrs Pell's hand.",
         blocks=[
             ("sub", "Laundry round, 4 November"),
             ("hand", "Room 1 — 4.05, linen out. Room empty."),
             ("hand", "Room 2 — 4.15, linen out. Doctor in his chair by the window. 4.40, pressed linen back in. "
                      "Doctor in the same chair with the same book. He asked me the time and I said twenty to five."),
             ("hand", "Room 4 — 4.45, linen out. Room empty."),
             ("sub", "Kitchen book, 4 November"),
             ("hand", "4.20 — six loaves out. 4.44 — eight loaves in, oven at full. 5.20 — out."),
         ]),

    dict(num="C-9", round=2, kind="form", full=False,
         head="BIRCHFIELD & SON, CARRIERS",
         title="Delivery ticket",
         meta="Delivery to the Juniper Inn, 4 November, with the carter's note written on the back the next "
              "morning at the constable's request.",
         blocks=[
             ("kv", [("Delivered", "2 crates, 1 sack"),
                     ("Where", "At the lane gate, not carried in"),
                     ("Received by", "N. Fisk"),
                     ("Time signed", "4.26 p.m.")]),
             ("note", "On the back: “Rain came on hard as I turned into the lane. I stood under the gate with the "
                      "girl till it went over and got away at 4.44 by my own watch. She never went in the whole "
                      "time. She was at the horse's head, because he won't stand for thunder and there was "
                      "thunder in it. — W. Birchfield, carter.”"),
         ]),

    dict(num="C-10", round=3, kind="type", full=True,
         head="WREN'S HOLLOW CONSTABULARY",
         title="The measurements",
         meta="Constable A. Dorrit's second sheet. Prints taken 5.05 p.m. Footwear measured 5.15 p.m., everybody "
              "present and watching.",
         blocks=[
             ("sub", "The damp prints on the cellar floor"),
             ("p", "One line of them, from the foot of the hatch steps to the body and back again. Nothing "
                   "anywhere else. The print measures 9¼ inches heel to toe and 3 inches across the ball. "
                   "Smooth leather sole with a stitched welt — the stitching prints as a broken line about "
                   "three-eighths of an inch in from the edge. On the right foot there is a crescent of wear on "
                   "the outer edge of the heel, about an inch across, and it prints every time."),
             ("sub", "Every pair of shoes in the house"),
             ("table", [
                 ["Mrs H. Pell", "House shoes, on since morning. Dry inside and out.",
                  "9½ in", "Smooth sole, no welt stitching. Heel worn square across. No crescent."],
                 ["Mr S. Bram", "Town shoes. Damp across the toe and along the welt. His rubber overshoes are not "
                                "on the hall stand and he cannot say where he left them.",
                  "9¼ in", "Smooth sole, stitched welt. Crescent of wear on the outer edge of the right heel, "
                               "one inch."],
                 ["Miss N. Fisk", "Rubber yard boots, wet through.",
                  "11½ in", "Cleated rubber. No welt."],
                 ["Dr A. Quill", "Carpet slippers, worn indoors. His outdoor boots are on the hall rack, dry, and "
                                 "the laces are tied in a bow with dust lying across the knot.",
                  "Slippers 10 in · boots 10¼ in", "Slippers felt. Boots crepe. No welt on either."],
                 ["Mr J. Pryor", "Boots, wet. He came in by the hatch at 4.52 and went no further than the steps.",
                  "12 in", "Cleated. No welt."],
                 ["The house's spare yard shoes", "On the scullery shelf. Dry. Dust undisturbed on the shelf "
                                                  "around them.", "9 in", "Wooden-soled clogs. No welt, no heel."],
             ]),
             ("note", "I make no accusation in this sheet. I have set down what I measured, and I have measured "
                      "everything there was."),
         ]),

    dict(num="C-11", round=3, kind="type", full=False,
         head="WREN'S HOLLOW CONSTABULARY",
         title="The yard and the hall stand",
         meta="Constable A. Dorrit's third sheet, 4 November, 5.30 p.m., and the Saturday dusting checked with "
              "Mrs Sallow on the 5th.",
         blocks=[
             ("list", [
                 "1. At the top of the hatch steps, against the north-east wall of the yard, standing side by "
                 "side and upright: a pair of men's rubber overshoes, the size that goes over a 9 or a 10 shoe. "
                 "Both of them full of water to the brim. The gutter comes down eighteen inches above them.",
                 "2. The hall stand in the front passage has four pegs and a boot rail. Dr Quill's boots are on "
                 "the rail, dry. Next to them there is a clean oval on the rail, free of dust, eleven inches by "
                 "four, where a pair of overshoes has stood since Mrs Sallow last dusted the rail on Saturday.",
                 "3. The garden gate at the far side of the yard, which gives on to the lane above the gate the "
                 "carter was standing under, was open. The wet grass beyond it is trodden in one direction only "
                 "— away from the yard, towards the lane.",
                 "4. Nobody in the house owns a second pair of overshoes and nobody claims these.",
             ]),
         ]),
]

# ----------------------------------------------------------------- case board
BOARD_ROWS = [
    "WHEN could it have happened? (C-1, C-2)",
    "HOW did whoever it was get into the cellar? (C-1)",
    "WHICH of the four papers is missing, and how do we know? (C-1, C-3)",
    "WHAT did that paper say? (C-5)",
    "WHO is cleared between 4.20 and 4.52, and by which document?",
    "WHO could have made the print? (C-10)",
    "WHOSE overshoes are at the hatch? (C-10, C-11)",
    "THE ONE FACT we would hang it on:",
]

BALLOT_LINES = [
    "I say it was",
    "The one fact on paper I would hang it on",
    "The document it is printed on (C-  )",
    "I could not clear",
    "Signed",
]

# ----------------------------------------------------------------- the answer file
STOP = ("Do not read this file until every ballot is folded. "
        "The other file is the whole game and it does not contain the answer. This one does.")

REVEAL = [
    ("p", "It was MR SILAS BRAM, the bookkeeper. He did not know it either, and neither did the person holding "
          "his card, which is the point of the thing."),
    ("rule",),
    ("h", "What actually happened"),
    ("p", "On the 31st of October Harriet Pell put four hundred and twelve pounds in Silas Bram's hands — "
          "the whole of the post office savings, everything she had — and asked him to carry it to Edmund Rook "
          "and be done with the note. He wrote her a line for it, and she pinned the line into the day book, and "
          "he kept the money."),
    ("p", "On the 2nd he told her it was settled. On the 3rd he told her Rook was slow with paper. He was buying "
          "days, and he would probably have gone on buying them until Friday, because bookkeepers are believed."),
    ("p", "Then at eighteen minutes past four on Tuesday afternoon he stood at the front desk and telephoned the "
          "Bell Hotel at Aldersbury, and a desk clerk told him twice over that there was nothing in the book "
          "against Mr Rook's name. He cleared the call at half past four. Mr Rook was already in the house, and "
          "Mrs Pell had told Bram at four o'clock exactly where he was: below, counting the barrels, behind a "
          "door she had bolted herself at ten past four."),
    ("p", "The rain stopped at twenty-five to five. Bram crossed the yard in his overshoes, stepped out of them "
          "against the north-east wall at the top of the hatch steps — rubber is loud on brick, and he meant to "
          "be quiet — and went down into two inches of gutter water and then into the dry cellar. Dr Quill, "
          "reading in room 2 above the hatch, heard somebody cross the yard and did not look out."),
    ("p", "He took the door-weight off its hook so hard that he frayed the cord, and he hit Edmund Rook once, "
          "from behind, and Rook went down the last two steps."),
    ("p", "And then — this is the part that convicts him — he opened the wallet and unfolded all four papers, "
          "one after another, by the light of the lamp, because folded they are identical. Three of them meant "
          "nothing to him and he folded them back the wrong way round. The fourth was sealed and addressed to "
          "Mrs Pell by hand, and when he opened it he was reading his own name."),
    ("p", "He took that one. He went back up the steps, heard the carter's horse still in the lane, and went out "
          "through the garden gate rather than back across the yard, which is why the wet grass is trodden one "
          "way only and why his overshoes were still standing against the wall, filling with rainwater, when "
          "Constable Dorrit found them."),
    ("p", "What he did not know was that Edmund Rook kept a damp press copy of every letter he ever wrote, in a "
          "copy book on his desk in Aldersbury, and that the constable would be standing over that desk before "
          "ten o'clock on Wednesday morning."),
]

PROOF = [
    ("h", "The three chains"),
    ("p", "The solution stands on three legs that do not touch each other. A table that only got two of them "
          "still arrives at Silas Bram."),
    ("sub", "One — the paper (C-4, C-5, C-7)"),
    ("p", "The day book shows Mrs Pell handed Bram £412 and shows his own signed line for it. Rook's press copy "
          "says the money never reached him and that he was going to put that in her hand on Tuesday afternoon. "
          "The Bell Hotel confirms it independently, and adds that a man telephoned from Wren's Hollow at twenty "
          "past four to find out. Only one person in the house is worse off when that sealed letter is opened."),
    ("sub", "Two — the route and the clock (C-1, C-2, C-6, C-8, C-9)"),
    ("p", "The pantry stair was bolted from ten past four to five to five, so the killer came down the hatch from "
          "the yard, and the damp prints say the yard was wet when they did. Fisk is with the carter, in his "
          "sight, from 4.26 to 4.44. Quill is in his chair at 4.15 and again at 4.40, seen both times. Bram is on "
          "the telephone until 4.33 and nowhere after it. Pell is alone in the kitchen — and she is the one "
          "person the missing letter was written to help."),
    ("sub", "Three — the measurements (C-10, C-11)"),
    ("p", "The print is 9¼ inches, smooth sole, stitched welt, crescent of wear on the outer right heel. "
          "Pell's shoes are the wrong length and the wrong heel and they are dry. Fisk's and Pryor's are cleated "
          "rubber and far too big. Quill's boots are dry with dust across the laces. The spare yard shoes are "
          "clogs and have not been off the shelf. One pair in the house matches on all four points, and its "
          "owner's overshoes are missing from a dust-free oval on the hall rail and standing full of water at the "
          "top of the hatch steps."),
    ("h", "The three honest red herrings, and why they are fair"),
    ("li", "MRS PELL bolted the door that sealed Rook in, was alone for twenty-five minutes with the yard door "
           "propped open, and owed the money. All true, all on her card. But the paper that was taken was "
           "addressed to her and was the only thing in the world that would have got her £412 back."),
    ("li", "MISS FISK was out in the rain and her boots are still wet, which is the first thing anybody says "
           "out loud. Her boots are cleated rubber and two and a quarter inches too long, and a carter who has "
           "nothing to do with any of it watched her for eighteen minutes."),
    ("li", "DR QUILL asked the dead man what he would take for the freehold, wrote the figure down and never "
           "mentioned it. He is also the one who heard the killer cross the yard."),
    ("h", "If your table got it wrong"),
    ("p", "There are only two documents you can walk past and still lose this: C-3, the flyleaf, which is the "
          "only thing that tells you a fourth paper ever existed; and the last line of C-1, which is the "
          "refolding. Everything else can be missed and the answer still arrives."),
]
