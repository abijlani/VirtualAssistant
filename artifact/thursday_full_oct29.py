# Thursday Oct 30... no — Thursday Oct 29, 2026 — FULL morning pass (UGM final day).
# Wednesday closed 9F/0NA/3S (two morning minutes + the Bullock evening burst).
# Thursday opened with a SUCCESS pair at 7:11 AM (0-0-2). Overnight: Whova booth
# report counts 55 leads. New today: "Call Lori to set up a call with Ken" 3:30-3:45
# (Bodhi created 5:42 AM, sits inside the 3:30-4 Reserved block). New Wed Nov 4:
# Ashlyn/Taylor/Bodhi Kick Off 11-1 (Taylor Davis / wildlysatisfied), overlapping
# DW Project Engineering 11-3 -> Wed Nov 4 now 8.5h with a collision. Hubler reply
# to Laura is DRAFTED but unsent (asks for partner contact). Tim drafts still unsent
# => day ten. No Cathy motion => fifteen days past. Iris $5,000 invoice due TODAY.
# Chart rolls Thu 29 - Wed Nov 4. cc-state empty.
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
rep('day fifty-two', 'day fifty-three', 3)                   # #799
rep('day fifty-one', 'day fifty-two', 3)                     # Eric / Izzy trio
rep('day forty-three;', 'day forty-four;', 1)                # JDs
rep('forty-six days past', 'forty-seven days past', 2)
rep('night forty-four', 'night forty-five', 2)
rep('thirty-six days past', 'thirty-seven days past', 1)     # Appulse
rep('fourteen days past', 'fifteen days past', 6)            # ProGraphix
rep('Fourteen days past', 'Fifteen days past', 1)
rep('(fourteen days)', '(fifteen days)', 2)
rep('day nine', 'day ten', 5)                                # Tim ('day ninet' == 0 checked)
rep('Eight days past the promise', 'Nine days past the promise', 1)
rep('Iris, day seventeen', 'Iris, day eighteen', 1)
rep('hr-nda is 72 days old', 'hr-nda is 73 days old', 1)
rep('Ages as of Oct 28', 'Ages as of Oct 29', 1)
rep('due tomorrow, Oct 29', 'due today, Oct 29', 2)

def chip1(m): return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
rx(r'(class="chip old">)(\d+)(d</span>)', chip1, 2)
rx(r'(class="chip old">)(\d+)(d &mdash;)', chip1, 3)

# ---------- date turn ----------
rep('2026-10-28T22:08:00-05:00', '2026-10-29T07:40:00-05:00', 2)
rep('Wednesday, October 28 &middot; 2026', 'Thursday, October 29 &middot; 2026', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)
rep('<b>Brief compiled</b> Wed 7:40 AM &middot; data checked Wed 10:08 PM CT',
    '<b>Brief compiled</b> Thu 7:40 AM &middot; data checked Thu 7:40 AM CT', 1)

# ---------- masthead (full replace) ----------
m0 = s.find('Tuesday closed <b>5&ndash;0&ndash;3</b>')
m1 = s.find('No reactions saved.</p>', m0) + len('No reactions saved.</p>')
assert 0 < m0 < m1
s = s[:m0] + (
 'Wednesday closed <b>9&ndash;0&ndash;3</b> &mdash; the heaviest failure day since Sunday, nearly all of it in '
 'the Bullock evening (five failures 6:11&ndash;6:52). Overnight the conference paid out a number: <b>the Whova '
 'booth report counts 55 leads</b>. Today is <b>UGM&rsquo;s final day, and the lightest</b>: booth '
 '7:30&ndash;10:30, lunch 12&ndash;1, Scott at 2, a 3:30 call you added this morning (Lori, to set up a call with '
 'Ken), then the week&rsquo;s <b>first open afternoon, 4 to 8</b>, before <b>Hand and Stone at 8</b>. The queue '
 'for that afternoon: <b>send the Hubler reply</b> (drafted yesterday, still in drafts), <b>the Cathy call</b> '
 '(fifteen days past), <b>the Tim record on day ten</b>, and the 55-lead export. The Iris <b>$5,000 invoice is '
 'due today</b>. New on the calendar: <b>the Taylor kickoff landed</b> &mdash; Ashlyn/Taylor/Bodhi, Wed Nov 4 '
 '11&ndash;1, on top of the engineering block. Thursday opened with a success pair at 7:11. No reactions saved.</p>'
) + s[m1:]

