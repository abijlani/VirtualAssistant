# Tuesday Nov 3, 2026 FULL morning pass (fired 6:13 AM CST).
# Overnight verified (16h trash-inclusive): Monday's late tail = failure 11:14 PM +
# NAs 11:15/11:16 PM -> MONDAY CLOSES 8-9-3 (twenty events, busiest weekday on the
# ledger; nine NAs in one day). Tuesday opened silent. cc-state EMPTY.
# Monday evening delivered: Hubler report + Lakeland case study SENT 6:11 PM (Laura/
# Alex/LeVarr + team cc); Nortec proposal SENT 5:09 PM (Steve + Tyler cc Jr) with
# price movement. Nortec demo notes: 300 customers, ripping out Cairo (13+s dead
# air), DECISION WITHIN 48 HOURS; still owed: SpectrumVoIP live number + NetSapiens
# onboarding doc. Illia catch-up: Bodhi takes over Illia's 6 open PRs; ConnectWise
# blocked on Jeff Ogden creds (Junior asked Fri); Pipedrive finishing today/tmrw.
# Drafts folder now EMPTY - Tim + Racquel bracket drafts gone unsent (day fifteen).
# Pagebakers requested changes this morning on Bodhi's #1073 and #1080 (screenshots
# + React fixes). Sahiti (Drive Capital) said yes to the Ora intro Monday night.
# Calendar: Tue 10h (Izzy 10, Onboarding 11, Iris 1, TTT 2, Parr PT 3:30 + drives);
# Fri gained Mike and Bodhi 11-12; Nov 11 gained Ellie x Caroline 10:30; Nov 12
# Friendsgiving 6-9 PM needsAction (out of chart). Chart rolls Tue Nov 3 - Mon Nov 9.
# SUBSTRING HAZARDS: 'weekday thirteen' x2 ('day thirteen'); 'opening-Sunday
# fourteen' ('day fourteen') -> Tim bumps anchored; next: 'day fifteen' is clean.
import re

p = 'page-template.html'
s = open(p, encoding='utf-8').read()

def rep(old, new, n):
    global s
    c = s.count(old)
    assert c == n, f"rep {old[:70]!r}: expected {n}, found {c}"
    s = s.replace(old, new)

def rx(pat, new, n, flags=0):
    global s
    s, c = re.subn(pat, new, s, flags=flags)
    assert c == n, f"rx {pat[:70]!r}: expected {n}, replaced {c}"

def splice(a, b, new, incl_b=False):
    global s
    i0 = s.find(a)
    assert i0 >= 0, f"splice start missing: {a[:60]!r}"
    i1 = s.find(b, i0)
    assert i1 > i0, f"splice end missing: {b[:60]!r}"
    if incl_b: i1 += len(b)
    s = s[:i0] + new + s[i1:]

# ---------- 1. GLOBAL AGE BUMPS (highest first) ----------
rep('day fifty-seven', 'day fifty-eight', 3)                  # #799
rep('day fifty-six', 'day fifty-seven', 3)                    # Eric / Izzy trio
rep('night forty-nine', 'night fifty', 2)
rep('day forty-eight;', 'day forty-nine;', 1)                 # JDs
rep('fifty-one days past', 'fifty-two days past', 2)
rep('forty-one days past', 'forty-two days past', 1)          # Appulse
rep('nineteen days past', 'twenty days past', 5)              # ProGraphix
rep('Nineteen days past', 'Twenty days past', 1)
rep('(nineteen days)', '(twenty days)', 3)
rx(r'(?<!Sun)day fourteen', 'day fifteen', 4)                 # Tim ('opening-Sunday fourteen' stays)
rep('Thirteen days past the promise', 'Fourteen days past the promise', 1)
rep('Iris, day twenty-two', 'Iris, day twenty-three', 1)
rep('hr-nda is 77 days old', 'hr-nda is 78 days old', 1)
rep('Ages as of Nov 2', 'Ages as of Nov 3', 1)
rep('is four days past due (Oct 29)', 'is five days past due (Oct 29)', 2)

def chip1(m): return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
rx(r'(class="chip old">)(\d+)(d</span>)', chip1, 2)
rx(r'(class="chip old">)(\d+)(d &mdash;)', chip1, 3)

# ---------- 2. STAMPS / HEADER ----------
rep('2026-11-02T21:10:00-06:00', '2026-11-03T06:50:00-06:00', 2)
rep('<b>Brief compiled</b> Mon 6:55 AM &middot; data checked Mon 9:10 PM CT',
    '<b>Brief compiled</b> Tue 6:50 AM &middot; data checked Tue 6:50 AM CT', 1)
