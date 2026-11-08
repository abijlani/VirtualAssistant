# Sunday Nov 8, 2026 weekend date turn (hourly pass; the morning trigger is weekdays-only).
# Verified facts: Saturday closed 3-0-1 (four events) - failures 6:10 AM, 7:09 AM and an
# evening 7:05 PM after eleven quiet hours; success 7:25 AM. Padel happened 3-4:30.
# Overnight into Sunday quiet: failure thread holds at 44, no new alerts by 7:09 AM.
# Sunday calendar: CLEAR - nothing booked. Week unchanged: Mon sync 8 / DW 9-1 with demo
# at 11 inside / Hand and Stone 8 PM; Tue Iris Sync 9 + Izzy 10 + DW Client 10-2;
# Wed 7h; Thu 8.5h; Fri Review Crew 5:30; Sat Nov 14 clear. Chart rolls Sun 8 - Sat 14.
# Overnight inbox routine only (Sentry budget notices, WebinarJam survey) - off page.
# No Tyler/Nortec reply, Tim draft still in Drafts (day twenty today).
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
rep('day sixty-two', 'day sixty-three', 3)                    # #799
rep('day sixty-one', 'day sixty-two', 3)                      # Eric / Izzy trio
rep('night fifty-four', 'night fifty-five', 2)
rep('day fifty-three;', 'day fifty-four;', 1)
rep('fifty-six days past', 'fifty-seven days past', 4)
rep('forty-six days past', 'forty-seven days past', 1)
rep('twenty-four days past', 'twenty-five days past', 2)      # Cathy
rep('Twenty-four days past', 'Twenty-five days past', 2)
rep('(twenty-four days)', '(twenty-five days)', 3)
rep('day nineteen', 'day twenty', 5)                          # Tim
rep('Iris, day twenty-seven', 'Iris, day twenty-eight', 1)
rep('hr-nda is 82 days old', 'hr-nda is 83 days old', 1)
rep('Ages as of Nov 7', 'Ages as of Nov 8', 1)
rep('nine days past due', 'ten days past due', 4)
rep('is three days old', 'is four days old', 1)               # ATS promise

def chip1(m): return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
rx(r'(class="chip old">)(\d+)(d</span>)', chip1, 2)
rx(r'(class="chip old">)(\d+)(d &mdash;)', chip1, 3)

# ---------- 2. STAMPS / HEADER ----------
rep('2026-11-07T21:07:00-06:00', '2026-11-08T07:09:00-06:00', 2)
rep('<b>Brief compiled</b> Sat 7:07 AM &middot; data checked Sat 9:07 PM CT',
    '<b>Brief compiled</b> Sun 7:09 AM &middot; data checked Sun 7:09 AM CT', 1)
rep('Saturday, November 7 &middot; 2026', 'Sunday, November 8 &middot; 2026', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)

# ---------- 3. MASTHEAD ----------
m0 = s.find('Friday delivered the reseller tripleheader')
m1 = s.find('No reactions saved.</p>', m0) + len('No reactions saved.</p>')
assert 0 < m0 < m1
s = s[:m0] + (
 'The weekend is doing its job: Saturday was padel and little else, and the line behaved &mdash; <b>Saturday '
 'closed 3&ndash;0&ndash;1</b> (two early failures, a success, and one evening failure after eleven quiet '
 'hours), and <b>Sunday opened clean</b> with nothing on the calendar. Monday is the gate everything queues '
 'behind: sync at 8, then <b>the new Voxtell AI Demo at 11</b> (Jr and Carlos joining) inside the 9&ndash;1 '
 'engineering block, Hand and Stone at 8 PM. Monday&rsquo;s queue, in order: <b>the Tim Send</b> (day twenty '
 'in Drafts &mdash; one click), <b>the Tyler/Nortec follow-up</b> (Jr&rsquo;s Thursday &ldquo;that '
 'works&rdquo; still has no confirmation or paperwork back), <b>the Cathy call</b> (twenty-five days), <b>the '
 'ATS nudge</b> (promised orders four days overdue), <b>Catherine Weir&rsquo;s reply</b>, and the review '
 'queue. The Iris <b>invoice is ten days past due</b>; Tuesday&rsquo;s Monthly Iris Sync at 9 is the agenda '
 'slot. No reactions saved.</p>'
) + s[m1:]