# ---------- ledger: Thursday opener ('window open' 1 -> 2) ----------
rep('Wednesday closes 9&ndash;0&ndash;3 &mdash; the heaviest failure day since Sunday, all of it in two morning minutes and the Bullock evening.',
    'Wednesday closes 9&ndash;0&ndash;3 &mdash; the heaviest failure day since Sunday, all of it in two morning '
    'minutes and the Bullock evening. Thursday opened the other way: <b>a success pair at 7:11 AM</b> &mdash; '
    '0&ndash;0&ndash;2 by 7:40, window open.', 1)

# ---------- today schedule ----------
rep('13h booked &mdash; UGM day three: booth till 4, Bullock reception at 6',
    '7.75h booked &mdash; UGM final day: booth till 10:30, open 4&ndash;8, Hand and Stone at 8', 1)
i0 = s.find('<div class="card sched" id="todaysched">')
assert i0 > 0
i0 = s.find('>', i0) + 1
i1 = s.find('</section>', i0)
assert i1 > i0
s = s[:i0] + ('\n'
 '        <div class="slot past"><div class="t">7:00&ndash;7:30</div><div class="w">UGM Breakfast<small>the final day opens</small></div></div>\n'
 '        <div class="slot"><div class="t">7:30&ndash;10:30</div><div class="w">UGM Booth Time<small>Moontower &mdash; the last booth block of UGM</small></div></div>\n'
 '        <div class="slot"><div class="t">12:00&ndash;1:00</div><div class="w">UGM Lunch</div></div>\n'
 '        <div class="slot"><div class="t">1:30&ndash;2:00</div><div class="w">Reserved</div></div>\n'
 '        <div class="slot"><div class="t">2:00&ndash;3:00</div><div class="w">Call with Scott Van Camp<small>doxy.me link on the invite</small></div></div>\n'
 '        <div class="slot"><div class="t">3:30&ndash;4:00</div><div class="w">Reserved + the Lori call<small>3:30&ndash;3:45: call Lori to set up a call with Ken &mdash; added this morning, inside the Reserved half-hour</small></div></div>\n'
 '        <div class="slot free"><div class="t">4:00&ndash;8:00</div><div class="w">Open afternoon &mdash; the first of UGM week<small>queue: send the Hubler draft, the Cathy call (fifteen days), the Tim record (day ten), the Whova 55-lead export</small></div></div>\n'
 '        <div class="slot"><div class="t">8:00&ndash;9:00</div><div class="w">Hand and Stone<small>booked Tuesday night &mdash; closes the conference</small></div></div>\n'
 '      </div>\n    '
) + s[i1:]

# ---------- top 5 ----------
rep('two UGM days have gone by with the thread silent',
    'the whole UGM week has gone by with the thread silent', 1)
rep('It is a from-the-floor call now: the 4&ndash;6 gap before the Bullock reception is today&rsquo;s opening, and after Thursday the week is gone.',
    'Today is the last UGM day and the afternoon is open from 4 &mdash; the call happens today or the week is gone.', 1)
rep('UGM is here: the 4&ndash;6 gap today or Thursday&rsquo;s Reserved blocks are the realistic slots.',
    'UGM ends today and the afternoon is open from 4 &mdash; both drafts are still sitting unsent; fill the brackets and send.', 1)
rep('This is the Iris customer asking directly, in week three of the engagement; a reply with a proposed time beats a perfect plan. The 4&ndash;6 pocket today or Thursday&rsquo;s Reserved blocks fit.',
    'This is the Iris customer asking directly, in week three of the engagement &mdash; and <b>a reply is already '
    'drafted</b> (it asks Laura for the Hubler contact&rsquo;s name and email and promises the call-error dig): it '
    'has sat in drafts since yesterday morning. Send it in the open afternoon.', 1)