rep('Monday, November 2 &middot; 2026', 'Tuesday, November 3 &middot; 2026', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)

# ---------- 3. MASTHEAD ----------
m0 = s.find('The Friday blast is converting:')
m1 = s.find('No reactions saved.</p>', m0) + len('No reactions saved.</p>')
assert 0 < m0 < m1
s = s[:m0] + (
 'Monday delivered. <b>Two of Friday&rsquo;s three deliverables shipped at 6:11 PM</b> &mdash; the '
 'Hubler performance report and the Lakeland case study went to Laura, Alex and LeVarr with the full '
 'team copied &mdash; and <b>the Nortec demo turned into a proposal the same day</b> (sent 5:09 PM to '
 'Steve and Tyler, with movement on price). The demo notes raise the stakes: Nortec runs 300 '
 'customers, is actively ripping out Cairo AI (thirteen-plus seconds of dead air on transfers; they '
 'halted their own demos), and <b>wants a decision within 48 hours</b>. Still owed from the call: '
 '<b>the SpectrumVoIP live number</b> for Steve&rsquo;s latency test and <b>the NetSapiens onboarding '
 'doc</b> &mdash; send both this morning; the clock likely runs out tomorrow. Monday also set a record '
 'the other way: <b>closed 8&ndash;9&ndash;3</b> &mdash; twenty events, the busiest weekday on the '
 'ledger, nine needs-attention in one day. Today is the week&rsquo;s wall: <b>ten hours from 10</b> '
 '&mdash; Izzy at 10, <b>Voxtell AI Onboarding at 11</b>, <b>Iris at 1</b> (the invoice is five days '
 'past due &mdash; raise it), TTT at 2, Parr PT at 3:30. Also new: you took over <b>Illia&rsquo;s six '
 'open PRs</b>, Pagebakers requested changes on <b>#1073 and #1080</b> this morning, and the <b>Tim '
 'and Racquel drafts vanished from Drafts unsent</b> &mdash; the written record is back to zero on day '
 'fifteen. Carried: <b>the Cathy call</b> (twenty days past) and <b>the CCI booking</b>. No reactions '
 'saved.</p>'
) + s[m1:]

# ---------- 4. LEDGER: close Monday + open Tuesday ----------
rep('a seventh failure at 7:14 &mdash; <b>7&ndash;7&ndash;3 by 9:10, window open</b>, quiet since 7:14.',
    'a seventh failure at 7:14, then a late-night tail &mdash; an eighth failure at 11:14 and two '
    'needs-attention at 11:15 and 11:16. <b>Monday closes 8&ndash;9&ndash;3</b> &mdash; twenty events, '
    'the busiest weekday on the ledger (the old record was thirteen) and nine needs-attention in one '
    'day, verified Tuesday morning with trash included; the 10 PM close never ran. Tuesday opened '
    'silent &mdash; nothing by 6:50, window open.', 1)

# ---------- 5. "Needs a decision" note ----------
rep('ProGraphix is twenty days past its submit-by date with the drafted reply deleted unsent &mdash; 10/23 passed silent &mdash; Monday is a damage-control call to Cathy',
    'Nortec decides within 48 hours &mdash; the live number and onboarding doc go out before the 10 AM wall', 1)

# ---------- 6. TODAY SCHEDULE ----------
rep('The booked day is done &mdash; evening open; Tuesday runs ten hours from 10 AM',
    'Ten hours booked from 10 &mdash; the pre-10 morning is the only pocket', 1)
