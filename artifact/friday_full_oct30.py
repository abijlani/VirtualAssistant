# Friday Oct 30, 2026 — FULL morning pass (first post-UGM day).
# Thursday closed 6F/0NA/4S. Friday opened with a failure pair 7:15/7:21 AM.
# NEW: Taylor (hello@wildlysatisfied.com) booked a GamifyOS Working Session
# Wed Nov 4 1-3 PM on top of the 11-1 Kick Off -> Nov 4 is now 10.5h and the
# DW (Project Engineering) 11-3 block is fully double-booked. Hubler reply draft
# UNSENT (two days). Tim drafts unsent => day eleven. No Cathy motion => sixteen
# days. Iris $5,000 invoice was due YESTERDAY (Oct 29) — no payment confirmation.
# Today: Gevity pizza 12:30-1:30, Iris session 2-3, rest open. Chart rolls
# Fri 30 - Thu Nov 5. cc-state empty.
import re

p = 'page-template.html'
s = open(p).read()

def rep(old, new, n):
    global s
    assert s.count(old) == n, f"{old!r}: {s.count(old)} != {n}"
    s = s.replace(old, new)

def rx(pat, new, n, flags=0):
    global s
    s, c = re.subn(pat, new, s, flags=flags)
    assert c == n, f"{pat!r}: {c} != {n}"

# ---------- global age bumps FIRST (higher numbers before lower) ----------
rep('day fifty-three', 'day fifty-four', 3)                  # #799
rep('day fifty-two', 'day fifty-three', 3)                   # Eric / Izzy trio
rep('day forty-four;', 'day forty-five;', 1)                 # JDs
rep('forty-seven days past', 'forty-eight days past', 2)
rep('night forty-five', 'night forty-six', 2)
rep('thirty-seven days past', 'thirty-eight days past', 1)   # Appulse
rep('fifteen days past', 'sixteen days past', 6)             # ProGraphix
rep('Fifteen days past', 'Sixteen days past', 1)
rep('(fifteen days)', '(sixteen days)', 2)
rep('day ten', 'day eleven', 5)                              # Tim
rep('Nine days past the promise', 'Ten days past the promise', 1)
rep('Iris, day eighteen', 'Iris, day nineteen', 1)
rep('hr-nda is 73 days old', 'hr-nda is 74 days old', 1)
rep('Ages as of Oct 29', 'Ages as of Oct 30', 1)
rep('$5,000 invoice is due today, Oct 29',
    '$5,000 invoice was due yesterday, Oct 29 &mdash; no payment confirmation has landed', 2)

def chip1(m): return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
rx(r'(class="chip old">)(\d+)(d</span>)', chip1, 2)
rx(r'(class="chip old">)(\d+)(d &mdash;)', chip1, 3)

# ---------- date turn ----------
rep('2026-10-29T22:08:00-05:00', '2026-10-30T07:35:00-05:00', 2)
rep('Thursday, October 29 &middot; 2026', 'Friday, October 30 &middot; 2026', 1)
rep('<b>Brief compiled</b> Thu 7:40 AM &middot; data checked Thu 10:08 PM CT',
    '<b>Brief compiled</b> Fri 7:35 AM &middot; data checked Fri 7:35 AM CT', 1)

# ---------- masthead (full replace) ----------
m0 = s.find('Wednesday closed <b>9&ndash;0&ndash;3</b>')
m1 = s.find('No reactions saved.</p>', m0) + len('No reactions saved.</p>')
assert 0 < m0 < m1
s = s[:m0] + (
 'Thursday closed <b>6&ndash;0&ndash;4</b> and UGM is over &mdash; a morning success pair, eleven silent hours '
 '(the longest quiet stretch in weeks), then a dinner-hour burst. Today is <b>the recovery day and the send-out '
 'day</b>: the pizza party at 12:30, <b>the Iris session at 2</b>, and everything else open &mdash; the first '
 'working morning in two weeks. The queue: <b>send the Hubler reply</b> (drafted Wednesday, still in drafts, and '
 'it promises action &ldquo;right after UGM&rdquo; &mdash; that is now), <b>the Cathy call</b> (sixteen days '
 'past), <b>the Tim record on day eleven</b>, the <b>CCI and Dynalink follow-up sends</b>, and the 55-lead '
 'export. The Iris <b>$5,000 invoice was due yesterday</b> with no payment confirmation in sight. And <b>Taylor '
 'doubled down on Wednesday</b>: a GamifyOS working session Nov 4, 1&ndash;3, on top of the 11&ndash;1 kickoff '
 '&mdash; that day is now 10.5 hours and the engineering block under it is gone. Friday opened with a failure '
 'pair at 7:15. No reactions saved.</p>'
) + s[m1:]

