# Saturday Nov 7, 2026 weekend date turn (hourly pass; the morning trigger is weekdays-only).
# Verified facts: Friday closed 7-2-2, eleven events - failures 7:05/7:11/7:22, late-surfacing
# 9:13, evening burst of three (last 7:37, 26th straight weekday evening); NA 7:14 and 6:49;
# successes 7:29 and 6:02 PM. Saturday opened with a failure at 6:10 AM (thread 42 msgs).
# No Tyler/Nortec reply, no ATS orders, Tim draft still in Drafts (day nineteen). Overnight
# inbox routine: LiveKit invoices ($3,082.47 prod / $57.64 dev) + Mercury charge - off page
# per rules. New Saturday events: padel at Padel39 East Austin 3-4:30 roofed Court 5, drives
# 2:30-3 and 4:30-5 (counted personal, 2.5h). Monday demo 11-12 stands. Chart rolls
# Sat Nov 7 - Fri Nov 13: Sat 2.5p / Sun 0 / Mon 6.75 / Tue 5 / Wed 7 / Thu 8.5 / Fri 1.5.
# Hazards: 'day sixty' is a prefix of 'day sixty-one/-two' -> bump via regex lookahead;
# Meet codes (nyg-hguu-mmh etc.) and Teams passcodes must not reach the page.
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
rep('day sixty-one', 'day sixty-two', 3)                      # #799
rx(r'day sixty(?!-)', 'day sixty-one', 3)                     # Eric / Izzy trio (bare only)
rep('night fifty-three', 'night fifty-four', 2)
rep('day fifty-two;', 'day fifty-three;', 1)
rep('fifty-five days past', 'fifty-six days past', 4)
rep('forty-five days past', 'forty-six days past', 1)
rep('twenty-three days past', 'twenty-four days past', 2)     # Cathy
rep('Twenty-three days past', 'Twenty-four days past', 2)
rep('(twenty-three days)', '(twenty-four days)', 4)
rep('day eighteen', 'day nineteen', 3)                        # Tim
rep('Iris, day twenty-six', 'Iris, day twenty-seven', 1)
rep('hr-nda is 81 days old', 'hr-nda is 82 days old', 1)
rep('Ages as of Nov 6', 'Ages as of Nov 7', 1)
rep('eight days past due', 'nine days past due', 4)

def chip1(m): return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
rx(r'(class="chip old">)(\d+)(d</span>)', chip1, 2)
rx(r'(class="chip old">)(\d+)(d &mdash;)', chip1, 3)

# ---------- 2. STAMPS / HEADER ----------
rep('2026-11-06T21:07:00-06:00', '2026-11-07T07:07:00-06:00', 2)
rep('<b>Brief compiled</b> Fri 6:55 AM &middot; data checked Fri 9:07 PM CT',
    '<b>Brief compiled</b> Sat 7:07 AM &middot; data checked Sat 7:07 AM CT', 1)
rep('Friday, November 6 &middot; 2026', 'Saturday, November 7 &middot; 2026', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)

# ---------- 3. MASTHEAD ----------
m0 = s.find('Nortec is agreed. Tyler asked')
m1 = s.find('No reactions saved.</p>', m0) + len('No reactions saved.</p>')
assert 0 < m0 < m1
s = s[:m0] + (
 'Friday delivered the reseller tripleheader &mdash; <b>Mike at Gevity, Stratus Networks (1,200 customers) and '
 'GigTel (80,000)</b> back to back, then three hours of GamifyOS with Taylor &mdash; and the line kept score '
 'around it: <b>Friday closed 7&ndash;2&ndash;2</b>, a busy morning cluster plus the twenty-sixth straight '
 'weekday-evening burst. <b>Nortec is still waiting on Tyler</b>: Jr&rsquo;s &ldquo;that works&rdquo; went out '
 'Thursday at 10:34 and no confirmation or paperwork has landed &mdash; Monday&rsquo;s first follow-up. <b>The '
 'Tim record is on day nineteen</b>: the reply has sat in Drafts since Thursday morning and still just needs '
 'Send. Today is nearly clear &mdash; <b>padel at 3, roofed Court 5 at Padel39</b> (drive out 2:30, home by 5). '
 'Monday is the real gate: sync at 8, then <b>the new Voxtell AI Demo at 11</b> (Jr and Carlos joining) sitting '
 'inside the 9&ndash;1 engineering block, Hand and Stone at 8 PM. The Iris <b>invoice is nine days past due</b>; '
 'Tuesday&rsquo;s Monthly Iris Sync at 9 is the agenda slot. No reactions saved.</p>'
) + s[m1:]

