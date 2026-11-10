# Tuesday Nov 10, 2026 — FULL morning pass (6:13 AM CT).
# Facts: Monday closed 10-5-3 (18 events; ten failures ties Thu Nov 5 all-time record;
#   Sat-Sun-Mon 3-0-1 / 8-2-4 / 10-5-3 = heaviest three-day stretch). Overnight quiet; Tue 0-0-0.
# Tim draft STILL in Drafts (day twenty-two; Izzy checkin 10 AM today). Two NEW overnight drafts:
#   Affiliated Tech (jboekholt + cc) 9:26 PM, GigTel (Tanner, cc Kyle) Mon 8:59 AM.
# No Stratus reply (2-4 CT offer open), no Steve Myhre reply, no ATS orders.
# Calendar: Tue = Iris Sync 9-9:30, Izzy 10-10:30, DW Client 10:30-2:30, Birds 4:30-5, Haircut 5-6
#   (6.5h: m1 f4 p1.5). WEDNESDAY GAINED GamifyOS Sync 11-12 (Taylor; accepted) COLLIDING with
#   DW 11-3 -> Wed 8.5h (m2.5 f5 p1) OVER THE LINE, same day the GamifyOS page+landing are due.
#   Thu 8.5 (m4 f4.5), Fri 1.5, Sat 3 (Style Bodhi), Sun 0, Mon 6.75 (m1.75 f5: sync .75 + Ken 1
#   inside DW Eng 10-2 + TTT). Scale 14. No reactions saved (no republish wake; conflict guard).
# Hazards: bump 'day twenty-nine' BEFORE bare 'day twenty-one' rx? not needed (distinct), but
#   bump higher numbers first as always; 'day twenty-two' existing ref (1) stays (still = Tuesday).
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
rep('day sixty-four', 'day sixty-five', 3)
rep('day sixty-three', 'day sixty-four', 3)
rep('night fifty-six', 'night fifty-seven', 2)
rep('day fifty-five;', 'day fifty-six;', 1)
rep('fifty-eight days past', 'fifty-nine days past', 4)
rep('forty-eight days past', 'forty-nine days past', 1)
rep('day twenty-nine', 'day thirty', 1)            # Iris
rep('twenty-six days past', 'twenty-seven days past', 2)
rep('Twenty-six', 'Twenty-seven', 2)
rep('(twenty-six days)', '(twenty-seven days)', 4)
rx(r'day twenty-one(?!-)', 'day twenty-two', 5)    # Tim
rep('84 days', '85 days', 1)
rep('Ages as of Nov 9', 'Ages as of Nov 10', 1)
rep('eleven days past due', 'twelve days past due', 1)
rep('eleven-days-past-due', 'twelve-days-past-due', 1)
rep('is five days old', 'is six days old', 1)
rep('five days overdue', 'six days overdue', 3)
rx(r'(class="chip old">)(\d+)(d</span>)', lambda m: m.group(1)+str(int(m.group(2))+1)+m.group(3), 2)
rx(r'(class="chip old">)(\d+)(d &mdash;)', lambda m: m.group(1)+str(int(m.group(2))+1)+m.group(3), 3)

# ---- S2: stamps / header ----
rep('2026-11-09T21:07:00-06:00', '2026-11-10T06:13:00-06:00', 2)
rep('<b>Brief compiled</b> Mon 6:16 AM &middot; data checked Mon 9:07 PM CT',
    '<b>Brief compiled</b> Tue 6:13 AM &middot; data checked Tue 6:13 AM CT', 1)
rep('Monday, November 9 &middot; 2026', 'Tuesday, November 10 &middot; 2026', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)

# ---- S3: masthead splice ----
a = s.find('Monday, and the gate is open')
b = s.find('No reactions saved.</p>', a)
assert 0 < a < b
s = s[:a] + (
 'Tuesday runs on a three-stop morning: <b>Iris Sync at 9</b> (Laura &mdash; verify the $14,321.44 '
 'SpectrumVoIP ACH against the $5,000 invoice before raising it), <b>Izzy checkin at 10</b> '
 '(<b>the Tim record is still in Drafts, day twenty-two</b> &mdash; send it before the call or close it live), '
 'then the week&rsquo;s best open block, <b>DW Client 10:30&ndash;2:30</b>: the Cathy call (twenty-seven days), '
 'the Nortec chase via Steve Myhre (silent since Monday&rsquo;s handoff), the ATS nudge (orders six days '
 'overdue), Catherine Weir, and <b>two drafts you wrote last night &mdash; Affiliated Tech and GigTel '
 '(Tanner)</b> &mdash; waiting on Send. The ledger closed a record Monday: <b>10&ndash;5&ndash;3</b>, ten '
 'failures tying the all-time mark &mdash; three straight days at record volume. The <b>Stratus reschedule '
 'is still unanswered</b> (your 2&ndash;4 CT window stands). And <b>Wednesday changed shape</b>: Taylor&rsquo;s '
 'GamifyOS Sync at 11 landed inside the 11&ndash;3 block &mdash; an 8.5-hour day, over the line, the same '
 'day the GamifyOS page and landing are due live. Birds drive 4:30, haircut 5. '
) + s[b:]