# ---------- ledger: Friday opener ('window open' 1 -> 2) ----------
rep('Thursday closes 6&ndash;0&ndash;4 &mdash; a mirror of the UGM pattern: one morning pair, silence all day, everything else in the evening after the conference ended.',
    'Thursday closes 6&ndash;0&ndash;4 &mdash; a mirror of the UGM pattern: one morning pair, silence all day, '
    'everything else in the evening after the conference ended. Friday opened with <b>a failure pair at 7:15 and '
    '7:21 AM</b> &mdash; 2&ndash;0&ndash;0 by 7:35, window open.', 1)

# ---------- today schedule ----------
rep('7.75h booked &mdash; UGM final day: booth till 10:30, open 4&ndash;8, Hand and Stone at 8',
    '2h booked &mdash; post-UGM recovery day: pizza at 12:30, Iris at 2, the rest open', 1)
i0 = s.find('<div class="card sched" id="todaysched">')
assert i0 > 0
i0 = s.find('>', i0) + 1
i1 = s.find('</section>', i0)
assert i1 > i0
s = s[:i0] + ('\n'
 '        <div class="slot free"><div class="t">7:30&ndash;12:30</div><div class="w">Open morning &mdash; the first post-UGM block<small>queue: send the Hubler draft, the Cathy call (sixteen days), the Tim record (day eleven), the CCI/Dynalink follow-ups, the 55-lead export</small></div></div>\n'
 '        <div class="slot"><div class="t">12:30&ndash;1:30</div><div class="w">Gevity Pizza Party<small>Sammataro &mdash; member social</small></div></div>\n'
 '        <div class="slot"><div class="t">2:00&ndash;3:00</div><div class="w">Iris Training with Bodhi<small>the series resumes &mdash; Laura and team; invoice and Hubler both belong on this call</small></div></div>\n'
 '        <div class="slot free"><div class="t">3:00&ndash;</div><div class="w">Open afternoon<small>overflow from the morning queue</small></div></div>\n'
 '      </div>\n    '
) + s[i1:]

# ---------- top 5 ----------
rep('the whole UGM week has gone by with the thread silent',
    'UGM is over and the thread is still silent', 1)
rep('Today is the last UGM day and the afternoon is open from 4 &mdash; the call happens today or the week is gone.',
    'UGM is over and the morning is wide open &mdash; if the table cover and banner still matter, today is the day the call happens.', 1)
rep('UGM ends today and the afternoon is open from 4 &mdash; both drafts are still sitting unsent; fill the brackets and send.',
    'UGM is over and the day is wide open &mdash; both drafts are still sitting unsent; fill the brackets and send.', 1)
rep('it has sat in drafts since yesterday morning. Send it in the open afternoon.',
    'it has sat in drafts for two days, and it promises action &ldquo;right after UGM&rdquo; &mdash; that is now. '
    'Send it this morning, before the 2 PM session with Laura.', 1)
rep('the follow-up emails are post-UGM sends &mdash; tomorrow or Monday.',
    'the follow-up emails are due now &mdash; today while the booth conversations are fresh, or Monday at the latest.', 1)

