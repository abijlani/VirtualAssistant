# Sunday Nov 15 day-turn — run by the 7:08 AM CT light tick (morning full-pass
# trigger is weekdays-only). Day facts: Saturday closed 1-0-1 (failure 6:33 PM,
# success 6:58 PM — both in the 6-9 window; the window has produced events four
# evenings running, Wednesday Nov 11 excepted). Sunday 0-0-0, calendar clear
# (Sundays in nature). Calendar news: GamifyOS Sync landed on Tue Nov 24 12-1
# (NOT this week); ATS/Voxtell weekly catch-up Tue Nov 24 10:30; still no
# Kimberly event and no Laura IRIS Tuesday invite. Chart rolls Sun 15 - Sat 21:
# Sun 0 / Mon 6.75 / Tue 6.5 / Wed 7.5 / Thu 6.5 / Fri 1 / Sat 0.
# Hazards: 'window open' must stay ==2; greeting ==1; bare 'day sixty' needs
# regex (substring of sixty-eight/sixty-nine); 'hit day thirty' frozen; bars ==7.
import re
p = 'page-template.html'
s = open(p).read()

def rep(old, new, n):
    global s
    assert s.count(old) == n, (old[:60], s.count(old), n)
    s = s.replace(old, new)

def splice(start, end, new):
    global s
    assert s.count(start) == 1, start[:60]
    i = s.index(start)
    j = s.index(end, i) + len(end)
    s = s[:i] + new + s[j:]

# ---------- 1. Global age bumps (highest first) ----------
rep('day sixty-nine', 'day seventy', 3)
rep('day sixty-eight', 'day sixty-nine', 3)
rep('night sixty-one', 'night sixty-two', 2)
assert len(re.findall(r'day sixty(?!-)', s)) == 1
s = re.sub(r'day sixty(?!-)', 'day sixty-one', s)
rep('sixty-three days past', 'sixty-four days past', 4)
rep('fifty-three days past', 'fifty-four days past', 1)
rep('day thirty-four', 'day thirty-five', 1)
rep('Thirty-one days past', 'Thirty-two days past', 2)
rep('thirty-one days past', 'thirty-two days past', 2)
rep('(thirty-one days)', '(thirty-two days)', 2)
rep('Day twenty-six &mdash; one click closes it',
    'Day twenty-seven &mdash; one click closes it', 1)
rep('day twenty-six', 'day twenty-seven', 6)
rep('89 days', '90 days', 1)
rep('sixteen days past due', 'seventeen days past due', 2)
rep('is ten days old', 'is eleven days old', 1)
rep('Ages as of Nov 14', 'Ages as of Nov 15', 1)

# ---------- 2. Stamps / header / greeting ----------
rep('2026-11-14T21:07:00-06:00', '2026-11-15T07:08:00-06:00', 2)
rep('<b>Brief compiled</b> Fri 6:13 AM &middot; data checked Sat 9:07 PM CT',
    '<b>Brief compiled</b> Fri 6:13 AM &middot; day turned &amp; data checked Sun 7:08 AM CT', 1)
rep('Saturday, November 14', 'Sunday, November 15', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)

# ---------- 3. Masthead ----------
splice('Saturday, with one block on the calendar', 'No reactions saved.</p>',
 'Sunday, clear by design &mdash; the rhythm says nature and the calendar agrees: nothing '
 'scheduled. Saturday closed <b>1&ndash;0&ndash;1</b>: silent all day until the 6&ndash;9 window '
 'produced a <b>failure at 6:33 PM</b> and a <b>success at 6:58</b> &mdash; that window has now '
 'spoken four evenings running. Monday opens the real week with a first-thing pair: <b>the '
 'Kimberly reschedule note</b> (her Friday 2 PM ask passed uninvited, two days old by Monday) and '
 '<b>the Stratus consolidation</b> (your Tue 10:40 demo vs Jr&rsquo;s Wed 10:40, kickoff stacked '
 'on Wednesday &mdash; the duplicate fires Tuesday morning if nobody cancels one). One calendar '
 'confirmation overnight Friday: <b>the GamifyOS Sync landed on Tuesday Nov 24, 12&ndash;1</b> '
 '&mdash; not this week &mdash; so Tuesday the 17th stays Izzy 10 + Stratus demo 10:40, and '
 'Laura&rsquo;s IRIS invite still hasn&rsquo;t appeared. <b>Three drafts still wait on Send</b>: '
 'Tim (day twenty-seven), Affiliated Tech, GigTel. No reactions saved.</p>')

