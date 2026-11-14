# Saturday Nov 14 day-turn — run by the 7:07 AM CT light tick (the morning
# full-pass trigger is weekdays-only: cron 0 12 * * 1-5, next run Mon Nov 16).
# Day facts: Friday closed 5-0-2 (success 6:51 AM; failure 1:51 PM; evening
# cluster success 6:07, failures 6:11/6:45/7:33/8:44 PM — four of five
# failures in the 6-9 window). Saturday 0-0-0 at 7:07 AM. Calendar: Saturday
# has only Style Bodhi! 10-1. Heart-Led Wellness invite is now a real event
# (first session Thu Nov 19 11-12, inside DW 8:30-12:30). GamifyOS Tuesday
# Sync 12-1 is NOT on the calendar this week (Tue drops 7.5h -> 6.5h).
# Laura's Tuesday IRIS invite still not landed; no Kimberly event (slot
# missed -> reschedule note is the follow-up). Pitch and Run renamed
# "Pitch and Run ATX", Fri Nov 20 8-9 (personal).
# Hazards: 'window open' must stay ==2 (one is 'window opened' in old ledger
# text); greeting count ==1; 'hit day thirty' is frozen (Sep 8 promises);
# eyebrow 'Friday, November 13' is unique; chart bars must stay ==7.
p = 'page-template.html'
s = open(p).read()

def rep(old, new, n):
    global s
    assert s.count(old) == n, (old[:60], s.count(old), n)
    s = s.replace(old, new)

def splice(start, end, new):
    """Replace from start-anchor through end-anchor (inclusive) with new."""
    global s
    assert s.count(start) == 1, start[:60]
    i = s.index(start)
    j = s.index(end, i) + len(end)
    s = s[:i] + new + s[j:]

# ---------- 1. Global age bumps (highest first) ----------
rep('day sixty-eight', 'day sixty-nine', 3)
rep('day sixty-seven', 'day sixty-eight', 3)
rep('night sixty', 'night sixty-one', 2)
rep('day fifty-nine', 'day sixty', 1)
rep('sixty-two days past', 'sixty-three days past', 4)
rep('fifty-two days past', 'fifty-three days past', 1)
rep('day thirty-three', 'day thirty-four', 1)
rep('Thirty days past', 'Thirty-one days past', 2)
rep('thirty days past', 'thirty-one days past', 2)
rep('(thirty days)', '(thirty-one days)', 2)
rep('Day twenty-five &mdash; one click closes it',
    'Day twenty-six &mdash; one click closes it', 1)
rep('day twenty-five', 'day twenty-six', 6)
rep('88 days', '89 days', 1)
rep('fifteen days past due', 'sixteen days past due', 2)
rep('is nine days old', 'is ten days old', 1)
rep('Ages as of Nov 13', 'Ages as of Nov 14', 1)

# ---------- 2. Stamps / header / greeting ----------
rep('2026-11-13T21:07:00-06:00', '2026-11-14T07:07:00-06:00', 2)
rep('<b>Brief compiled</b> Fri 6:13 AM &middot; data checked Fri 9:07 PM CT',
    '<b>Brief compiled</b> Fri 6:13 AM &middot; day turned &amp; data checked Sat 7:07 AM CT', 1)
rep('Friday, November 13', 'Saturday, November 14', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)

# ---------- 3. Masthead ----------
splice('Friday is the light day', 'No reactions saved.</p>',
 'Saturday, with one block on the calendar: <b>Style Bodhi! 10&ndash;1</b>. '
 'Friday closed <b>5&ndash;0&ndash;2</b> &mdash; quiet until 1:51, then an evening cluster '
 '(success 6:07; failures 6:11, 6:45, 7:33 and 8:44 PM) put four of the day&rsquo;s five failures '
 'in the 6&ndash;9 window. <b>The Kimberly slot came and went with no invite</b> &mdash; the follow-up '
 'is now a reschedule note: own the miss in one line Monday morning, propose two concrete times, '
 'and lock Taylor in. One thing turned real overnight: <b>the Heart-Led Wellness cadence is on the '
 'calendar</b> &mdash; first session Thursday 11&ndash;12 (Ashlyn &times; Taylor &times; you), inside '
 'the Deep Work block. Tuesday loosened a notch: <b>the GamifyOS Sync is not on this week&rsquo;s '
 'calendar</b> and Laura&rsquo;s IRIS invite still hasn&rsquo;t landed, so the pinch is Izzy 10 + '
 'Stratus demo 10:40 for now &mdash; but <b>the Stratus duplicate still needs consolidating before '
 'Tuesday</b> (your Tue 10:40 vs Jr&rsquo;s Wed 10:40, with the billing kickoff wanting Wed '
 '11&ndash;12 on top). <b>Three drafts still wait on Send</b>: Tim (day twenty-six), Affiliated '
 'Tech, GigTel. No reactions saved.</p>')