i0 = s.find('<div class="card sched" id="todaysched">')
assert i0 > 0
i0 = s.find('>', i0) + 1
i1 = s.find('</section>', i0)
assert i1 > i0
s = s[:i0] + ('\n'
 '        <div class="slot free"><div class="t">Before 10</div><div class="w">Open &mdash; the Nortec sends<small>The SpectrumVoIP live number + the onboarding doc; then the #1073 / #1080 rework screenshots</small></div></div>\n'
 '        <div class="slot"><div class="t">10:00&ndash;2:00</div><div class="w">DW (Client + Admin + Sales)<small>The client block &mdash; three calls sit inside it</small></div></div>\n'
 '        <div class="slot"><div class="t">10:00&ndash;10:30</div><div class="w">Izzy Weekly Checkin<small>Inside the block &mdash; the Levitt verdict is still owed on iz-10dlc</small></div></div>\n'
 '        <div class="slot"><div class="t">11:00&ndash;12:00</div><div class="w">Voxtell AI Onboarding<small>New &mdash; landed off the blast week</small></div></div>\n'
 '        <div class="slot"><div class="t">1:00&ndash;2:00</div><div class="w">Iris Training with Bodhi<small>The invoice is five days past due &mdash; raise it here if it hasn&rsquo;t cleared</small></div></div>\n'
 '        <div class="slot"><div class="t">2:00&ndash;3:00</div><div class="w">Transition, Talking, Triage<small>The Cathy call fits here</small></div></div>\n'
 '        <div class="slot"><div class="t">3:00&ndash;5:30</div><div class="w">Parr PT, with the drives<small>Drive 3, PT 3:30&ndash;4:45, back by 5:30</small></div></div>\n'
 '        <div class="slot free"><div class="t">After 5:30</div><div class="w">Open evening<small>Recovery &mdash; the day ran ten hours</small></div></div>\n'
 '      </div>\n    '
) + s[i1:]

# ---------- 7. TOP 5 ----------
rep('<span class="note">Customer replies first, then the promised job descriptions</span>',
    '<span class="note">The Nortec clock first &mdash; then Cathy and the Spectrum chases</span>', 1)

# li1: ProGraphix -> Nortec 48h
splice('<h4>ProGraphix &mdash; twenty days past &mdash; UGM is over and the thread is still silent</h4>',
       '</div></li>',
 '<h4>Nortec decides within 48 hours &mdash; the proposal is out; the live number and onboarding doc are still owed</h4>\n'
 '          <p class="why">Monday&rsquo;s demo (Jr joined) reset the stakes: <b>Nortec runs 300 '
 'customers over thirty years and is actively turning Cairo AI off</b> &mdash; thirteen-plus seconds '
 'of dead air on simple transfers, customer demos halted &mdash; and Steve wants a replacement '
 'decision <b>within 48 hours</b>. He pushed back on price, and <b>the proposal went out the same '
 'evening (5:09 PM, Steve + Tyler)</b> with movement on it. Two asks from the call are still '
 'unanswered: <b>the SpectrumVoIP live number</b> he wants to dial for a real-world latency check, and '
 '<b>the NetSapiens onboarding document</b> he wants to review before committing. Both are '
 'five-minute sends &mdash; before the 10 AM wall. Also still unbooked from the booth list: <b>Michael '
 'at CCI asked for a call, not an email</b>.</p>\n'
 '          <div class="meta"><span class="pill crit">Decision inside 48h</span><span class="pill good">Proposal sent Mon 5:09 PM</span></div>\n'
 '        ')

# li2 Tim: drafts gone
rep('Friday&rsquo;s blast reached fifteen booth leads, but these two drafts didn&rsquo;t move &mdash; both still sit with bracket placeholders. Today: fill the brackets and send.',
    'And overnight the Drafts folder went empty: <b>both bracket drafts are gone, with no send on '
    'either thread</b>. The written record now has to be rewritten from scratch &mdash; day fifteen.', 1)
rep('<span class="pill warn">Draft unsent &middot; day fifteen</span>',
    '<span class="pill warn">Drafts deleted &middot; day fifteen</span>', 1)

# li3 Hubler -> shipped
splice('<h4>Hubler moved from an email to deliverables: the performance report and the Lakeland case study are yours</h4>',
       '</p>',
 '<h4>Two of Friday&rsquo;s three deliverables shipped Monday night &mdash; what&rsquo;s left is the Jeff chase and the invoice</h4>\n'
 '          <p class="why"><b>The Hubler performance report and the Lakeland case study went out '
 'Monday 6:11 PM</b> to Laura, Alex and LeVarr, with Jason, Jake, Grayson and Jr copied &mdash; two of '
 'the three session deliverables, done on day one. What remains points at one person: <b>Jeff at '
 'Spectrum</b> &mdash; the mail-server follow-up (agent emails must send from a SpectrumVoIP address) '
 'and, from Monday&rsquo;s Illia catch-up, <b>ConnectWise access credentials</b> (Junior asked him '
 'Friday, Illia has chased twice; the integration is blocked on it). Today&rsquo;s 1 PM session is the '
 'natural place to push both &mdash; and the <b>$5,000 invoice is five days past due (Oct 29) &mdash; '
 'no payment confirmation has landed</b>.</p>', incl_b=True)
