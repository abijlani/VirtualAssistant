# Monday Nov 16 FULL morning pass (fired 6:13 AM CT). Day facts: Sunday closed
# 12-3-10 = 25 events (busiest day ever, +7 over the old 18; twelve failures a
# new single-day record; late success 11:11 PM; overnight into Monday quiet).
# cc-state: no reactions saved (no page-save republish has ever occurred;
# wake subscription intact). Drafts now FOUR: Laura reply (new, Fri 9:08 AM),
# Tim (day twenty-eight), Affiliated Tech, GigTel. Taylor sent the Dec 11
# "Gamify Your Life" workshop concept to Caroline & Ellie (Bodhi CC'd) Sunday.
# Eelco created a QuickBooks app "Smart Konnect" on the Voxtell dev account.
# Calendar: Mon 6.75h (sync 8, DW Eng 10-2, Call Ken 12-1 inside, TTT 2);
# Stratus duplicate still live (Tue 10:40 Bodhi's vs Wed 10:40 Jr's); no
# Kimberly event; no Laura IRIS Tuesday invite. Chart rolls Mon 16 - Sun 22.
# Hazards: 'window open' stays ==2; greeting ==1; bars ==7; 'hit day thirty'
# frozen; 'day seventy' bump FIRST (before sixty-nine -> seventy).
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
rep('day seventy', 'day seventy-one', 3)
rep('day sixty-nine', 'day seventy', 3)
rep('night sixty-two', 'night sixty-three', 2)
rep('day sixty-one', 'day sixty-two', 1)
rep('sixty-four days past', 'sixty-five days past', 4)
rep('fifty-four days past', 'fifty-five days past', 1)
rep('day thirty-five', 'day thirty-six', 1)
rep('Thirty-two days past', 'Thirty-three days past', 2)
rep('thirty-two days past', 'thirty-three days past', 2)
rep('(thirty-two days)', '(thirty-three days)', 2)
rep('Day twenty-seven &mdash; one click closes it',
    'Day twenty-eight &mdash; one click closes it', 1)
rep('day twenty-seven', 'day twenty-eight', 5)
rep('90 days', '91 days', 1)
rep('seventeen days past due', 'eighteen days past due', 2)
rep('is eleven days old', 'is twelve days old', 1)
rep('Ages as of Nov 15', 'Ages as of Nov 16', 1)

# ---------- 2. Stamps / header / greeting ----------
rep('2026-11-15T21:07:00-06:00', '2026-11-16T06:13:00-06:00', 2)
rep('<b>Brief compiled</b> Fri 6:13 AM &middot; data checked Sun 9:07 PM CT',
    '<b>Brief compiled</b> Mon 6:13 AM &middot; data checked Mon 6:13 AM CT', 1)
rep('Sunday, November 15', 'Monday, November 16', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)

# ---------- 3. Masthead ----------
splice('Sunday, clear by design', 'No reactions saved.</p>',
 'Monday opens the week with a first-thing pair in the 8:45&ndash;10 gap after sync: <b>the '
 'Kimberly reschedule note</b> (her Friday 2 PM ask passed uninvited and is now three days old '
 '&mdash; one line owning the miss, two concrete times, Taylor locked in) and <b>the Stratus '
 'consolidation</b> (your Tuesday 10:40 demo vs Jr&rsquo;s Wednesday 10:40 &mdash; the duplicate '
 'fires <i>tomorrow morning</i>; cancel one today, Tuesday should win). The day itself: <b>sync '
 '8</b>, <b>Deep Work Engineering 10&ndash;2</b> with <b>Call Ken at noon</b> inside it, TTT 2. '
 'The loud story is the ledger: <b>Sunday closed 12&ndash;3&ndash;10 &mdash; twenty-five events, '
 'the busiest day ever recorded</b>, with twelve failures a new single-day record; worth asking '
 'what ran Sunday. <b>Four drafts now wait on Send</b>: a new reply to Laura (sitting since '
 'Friday morning), Tim (day twenty-eight &mdash; tomorrow&rsquo;s Izzy checkin is the natural '
 'close), Affiliated Tech, GigTel. Quieter news: <b>Taylor sent Caroline and Ellie the Dec 11 '
 'workshop concept</b> (you CC&rsquo;d &mdash; curriculum ball now in Gevity&rsquo;s court), and '
 '<b>Eelco spun up a QuickBooks app, &ldquo;Smart Konnect,&rdquo;</b> on the Voxtell developer '
 'account &mdash; billing-platform plumbing ahead of Wednesday&rsquo;s kickoff. '
 'No reactions saved.</p>')

