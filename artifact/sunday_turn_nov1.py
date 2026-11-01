# Sunday Nov 1, 2026 weekend date turn (hourly pass; morning trigger is weekdays-only).
# DST ENDED overnight: CT is now CST (UTC-6) — ISO stamps switch to -06:00.
# Verified: Halloween closed 3F/0NA/0S. Sunday opened with SUCCESSES ONLY — 1:03 AM,
# then a pair at 5:17/5:21 AM (all trashed already) => 0-0-3 by 7:13. New digest name:
# "Great American RV SuperStores" joined Trinity + Lakeland on the Daily Digest list.
# Today: open Sunday; the AI Implementation Club (Gevity, 1-4) is still unaccepted —
# shown on the schedule, excluded from the chart. Chart rolls Sun Nov 1 - Sat Nov 7.
# NOTE for future bumps: 'weekday thirteen' (x2, the Monday record) contains
# 'day thirteen' — anchor Tim bumps accordingly from here on. cc-state empty.
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
rep('day fifty-five', 'day fifty-six', 3)                    # #799
rep('day fifty-four', 'day fifty-five', 3)                   # Eric / Izzy trio
rep('day forty-six;', 'day forty-seven;', 1)                 # JDs
rep('forty-nine days past', 'fifty days past', 2)
rep('night forty-seven', 'night forty-eight', 2)
rep('thirty-nine days past', 'forty days past', 1)           # Appulse
rep('seventeen days past', 'eighteen days past', 5)          # ProGraphix
rep('Seventeen days past', 'Eighteen days past', 1)
rep('(seventeen days)', '(eighteen days)', 3)
rep('day twelve', 'day thirteen', 4)                         # Tim ('weekday thirteen' x2 pre-exists)
rep('Eleven days past the promise', 'Twelve days past the promise', 1)
rep('Iris, day twenty', 'Iris, day twenty-one', 1)
rep('hr-nda is 75 days old', 'hr-nda is 76 days old', 1)
rep('Ages as of Oct 31', 'Ages as of Nov 1', 1)
rep('is two days past due (Oct 29)', 'is three days past due (Oct 29)', 2)

def chip1(m): return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
rx(r'(class="chip old">)(\d+)(d</span>)', chip1, 2)
rx(r'(class="chip old">)(\d+)(d &mdash;)', chip1, 3)

# ---------- 2. STAMPS / HEADER (DST: -06:00 from here on) ----------
rep('2026-10-31T22:07:00-05:00', '2026-11-01T07:13:00-06:00', 2)
rep('<b>Brief compiled</b> Sat 8:08 AM &middot; data checked Sat 10:07 PM CT',
    '<b>Brief compiled</b> Sun 7:13 AM &middot; data checked Sun 7:13 AM CT', 1)
rep('Saturday, October 31 &middot; 2026', 'Sunday, November 1 &middot; 2026', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)

# ---------- 3. MASTHEAD ----------
m0 = s.find('Friday earned its send-out-day name')
m1 = s.find('No reactions saved.</p>', m0) + len('No reactions saved.</p>')
assert 0 < m0 < m1
s = s[:m0] + (
 'Halloween closed <b>3&ndash;0&ndash;0</b> &mdash; ten clean hours, then three evening failures and not one '
 'success. Sunday opened the other way: <b>successes only</b> &mdash; one at 1:03 AM, a pair at 5:17 and 5:21 '
 '(all already cleared to trash). A small new signal in the digests: <b>Great American RV SuperStores</b> joined '
 'Trinity and Lakeland on the Daily Digest list. Today is the usual recovery Sunday; the one decision is the '
 '<b>unaccepted AI Implementation Club, 1&ndash;4 at Gevity</b> &mdash; accept it or let it pass. Monday opens '
 'the follow-through week: Product Sync at 8, <b>DW Engineering 10&ndash;2</b>, and the carry &mdash; <b>the '
 'Cathy call</b> (eighteen days past), <b>the Tim record on day thirteen</b>, <b>the CCI call booking</b>, the '
 'Hubler confirm, and the Iris <b>invoice chase, three days past due</b>. The clocks fell back overnight. No '
 'reactions saved.</p>'
) + s[m1:]

# ---------- 4. LEDGER: Sunday opener ----------
rep('Saturday Oct 24 stays the only clean day on record.',
    'Saturday Oct 24 stays the only clean day on record. Sunday opened with successes only &mdash; <b>1:03 AM, '
    'then a pair at 5:17 and 5:21</b> &mdash; 0&ndash;0&ndash;3 by 7:13, window open.', 1)

# ---------- 5. TODAY SCHEDULE ----------
rep('Nothing booked &mdash; Halloween Saturday; Monday opens with the Product Sync at 8',
    'Open Sunday &mdash; one unaccepted invite at 1; the week starts Monday at 8', 1)