# ---------- flags ----------
f0 = s.find('<h3><span class="pill warn">Today</span> UGM final day &mdash; booth ends at 10:30, and the week&rsquo;s first open afternoon follows</h3>')
f1 = s.find('</p>', f0) + len('</p>')
assert 0 < f0 < f1
s = s[:f0] + (
 '<h3><span class="pill warn">Today</span> The recovery day is also the send-out day</h3>\n'
 '          <p>Two events: <b>the Gevity pizza party 12:30&ndash;1:30</b> and <b>the Iris session 2&ndash;3</b> '
 '&mdash; the rest is the first open working day in two weeks. Five sends want the morning: <b>the Hubler '
 'reply</b> (drafted Wednesday, promises action right after UGM), <b>the Cathy call</b> (sixteen days past), '
 '<b>the Tim record</b> (day eleven), <b>the CCI and Dynalink follow-ups</b> (booth conversations go stale over '
 'a weekend), and the <b>Whova work</b> (three waiting contacts, the 55-lead export, and the attendee list '
 '&mdash; Whova sent an updated link overnight). The Iris <b>invoice chase</b> starts today too.</p>'
) + s[f1:]

f0 = s.find('booth time ran 7:30&ndash;4 Tuesday and Wednesday')
f1 = s.find('</p>', f0) + len('</p>')
assert 0 < f0 < f1
s = s[:f0] + (
 'UGM wrapped Thursday</b> &mdash; Whova sent the thank-you and an updated <b>attendee-list link</b> overnight, '
 'on top of the booth report&rsquo;s 55 leads. Still on the wire: <b>LiveKit&rsquo;s uncharged-invoices '
 'notice</b> and the GPT-Live BAA answer (Jr&rsquo;s call), and the booth-bill payment (the BillCenter reset '
 'was Thursday evening &mdash; still unconfirmed either way). The Whova three are still waiting: Vipin Gupta '
 '(Tragofone), Nunnally Torres with Hydnrazl Gutierrez (.ppl Solutions), and Matthew Abraham. And the calendar '
 'moved under Wednesday: <b>Taylor&rsquo;s GamifyOS working session (Nov 4, 1&ndash;3) landed on top of the '
 'kickoff (11&ndash;1)</b>, burying the 11&ndash;3 engineering block &mdash; Nov 4 now reads 10.5h; if the '
 'engineering block matters that week, it has to move.</p>'
) + s[f1:]
# fix the orphaned lead-in bold for flag2 (it began '<b>The UGM schedule filled in' before)
rep('<b>The UGM schedule filled in</b>: UGM wrapped Thursday</b>', '<b>UGM wrapped Thursday</b>', 1)
rep('<h3><span class="pill warn">This week</span> UGM takes this week &mdash; today through Thursday in Austin</h3>',
    '<h3><span class="pill warn">On the wire</span> UGM wrapped &mdash; and Wednesday&rsquo;s calendar moved underneath you</h3>', 1)

# ---------- markers card ----------
rep('Wednesday closed 9&ndash;0&ndash;3 &mdash; the heaviest day since Sunday, nearly all of it in the Bullock evening. <b>UGM ends today</b>: booth till 10:30, then the first open afternoon of the week; Friday brings the Gevity pizza party and <b>the Iris session at 2</b>.',
    'Thursday closed 6&ndash;0&ndash;4 and <b>UGM is over</b> &mdash; four 13-to-9-hour days, 55 booth leads, two '
    'named prospects. Today: the pizza party at 12:30 and <b>the Iris session at 2</b>, the rest open.', 1)

# ---------- coming-up card ----------
c0 = s.find('Today &mdash; UGM final day: booth till 10:30, then the week opens up')
c1 = s.find('</p>', c0) + len('</p>')
assert 0 < c0 < c1
s = s[:c0] + (
 'Today &mdash; post-UGM: two events, the rest is yours</h4>\n'
 '          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">Gevity pizza 12:30&ndash;1:30, <b>Iris '
 'session 2&ndash;3</b>, open morning and afternoon around them. Carried in: <b>the Hubler draft to send</b>, '
 '<b>the Cathy call</b> (sixteen days past), <b>the Tim record</b> (day eleven), the <b>CCI/Dynalink sends</b>, '
 'the review queue (#886, #991, #992, #799), and the <b>Whova trio + 55-lead export</b>. The Iris <b>invoice '
 'was due yesterday</b> &mdash; chase it on today&rsquo;s session. Ahead: the weekend is clear (AI Implementation '
 'Club Sunday is still unaccepted), Monday holds the product sync and the 10&ndash;2 engineering block, and '
 '<b>Wednesday Nov 4 is now 10.5h</b> &mdash; Taylor&rsquo;s kickoff 11&ndash;1 plus the GamifyOS working session '
 '1&ndash;3 sit squarely on the 11&ndash;3 engineering block.</p>'
) + s[c1:]