rep('<span class="pill warn">Two reports owed &middot; set Friday</span>',
    '<span class="pill good">Reports sent Mon 6:11 PM</span>', 1)

# li4: leads -> Cathy
splice('<h4>Two live leads walked up to the booth &mdash; CCI (AppDirect) and Dynalink</h4>',
       '</div></li>',
 '<h4>ProGraphix &mdash; twenty days past &mdash; the thread has outlived its conference</h4>\n'
 '          <p class="why">Cathy needed everything by mid-October to hold 10/23 for the table cover '
 'and banner; her follow-up is still unanswered, the drafted reply was deleted unsent, and nothing has '
 'moved on the thread since Oct 14. Monday&rsquo;s window came and went again. If the material (or the '
 'relationship) still matters, this is a phone call, not an email &mdash; <b>today&rsquo;s TTT hour at '
 '2 is the slot</b>. Twenty days past, and every day makes the call harder.</p>\n'
 '          <div class="meta"><span class="pill crit">Twenty days past due</span><span class="pill warn">Call, not email &middot; TTT at 2</span></div>\n'
 '        ')

# li5: reviews
splice('<h4>#799 at day fifty-eight &mdash; and the review queue grew to four this morning</h4>',
       '</div></li>',
 '<h4>#799 at day fifty-eight &mdash; and you took over Illia&rsquo;s six open PRs</h4>\n'
 '          <p class="why">Monday&rsquo;s catch-up settled it: Eelco is buried, so <b>you review and '
 'test Illia&rsquo;s six self-tested PRs</b> to unblock the merges (his Pipedrive integration &mdash; '
 'OAuth tested on a real account, no marketplace approval needed &mdash; finishes today or tomorrow). '
 'On top: <b>Pagebakers requested changes on your #1073 and #1080 this morning</b> &mdash; both want '
 'UI verification (recordings/screenshots), #1080 also React fixes &mdash; and #886, #991 and #992 '
 'still wait on you. #799 itself is double-approved and unmerged at day fifty-eight. <b>The next '
 'engineering block is Thursday 8:30&ndash;12:30</b>; the rework screenshots fit the pre-10 pocket '
 'today.</p>\n'
 '          <div class="meta"><span class="pill warn">Six PRs + two reworks</span><span class="pill quiet">Next DW: Thu 8:30</span></div>\n'
 '        ')

# ---------- 8. FLAG 1 (Today) ----------
f0 = s.find('<h3><span class="pill warn">Today</span> Monday &mdash; the follow-through week opens, and the blast already converted</h3>')
f1 = s.find('</p>', f0) + len('</p>')
assert 0 < f0 < f1
s = s[:f0] + (
 '<h3><span class="pill warn">Today</span> Ten-hour Tuesday &mdash; and the Nortec clock runs while you&rsquo;re in calls</h3>\n'
 '          <p>The pre-10 pocket is the only open ground: <b>send Steve the SpectrumVoIP live number '
 'and the NetSapiens onboarding doc</b> (his 48-hour decision likely lands tomorrow), then the '
 '#1073/#1080 rework screenshots. From 10 the day runs itself: Izzy at 10 (the Levitt verdict is still '
 'owed), <b>Onboarding at 11</b>, <b>Iris at 1</b> &mdash; push the invoice (five days past due) and '
 'the Jeff items (mail-server config, ConnectWise credentials) &mdash; TTT at 2 (<b>the Cathy call</b> '
 'fits here, twenty days), then Parr PT with the drives, back by 5:30. Evening is recovery.</p>'
) + s[f1:]

# ---------- 9. FLAG 2 (On the wire) ----------
rep('<h3><span class="pill warn">On the wire</span> UGM loose ends &mdash; plus two new wires from Friday&rsquo;s session</h3>',
    '<h3><span class="pill warn">On the wire</span> The Jeff chases, Pipedrive, and the UGM loose ends</h3>', 1)