i0 = s.find('<div class="card sched" id="todaysched">')
assert i0 > 0
i0 = s.find('>', i0) + 1
i1 = s.find('</section>', i0)
assert i1 > i0
s = s[:i0] + ('\n'
 '        <div class="slot free"><div class="t">Morning</div><div class="w">Open &mdash; the usual recovery Sunday</div></div>\n'
 '        <div class="slot"><div class="t">1:00&ndash;4:00</div><div class="w">The AI Implementation Club<small>Gevity, in person &mdash; invite still unaccepted; stays out of the chart until it isn&rsquo;t</small></div></div>\n'
 '        <div class="slot free"><div class="t">After 4</div><div class="w">Open evening<small>Monday opens with the Product Sync at 8 and the 10&ndash;2 engineering block</small></div></div>\n'
 '      </div>\n    '
) + s[i1:]

# ---------- 6. CHART: roll to Sun Nov 1 - Sat Nov 7 ----------
rep('Sat Oct 31 &ndash; Fri Nov 6', 'Sun Nov 1 &ndash; Sat Nov 7', 1)
plot0 = s.find('<div class="plot" id="plot">')
c0 = s.find('<div class="bar">', plot0)
cx = s.find('<div class="xaxis"', plot0)
c1 = s.rfind('</div>', c0, cx)
assert 0 < plot0 < c0 < c1 < cx
s = s[:c0] + (
 '<div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(41.07% + 6px)">5.75</div>\n'
 '            <div class="seg m" style="height:5.36%"></div><div class="seg f" style="height:35.71%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(55.36% + 6px)">7.75</div>\n'
 '            <div class="seg m" style="height:19.64%"></div><div class="seg f" style="height:35.71%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(75% + 6px)">10.5</div>\n'
 '            <div class="seg m" style="height:35.71%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:3.57%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(42.86% + 6px)">6</div>\n'
 '            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:35.71%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '        '
) + s[c1:]
rep('<div><b>Sat</b>31</div><div><b>Sun</b>1</div>\n          <div><b>Mon</b>2</div><div><b>Tue</b>3</div><div><b>Wed</b>4</div><div><b>Thu</b>5</div><div><b>Fri</b>6</div>',
    '<div><b>Sun</b>1</div><div><b>Mon</b>2</div>\n          <div><b>Tue</b>3</div><div><b>Wed</b>4</div><div><b>Thu</b>5</div><div><b>Fri</b>6</div><div><b>Sat</b>7</div>', 1)

# ---------- 7. FLAGS ----------
f0 = s.find('<h3><span class="pill warn">Today</span> Halloween Saturday &mdash; nothing booked, and Friday&rsquo;s scorecard is mostly green</h3>')
f1 = s.find('</p>', f0) + len('</p>')
assert 0 < f0 < f1
s = s[:f0] + (
 '<h3><span class="pill warn">Today</span> Recovery Sunday &mdash; one decision: the 1 PM build session</h3>\n'
 '          <p>The <b>AI Implementation Club</b> (Gevity, in person, 1&ndash;4) is still unaccepted &mdash; '
 'accept it or let it pass; it stays out of the chart either way. Otherwise the day is open. Monday carries the '
 'real load: Product Sync at 8, <b>DW Engineering 10&ndash;2</b>, TTT 2&ndash;3, and the queue lands on it '
 '&mdash; <b>the Cathy call</b> (eighteen days), <b>the Tim record</b> (day thirteen), <b>the CCI call '
 'booking</b>, <b>the Hubler confirm</b>, and the <b>invoice chase</b> (three days past due).</p>'
) + s[f1:]

# ---------- 8. MARKERS ----------
rep('Friday closed 7&ndash;0&ndash;2 &mdash; spotless until evening, then five failures 7:25&ndash;9:04, the twenty-first straight weekday-evening burst. <b>The follow-up blast shipped Friday evening</b>; the weekend is open.',
    'Halloween closed 3&ndash;0&ndash;0 (three evening failures, no successes) and Sunday opened with successes '
    'only. <b>The follow-up blast shipped Friday evening</b>; Monday starts the follow-through week.', 1)

# ---------- 9. COMING-UP ----------
rep('Nothing booked today; Sunday holds only the unaccepted AI Implementation Club (1&ndash;4).',
    'Today holds only the unaccepted AI Implementation Club (1&ndash;4).', 1)
rep('The weekend &mdash; open; then a loaded week', 'Sunday &mdash; one invite; then a loaded week', 1)

# ---------- SANITY ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-01T07:13:00-06:00') == 2
assert s.count('window open') == 2
assert s.count('Sat Oct 31 &ndash;') == 0
assert s.count('seventeen days') == 0 and s.count('day twelve') == 0
assert 'Good evening' not in s and 'Halloween Saturday' not in s
assert 'PasswordReset' not in s and 'billcenter.net' not in s and 'Jose Luiz' not in s
assert '5WY67Sa2' not in s and 'pY3DM73R' not in s and 'bT5uDhjRSBk3' not in s

open(p, 'w', encoding='utf-8').write(s)
print('sunday turn ok', len(s))