# ---------- 4. LEDGER: close Saturday, open Sunday ----------
rep('Saturday opened with <b>failures at 6:10 and 7:09 AM</b> and a success at 7:25, then eleven quiet hours '
    'broken by an <b>evening failure at 7:05 PM</b> &mdash; <b>3&ndash;0&ndash;1 by 9:07, window open</b>.',
    'Saturday closed <b>3&ndash;0&ndash;1</b> &mdash; failures at 6:10 and 7:09 AM, a success at 7:25, and an '
    'evening failure at 7:05 PM after eleven quiet hours. The overnight into Sunday stayed quiet &mdash; '
    '<b>Sunday opened clean: no alerts by 7:09 AM, window open</b>.', 1)

# ---------- 5. TODAY NOTE + SCHEDULE ----------
rep('Padel Saturday &mdash; roofed Court 5 at 3, home by 5; otherwise clear',
    'Clear Sunday &mdash; nothing booked; Monday opens with the 8 AM sync and the demo at 11', 1)
i0 = s.find('<div class="card sched" id="todaysched">')
assert i0 > 0
i0 = s.find('>', i0) + 1
i1 = s.find('</section>', i0)
assert i1 > i0
s = s[:i0] + ('\n'
 '        <div class="slot free"><div class="t">All day</div><div class="w">Open &mdash; clear Sunday<small>Nothing on the calendar; Monday opens with the 8 AM sync, the demo at 11 inside the 9&ndash;1 block, and Hand and Stone at 8 PM</small></div></div>\n'
 '      </div>\n    '
) + s[i1:]

# ---------- 6. CHART: roll to Sun Nov 8 - Sat Nov 14 ----------
rep('Sat Nov 7 &ndash; Fri Nov 13', 'Sun Nov 8 &ndash; Sat Nov 14', 1)
plot0 = s.find('<div class="plot" id="plot">')
c0 = s.find('<div class="bar">', plot0)
cx = s.find('<div class="xaxis"', plot0)
c1 = s.rfind('</div>', c0, cx)
assert 0 < plot0 < c0 < c1 < cx
s = s[:c0] + (
 '<div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(48.21% + 6px)">6.75</div>\n'
 '            <div class="seg m" style="height:12.5%"></div><div class="seg f" style="height:28.57%"></div><div class="seg p" style="height:7.14%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(35.71% + 6px)">5</div>\n'
 '            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:28.57%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(50% + 6px)">7</div>\n'
 '            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:3.57%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(60.71% + 6px)">8.5</div>\n'
 '            <div class="seg m" style="height:28.57%"></div><div class="seg f" style="height:32.14%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(10.71% + 6px)">1.5</div>\n'
 '            <div class="seg m" style="height:10.71%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '        '
) + s[c1:]
rep('<div><b>Sat</b>7</div><div><b>Sun</b>8</div>\n          <div><b>Mon</b>9</div><div><b>Tue</b>10</div><div><b>Wed</b>11</div><div><b>Thu</b>12</div><div><b>Fri</b>13</div>',
    '<div><b>Sun</b>8</div><div><b>Mon</b>9</div>\n          <div><b>Tue</b>10</div><div><b>Wed</b>11</div><div><b>Thu</b>12</div><div><b>Fri</b>13</div><div><b>Sat</b>14</div>', 1)

# ---------- 7. FLAG 1 (Today) ----------
f0 = s.find('<span class="pill warn">Today</span> Padel Saturday')
f0 = s.rfind('<h3>', 0, f0)
f1 = s.find('</p>', f0) + len('</p>')
assert 0 < f0 < f1
s = s[:f0] + (
 '<h3><span class="pill warn">Today</span> Clear Sunday &mdash; the queue holds for Monday morning</h3>\n'
 '          <p>Nothing booked today. Monday is the real start: <b>sync at 8</b>, then the 9&ndash;1 engineering '
 'block with <b>the new demo at 11</b> cutting an hour out of it. The queue, in order: <b>the Tim Send</b> (day '
 'twenty), <b>the Tyler/Nortec follow-up</b> (no paperwork yet), <b>the Cathy call</b> (twenty-five days), '
 '<b>the ATS nudge</b> (orders four days overdue), <b>Catherine Weir&rsquo;s reply</b>, and the review queue '
 '(#886, #991, #992, #799, Illia&rsquo;s six, Pipedrive voxai-851). The <b>GamifyOS page and community landing '
 'stay due live Wednesday Nov 12</b>, and the Iris <b>invoice (ten days) belongs on Tuesday&rsquo;s Sync '
 'agenda</b>.</p>'
) + s[f1:]