# ---------- 4. Ledger: close Friday, open Saturday ----------
rep('then an evening burst: <b>success 6:07</b>, <b>failures 6:11, 6:45, 7:33 and 8:44 PM</b> '
    '&mdash; <b>5&ndash;0&ndash;2 by 9:07, window open</b>.',
    'then an evening cluster: <b>success 6:07</b>, <b>failures 6:11, 6:45, 7:33 and 8:44 PM</b> '
    '&mdash; four of the five failures inside the 6&ndash;9 window, its loudest night since the '
    'streak broke Wednesday. <b>Friday closes 5&ndash;0&ndash;2</b>, seven events, verified '
    'Saturday morning with trash included. The overnight into Saturday stayed quiet; '
    '<b>Saturday stands 0&ndash;0&ndash;0 by 7:07 AM, window open</b>.', 1)

# ---------- 5. Today note + schedule ----------
rep('Light Friday, one loud clock &mdash; Kimberly&rsquo;s 2 PM slot is uninvited; '
    'PnR 8, EquiStamp 9, Dan 11, Review Crew 5:30',
    'Saturday &mdash; one block: Style Bodhi! 10&ndash;1; the Kimberly reschedule note '
    'is the Monday opener', 1)
splice('<div class="card sched" id="todaysched">', '</section>',
 '''<div class="card sched" id="todaysched">
        <div class="slot free"><div class="t">7:00&ndash;10:00</div><div class="w">Open morning<small>Nothing scheduled before ten</small></div></div>
        <div class="slot"><div class="t">10:00&ndash;1:00</div><div class="w">Style Bodhi!<small>Personal &mdash; the only block on the calendar</small></div></div>
        <div class="slot free"><div class="t">1:00&ndash;</div><div class="w">Open afternoon<small>If anything: the three drafts (Tim day twenty-six, Affiliated Tech, GigTel) and the Kimberly reschedule note are one sitting &mdash; none of it is a Saturday must</small></div></div>
      </div>
    </section>''')

# ---------- 6. Week chart: Sat 14 - Fri 20 ----------
splice('<div class="plot" id="plot">', '<div class="xaxis"',
 '''<div class="plot" id="plot">
          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>
          <div class="bar"><div class="tot" style="bottom:calc(21.43% + 6px)">3</div>
            <div class="seg p" style="height:21.43%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(48.21% + 6px)">6.75</div>
            <div class="seg m" style="height:12.5%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(53.57% + 6px)">7.5</div>
            <div class="seg m" style="height:14.29%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:3.57%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
            <div class="seg m" style="height:14.29%"></div><div class="seg f" style="height:32.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(7.14% + 6px)">1</div>
            <div class="seg p" style="height:7.14%"></div></div>
        </div>
        <div class="xaxis"''')
rep('''<div><b>Fri</b>13</div><div><b>Sat</b>14</div>
          <div><b>Sun</b>15</div><div><b>Mon</b>16</div><div><b>Tue</b>17</div><div><b>Wed</b>18</div><div><b>Thu</b>19</div>''',
    '''<div><b>Sat</b>14</div><div><b>Sun</b>15</div>
          <div><b>Mon</b>16</div><div><b>Tue</b>17</div><div><b>Wed</b>18</div><div><b>Thu</b>19</div><div><b>Fri</b>20</div>''', 1)
rep('Fri Nov 13 &ndash; Thu Nov 19', 'Sat Nov 14 &ndash; Fri Nov 20', 1)

# ---------- 7. Flag 1 ----------
splice('<h3><span class="pill warn">Today</span>', '</p>',
 '<h3><span class="pill warn">Carry-over</span> The Kimberly slot passed with no invite '
 '&mdash; the follow-up is a reschedule</h3>\n          '
 '<p><b>Kimberly Ragsdale asked for Friday 2 PM with Taylor joining</b>, briefed her co-CEOs, '
 'and the slot came and went without an event ever existing. The ask is a day old and cooling: '
 '<b>send a reschedule note Monday morning</b> &mdash; own the miss in one line, propose two '
 'concrete times, and lock Taylor in before her week fills. Nothing else has a Saturday clock: '
 'the <b>three drafts</b> (Tim day twenty-six, Affiliated Tech, GigTel) and the <b>Stratus '
 'consolidation</b> (Tue 17 vs Wed 18) are Monday work &mdash; though Stratus is the one with '
 'a deadline, since the duplicate demos start Tuesday 10:40.</p>')

