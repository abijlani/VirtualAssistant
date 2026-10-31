# Saturday Oct 31, 2026 weekend date turn (hourly pass; the morning trigger is weekdays-only).
# Verified facts: the UGM follow-up blast went OUT Friday 6:13-6:27 PM CT — 15+ personalized
# sends off the 55-lead export (Dynalink's David 6:17, Reo/UnitedCloud on Telzino, demo asks
# from YOVU, TruLeap, GeoStar, SumoFiber, Nortec, Stratus, CyberNet, Globalgig, Telin,
# TELCLOUD, Threshold, Will/ITVoice, mbrinkman/team-meta...). NO send to lmathwig in 2d and
# the Hubler draft is GONE from drafts => deleted or superseded (likely covered live in
# Friday's 2 PM Iris session) — confirm Monday. Tim + Racquel drafts still sitting => day
# twelve. No Cathy motion => seventeen days. Iris invoice two days past due. Friday closed
# 7F/0NA/2S (five evening failures 7:25-9:04); overnight quiet; Saturday opened clean.
# Halloween: nothing booked today. Chart rolls Sat 31 - Fri Nov 6. cc-state empty.
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

# ---------- 1. GLOBAL AGE BUMPS (highest first) ----------
rep('day fifty-four', 'day fifty-five', 3)                   # #799
rep('day fifty-three', 'day fifty-four', 3)                  # Eric / Izzy trio
rep('day forty-five;', 'day forty-six;', 1)                  # JDs
rep('forty-eight days past', 'forty-nine days past', 2)
rep('night forty-six', 'night forty-seven', 2)
rep('thirty-eight days past', 'thirty-nine days past', 1)    # Appulse
rep('sixteen days past', 'seventeen days past', 6)           # ProGraphix
rep('Sixteen days past', 'Seventeen days past', 1)
rep('(sixteen days)', '(seventeen days)', 2)
rep('day eleven', 'day twelve', 5)                           # Tim
rep('Ten days past the promise', 'Eleven days past the promise', 1)
rep('Iris, day nineteen', 'Iris, day twenty', 1)
rep('hr-nda is 74 days old', 'hr-nda is 75 days old', 1)
rep('Ages as of Oct 30', 'Ages as of Oct 31', 1)
rep('was due yesterday, Oct 29 &mdash; no payment confirmation has landed',
    'is two days past due (Oct 29) &mdash; no payment confirmation has landed', 2)

def chip1(m): return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
rx(r'(class="chip old">)(\d+)(d</span>)', chip1, 2)
rx(r'(class="chip old">)(\d+)(d &mdash;)', chip1, 3)

# ---------- 2. STAMPS / HEADER ----------
rep('2026-10-30T22:07:00-05:00', '2026-10-31T08:08:00-05:00', 2)
rep('<b>Brief compiled</b> Fri 7:35 AM &middot; data checked Fri 10:07 PM CT',
    '<b>Brief compiled</b> Sat 8:08 AM &middot; data checked Sat 8:08 AM CT', 1)
rep('Friday, October 30 &middot; 2026', 'Saturday, October 31 &middot; 2026', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)

# ---------- 3. MASTHEAD ----------
m0 = s.find('Thursday closed <b>6&ndash;0&ndash;4</b>')
m1 = s.find('No reactions saved.</p>', m0) + len('No reactions saved.</p>')
assert 0 < m0 < m1
s = s[:m0] + (
 'Friday earned its send-out-day name: <b>the UGM follow-up blast went out between 6:13 and 6:27 PM</b> &mdash; '
 'fifteen-plus personalized emails off the 55-lead export, <b>Dynalink&rsquo;s David included</b>, plus demo '
 'requests from YOVU, TruLeap, GeoStar, SumoFiber, Nortec, Stratus, CyberNet, Globalgig, Telin, TELCLOUD, '
 'Threshold and Reo at UnitedCloud (the Telzino user). Then the line answered back: <b>five failures between '
 '7:25 and 9:04 PM</b>, the heaviest evening since the Bullock &mdash; Friday closed <b>7&ndash;0&ndash;2</b>. '
 'The overnight stayed quiet and <b>Saturday opened clean</b>: Halloween, nothing booked. Still carried into '
 'Monday: <b>the Hubler ask</b> (the drafted reply left drafts with no email to Laura sent &mdash; likely '
 'handled live in Friday&rsquo;s session, worth a one-line confirm), <b>the Cathy call</b> (seventeen days '
 'past), <b>the Tim record on day twelve</b>, <b>the CCI call booking</b>, and the Iris <b>$5,000 invoice, two '
 'days past due</b>. No reactions saved.</p>'
) + s[m1:]

# ---------- 4. LEDGER: Saturday opener ----------
rep('the heaviest evening since the Bullock.',
    'the heaviest evening since the Bullock. The overnight into Saturday stayed quiet &mdash; <b>Saturday '
    'opened clean</b>: digests on schedule, no alerts by 8:08 AM &mdash; window open.', 1)