# ---------- 4. Ledger: close Sunday, open Monday ----------
rep('a <b>needs-attention at 7:17</b> and a <b>failure at 8:53</b>: <b>12&ndash;3&ndash;9 by '
    '9:07, window open</b>. Twenty-four events is a new all-time daily record, and twelve '
    'failures a new single-day failure record.',
    'a <b>needs-attention at 7:17</b>, a <b>failure at 8:53</b> and a late <b>success at 11:11 '
    'PM</b>. <b>Sunday closes 12&ndash;3&ndash;10</b> &mdash; twenty-five events, verified Monday '
    'morning with trash included: the busiest day on the ledger by seven events, with <b>twelve '
    'failures</b> a new single-day failure record (the old record of ten stood twice). The '
    'overnight into Monday stayed quiet; <b>Monday stands 0&ndash;0&ndash;0 by 6:13 AM, window '
    'open</b>.', 1)

# ---------- 5. Today note + schedule ----------
rep('Sunday &mdash; clear by design; Monday opens with the Kimberly note and the '
    'Stratus consolidation',
    'Monday &mdash; sync 8, DW Engineering 10&ndash;2 with Call Ken at noon inside it; '
    'first thing: the Kimberly note and the Stratus consolidation', 1)
splice('<div class="card sched" id="todaysched">', '</section>',
 '''<div class="card sched" id="todaysched">
        <div class="slot"><div class="t">8:00&ndash;8:45</div><div class="w">Weekly Product Sync<small>Eelco + Jr &mdash; ask about the new &ldquo;Smart Konnect&rdquo; QuickBooks app and where PR #1158 stands</small></div></div>
        <div class="slot free"><div class="t">8:45&ndash;10:00</div><div class="w">Open &mdash; the first-thing pair<small><b>Send the Kimberly reschedule note</b> (two concrete times, Taylor locked in) and <b>cancel one Stratus demo</b> before the duplicate fires tomorrow 10:40</small></div></div>
        <div class="slot"><div class="t">10:00&ndash;2:00</div><div class="w">Deep Work (Engineering)<small><b>Call Ken sits inside it, 12&ndash;1</b> &mdash; the block is really 10&ndash;12 + 1&ndash;2</small></div></div>
        <div class="slot"><div class="t">2:00&ndash;3:00</div><div class="w">Transition, Talking, Triage<small>The four drafts in one sitting: Laura (new Friday), Tim day twenty-eight, Affiliated Tech, GigTel</small></div></div>
      </div>
    </section>''')

# ---------- 6. Week chart: Mon 16 - Sun 22 ----------
splice('<div class="plot" id="plot">', '<div class="xaxis"',
 '''<div class="plot" id="plot">
          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>
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
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
        </div>
        <div class="xaxis"''')
rep('''<div><b>Sun</b>15</div><div><b>Mon</b>16</div>
          <div><b>Tue</b>17</div><div><b>Wed</b>18</div><div><b>Thu</b>19</div><div><b>Fri</b>20</div><div><b>Sat</b>21</div>''',
    '''<div><b>Mon</b>16</div><div><b>Tue</b>17</div>
          <div><b>Wed</b>18</div><div><b>Thu</b>19</div><div><b>Fri</b>20</div><div><b>Sat</b>21</div><div><b>Sun</b>22</div>''', 1)
rep('Sun Nov 15 &ndash; Sat Nov 21', 'Mon Nov 16 &ndash; Sun Nov 22', 1)

# ---------- 7. Flag 1 ----------
splice('<h3><span class="pill warn">Monday</span>', '</p>',
 '<h3><span class="pill warn">Today</span> The first-thing pair &mdash; and a record Sunday '
 'worth a look</h3>\n          '
 '<p><b>Kimberly Ragsdale&rsquo;s ask is three days old</b>: send the reschedule note in the '
 '8:45&ndash;10 gap &mdash; own the miss in one line, propose two concrete times, lock Taylor '
 'in. <b>The Stratus duplicate fires tomorrow 10:40</b>: cancel one demo today (Tuesday should '
 'win &mdash; it dodges Wednesday&rsquo;s kickoff stack). And <b>Sunday&rsquo;s ledger deserves '
 'two minutes</b>: twenty-five events on a day with nothing scheduled &mdash; an all-success '
 'morning, a nine-event storm in the 11 o&rsquo;clock hour, twelve failures by day&rsquo;s end. '
 'If a client campaign or a migration ran Sunday, fine; if not, something is retrying hard and '
 'failing often.</p>')