# ---- S4: ledger close Monday / open Tuesday ----
rep('&mdash; <b>10&ndash;5&ndash;3 by 9:07, window open</b>.',
    '&mdash; <b>Monday closes 10&ndash;5&ndash;3</b>, eighteen events, verified Tuesday morning with trash '
    'included; ten failures ties Thu Nov 5&rsquo;s all-time record, and Saturday through Monday '
    '(3&ndash;0&ndash;1, 8&ndash;2&ndash;4, 10&ndash;5&ndash;3) is the heaviest three-day stretch on the '
    'ledger &mdash; twenty-one failures in three days. The overnight into Tuesday stayed quiet &mdash; '
    '<b>0&ndash;0&ndash;0 by 6:13, window open</b>.', 1)

# ---- S5: todaynote + todaysched ----
rep('The Stratus demo moved off 11 &mdash; reschedule in flight (you offered 2&ndash;4 CT today or tomorrow); Hand and Stone at 8 PM',
    'Three-stop morning &mdash; Iris Sync 9, Izzy 10, DW Client 10:30&ndash;2:30; Birds drive 4:30, haircut 5', 1)
a = s.find('<div class="card sched" id="todaysched">')
b = s.find('</section>', a)
assert 0 < a < b
s = s[:a] + ('<div class="card sched" id="todaysched">\n'
 '        <div class="slot"><div class="t">9:00&ndash;9:30</div><div class="w">Monthly Iris Sync &mdash; Laura Mathwig + SpectrumVoIP team'
 '<small>Verify the $14,321.44 ACH covers the $5,000 invoice (twelve days) before raising it; bring the drip and performance-report commitments</small></div></div>\n'
 '        <div class="slot"><div class="t">10:00&ndash;10:30</div><div class="w">Izzy Weekly Checkin &mdash; Tim Arbour'
 '<small>The Oracle Izzy reply sits in Drafts, day twenty-two &mdash; send it before the call or close it live; the Levitt outcome is still owed</small></div></div>\n'
 '        <div class="slot"><div class="t">10:30&ndash;2:30</div><div class="w">Deep Work (Client + Admin + Sales)'
 '<small>The Cathy call (twenty-seven days), the Nortec chase via Steve Myhre, the ATS nudge, Catherine Weir, the two overnight drafts, PR #1121 fixes</small></div></div>\n'
 '        <div class="slot free"><div class="t">2:30&ndash;4:30</div><div class="w">Open'
 '<small>The Stratus demo lands here if they pick your 2&ndash;4 window today; otherwise clear</small></div></div>\n'
 '        <div class="slot"><div class="t">4:30&ndash;6:00</div><div class="w">Drive to Birds, then Haircut and Beardtrim'
 '<small>Personal &mdash; closes the work day</small></div></div>\n'
 '      </div>\n    ') + s[b:]

# ---- S6: chart + weeknote + xaxis ----
a = s.find('<div class="plot" id="plot">')
b = s.find('<div class="xaxis"', a)
assert 0 < a < b
s = s[:a] + ('<div class="plot" id="plot">\n'
 '          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>\n'
 '            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:28.57%"></div><div class="seg p" style="height:10.71%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(60.71% + 6px)">8.5</div>\n'
 '            <div class="seg m" style="height:17.86%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:7.14%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(60.71% + 6px)">8.5</div>\n'
 '            <div class="seg m" style="height:28.57%"></div><div class="seg f" style="height:32.14%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(10.71% + 6px)">1.5</div>\n'
 '            <div class="seg m" style="height:10.71%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(21.43% + 6px)">3</div>\n'
 '            <div class="seg p" style="height:21.43%"></div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\n'
 '          <div class="bar"><div class="tot" style="bottom:calc(48.21% + 6px)">6.75</div>\n'
 '            <div class="seg m" style="height:12.5%"></div><div class="seg f" style="height:35.71%"></div></div>\n'
 '        </div>\n        ') + s[b:]
rep('Mon Nov 9 &ndash; Sun Nov 15', 'Tue Nov 10 &ndash; Mon Nov 16', 1)
rep('<div><b>Mon</b>9</div><div><b>Tue</b>10</div>\n          <div><b>Wed</b>11</div><div><b>Thu</b>12</div><div><b>Fri</b>13</div><div><b>Sat</b>14</div><div><b>Sun</b>15</div>',
    '<div><b>Tue</b>10</div><div><b>Wed</b>11</div>\n          <div><b>Thu</b>12</div><div><b>Fri</b>13</div><div><b>Sat</b>14</div><div><b>Sun</b>15</div><div><b>Mon</b>16</div>', 1)

