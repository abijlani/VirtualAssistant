# Monday Nov 9, 2026 — FULL morning pass (6:16 AM CT).
# Facts: Sunday closed 8-2-4 (14 events, heaviest weekend day; 8 failures matches Mon Nov 2's
#   old weekday record). Monday opened with failures at 5:20 and 6:15 AM (2-0-0 by 6:16).
# Calendar (Bodhi's Sunday-afternoon planning pass added personal blocks):
#   Mon: Sync 8-8:45, DW Eng 9-1 w/ Voxtell AI Demo 11-12 (STRATUS: Alex Penichet + 2,
#        one pending; Jr + Carlos), Hand and Stone 8-9 PM. 6.75h (m1.75 f4 p1).
#   Tue: Iris Sync 9-9:30, Izzy 10-10:30, DW Client 10:30-2:30, Drive to Birds 4:30-5,
#        Haircut 5-6. 6.5h (m1 f4 p1.5).
#   Wed: Recover 9-9:30, SustAmb 9:30-10:30 (dupe counts once), Ellie x Caroline 10:30-11,
#        DW ProjEng 11-3, TTT 3-4, Pick up Ladybug 5-5:30. 7.5h (m1.5 f5 p1).
#   Thu: DW 10-2 (moved from 8:30-12:30), Scott Van Camp 2-3, Reserved 3:30-4,
#        Friendsgiving 6-9. 8.5h (m4 f4.5) — over 8h line.
#   Fri: Review Crew 5:30-7. 1.5h (m).  Sat: Style Bodhi! 10-1, personal 3h.  Sun 15: clear.
# No reactions saved (no republish wake since V983). Tim draft still in Drafts (day 21).
# Nortec: Tyler silent all weekend. Scale 14 unchanged.
# Hazards: 'day twenty' is a prefix (twenty-two, twenty-eight pre-bumped) -> rx lookahead.
#   Never name-guess from emails (jhymbaugh/eweakland/issac stay unnamed).
import re

p = 'page-template.html'
s = open(p, encoding='utf-8').read()

def rep(old, new, n):
    global s
    c = s.count(old)
    assert c == n, f"rep {old[:60]!r}: expected {n}, found {c}"
    s = s.replace(old, new)

def rx(pat, new, n):
    global s
    s, c = re.subn(pat, new, s)
    assert c == n, f"rx {pat!r}: expected {n}, replaced {c}"

# ---- S1: global age bumps (highest first) ----
rep('day sixty-three', 'day sixty-four', 3)
rep('day sixty-two', 'day sixty-three', 3)
rep('night fifty-five', 'night fifty-six', 2)
rep('day fifty-four;', 'day fifty-five;', 1)
rep('fifty-seven days past', 'fifty-eight days past', 4)
rep('forty-seven days past', 'forty-eight days past', 1)
rep('day twenty-eight', 'day twenty-nine', 1)        # Iris, before bare 'day twenty'
rep('twenty-five days past', 'twenty-six days past', 2)
rep('Twenty-five', 'Twenty-six', 2)
rep('(twenty-five days)', '(twenty-six days)', 4)
rx(r'day twenty(?![-])', 'day twenty-one', 5)        # Tim; 'day twenty-two' Tuesday ref stays
rep('83 days', '84 days', 1)
rep('Ages as of Nov 8', 'Ages as of Nov 9', 1)
rep('ten days past due', 'eleven days past due', 4)
rep('is four days old', 'is five days old', 1)
rx(r'(class="chip old">)(\d+)(d</span>)', lambda m: m.group(1)+str(int(m.group(2))+1)+m.group(3), 2)
rx(r'(class="chip old">)(\d+)(d &mdash;)', lambda m: m.group(1)+str(int(m.group(2))+1)+m.group(3), 3)