# ---------- 5. TODAY SCHEDULE ----------
rep('2h booked &mdash; post-UGM recovery day: pizza at 12:30, Iris at 2, the rest open',
    'Nothing booked &mdash; Halloween Saturday; Monday opens with the Product Sync at 8', 1)
i0 = s.find('<div class="card sched" id="todaysched">')
assert i0 > 0
i0 = s.find('>', i0) + 1
i1 = s.find('</section>', i0)
assert i1 > i0
s = s[:i0] + ('\n'
 '        <div class="slot free"><div class="t">All day</div><div class="w">Open &mdash; Halloween Saturday<small>nothing on the calendar; Sunday holds only the unaccepted AI Implementation Club 1&ndash;4</small></div></div>\n'
 '      </div>\n    '
) + s[i1:]

# ---------- 6. CHART: roll to Sat Oct 31 - Fri Nov 6 ----------
rep('Fri Oct 30 &ndash; Thu Nov 5', 'Sat Oct 31 &ndash; Fri Nov 6', 1)
plot0 = s.find('<div class="plot" id="plot">')
c0 = s.find('<div class="bar">', plot0)
cx = s.find('<div class="xaxis"', plot0)
c1 = s.rfind('</div>', c0, cx)
assert 0 < plot0 < c0 < c1 < cx
s = s[:c0] + (
 '<div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(41.07% + 6px)">5.75</div>\n'
 '            <div class="seg m" style="height:5.36%"></div><div class="seg f" style="height:35.71%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(55.36% + 6px)">7.75</div>\n'
 '            <div class="seg m" style="height:19.64%"></div><div class="seg f" style="height:35.71%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(75% + 6px)">10.5</div>\n'
 '            <div class="seg m" style="height:35.71%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:3.57%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(42.86% + 6px)">6</div>\n'
 '            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:35.71%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '        '
) + s[c1:]
rep('<div><b>Fri</b>30</div><div><b>Sat</b>31</div>\n          <div><b>Sun</b>1</div><div><b>Mon</b>2</div><div><b>Tue</b>3</div><div><b>Wed</b>4</div><div><b>Thu</b>5</div>',
    '<div><b>Sat</b>31</div><div><b>Sun</b>1</div>\n          <div><b>Mon</b>2</div><div><b>Tue</b>3</div><div><b>Wed</b>4</div><div><b>Thu</b>5</div><div><b>Fri</b>6</div>', 1)

# ---------- 7. TOP 5 ----------
rep('UGM is over and the morning is wide open &mdash; if the table cover and banner still matter, today is the day the call happens.',
    'Friday passed without visible motion &mdash; <b>Monday is the call</b>: seventeen days past, and the thread has now outlived the conference it was for.', 1)
rep('UGM is over and the day is wide open &mdash; both drafts are still sitting unsent; fill the brackets and send.',
    'Friday&rsquo;s blast reached fifteen booth leads, but these two drafts didn&rsquo;t move &mdash; both still sit with bracket placeholders. Monday: fill the brackets and send.', 1)
rep('This is the Iris customer asking directly, in week three of the engagement &mdash; and <b>a reply is already drafted</b> (it asks Laura for the Hubler contact&rsquo;s name and email and promises the call-error dig): it has sat in drafts for two days, and it promises action &ldquo;right after UGM&rdquo; &mdash; that is now. Send it this morning, before the 2 PM session with Laura.',
    'This is the Iris customer asking directly &mdash; and the picture moved Friday: <b>the drafted reply left '
    'drafts, and no email to Laura went out</b>. The likely story is the ask was handled live in Friday&rsquo;s '
    '2 PM session; if not, a customer ask is sitting unanswered on day five. Either way, <b>a one-line confirm '
    'to Laura on Monday</b> closes the loop &mdash; and the call-error dig she flagged still needs an owner.', 1)
rep('<span class="pill crit">Reply drafted &middot; unsent</span>',
    '<span class="pill warn">Draft gone, no send &mdash; confirm Monday</span>', 1)
rep('Both are captured in Granola, and this morning&rsquo;s <b>Whova booth report counts 55 leads</b> behind them; the follow-up emails are due now &mdash; today while the booth conversations are fresh, or Monday at the latest.',
    'Mostly DONE: <b>the follow-up blast went out Friday evening</b> &mdash; David at Dynalink got his at 6:17 '
    'PM, alongside fifteen-plus sends off the 55-lead list. Still open: <b>Michael at CCI asked for a call, not '
    'an email</b>, and no CCI send is visible in the blast &mdash; Monday is the booking window for that call.', 1)
rep('<span class="pill quiet">Dynalink: call intelligence</span>',
    '<span class="pill good">Dynalink: sent Fri 6:17 PM</span>', 1)