# ---------- 4. LEDGER: close Friday, open Saturday ----------
rep('Friday opened busy: <b>failures at 7:05, 7:11 and 7:22</b>, a needs-attention at 7:14 and a success at 7:29, '
    'then a late-surfacing <b>failure at 9:13</b>, then a <b>success at 6:02 PM</b>, a <b>needs-attention at '
    '6:49</b> and an evening burst of <b>three failures, the last at 7:37</b> &mdash; the 26th straight weekday '
    'evening &mdash; <b>7&ndash;2&ndash;2 by 9:07, window open</b>.',
    'Friday closed <b>7&ndash;2&ndash;2</b> &mdash; eleven events: failures at 7:05, 7:11 and 7:22, a '
    'late-surfacing 9:13, and an evening burst of three ending 7:37 (the 26th straight weekday evening); '
    'needs-attention at 7:14 and 6:49; successes at 7:29 and 6:02 PM. Saturday opened with a <b>failure at '
    '6:10 AM &mdash; 1&ndash;0&ndash;0 by 7:07, window open</b>.', 1)

# ---------- 5. TODAY NOTE + SCHEDULE ----------
rep('Reseller day &mdash; three calls 11&ndash;1:30, then three hours with Taylor',
    'Padel Saturday &mdash; roofed Court 5 at 3, home by 5; otherwise clear', 1)
i0 = s.find('<div class="card sched" id="todaysched">')
assert i0 > 0
i0 = s.find('>', i0) + 1
i1 = s.find('</section>', i0)
assert i1 > i0
s = s[:i0] + ('\n'
 '        <div class="slot free"><div class="t">Until 2:30</div><div class="w">Open day<small>Nothing scheduled; the Tim Send, Tyler follow-up and Cathy call all queue for Monday</small></div></div>\n'
 '        <div class="slot"><div class="t">2:30&ndash;3:00</div><div class="w">Drive to Padel39 East Austin<small>4716 E 5th Street</small></div></div>\n'
 '        <div class="slot"><div class="t">3:00&ndash;4:30</div><div class="w">Padel &mdash; roofed Court 5<small>90 minutes, confirmed doubles</small></div></div>\n'
 '        <div class="slot"><div class="t">4:30&ndash;5:00</div><div class="w">Drive home<small>Back by 5</small></div></div>\n'
 '        <div class="slot free"><div class="t">After 5</div><div class="w">Open evening<small>Sunday is clear; Monday opens with the 8 AM sync and the demo at 11</small></div></div>\n'
 '      </div>\n    '
) + s[i1:]

# ---------- 6. CHART: roll to Sat Nov 7 - Fri Nov 13 ----------
rep('Fri Nov 6 &ndash; Thu Nov 12', 'Sat Nov 7 &ndash; Fri Nov 13', 1)
plot0 = s.find('<div class="plot" id="plot">')
c0 = s.find('<div class="bar">', plot0)
cx = s.find('<div class="xaxis"', plot0)
c1 = s.rfind('</div>', c0, cx)
assert 0 < plot0 < c0 < c1 < cx
s = s[:c0] + (
 '<div class="bar"><div class="tot" style="bottom:calc(17.86% + 6px)">2.5</div>\n'
 '            <div class="seg p" style="height:17.86%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
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
 '        '
) + s[c1:]
rep('<div><b>Fri</b>6</div><div><b>Sat</b>7</div>\n          <div><b>Sun</b>8</div><div><b>Mon</b>9</div><div><b>Tue</b>10</div><div><b>Wed</b>11</div><div><b>Thu</b>12</div>',
    '<div><b>Sat</b>7</div><div><b>Sun</b>8</div>\n          <div><b>Mon</b>9</div><div><b>Tue</b>10</div><div><b>Wed</b>11</div><div><b>Thu</b>12</div><div><b>Fri</b>13</div>', 1)