# ---------- 4. Ledger: close Saturday, open Sunday ----------
rep('a <b>failure at 6:33 PM</b>, then a <b>success at 6:58</b> &mdash; '
    '<b>1&ndash;0&ndash;1 by 9:07, window open</b>.',
    'a <b>failure at 6:33 PM</b>, then a <b>success at 6:58</b> &mdash; <b>Saturday closes '
    '1&ndash;0&ndash;1</b>, two events, verified Sunday morning with trash included; the '
    '6&ndash;9 window has now produced events four evenings running. The overnight into Sunday '
    'stayed quiet; <b>Sunday stands 0&ndash;0&ndash;0 by 7:08 AM, window open</b>.', 1)

# ---------- 5. Today note + schedule ----------
rep('Saturday &mdash; one block: Style Bodhi! 10&ndash;1; the Kimberly reschedule note '
    'is the Monday opener',
    'Sunday &mdash; clear by design; Monday opens with the Kimberly note and the '
    'Stratus consolidation', 1)
splice('<div class="card sched" id="todaysched">', '</section>',
 '''<div class="card sched" id="todaysched">
        <div class="slot free"><div class="t">All day</div><div class="w">Nothing scheduled<small>Sundays are for nature &mdash; the week starts Monday with sync at 8, and the Kimberly note + Stratus consolidation are the first desk items</small></div></div>
      </div>
    </section>''')

# ---------- 6. Week chart: Sun 15 - Sat 21 ----------
splice('<div class="plot" id="plot">', '<div class="xaxis"',
 '''<div class="plot" id="plot">
          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>
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
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
        </div>
        <div class="xaxis"''')
rep('''<div><b>Sat</b>14</div><div><b>Sun</b>15</div>
          <div><b>Mon</b>16</div><div><b>Tue</b>17</div><div><b>Wed</b>18</div><div><b>Thu</b>19</div><div><b>Fri</b>20</div>''',
    '''<div><b>Sun</b>15</div><div><b>Mon</b>16</div>
          <div><b>Tue</b>17</div><div><b>Wed</b>18</div><div><b>Thu</b>19</div><div><b>Fri</b>20</div><div><b>Sat</b>21</div>''', 1)
rep('Sat Nov 14 &ndash; Fri Nov 20', 'Sun Nov 15 &ndash; Sat Nov 21', 1)

# ---------- 7. Flag 1 ----------
splice('<h3><span class="pill warn">Carry-over</span>', '</p>',
 '<h3><span class="pill warn">Monday</span> Two opens before the week starts rolling: the '
 'Kimberly note and the Stratus consolidation</h3>\n          '
 '<p><b>Kimberly Ragsdale&rsquo;s Friday 2 PM slot passed with no invite</b> &mdash; the ask is '
 'two days old by Monday morning: own the miss in one line, propose two concrete times, and lock '
 'Taylor in before her week fills. <b>Stratus is still double-booked</b> &mdash; your Tuesday '
 '10:40 demo vs Jr&rsquo;s Wednesday 10:40, with the billing kickoff wanting Wednesday '
 '11&ndash;12 on top: consolidate to Tuesday before the duplicate fires. Behind those: the '
 '<b>three drafts</b> (Tim day twenty-seven, Affiliated Tech, GigTel) and the <b>GamifyOS '
 'curriculum for Caroline</b>.</p>')