# ---------- 8. Markers ----------
i = s.index('The week&rsquo;s markers</h4>')
j = s.index('<p ', i); k = s.index('</p>', j) + len('</p>')
s = s[:j] + ('<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Sunday closed '
 '<b>12&ndash;3&ndash;10</b> &mdash; twenty-five events, the busiest day on the ledger by seven, '
 'and <b>twelve failures</b> a new single-day record. The shape: all-success morning (8:23, '
 '9:33, 9:46), a <b>nine-event storm between 11:15 and 11:54</b>, steady failures through the '
 'afternoon, four events in the 6&ndash;9 window &mdash; the fifth evening running &mdash; and a '
 'late success at 11:11 PM. <b>Worth asking what ran Sunday.</b> Saturday before it was '
 '1&ndash;0&ndash;1; Friday 5&ndash;0&ndash;2. Pipeline: <b>Kimberly</b> reschedule note goes '
 'today; <b>Stratus</b> duplicate resolves today or fires tomorrow 10:40; <b>Nortec</b> quiet '
 'since Jr&rsquo;s Thursday send; <b>GigTel</b> and <b>Affiliated Tech</b> drafts pending, plus '
 'a <b>new Laura reply drafted Friday</b>; <b>Threshold</b> on the NDA check; <b>Heart-Led '
 'Wellness</b> first session Thursday 11&ndash;12 inside Deep Work. <b>Taylor sent the Dec 11 '
 'workshop concept to Caroline and Ellie</b> &mdash; curriculum ball in Gevity&rsquo;s court. '
 '<b>Eelco created &ldquo;Smart Konnect,&rdquo; a QuickBooks app</b> on the Voxtell developer '
 'account &mdash; billing-platform plumbing before Wednesday&rsquo;s kickoff. <b>The Tim record '
 'is day twenty-eight</b> &mdash; tomorrow&rsquo;s Izzy checkin is the natural close. Alert '
 'routing and the GamifyOS go-live both remain unconfirmed.</p>') + s[k:]

# ---------- 9. Coming up ----------
old_h4 = 'A clear Sunday, then a demo-day Tuesday and a stacked Wednesday</h4>'
new_h4 = 'A steady Monday, a demo-day Tuesday, a stacked Wednesday</h4>'
i = s.index(old_h4)
s = s[:i] + new_h4 + s[i + len(old_h4):]
i = s.index(new_h4)
j = s.index('<p ', i); k = s.index('</p>', j) + len('</p>')
s = s[:j] + ('<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Today &mdash; 6.75h: '
 'sync 8, DW Engineering 10&ndash;2 with <b>Call Ken at noon</b> inside it, TTT 2 &mdash; and '
 'the <b>Kimberly note</b> + <b>Stratus consolidation</b> first thing. Tuesday Nov 17 &mdash; '
 '6.5h: <b>Izzy checkin 10</b> and <b>Stratus demo 10:40</b> inside DW Client 10&ndash;2 '
 '(close Tim on the checkin). Wednesday Nov 18 &mdash; 7.5h, the stacked one: Recover 9, SustAmb '
 '9:30, <b>Jr&rsquo;s demo event 10:40</b> (should be gone by then), <b>billing kickoff '
 '11&ndash;12</b>, DW 11&ndash;3, TTT 3. Thursday Nov 19 &mdash; 6.5h: DW 8:30&ndash;12:30 with '
 '<b>Heart-Led Wellness 11&ndash;12 inside it</b> (first session), Reserved 3:30, <b>Scott Van '
 'Camp 4</b>. Friday Nov 20: <b>Pitch and Run 8</b>, then a clear weekend. Next week: <b>ATS '
 'catch-up Tue 24, 10:30</b> and <b>GamifyOS Sync Tue 24, 12&ndash;1</b>. Carried: <b>the Cathy '
 'call</b> (thirty-three days), <b>the CCI booking</b>, the drip and performance reports, the '
 'ATS five, the Whova trio, the Sahiti intro, the <b>Rev.io sessions ask</b>, and the '
 '<b>invoice &mdash; eighteen days past due unless the ACH cleared it</b>.</p>') + s[k:]

# ---------- Sanity ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-16T06:13:00-06:00') == 2
assert s.count('window open') == 2
assert s.count('Good morning, Bodhi') == 1 and s.count('Good evening, Bodhi') == 0
assert s.count('Monday, November 16') == 1
assert s.count('hit day thirty') == 1
for bad in ['ebccf397', 'atscall', '3,082', 'Jose Luiz', '5WY67Sa2', 'PasswordReset',
            'billcenter.net', 'hw7Mh6cK', 'pY3DM73R', 'bT5uDhjRSBk3', 'mm7me9zr']:
    assert bad not in s, bad
open(p, 'w').write(s)
print('monday turn ok', len(s))