# ---------- 7. TOP 5 ----------
rep('The Nortec paperwork, the reseller double-header, and the Send button on the Tim draft',
    'The Nortec paperwork, the Tim Send, and the Cathy call &mdash; all Monday-morning items', 1)
rep('closed the terms at 10:34 yesterday', 'closed the terms Thursday at 10:34', 1)
rep('Two white-label resellers today &mdash; Stratus at noon (1,200 customers), GigTel at 1 (80,000)',
    'Two white-label resellers pitched Friday &mdash; Stratus (1,200 customers) and GigTel (80,000); follow-ups are Monday&rsquo;s', 1)
rep('sat in Drafts since 9:07 yesterday morning. Send it.',
    'sat in Drafts since Thursday morning. Send it Monday, first thing.', 1)
rep('Call, not email &middot; before 11', 'Call, not email &middot; Monday', 1)
rep('this morning before Mike at 11 is the slot', 'Monday morning before the 11 AM demo is the slot', 1)
rep('is two days old', 'is three days old', 1)

# ---------- 8. FLAG 1 (Today) ----------
f0 = s.find('<span class="pill warn">Today</span> Reseller Friday')
f0 = s.rfind('<h3>', 0, f0)
f1 = s.find('</p>', f0) + len('</p>')
assert 0 < f0 < f1
s = s[:f0] + (
 '<h3><span class="pill warn">Today</span> Padel Saturday &mdash; Court 5 at 3; everything else queues for Monday</h3>\n'
 '          <p>One booking today: <b>padel 3&ndash;4:30, roofed Court 5 at Padel39</b> (out at 2:30, home by 5). '
 'Friday delivered the tripleheader &mdash; Mike, Stratus and GigTel &mdash; plus Taylor&rsquo;s three GamifyOS '
 'hours; the <b>web page and community landing stay due live Wednesday Nov 12</b>. Monday&rsquo;s queue, in '
 'order: <b>the Tim Send</b> (day nineteen), <b>the Tyler/Nortec follow-up</b> (no paperwork yet), <b>the Cathy '
 'call</b> (twenty-four days), <b>the ATS nudge</b>, <b>Catherine Weir&rsquo;s reply</b>, and the review queue '
 'inside the 9&ndash;1 block &mdash; with <b>the new demo at 11</b> cutting an hour out of it.</p>'
) + s[f1:]

# ---------- 9. MARKERS ----------
k0 = s.find('The week&rsquo;s markers</h4>')
kp = s.find('<p', k0)
k1 = s.find('</p>', kp) + len('</p>')
assert 0 < k0 < kp < k1
s = s[:kp] + (
 '<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Friday closed <b>7&ndash;2&ndash;2</b> &mdash; '
 'eleven events: a busy first half hour, a late-surfacing 9:13, and the <b>twenty-sixth straight '
 'weekday-evening burst</b> (three failures, last 7:37). Saturday opened with a 6:10 AM failure. The pipeline: '
 '<b>Nortec agreed on terms Thursday</b> &mdash; Tyler&rsquo;s confirmation and paperwork still out; <b>both '
 'resellers pitched Friday</b> (Stratus 1,200, GigTel 80,000) &mdash; follow-ups Monday; ATS&rsquo;s promised '
 'orders are three days overdue. <b>The Tim record is drafted and unsent</b> &mdash; one click closes day '
 'nineteen. The next engineering block is <b>Monday 9&ndash;1, with the new demo at 11 inside it</b>.</p>'
) + s[k1:]