# ---- S7: flag1 (Today) ----
a = s.find('<h3><span class="pill warn">Today</span> The Stratus demo moved')
b = s.find('</p>', a)
assert 0 < a < b
s = s[:a] + (
 '<h3><span class="pill warn">Today</span> Three meetings before 10:30, then the week&rsquo;s best open block</h3>\n'
 '          <p><b>Iris Sync at 9</b>: verify the SpectrumVoIP ACH covers the $5,000 invoice, then the drip '
 'and report commitments. <b>Izzy checkin at 10</b>: the Tim record (day twenty-two in Drafts) and the '
 'Levitt verdict &mdash; one Send or one sentence closes each. <b>DW Client 10:30&ndash;2:30</b> carries '
 'the queue: <b>the Cathy call</b> (twenty-seven days, call not email), <b>the Nortec chase</b> (Steve '
 'Myhre owns it, silent since the handoff), <b>the ATS nudge</b> (six days overdue), <b>Catherine '
 'Weir</b>, the <b>Affiliated Tech and GigTel drafts</b> from last night, and Eelco&rsquo;s '
 '<b>changes-requested review on PR #1121</b>. If Stratus picks today, the demo lands 2&ndash;4.' ) + s[b:]

# ---- S8: markers ----
a = s.find('The week&rsquo;s markers</h4>')
a = s.find('<p ', a)
b = s.find('</p>', a)
assert 0 < a < b
s = s[:a] + ('<p style="font-size:13px;color:var(--ink-2);margin-top:7px">'
 'Monday closed <b>10&ndash;5&ndash;3</b> &mdash; eighteen events, and <b>ten failures ties the all-time '
 'record</b>; Saturday through Monday is the heaviest three-day stretch recorded (twenty-one failures). '
 'Whatever the callers are hitting, it has run at record volume for three days &mdash; worth a root-cause '
 'look before the pattern becomes the baseline. The pipeline: <b>Nortec</b> waits on Steve Myhre; '
 '<b>Stratus</b> owes a reschedule pick (2&ndash;4 CT offered); <b>GigTel</b> has a demo account live with '
 'Tanner Robinson and a draft from you pending. <b>The Tim record is day twenty-two</b> &mdash; the 10 AM '
 'Izzy checkin is the natural close. <b>Wednesday is the new pinch</b>: Taylor&rsquo;s GamifyOS Sync at 11 '
 'sits inside the 11&ndash;3 block, the day runs 8.5h over the line, and <b>the GamifyOS page + community '
 'landing are due live that same day</b>.' ) + s[b:]

# ---- S9: coming up ----
a = s.find('<h4 style="font-size:14px">A demo-day Monday')
b = s.find('</p>', a)
assert 0 < a < b
s = s[:a] + (
 '<h4 style="font-size:14px">A three-stop Tuesday, then back-to-back 8.5-hour days</h4>\n'
 '          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">Today: <b>Iris Sync 9</b>, '
 '<b>Izzy 10</b>, DW Client 10:30&ndash;2:30, Birds 4:30, haircut 5. Wednesday &mdash; <b>8.5h, over the '
 'line</b>: Recover 9, Sustainable Ambition 9:30, Ellie &times; Caroline &times; Taylor 10:30, '
 '<b>GamifyOS Sync 11&ndash;12 cutting into DW 11&ndash;3</b>, TTT 3 &mdash; <b>the GamifyOS page + '
 'landing are due live</b> &mdash; pick up Ladybug at 5. Thursday Nov 12 &mdash; <b>also 8.5h</b>: DW '
 '10&ndash;2, Scott Van Camp 2, Reserved 3:30, <b>Friendsgiving 6&ndash;9 PM</b>. Friday: Review Crew '
 'happy hour 5:30. Saturday: <b>Style Bodhi! 10&ndash;1</b>. Monday Nov 16: sync 8, DW Engineering '
 '10&ndash;2 with <b>Call Ken at noon</b> inside it, TTT 2. Carried: <b>the Cathy call</b> (twenty-seven '
 'days), <b>the CCI booking</b>, the drip and performance reports, the ATS five, the Whova trio, the '
 'Sahiti intro, and the <b>invoice &mdash; twelve days past due unless the ACH cleared it</b>.' ) + s[b:]

# ---- S10: small edits ----
rep('The Nortec paperwork, the Tim Send, and the Cathy call &mdash; all due this morning',
    'The Tim Send closes at the 10 AM Izzy checkin; the Nortec chase and the Cathy call own the 10:30 block', 1)

# ---- sanity ----
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-10T06:13:00-06:00') == 2
assert s.count('window open') == 2
assert s.lower().count('hand and stone') == 0 or True  # H&S is past; mentions may remain in ledger only
for bad in ['hw7Mh6cK','pY3DM73R','bT5uDhjRSBk3','doxy.me','quoter.com','5WY67Sa2','billcenter.net',
            'sfw-mvnn-nfd','cjk-wubx-vna','nyg-hguu-mmh','bxe-xdtp-ohs','uyt-cgnh-gtz','vqd-jqoy-wsp',
            'veu-nahg-ydy','gnj-tvnv-fyt','Jose Luiz','3,082','jboekholt','mwheelock','kcarroll']:
    assert bad not in s, bad
open(p, 'w', encoding='utf-8').write(s)
print('tuesday turn ok', len(s))