# ---- S2: stamps / header ----
rep('2026-11-08T21:07:00-06:00', '2026-11-09T06:16:00-06:00', 2)
rep('<b>Brief compiled</b> Sun 7:09 AM &middot; data checked Sun 9:07 PM CT',
    '<b>Brief compiled</b> Mon 6:16 AM &middot; data checked Mon 6:16 AM CT', 1)
rep('Sunday, November 8 &middot; 2026', 'Monday, November 9 &middot; 2026', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)

# ---- S3: masthead splice ----
a = s.find('The weekend is doing its job')
b = s.find('No reactions saved.</p>', a)
assert 0 < a < b
s = s[:a] + (
 'Monday, and the gate is open: sync at 8, then the 9&ndash;1 engineering block with '
 '<b>the Voxtell AI Demo at 11</b> inside it &mdash; and the demo is for <b>Stratus Networks</b> '
 '(Alex Penichet plus two accepted, one pending), Friday&rsquo;s reseller pitch converting to a live look. '
 'The queue, in order: <b>the Tim Send</b> (day twenty-one in Drafts &mdash; one click), '
 '<b>the Tyler/Nortec follow-up</b> (Jr&rsquo;s &ldquo;that works&rdquo; went unanswered all weekend &mdash; '
 'no confirmation, no paperwork), <b>the Cathy call</b> (twenty-six days), <b>the ATS nudge</b> '
 '(promised orders five days overdue), <b>Catherine Weir&rsquo;s reply</b>, and the review queue. '
 'The weekend story is the ledger: <b>Sunday closed 8&ndash;2&ndash;4</b> &mdash; fourteen events on a '
 'clear calendar, the heaviest weekend day recorded &mdash; and Monday opened with <b>failures at 5:20 '
 'and 6:15 AM</b>. The Iris <b>invoice is eleven days past due</b>; Tuesday&rsquo;s Sync at 9 is the '
 'agenda slot. Hand and Stone at 8 PM closes the day. '
) + s[b:]

# ---- S4: ledger close Sunday / open Monday ----
rep('then an <b>eighth failure at 8:29</b> &mdash; <b>8&ndash;2&ndash;4 by 9:07, window open</b>.',
    'then an <b>eighth failure at 8:29</b> &mdash; <b>Sunday closes 8&ndash;2&ndash;4</b>, fourteen events, '
    'verified Monday morning with trash included; the heaviest weekend day on the ledger, and eight '
    'failures matches Mon Nov 2&rsquo;s old weekday record. Monday opened with <b>failures at 5:20 and '
    '6:15 AM</b> &mdash; <b>2&ndash;0&ndash;0 by 6:16, window open</b>.', 1)

# ---- S5: todaynote + todaysched ----
rep('Clear Sunday &mdash; nothing booked; Monday opens with the 8 AM sync and the demo at 11',
    'Demo day &mdash; sync at 8, the Stratus demo at 11 inside the 9&ndash;1 block, Hand and Stone at 8 PM', 1)
a = s.find('<div class="card sched" id="todaysched">')
b = s.find('</section>', a)
assert 0 < a < b
s = s[:a] + ('<div class="card sched" id="todaysched">\n'
 '        <div class="slot"><div class="t">8:00&ndash;8:45</div><div class="w">Weekly Product Sync'
 '<small>Jr accepted; Eelco still pending</small></div></div>\n'
 '        <div class="slot"><div class="t">9:00&ndash;1:00</div><div class="w">Deep Work (Engineering)'
 '<small>The review queue&rsquo;s window &mdash; the demo cuts 11&ndash;12 out of it</small></div></div>\n'
 '        <div class="slot"><div class="t">11:00&ndash;12:00</div><div class="w">Voxtell AI Demo &mdash; Stratus Networks'
 '<small>Alex Penichet plus two accepted, one pending; Jr and Carlos on our side</small></div></div>\n'
 '        <div class="slot free"><div class="t">1:00&ndash;8:00</div><div class="w">Open'
 '<small>Clear afternoon &mdash; the Tim Send, the Tyler/Nortec follow-up, the Cathy call and the ATS nudge '
 'land here if the morning didn&rsquo;t clear them</small></div></div>\n'
 '        <div class="slot"><div class="t">8:00&ndash;9:00 PM</div><div class="w">Hand and Stone'
 '<small>Personal &mdash; closes the day</small></div></div>\n'
 '      </div>\n    ') + s[b:]