rep('<span class="pill crit">New ask &middot; Tue 11:54 AM</span>',
    '<span class="pill crit">Reply drafted &middot; unsent</span>', 1)
rep('Both are captured in Granola; the follow-up emails are post-UGM sends &mdash; Friday or Monday.',
    'Both are captured in Granola, and this morning&rsquo;s <b>Whova booth report counts 55 leads</b> behind them; '
    'the follow-up emails are post-UGM sends &mdash; tomorrow or Monday.', 1)

# ---------- flags ----------
f0 = s.find('<h3><span class="pill warn">Today</span> UGM day three &mdash; the second 13-hour day, and the pocket has a queue</h3>')
f1 = s.find('</p>', f0) + len('</p>')
assert 0 < f0 < f1
s = s[:f0] + (
 '<h3><span class="pill warn">Today</span> UGM final day &mdash; booth ends at 10:30, and the week&rsquo;s first open afternoon follows</h3>\n'
 '          <p>Booth <b>7:30&ndash;10:30</b> at Moontower, lunch 12&ndash;1, Reserved 1:30, <b>Scott at 2</b>, and '
 'the <b>3:30 Lori call</b> (to set up a call with Ken &mdash; added this morning, inside the Reserved '
 'half-hour). Then <b>open from 4 to 8</b>: the first unclaimed afternoon of UGM week. Four things want it '
 '&mdash; <b>the Hubler reply</b> (drafted, unsent), <b>the Cathy call</b> (fifteen days past), <b>the Tim '
 'record</b> (day ten), and the <b>Whova work</b> (three waiting contacts, plus the 55-lead export). <b>Hand and '
 'Stone at 8</b> closes the conference.</p>'
) + s[f1:]

rep('booth time ran 7:30&ndash;4 Tuesday and runs again today &mdash; <b>13-hour days</b> once the evening events are counted (Banger&rsquo;s Tuesday, the Bullock Museum reception Wednesday) &mdash; and Thursday holds booth till 10:30, Scott at 2, two Reserved blocks and <b>Hand and Stone at 8</b>;',
    'booth time ran 7:30&ndash;4 Tuesday and Wednesday (13-hour days with Banger&rsquo;s and the Bullock) and '
    '<b>today closes at 10:30</b> &mdash; Scott at 2, two Reserved blocks and <b>Hand and Stone at 8</b>;', 1)
rep('BillCenter resets Thursday, unconfirmed', 'BillCenter resets this evening, unconfirmed', 1)

# ---------- markers card ----------
rep('Monday closed 4&ndash;1&ndash;4 and Tuesday repeated the shape at 5&ndash;0&ndash;3 (a Banger&rsquo;s-hour burst, quiet by 6:44). <b>UGM runs through Thursday</b> (Austin): today and Wednesday are 13-hour booth days, Thursday holds Scott at 2, Friday the Gevity pizza party and <b>the Iris session at 2</b>.',
    'Wednesday closed 9&ndash;0&ndash;3 &mdash; the heaviest day since Sunday, nearly all of it in the Bullock '
    'evening. <b>UGM ends today</b>: booth till 10:30, then the first open afternoon of the week; Friday brings '
    'the Gevity pizza party and <b>the Iris session at 2</b>.', 1)