# ---------- 8. Markers ----------
i = s.index('The week&rsquo;s markers</h4>')
j = s.index('<p ', i); k = s.index('</p>', j) + len('</p>')
s = s[:j] + ('<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Friday closed '
 '<b>5&ndash;0&ndash;2</b> &mdash; seven events: quiet until 1:51, then an evening cluster put '
 '<b>four failures in the 6&ndash;9 window</b> (6:11, 6:45, 7:33, 8:44) around a 6:07 success '
 '&mdash; the window&rsquo;s loudest night since the streak broke Wednesday. <b>The Kimberly '
 'invite never went out</b> and the slot passed: the reschedule note is the Monday opener. '
 '<b>Heart-Led Wellness is on the calendar</b> &mdash; first session Thursday 11&ndash;12 '
 '(Ashlyn &times; Taylor &times; you), inside the Deep Work block. <b>Tuesday loosened</b>: the '
 'GamifyOS Sync is off this week&rsquo;s calendar and Laura&rsquo;s IRIS invite hasn&rsquo;t '
 'landed &mdash; watch both; <b>Stratus</b> stays double-booked (Tue 17 yours, Wed 18 Jr&rsquo;s, '
 'billing kickoff stacked on Wednesday): consolidate to Tuesday. <b>Nortec&rsquo;s ball is in '
 'their court</b> since Jr&rsquo;s Thursday 1:50 send. <b>GigTel</b> draft pending; '
 '<b>Threshold</b> waiting on the NDA check; <b>the Tim record is day twenty-six</b> &mdash; '
 'Tuesday&rsquo;s Izzy checkin is the natural close. Whether <b>alert routing shipped Friday</b> '
 'is unconfirmed &mdash; so is the GamifyOS go-live.</p>') + s[k:]

# ---------- 9. Coming up ----------
i = s.index('A light Friday with one loud clock, then the Tuesday pinch</h4>')
s = s[:i] + 'A quiet weekend, then a demo-day Tuesday and a stacked Wednesday</h4>' + \
    s[i + len('A light Friday with one loud clock, then the Tuesday pinch</h4>'):]
i = s.index('A quiet weekend, then a demo-day Tuesday and a stacked Wednesday</h4>')
j = s.index('<p ', i); k = s.index('</p>', j) + len('</p>')
s = s[:j] + ('<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Today: <b>Style Bodhi! '
 '10&ndash;1</b>, nothing else. Sunday: clear. Monday Nov 16 &mdash; 6.75h: sync 8, DW Engineering '
 '10&ndash;2 with <b>Call Ken at noon</b> inside it, TTT 2 &mdash; plus the <b>Kimberly reschedule '
 'note</b> and the <b>Stratus consolidation</b> first thing. Tuesday Nov 17 &mdash; 6.5h: <b>Izzy '
 'checkin 10</b> and <b>Stratus demo 10:40</b> inside DW Client 10&ndash;2 (the GamifyOS Sync is '
 'off this week&rsquo;s calendar; Laura&rsquo;s IRIS invite could still land here). Wednesday '
 'Nov 18 &mdash; 7.5h, the stacked one: Recover 9, SustAmb 9:30, <b>Jr&rsquo;s demo event 10:40</b> '
 '(cancel one), <b>billing kickoff 11&ndash;12</b>, DW 11&ndash;3, TTT 3. Thursday Nov 19 &mdash; '
 '6.5h: DW 8:30&ndash;12:30 with <b>Heart-Led Wellness 11&ndash;12 inside it</b> (first session), '
 'Reserved 3:30, <b>Scott Van Camp 4</b>. Friday Nov 20: <b>Pitch and Run 8</b> (renamed, '
 'run-group week). Carried: <b>the Cathy call</b> (thirty-one days), <b>the CCI booking</b>, the '
 'drip and performance reports, the ATS five, the Whova trio, the Sahiti intro, the <b>Rev.io '
 'sessions ask</b>, and the <b>invoice &mdash; sixteen days past due unless the ACH cleared '
 'it</b>.</p>') + s[k:]

# ---------- Sanity ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-14T07:07:00-06:00') == 2
assert s.count('window open') == 2
assert s.count('Good morning, Bodhi') == 1 and s.count('Good evening, Bodhi') == 0
assert s.count('Saturday, November 14') == 1
assert s.count('hit day thirty') == 1
for bad in ['ebccf397', 'atscall', '3,082', 'Jose Luiz', '5WY67Sa2', 'PasswordReset',
            'billcenter.net', 'hw7Mh6cK', 'pY3DM73R', 'bT5uDhjRSBk3']:
    assert bad not in s, bad
open(p, 'w').write(s)
print('saturday turn ok', len(s))