w0 = s.find('<p><b>UGM wrapped Thursday</b>')
w1 = s.find('</p>', w0) + len('</p>')
assert 0 < w0 < w1
s = s[:w0] + (
 '<p>Everything open at Spectrum now routes through <b>Jeff</b>: the mail-server follow-up from '
 'Friday&rsquo;s session (agent emails must send from a SpectrumVoIP address) and <b>ConnectWise '
 'access credentials</b> (Junior asked Friday, Illia has chased twice &mdash; the integration is '
 'blocked; your move is a nudge to Junior or a direct ask in today&rsquo;s 1 PM session). '
 '<b>Pipedrive finishes today or tomorrow</b> &mdash; Illia&rsquo;s OAuth is testing on a real account '
 'and needs no marketplace approval, unlike HubSpot and Salesforce (still waiting on partner '
 'paperwork). On the UGM tail: <b>a $500 LiveKit charge went through Sunday night with a receipt</b> '
 '&mdash; the uncharged-invoices notice may be clearing itself; worth one look at the billing console '
 'to confirm. The <b>booth bill</b> is still unconfirmed either way, the <b>Whova three</b> (Vipin '
 'Gupta, Nunnally Torres with Hydnrazl Gutierrez, Matthew Abraham) are still waiting, and the '
 'GPT-Live BAA call is still Jr&rsquo;s. One warm thread worth a minute: <b>Sahiti at Drive Capital '
 'said yes Monday night</b> to meeting your Gevity friend behind Ora &mdash; the intro email is yours '
 'to make.</p>'
) + s[w1:]

# ---------- 10. MARKERS ----------
k0 = s.find('<h4 style="font-size:14px">The week&rsquo;s markers</h4>')
assert k0 > 0
k1 = s.find('<p', k0)
k2 = s.find('</p>', k1) + len('</p>')
assert 0 < k1 < k2
s = s[:k1] + (
 '<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Monday closed <b>8&ndash;9&ndash;3 '
 '&mdash; twenty events, the busiest weekday on the ledger</b> (the old record was thirteen) and nine '
 'needs-attention in a single day, all on one thread. Against that: <b>two of Friday&rsquo;s three '
 'deliverables shipped Monday night, and the Nortec proposal is out on a 48-hour decision clock</b>. '
 'The next engineering block is <b>Thu Nov 5, 8:30&ndash;12:30</b>.</p>'
) + s[k2:]

# ---------- 11. COMING-UP week card ----------
c0 = s.find('<h4 style="font-size:14px">This week &mdash; the conversions stack onto a ten-hour Tuesday</h4>')
c1 = s.find('</p>', c0) + len('</p>')
assert 0 < c0 < c1
s = s[:c0] + (
 '<h4 style="font-size:14px">This week &mdash; today is the wall; Friday gained a call</h4>\n'
 '          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">Today: <b>ten hours</b> &mdash; '
 'Izzy 10, Onboarding 11, <b>Iris 1&ndash;2</b>, TTT 2, Parr PT 3:30 with the drives. Wednesday '
 '(7.25h): SA 9:30, HOLD 10:30, <b>Taylor kickoff 11&ndash;1 + GamifyOS 1&ndash;3</b>, pickup 4. '
 'Thursday: <b>DW Engineering 8:30&ndash;12:30</b> (the review stack&rsquo;s window), Scott at 4. '
 'Friday: <b>Mike and Bodhi 11&ndash;12</b> &mdash; new. The weekend is clear. Next week: sync Mon 8, '
 'Hand and Stone Mon 8 PM, <b>Monthly Iris Sync Tue Nov 10, 9</b>, Izzy Nov 10, <b>Ellie &times; '
 'Caroline &times; Taylor Wed Nov 11, 10:30</b> ahead of the moved engineering block (11&ndash;3), '
 'Scott again Thu Nov 12 at 2, and a <b>Friendsgiving social Thu 6&ndash;9 PM</b> (invite unaccepted '
 '&mdash; out of the chart). Carried: <b>the Cathy call</b> (twenty days), <b>the Tim record</b> (day '
 'fifteen, drafts deleted), <b>the CCI booking</b>, the Jeff chases, the review queue (#886, #991, '
 '#992, #799 + Illia&rsquo;s six), the Whova trio, and the <b>invoice &mdash; five days past due</b>.</p>'
) + s[c1:]

# ---------- 12. INBOX LEAD ----------
splice('The blast is converting: <b>Steve Myhre at Nortec booked a demo',
       'the 1:30&ndash;3:30 gap after Nortec is today&rsquo;s pocket.',
 'Monday evening was a shipping night: <b>the Hubler report and Lakeland case study went to the '
 'Spectrum team at 6:11 PM</b>, and <b>the Nortec proposal followed Steve&rsquo;s demo the same day '
 '(5:09 PM, Tyler copied)</b> &mdash; still owed there: the live test number and the onboarding doc. '
 'A warm loop opened too: you wrote <b>Sahiti at Drive Capital</b> about your Gevity friend&rsquo;s '
 'startup (Ora), and she answered within two hours &mdash; &ldquo;happy to chat&rdquo; &mdash; so '
 '<b>the intro email is yours to make</b>. This morning <b>Pagebakers requested changes on #1073 and '
 '#1080</b> (UI recordings/screenshots; React fixes on #1080). And a quiet loss: <b>the Drafts folder '
 'is empty</b> &mdash; the Tim record and the Racquel reply are gone unsent. Still needing words: '
 '<b>Cathy at ProGraphix</b> (twenty days), <b>the CCI booking</b>, and the <b>Whova three</b> &mdash; '
 'the pre-10 pocket is today&rsquo;s only open ground.', incl_b=True)