# ---------- 8. FLAGS ----------
f0 = s.find('<h3><span class="pill warn">Today</span> The recovery day is also the send-out day</h3>')
f1 = s.find('</p>', f0) + len('</p>')
assert 0 < f0 < f1
s = s[:f0] + (
 '<h3><span class="pill warn">Today</span> Halloween Saturday &mdash; nothing booked, and Friday&rsquo;s scorecard is mostly green</h3>\n'
 '          <p>Zero bookings today. Friday delivered the big one: <b>the UGM follow-up blast went out</b> '
 '(fifteen-plus personalized sends, 6:13&ndash;6:27 PM, off the 55-lead export). What didn&rsquo;t move: <b>the '
 'Cathy call</b> (seventeen days), <b>the Tim record</b> (day twelve, both drafts untouched), <b>the CCI call '
 'booking</b>, and the Hubler email (draft gone, no send &mdash; confirm with Laura Monday). Sunday holds only '
 'the unaccepted AI Implementation Club; <b>Monday opens with the Product Sync at 8 and the 10&ndash;2 '
 'engineering block</b>.</p>'
) + s[f1:]

# ---------- 9. MARKERS ----------
rep('Thursday closed 6&ndash;0&ndash;4 and <b>UGM is over</b> &mdash; four 13-to-9-hour days, 55 booth leads, two named prospects. Today: the pizza party at 12:30 and <b>the Iris session at 2</b>, the rest open.',
    'Friday closed 7&ndash;0&ndash;2 &mdash; spotless until evening, then five failures 7:25&ndash;9:04, the '
    'twenty-first straight weekday-evening burst. <b>The follow-up blast shipped Friday evening</b>; the weekend '
    'is open.', 1)

# ---------- 10. COMING-UP ----------
c0 = s.find('Today &mdash; post-UGM: two events, the rest is yours')
c1 = s.find('</p>', c0) + len('</p>')
assert 0 < c0 < c1
s = s[:c0] + (
 'The weekend &mdash; open; then a loaded week</h4>\n'
 '          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">Nothing booked today; Sunday holds only '
 'the unaccepted AI Implementation Club (1&ndash;4). Monday: Product Sync 8, <b>DW Engineering 10&ndash;2</b>, '
 'TTT 2&ndash;3. Tuesday: Izzy 10, Iris session 1&ndash;2, Parr PT 3:30. <b>Wednesday is the wall: 10.5h</b> '
 '&mdash; Taylor&rsquo;s kickoff 11&ndash;1 plus the GamifyOS session 1&ndash;3 sit on the 11&ndash;3 '
 'engineering block. Thursday: DW 8:30&ndash;12:30, Scott at 4. Carried to Monday: <b>the Cathy call</b> '
 '(seventeen days), <b>the Tim record</b> (day twelve), <b>the CCI call booking</b>, the Hubler confirm, the '
 'review queue (#886, #991, #992, #799), the Whova trio, and the <b>invoice chase &mdash; two days past '
 'due</b>.</p>'
) + s[c1:]

# ---------- 11. INBOX ----------
rep('New overnight: <b>Taylor booked the GamifyOS pair</b> (kickoff Nov 4 11&ndash;1, working session 1&ndash;3) and <b>Whova sent the wrap + an updated attendee-list link</b>. Still queued: <b>the Hubler reply</b> (drafted two days ago, unsent), the <b>CCI and Dynalink follow-ups</b> (due today or Monday), and the <b>55-lead export</b>.',
    'Friday evening delivered: <b>the UGM follow-up blast went out 6:13&ndash;6:27 PM</b> &mdash; fifteen-plus '
    'personalized sends off the 55-lead list, <b>Dynalink included</b>. Still queued: <b>the CCI call '
    'booking</b> (Michael asked for a call; no CCI send is visible in the blast), <b>the Hubler confirm</b> '
    '(the draft left drafts with no email sent), and the <b>Tim record</b>.', 1)
rep('the open morning is today&rsquo;s pocket &mdash; the first post-UGM block', 'Monday morning is the next pocket', 1)

# ---------- 12. IRIS CARD ----------
rep('The next session is <b>today, 2&ndash;3</b>, then Tue Nov 3, 1&ndash;2 &mdash; today&rsquo;s agenda: the invoice (a day past due), the Hubler outreach, and the Revio billing build.',
    'Friday&rsquo;s session has come and gone; the next is <b>Tue Nov 3, 1&ndash;2</b>. The items Friday should '
    'have covered &mdash; the invoice (two days past due) and the Hubler outreach &mdash; need a Monday '
    'confirmation either way.', 1)

# ---------- SANITY ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-10-31T08:08:00-05:00') == 2
assert s.count('window open') == 2
assert s.count('Fri Oct 30 &ndash;') == 0
assert s.count('sixteen days') == 0 and s.count('day eleven') == 0
assert s.count('due yesterday') == 0
assert 'Good evening' not in s
assert 'PasswordReset' not in s and 'billcenter.net' not in s and 'Jose Luiz' not in s
assert '5WY67Sa2' not in s and 'pY3DM73R' not in s and 'bT5uDhjRSBk3' not in s

open(p, 'w', encoding='utf-8').write(s)
print('saturday turn ok', len(s))