# ---------- 8. MARKERS ----------
k0 = s.find('The week&rsquo;s markers</h4>')
kp = s.find('<p', k0)
k1 = s.find('</p>', kp) + len('</p>')
assert 0 < k0 < kp < k1
s = s[:kp] + (
 '<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Saturday closed <b>3&ndash;0&ndash;1</b> &mdash; '
 'two early failures, a success, and a lone evening failure after eleven quiet hours; Sunday opened clean. '
 'Friday before it ran 7&ndash;2&ndash;2 with the twenty-sixth straight weekday-evening burst. The pipeline: '
 '<b>Nortec agreed on terms Thursday</b> &mdash; Tyler&rsquo;s confirmation and paperwork still out; <b>both '
 'resellers pitched Friday</b> (Stratus 1,200, GigTel 80,000) &mdash; follow-ups Monday; ATS&rsquo;s promised '
 'orders are four days overdue. <b>The Tim record is drafted and unsent</b> &mdash; one click closes day '
 'twenty. The next engineering block is <b>Monday 9&ndash;1, with the new demo at 11 inside it</b>.</p>'
) + s[k1:]

# ---------- 9. COMING-UP ----------
c0 = s.find('The weekend &mdash; padel today, clear Sunday; then a demo-day Monday and an 8.5-hour Thursday')
c1 = s.find('</p>', c0) + len('</p>')
assert 0 < c0 < c1
s = s[:c0] + (
 'Clear Sunday; then a demo-day Monday and an 8.5-hour Thursday</h4>\n'
 '          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">Today: nothing booked. Monday: sync 8, '
 '<b>DW Engineering 9&ndash;1 with the new Voxtell AI Demo at 11</b> inside it (Jr + Carlos) &mdash; the review '
 'queue&rsquo;s window (#886, #991, #992, #799, Illia&rsquo;s six, Pipedrive voxai-851) &mdash; Hand and Stone '
 '8 PM. Tuesday: <b>Monthly Iris Sync 9</b> (the ten-days-past-due invoice and the drip/report commitments '
 'belong on its agenda), <b>Izzy 10</b> (the Levitt verdict &mdash; and the Tim record, sent by then or on day '
 'twenty-two), DW Client 10&ndash;2. Wednesday: Sustainable Ambition 9:30, Ellie &times; Caroline &times; '
 'Taylor 10:30, DW 11&ndash;3, TTT 3 &mdash; and <b>the GamifyOS page + landing are due live</b>. Thursday '
 'Nov 12 is <b>the week&rsquo;s heaviest at 8.5h, over the 8h line</b>: DW 8:30&ndash;12:30, Scott Van Camp 2, '
 'Reserved 3:30, <b>Friendsgiving 6&ndash;9 PM</b>. Friday Nov 13: Review Crew happy hour 5:30; the following '
 'Saturday is clear. Carried: <b>the Cathy call</b> (twenty-five days), <b>the CCI booking</b>, the drip and '
 'performance reports, the ATS five, the Whova trio, the Sahiti intro, and the <b>invoice &mdash; ten days '
 'past due</b>.</p>'
) + s[c1:]

# ---------- SANITY ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-08T07:09:00-06:00') == 2
assert s.count('window open') == 2
assert s.count('Sat Nov 7 &ndash;') == 0
assert s.count('twenty-four days') == 0 and s.count('day nineteen') == 0
assert s.count('nine days past due') == 0
assert s.count('Padel') == 0 and s.count('padel') == 1  # one mention in masthead recap
assert 'Good evening' not in s
assert 'PasswordReset' not in s and 'billcenter.net' not in s and 'Jose Luiz' not in s
assert '5WY67Sa2' not in s and 'pY3DM73R' not in s and 'bT5uDhjRSBk3' not in s and 'hw7Mh6cK' not in s
assert 'doxy.me' not in s and 'nyg-hguu-mmh' not in s and 'bxe-xdtp-ohs' not in s
assert 'uyt-cgnh-gtz' not in s and 'vqd-jqoy-wsp' not in s
assert 'sfw-mvnn-nfd' not in s and 'cjk-wubx-vna' not in s
assert '3,082' not in s  # LiveKit charge stays off page (Sentry mentions are pre-existing tracked-task content)

open(p, 'w', encoding='utf-8').write(s)
print('sunday turn ok', len(s))