# ---------- 10. COMING-UP ----------
c0 = s.find('This week &mdash; reseller Friday, a clear weekend, and an 8.5-hour Thursday ahead')
c1 = s.find('</p>', c0) + len('</p>')
assert 0 < c0 < c1
s = s[:c0] + (
 'The weekend &mdash; padel today, clear Sunday; then a demo-day Monday and an 8.5-hour Thursday</h4>\n'
 '          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">Today: <b>padel 3&ndash;4:30</b> (roofed '
 'Court 5), nothing else. Sunday: clear. Monday: sync 8, <b>DW Engineering 9&ndash;1 with the new Voxtell AI '
 'Demo at 11</b> inside it (Jr + Carlos) &mdash; the review queue&rsquo;s window (#886, #991, #992, #799, '
 'Illia&rsquo;s six, Pipedrive voxai-851) &mdash; Hand and Stone 8 PM. Tuesday: <b>Monthly Iris Sync 9</b> (the '
 'nine-days-past-due invoice and the drip/report commitments belong on its agenda), <b>Izzy 10</b> (the Levitt '
 'verdict &mdash; and the Tim record, sent by then or on day twenty-two), DW Client 10&ndash;2. Wednesday: '
 'Sustainable Ambition 9:30, Ellie &times; Caroline &times; Taylor 10:30, DW 11&ndash;3, TTT 3 &mdash; and '
 '<b>the GamifyOS page + landing are due live</b>. Thursday Nov 12 is <b>the week&rsquo;s heaviest at 8.5h, '
 'over the 8h line</b>: DW 8:30&ndash;12:30, Scott Van Camp 2, Reserved 3:30, <b>Friendsgiving 6&ndash;9 PM</b>. '
 'Friday Nov 13: Review Crew happy hour 5:30. Carried: <b>the Cathy call</b> (twenty-four days), <b>the CCI '
 'booking</b>, the drip and performance reports, the ATS five, the Whova trio, the Sahiti intro, and the '
 '<b>invoice &mdash; nine days past due</b>.</p>'
) + s[c1:]

# ---------- 11. INBOX LEAD ----------
x0 = s.find('The Nortec thread closed its loop yesterday:')
x1 = s.find('today&rsquo;s ground.', x0) + len('today&rsquo;s ground.')
assert 0 < x0 < x1
s = s[:x0] + (
 'The Nortec thread is holding its breath: Jr&rsquo;s Thursday &ldquo;that works&rdquo; is out and <b>no '
 'confirmation or paperwork from Tyler has landed</b> &mdash; Monday&rsquo;s first follow-up. <b>Ben Cherry at '
 'LiveKit</b> stays a live channel for the TCP/SIP and BAA questions. <b>Catherine Weir (365agents)</b> still '
 'waits on a warm reply, <b>Illia&rsquo;s Pipedrive review</b> (voxai-851) waits on the Monday block, and <b>the '
 'Tim reply is on day nineteen in Drafts</b> &mdash; one Send closes it. Still needing words: <b>Cathy at '
 'ProGraphix</b> (twenty-four days), <b>the CCI booking</b>, the <b>Whova three</b>, and the <b>Sahiti '
 'intro</b> &mdash; Monday morning is the next ground.'
) + s[x1:]

# ---------- SANITY ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-07T07:07:00-06:00') == 2
assert s.count('window open') == 2
assert s.count('Fri Nov 6 &ndash;') == 0
assert s.count('twenty-three days') == 0 and s.count('day eighteen') == 0
assert s.count('eight days past due') == 0
assert s.count('Reseller day') == 0 and s.count('Reseller Friday') == 0
assert 'Good evening' not in s
assert 'PasswordReset' not in s and 'billcenter.net' not in s and 'Jose Luiz' not in s
assert '5WY67Sa2' not in s and 'pY3DM73R' not in s and 'bT5uDhjRSBk3' not in s and 'hw7Mh6cK' not in s
assert 'doxy.me' not in s and 'nyg-hguu-mmh' not in s and 'bxe-xdtp-ohs' not in s
assert 'uyt-cgnh-gtz' not in s and 'vqd-jqoy-wsp' not in s
assert 'sfw-mvnn-nfd' not in s and 'cjk-wubx-vna' not in s
assert '3,082' not in s and 'LiveKit invoice' not in s

open(p, 'w', encoding='utf-8').write(s)
print('saturday turn ok', len(s))