# ---------- 8. Markers ----------
i = s.index('The week&rsquo;s markers</h4>')
j = s.index('<p ', i); k = s.index('</p>', j) + len('</p>')
s = s[:j] + ('<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Saturday closed '
 '<b>1&ndash;0&ndash;1</b> &mdash; silent until the 6&ndash;9 window: failure 6:33, success 6:58. '
 'Friday before it closed <b>5&ndash;0&ndash;2</b> with four of five failures in that same window '
 '&mdash; <b>the evening window has produced events four nights running</b>, and it is where the '
 'failures live: worth a look at what changes after 6 PM. <b>The Kimberly invite never went '
 'out</b>: the reschedule note is Monday&rsquo;s opener. <b>Heart-Led Wellness is on the '
 'calendar</b> &mdash; first session Thursday 11&ndash;12, inside Deep Work. <b>The GamifyOS Sync '
 'landed on Tuesday Nov 24</b>, not this week, and <b>ATS moved to a weekly Tuesday 10:30 '
 'catch-up</b> starting the 24th &mdash; Tuesday the 17th stays Izzy + Stratus demo, with '
 'Laura&rsquo;s IRIS invite still unlanded. <b>Stratus</b> stays double-booked (Tue 17 yours, '
 'Wed 18 Jr&rsquo;s + kickoff): consolidate to Tuesday. <b>Nortec&rsquo;s ball is in their '
 'court</b> since Jr&rsquo;s Thursday send. <b>GigTel</b> draft pending; <b>Threshold</b> waiting '
 'on the NDA check; <b>the Tim record is day twenty-seven</b> &mdash; Tuesday&rsquo;s Izzy checkin '
 'is the natural close. Alert routing and the GamifyOS go-live both remain unconfirmed.</p>') + s[k:]

# ---------- 9. Coming up ----------
old_h4 = 'A quiet weekend, then a demo-day Tuesday and a stacked Wednesday</h4>'
new_h4 = 'A clear Sunday, then a demo-day Tuesday and a stacked Wednesday</h4>'
i = s.index(old_h4)
s = s[:i] + new_h4 + s[i + len(old_h4):]
i = s.index(new_h4)
j = s.index('<p ', i); k = s.index('</p>', j) + len('</p>')
s = s[:j] + ('<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Today: clear. Monday '
 'Nov 16 &mdash; 6.75h: sync 8, DW Engineering 10&ndash;2 with <b>Call Ken at noon</b> inside it, '
 'TTT 2 &mdash; plus the <b>Kimberly reschedule note</b> and the <b>Stratus consolidation</b> '
 'first thing. Tuesday Nov 17 &mdash; 6.5h: <b>Izzy checkin 10</b> and <b>Stratus demo 10:40</b> '
 'inside DW Client 10&ndash;2. Wednesday Nov 18 &mdash; 7.5h, the stacked one: Recover 9, SustAmb '
 '9:30, <b>Jr&rsquo;s demo event 10:40</b> (cancel one), <b>billing kickoff 11&ndash;12</b>, DW '
 '11&ndash;3, TTT 3. Thursday Nov 19 &mdash; 6.5h: DW 8:30&ndash;12:30 with <b>Heart-Led Wellness '
 '11&ndash;12 inside it</b> (first session), Reserved 3:30, <b>Scott Van Camp 4</b>. Friday '
 'Nov 20: <b>Pitch and Run 8</b>. Next week adds <b>ATS catch-up Tue 24, 10:30</b> and the '
 '<b>GamifyOS Sync Tue 24, 12&ndash;1</b>. Carried: <b>the Cathy call</b> (thirty-two days), '
 '<b>the CCI booking</b>, the drip and performance reports, the ATS five, the Whova trio, the '
 'Sahiti intro, the <b>Rev.io sessions ask</b>, and the <b>invoice &mdash; seventeen days past '
 'due unless the ACH cleared it</b>.</p>') + s[k:]

# ---------- Sanity ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-15T07:08:00-06:00') == 2
assert s.count('window open') == 2
assert s.count('Good morning, Bodhi') == 1 and s.count('Good evening, Bodhi') == 0
assert s.count('Sunday, November 15') == 1
assert s.count('hit day thirty') == 1
for bad in ['ebccf397', 'atscall', '3,082', 'Jose Luiz', '5WY67Sa2', 'PasswordReset',
            'billcenter.net', 'hw7Mh6cK', 'pY3DM73R', 'bT5uDhjRSBk3', 'mm7me9zr']:
    assert bad not in s, bad
open(p, 'w').write(s)
print('sunday turn ok', len(s))