# ---------- 13. IRIS CARD ----------
splice('Friday&rsquo;s session delivered: <b>Ask Iris demoed live</b>',
       ' lmccree is in the Voxtell Linear workspace',
 'Friday&rsquo;s session delivered (Ask Iris live on 1,880 calls at 89.1%, trial moved to 14 days, '
 'two-call onboarding cadence) &mdash; and <b>you shipped its two big deliverables Monday 6:11 PM</b>: '
 'the Hubler performance report and the Lakeland case study, to Laura, Alex and LeVarr with the full '
 'team copied. Still open from the session: <b>the Jeff mail-server follow-up</b> (agent emails must '
 'send from a SpectrumVoIP address) and the Revio billing-trigger validation on Laura&rsquo;s side; '
 'from Monday&rsquo;s Illia catch-up, <b>ConnectWise is blocked on Jeff Ogden&rsquo;s credentials</b> '
 'too. <b>The next session is today, 1&ndash;2</b> &mdash; raise the <b>invoice (five days past due)</b> '
 'and both Jeff items there; the <b>Monthly Iris Sync lands Nov 10, 9&ndash;9:30</b>.', incl_b=True)

# ---------- 14. CHART: roll to Tue Nov 3 - Mon Nov 9 ----------
rep('Mon Nov 2 &ndash; Sun Nov 8', 'Tue Nov 3 &ndash; Mon Nov 9', 1)
plot0 = s.find('<div class="plot" id="plot">')
c0 = s.find('<div class="bar">', plot0)
cx = s.find('<div class="xaxis"', plot0)
c1 = s.rfind('</div>', c0, cx)
assert 0 < plot0 < c0 < c1 < cx
s = s[:c0] + (
 '<div class="bar"><div class="tot" style="bottom:calc(71.43% + 6px)">10</div>\n'
 '            <div class="seg m" style="height:35.71%"></div><div class="seg f" style="height:35.71%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(51.79% + 6px)">7.25</div>\n'
 '            <div class="seg m" style="height:41.07%"></div><div class="seg f" style="height:7.14%"></div><div class="seg p" style="height:3.57%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(39.29% + 6px)">5.5</div>\n'
 '            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:32.14%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(7.14% + 6px)">1</div>\n'
 '            <div class="seg m" style="height:7.14%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(48.21% + 6px)">6.75</div>\n'
 '            <div class="seg m" style="height:5.36%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:7.14%"></div></div>\n'
 '        '
) + s[c1:]
rep('<div><b>Mon</b>2</div><div><b>Tue</b>3</div>\n          <div><b>Wed</b>4</div><div><b>Thu</b>5</div><div><b>Fri</b>6</div><div><b>Sat</b>7</div><div><b>Sun</b>8</div>',
    '<div><b>Tue</b>3</div><div><b>Wed</b>4</div>\n          <div><b>Thu</b>5</div><div><b>Fri</b>6</div><div><b>Sat</b>7</div><div><b>Sun</b>8</div><div><b>Mon</b>9</div>', 1)

# ---------- SANITY ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-03T06:50:00-06:00') == 2
assert s.count('window open') == 2
assert len(re.findall(r'(?<!Sun)day fourteen', s)) == 0
assert 'nineteen days' not in s and 'four days past due' not in s
assert 'Good evening' not in s and 'Monday, November 2' not in s
assert 'Mon Nov 2 &ndash; Sun Nov 8' not in s
assert 'Nortec booked &mdash; today 1 PM' not in s
assert 'quoter' not in s
assert 'PasswordReset' not in s and 'billcenter.net' not in s and 'Jose Luiz' not in s
assert '5WY67Sa2' not in s and 'pY3DM73R' not in s and 'bT5uDhjRSBk3' not in s
assert 'doxy.me/scottvlmft' not in s

open(p, 'w', encoding='utf-8').write(s)
print('tuesday full ok', len(s))