# ---------- coming-up card ----------
c0 = s.find('Today &mdash; UGM day three: booth, then the Bullock')
c1 = s.find('</p>', c0) + len('</p>')
assert 0 < c0 < c1
s = s[:c0] + (
 'Today &mdash; UGM final day: booth till 10:30, then the week opens up</h4>\n'
 '          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">Booth 7:30&ndash;10:30, lunch 12&ndash;1, '
 'Reserved 1:30, <b>Scott at 2</b>, the 3:30 Lori call, <b>open 4&ndash;8</b>, <b>Hand and Stone at 8</b>. '
 'Carried in: <b>the Hubler draft to send</b>, <b>the Cathy call</b> (fifteen days past), <b>the Tim record</b> '
 '(day ten), the review queue (#886, #991, #992, #799), the <b>Whova trio + 55-lead export</b>, and the '
 'CCI/Dynalink follow-up sends (tomorrow or Monday). The Iris <b>$5,000 invoice is due today</b>. <b>New: the '
 'Taylor kickoff</b> (Ashlyn/Taylor/Bodhi) landed Wed Nov 4, 11&ndash;1 &mdash; on top of the 11&ndash;3 '
 'engineering block; that day now reads 8.5h with a collision.</p>'
) + s[c1:]

# ---------- inbox panel ----------
rep('New in the queue: <b>Laura&rsquo;s Hubler ask</b> (Tue 11:54 AM, needs a reply with a proposed time) and the <b>CCI follow-up</b> (Michael wants a call next week).',
    'New in the queue: <b>the Whova booth report &mdash; 55 leads</b> to export, while <b>Laura&rsquo;s Hubler ask '
    'has a drafted reply sitting unsent</b> (it asks for the partner contact) and the <b>CCI follow-up</b> '
    '(Michael wants a call next week) is a tomorrow-or-Monday send.', 1)
rep('the 4&ndash;6 gap before the Bullock reception is today&rsquo;s pocket. ',
    'the open afternoon from 4 is today&rsquo;s pocket &mdash; the first free one of UGM week. ', 1)

# ---------- week chart: roll to Thu Oct 29 - Wed Nov 4 ----------
rep('Wed Oct 28 &ndash; Tue Nov 3', 'Thu Oct 29 &ndash; Wed Nov 4', 1)
plot0 = s.find('<div class="plot" id="plot">')
c0 = s.find('<div class="bar">', plot0)
cx = s.find('<div class="xaxis"', plot0)
c1 = s.rfind('</div>', c0, cx)
assert 0 < plot0 < c0 < c1 < cx
s = s[:c0] + (
 '<div class="bar"><div class="tot" style="bottom:calc(55.36% + 6px)">7.75</div>\n'
 '            <div class="seg m" style="height:48.21%"></div><div class="seg f" style="height:7.14%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(14.29% + 6px)">2</div>\n'
 '            <div class="seg m" style="height:14.29%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(41.07% + 6px)">5.75</div>\n'
 '            <div class="seg m" style="height:5.36%"></div><div class="seg f" style="height:35.71%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(55.36% + 6px)">7.75</div>\n'
 '            <div class="seg m" style="height:19.64%"></div><div class="seg f" style="height:35.71%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(60.71% + 6px)">8.5</div>\n'
 '            <div class="seg m" style="height:21.43%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:3.57%"></div></div>\n'
 '        '
) + s[c1:]
rep('<div><b>Wed</b>28</div><div><b>Thu</b>29</div>\n          <div><b>Fri</b>30</div><div><b>Sat</b>31</div><div><b>Sun</b>1</div><div><b>Mon</b>2</div><div><b>Tue</b>3</div>',
    '<div><b>Thu</b>29</div><div><b>Fri</b>30</div>\n          <div><b>Sat</b>31</div><div><b>Sun</b>1</div><div><b>Mon</b>2</div><div><b>Tue</b>3</div><div><b>Wed</b>4</div>', 1)

# ---------- sanity ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-10-29T07:40:00-05:00') == 2
assert s.count('window open') == 2
assert s.count('UGM day three') == 0
assert s.count('fourteen days') == 0 and s.count('day nine') == 0
assert s.count('due tomorrow') == 0 and s.count('due today, Oct 29') == 2
assert 'PasswordReset' not in s and 'billcenter.net' not in s and 'Jose Luiz' not in s
assert '5WY67Sa2' not in s and 'pY3DM73R' not in s and 'bT5uDhjRSBk3' not in s
assert 'doxy.me/scottvlmft' not in s

open(p, 'w').write(s)
print('thursday turn ok', len(s))