# ---------- inbox panel ----------
rep('New in the queue: <b>the Whova booth report &mdash; 55 leads</b> to export, while <b>Laura&rsquo;s Hubler ask has a drafted reply sitting unsent</b> (it asks for the partner contact) and the <b>CCI follow-up</b> (Michael wants a call next week) is a tomorrow-or-Monday send.',
    'New overnight: <b>Taylor booked the GamifyOS pair</b> (kickoff Nov 4 11&ndash;1, working session 1&ndash;3) '
    'and <b>Whova sent the wrap + an updated attendee-list link</b>. Still queued: <b>the Hubler reply</b> '
    '(drafted two days ago, unsent), the <b>CCI and Dynalink follow-ups</b> (due today or Monday), and the '
    '<b>55-lead export</b>.', 1)
rep('the open afternoon from 4 is today&rsquo;s pocket', 'the open morning is today&rsquo;s pocket &mdash; the first post-UGM block', 1)

# ---------- Iris card ----------
rep('The next session is Fri Oct 30, 2&ndash;3 (the Tuesday slot falls in UGM week), then Tue Nov 3, 1&ndash;2.',
    'The next session is <b>today, 2&ndash;3</b>, then Tue Nov 3, 1&ndash;2 &mdash; today&rsquo;s agenda: the '
    'invoice (a day past due), the Hubler outreach, and the Revio billing build.', 1)

# ---------- week chart: roll to Fri Oct 30 - Thu Nov 5 ----------
rep('Thu Oct 29 &ndash; Wed Nov 4', 'Fri Oct 30 &ndash; Thu Nov 5', 1)
plot0 = s.find('<div class="plot" id="plot">')
c0 = s.find('<div class="bar">', plot0)
cx = s.find('<div class="xaxis"', plot0)
c1 = s.rfind('</div>', c0, cx)
assert 0 < plot0 < c0 < c1 < cx
s = s[:c0] + (
 '<div class="bar"><div class="tot" style="bottom:calc(14.29% + 6px)">2</div>\n'
 '            <div class="seg m" style="height:14.29%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(41.07% + 6px)">5.75</div>\n'
 '            <div class="seg m" style="height:5.36%"></div><div class="seg f" style="height:35.71%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(55.36% + 6px)">7.75</div>\n'
 '            <div class="seg m" style="height:19.64%"></div><div class="seg f" style="height:35.71%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(75% + 6px)">10.5</div>\n'
 '            <div class="seg m" style="height:35.71%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:3.57%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(42.86% + 6px)">6</div>\n'
 '            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:35.71%"></div></div>\n'
 '        '
) + s[c1:]
rep('<div><b>Thu</b>29</div><div><b>Fri</b>30</div>\n          <div><b>Sat</b>31</div><div><b>Sun</b>1</div><div><b>Mon</b>2</div><div><b>Tue</b>3</div><div><b>Wed</b>4</div>',
    '<div><b>Fri</b>30</div><div><b>Sat</b>31</div>\n          <div><b>Sun</b>1</div><div><b>Mon</b>2</div><div><b>Tue</b>3</div><div><b>Wed</b>4</div><div><b>Thu</b>5</div>', 1)

# ---------- sanity ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-10-30T07:35:00-05:00') == 2
assert s.count('window open') == 2
assert s.count('UGM final day') == 0 and s.count('UGM ends today') == 0
assert s.count('fifteen days') == 0 and s.count('day ten') == 0
assert s.count('due today, Oct 29') == 0
assert 'PasswordReset' not in s and 'billcenter.net' not in s and 'Jose Luiz' not in s
assert '5WY67Sa2' not in s and 'pY3DM73R' not in s and 'bT5uDhjRSBk3' not in s
assert 'doxy.me/scottvlmft' not in s

open(p, 'w').write(s)
print('friday turn ok', len(s))