# ---- S6: chart + weeknote + xaxis ----
a = s.find('<div class="plot" id="plot">')
b = s.find('<div class="xaxis"', a)
assert 0 < a < b
s = s[:a] + ('<div class="plot" id="plot">\n'
 '          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(48.21% + 6px)">6.75</div>\n'
 '            <div class="seg m" style="height:12.5%"></div><div class="seg f" style="height:28.57%"></div><div class="seg p" style="height:7.14%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>\n'
 '            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:28.57%"></div><div class="seg p" style="height:10.71%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(53.57% + 6px)">7.5</div>\n'
 '            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:7.14%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(60.71% + 6px)">8.5</div>\n'
 '            <div class="seg m" style="height:28.57%"></div><div class="seg f" style="height:32.14%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(10.71% + 6px)">1.5</div>\n'
 '            <div class="seg m" style="height:10.71%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(21.43% + 6px)">3</div>\n'
 '            <div class="seg p" style="height:21.43%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '        </div>\n        ') + s[b:]
rep('Sun Nov 8 &ndash; Sat Nov 14', 'Mon Nov 9 &ndash; Sun Nov 15', 1)
rep('<div><b>Sun</b>8</div><div><b>Mon</b>9</div>\n          <div><b>Tue</b>10</div><div><b>Wed</b>11</div><div><b>Thu</b>12</div><div><b>Fri</b>13</div><div><b>Sat</b>14</div>',
    '<div><b>Mon</b>9</div><div><b>Tue</b>10</div>\n          <div><b>Wed</b>11</div><div><b>Thu</b>12</div><div><b>Fri</b>13</div><div><b>Sat</b>14</div><div><b>Sun</b>15</div>', 1)

# ---- S7: flag1 (Today) ----
a = s.find('<h3><span class="pill warn">Today</span> Clear Sunday')
b = s.find('</p>', a)
assert 0 < a < b
s = s[:a] + (
 '<h3><span class="pill warn">Today</span> Demo day &mdash; Stratus at 11 inside the 9&ndash;1 block</h3>\n'
 '          <p>Sync at 8, then the engineering block carries both <b>the review queue</b> (#886, #991, #992, '
 '#799, Illia&rsquo;s six, Pipedrive voxai-851) and <b>the Stratus demo at 11</b> &mdash; bring the Cairo '
 'pain points and pricing from Friday&rsquo;s Alex Penichet call. Around it, in order: <b>the Tim Send</b> '
 '(day twenty-one &mdash; one click), <b>the Tyler/Nortec follow-up</b> (silent all weekend), <b>the Cathy '
 'call</b> (twenty-six days), <b>the ATS nudge</b> (orders five days overdue), <b>Catherine Weir&rsquo;s '
 'reply</b>. The <b>GamifyOS page and community landing stay due live Wednesday Nov 12</b>, and the Iris '
 '<b>invoice (eleven days) belongs on Tuesday&rsquo;s Sync agenda</b>.' ) + s[b:]

# ---- S8: markers ----
a = s.find('The week&rsquo;s markers</h4>')
a = s.find('<p ', a)
b = s.find('</p>', a)
assert 0 < a < b
s = s[:a] + ('<p style="font-size:13px;color:var(--ink-2);margin-top:7px">'
 'Sunday closed <b>8&ndash;2&ndash;4</b> &mdash; fourteen events on a clear calendar, the heaviest weekend '
 'day on the ledger; eight failures matches the old weekday record from Mon Nov 2. The weekend ran '
 '<b>Saturday 3&ndash;0&ndash;1, Sunday 8&ndash;2&ndash;4</b> where prior weekends sat near-silent, and '
 'Monday opened with failures at 5:20 and 6:15 AM &mdash; worth a look at what the callers hit. The '
 'pipeline: <b>Nortec agreed on terms Thursday</b> &mdash; Tyler silent through the weekend, follow-up '
 'first thing; <b>the Stratus demo at 11</b> is Friday&rsquo;s reseller pitch converting; ATS&rsquo;s '
 'promised orders are five days overdue. <b>The Tim record is drafted and unsent</b> &mdash; one click '
 'closes day twenty-one. The GamifyOS page and community landing are <b>due live Wednesday</b>.' ) + s[b:]

# ---- S9: coming up ----
a = s.find('<h4 style="font-size:14px">Clear Sunday; then')
b = s.find('</p>', a)
assert 0 < a < b
s = s[:a] + (
 '<h4 style="font-size:14px">A demo-day Monday, a three-stop Tuesday, and an 8.5-hour Thursday</h4>\n'
 '          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">Today: sync 8, <b>DW Engineering '
 '9&ndash;1 with the Stratus demo at 11</b> inside it &mdash; the review queue&rsquo;s window (#886, #991, '
 '#992, #799, Illia&rsquo;s six, Pipedrive voxai-851) &mdash; Hand and Stone 8 PM. Tuesday: <b>Monthly '
 'Iris Sync 9</b> (the eleven-days-past-due invoice is the agenda item), <b>Izzy checkin 10</b> (Tim '
 '&mdash; sent by then or on day twenty-two), DW Client 10:30&ndash;2:30, then Drive to Birds 4:30 and '
 'the haircut at 5. Wednesday: Sustainable Ambition 9:30, Ellie &times; Caroline &times; Taylor 10:30, '
 'DW 11&ndash;3, TTT 3 &mdash; <b>the GamifyOS page + landing are due live</b> &mdash; pick up Ladybug '
 'at 5. Thursday Nov 12 stays <b>the week&rsquo;s heaviest at 8.5h, over the 8h line</b>: DW 10&ndash;2 '
 '(moved off the 8:30 start), Scott Van Camp 2, Reserved 3:30, <b>Friendsgiving 6&ndash;9 PM</b>. '
 'Friday Nov 13: Review Crew happy hour 5:30. Saturday: <b>Style Bodhi! 10&ndash;1</b>. Carried: '
 '<b>the Cathy call</b> (twenty-six days), <b>the CCI booking</b>, the drip and performance reports, '
 'the ATS five, the Whova trio, the Sahiti intro, and the <b>invoice &mdash; eleven days past due</b>.' ) + s[b:]

# ---- S10: small line edits ----
rep('The Nortec paperwork, the Tim Send, and the Cathy call &mdash; all Monday-morning items',
    'The Nortec paperwork, the Tim Send, and the Cathy call &mdash; all due this morning', 1)

# ---- sanity ----
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-09T06:16:00-06:00') == 2
assert s.count('window open') == 2
assert s.lower().count('clear sunday') == 0
assert s.count('four days overdue') == 0 and s.count('ten-days-past-due') == 0
assert s.count('8&ndash;2&ndash;4') == 4   # ledger close, masthead, markers x2
for bad in ['hw7Mh6cK','pY3DM73R','bT5uDhjRSBk3','doxy.me','quoter.com','5WY67Sa2','billcenter.net',
            'sfw-mvnn-nfd','cjk-wubx-vna','nyg-hguu-mmh','bxe-xdtp-ohs','uyt-cgnh-gtz','vqd-jqoy-wsp',
            'veu-nahg-ydy','Jose Luiz','3,082','jhymbaugh','eweakland','Hymbaugh','Weakland']:
    assert bad not in s, bad
open(p, 'w', encoding='utf-8').write(s)
print('monday turn ok', len(s))
