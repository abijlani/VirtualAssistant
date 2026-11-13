# Friday Nov 14... no: Friday Nov 13, 2026 full-pass day turn (fired 6:13 AM CT).
# Day facts: Thursday closed 3-1-5, nine events - first weekday with a success
# majority (morning burst: 5 successes through 7:28 + 2 failures through 7:20,
# fastest morning on ledger; then NA 6:54 PM, failure 7:56 PM - evening failure
# returned). Friday is light with one loud clock: the KIMBERLY 2 PM SLOT IS
# TODAY and the invite was never sent. New events: "Finish Honor's Proposal
# (EquiStamp)" moved to Fri 9-10 (prep Notion doc on event); "Bodhi <> Dan
# catch-up" 11-11:30 (dan@visionsoftware.ai). Overnight: Jr re-engaged Nortec
# 1:50 PM Thu - updated proposal finally SENT to Tyler Froemming + Steve Myhre
# ("I never followed up to let you know it was ready") - the silence is
# explained: the proposal had not been sent. LiveKit invoice paid (routine,
# off page). Drafts still three (Tim day 25). Granola: no Thursday notes.
# Chart rolls Fri Nov 13 - Thu Nov 19. Stratus duplicate + Wed-18 kickoff
# unchanged. Greeting already 'Good morning' (Thursday evening flip skipped).
import re

p = 'page-template.html'
s = open(p).read()

def rep(old, new, n):
    global s
    c = s.count(old)
    assert c == n, (old[:60], c, n)
    s = s.replace(old, new)

# ---------- 1. Global age bumps (highest first) ----------
rep('day sixty-seven', 'day sixty-eight', 3)
rep('day sixty-six', 'day sixty-seven', 3)
rep('night fifty-nine', 'night sixty', 2)
rep('day fifty-eight;', 'day fifty-nine;', 1)
rep('sixty-one days past', 'sixty-two days past', 4)
rep('fifty-one days past', 'fifty-two days past', 1)
rep('day thirty-two', 'day thirty-three', 1)
rep('twenty-nine days past', 'thirty days past', 2)
rep('Twenty-nine', 'Thirty', 2)
rep('(twenty-nine days)', '(thirty days)', 2)
rep('day twenty-four', 'day twenty-five', 6)
rep('Day twenty-four &mdash; one click closes it', 'Day twenty-five &mdash; one click closes it', 1)
rep('87 days', '88 days', 1)
rep('Ages as of Nov 12', 'Ages as of Nov 13', 1)
rep('fourteen days past due', 'fifteen days past due', 2)
rep('is eight days old', 'is nine days old', 1)

# ---------- 2. Stamps / header ----------
rep('2026-11-12T21:07:00-06:00', '2026-11-13T06:13:00-06:00', 2)
rep('<b>Brief compiled</b> Thu 6:13 AM &middot; data checked Thu 9:07 PM CT',
    '<b>Brief compiled</b> Fri 6:13 AM &middot; data checked Fri 6:13 AM CT', 1)
rep('Thursday, November 12', 'Friday, November 13', 1)

# ---------- 3. Masthead ----------
masthead = (
 'Friday is the light day with one loud clock: <b>the Kimberly Ragsdale discovery slot is today at '
 '2 PM and the invite never went out</b> &mdash; she briefed Lauren and Janet yesterday expecting it. '
 'Send it this morning (or propose a new time) and lock Taylor in; everything else can flex. The day '
 'itself: <b>Pitch and Run 8&ndash;9</b> (walk-group week), <b>Finish Honor&rsquo;s Proposal '
 '(EquiStamp) 9&ndash;10</b> &mdash; rescheduled from yesterday with a prep doc on the event &mdash; a '
 'new <b>Dan catch-up at 11</b> (Vision Software), and <b>Review Crew happy hour 5:30 at Remedy</b>. '
 'Overnight the Nortec story turned: <b>Jr sent Tyler Froemming and Steve Myhre the updated proposal '
 'at 1:50</b>, apologizing that it had sat ready without a follow-up &mdash; the three-week silence '
 'was a dropped baton, not a cold buyer, and the ball is now theirs. <b>Per-location alert routing is '
 'due to production today</b> (RV Country, 11 assistants). <b>Three drafts still wait on Send</b>: '
 'Tim (day twenty-five), Affiliated Tech, GigTel. <b>The Stratus duplicate still stands</b> &mdash; '
 'your Tuesday 10:40 event vs Jr&rsquo;s Wednesday one, with Jr&rsquo;s billing kickoff wanting '
 'Wednesday 11&ndash;12 on top of his own demo slot: consolidate to Tuesday. Thursday closed '
 '<b>3&ndash;1&ndash;5</b> &mdash; the first weekday where successes outnumbered failures. '
 'No reactions saved.</p>')
i = s.index('Thursday is the heaviest day of the week')
j = s.index('No reactions saved.</p>', i) + len('No reactions saved.</p>')
s = s[:i] + masthead + s[j:]

# ---------- 4. Ledger: close Thursday, open Friday ----------
rep('until a <b>needs-attention at 6:54 PM</b> and a <b>failure at 7:56 PM</b> &mdash; the 6&ndash;9 '
    'window produced a failure again after Wednesday&rsquo;s clean evening &mdash; <b>3&ndash;1&ndash;5 '
    'by 9:07, window open</b>.',
    'until a <b>needs-attention at 6:54 PM</b> and a <b>failure at 7:56 PM</b> &mdash; the 6&ndash;9 '
    'window produced a failure again after Wednesday&rsquo;s clean evening. <b>Thursday closes '
    '3&ndash;1&ndash;5</b>, nine events, verified Friday morning with trash included &mdash; the first '
    'weekday on the ledger where successes outnumbered failures. The overnight into Friday stayed '
    'quiet &mdash; <b>0&ndash;0&ndash;0 by 6:13, window open</b>.', 1)

# ---------- 5. Today note + schedule ----------
rep('Heaviest day of the week &mdash; 9.75h: Honor proposal 9, DW 10&ndash;2, Scott 2, Tash 4:45, '
    'Friendsgiving 6&ndash;9',
    'Light Friday, one loud clock &mdash; Kimberly&rsquo;s 2 PM slot is uninvited; PnR 8, EquiStamp 9, '
    'Dan 11, Review Crew 5:30', 1)

sched = '''<div class="card sched" id="todaysched">
        <div class="slot"><div class="t">8:00&ndash;9:00</div><div class="w">Pitch and Run/Walk ATX<small>Personal &mdash; first one since registering; the 2-mile walk group runs this week</small></div></div>
        <div class="slot"><div class="t">9:00&ndash;10:00</div><div class="w">Finish Honor&rsquo;s Proposal (EquiStamp)<small>Rescheduled from yesterday, prep doc on the event &mdash; and <b>send the Kimberly invite for 2 PM at the top of this block</b>, before the proposal swallows the hour</small></div></div>
        <div class="slot"><div class="t">11:00&ndash;11:30</div><div class="w">Bodhi &lt;&gt; Dan catch-up<small>Vision Software &mdash; your event, created yesterday afternoon</small></div></div>
        <div class="slot free"><div class="t">11:30&ndash;5:30</div><div class="w">Open afternoon<small>The <b>Kimberly discovery call lands at 2</b> if the invite goes out this morning; around it: the three drafts (Tim day twenty-five, Affiliated Tech, GigTel), the Stratus consolidation, the GamifyOS curriculum for Caroline</small></div></div>
        <div class="slot"><div class="t">5:30&ndash;7:00</div><div class="w">Review Crew: Happy Hour &mdash; Remedy<small>Austin Business Review crowd</small></div></div>
      </div>
    </section>'''
i = s.index('<div class="card sched" id="todaysched">')
j = s.index('</section>', i) + len('</section>')
s = s[:i] + sched + s[j:]

# ---------- 6. Chart: roll week Fri Nov 13 - Thu Nov 19 ----------
rep('Thu Nov 12 &ndash; Wed Nov 18', 'Fri Nov 13 &ndash; Thu Nov 19', 1)
plot = '''<div class="plot" id="plot">
          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>
          <div class="bar"><div class="tot" style="bottom:calc(28.57% + 6px)">4</div>
            <div class="seg m" style="height:21.43%"></div><div class="seg p" style="height:7.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(21.43% + 6px)">3</div>
            <div class="seg p" style="height:21.43%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(48.21% + 6px)">6.75</div>
            <div class="seg m" style="height:12.5%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(53.57% + 6px)">7.5</div>
            <div class="seg m" style="height:17.86%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(53.57% + 6px)">7.5</div>
            <div class="seg m" style="height:14.29%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:3.57%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(39.29% + 6px)">5.5</div>
            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:32.14%"></div></div>
        </div>
        '''
i = s.index('<div class="plot" id="plot">')
j = s.index('<div class="xaxis"', i)
s = s[:i] + plot + s[j:]

rep('<div><b>Thu</b>12</div><div><b>Fri</b>13</div>\n          <div><b>Sat</b>14</div><div><b>Sun</b>15</div><div><b>Mon</b>16</div><div><b>Tue</b>17</div><div><b>Wed</b>18</div>',
    '<div><b>Fri</b>13</div><div><b>Sat</b>14</div>\n          <div><b>Sun</b>15</div><div><b>Mon</b>16</div><div><b>Tue</b>17</div><div><b>Wed</b>18</div><div><b>Thu</b>19</div>', 1)

# ---------- 7. Flag 1 (Today) ----------
flag1 = ('<h3><span class="pill warn">Today</span> The Kimberly slot is today at 2 &mdash; and the '
 'invite never went out</h3>\n          '
 '<p><b>Kimberly Ragsdale asked for Friday 2 PM with Taylor joining</b>, briefed her co-CEOs '
 'yesterday, and there is still no event on the calendar. Send the invite at the top of the <b>9 AM '
 'EquiStamp block</b> &mdash; or propose a new time now, before the ask goes stale. The rest of the '
 'day is light: <b>Dan catch-up 11</b>, an open afternoon for the <b>three drafts</b> (Tim day '
 'twenty-five, Affiliated Tech, GigTel), the <b>Stratus consolidation</b> (Tue 17 vs Wed 18 &mdash; '
 'Wednesday now also carries Jr&rsquo;s billing kickoff 11&ndash;12), and the <b>GamifyOS curriculum '
 'for Caroline</b>. <b>Per-location alert routing ships to production today</b> &mdash; watch RV '
 'Country&rsquo;s alerts route to location managers, not IT. Review Crew at 5:30 closes the week.</p>')
i = s.index('<h3><span class="pill warn">Today</span>')
j = s.index('</p>', i) + len('</p>')
s = s[:i] + flag1 + s[j:]

# ---------- 8. Markers ----------
markers = ('<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Thursday closed '
 '<b>3&ndash;1&ndash;5</b> &mdash; nine events, and <b>the first weekday where successes outnumbered '
 'failures</b>: a record-fast morning (seven events before 7:30), then an evening needs-attention at '
 '6:54 and failure at 7:56 &mdash; the 6&ndash;9 window came back after Wednesday&rsquo;s clean '
 'evening. The week&rsquo;s biggest correction: <b>the Nortec silence was a dropped baton</b> &mdash; '
 'the updated proposal had never been sent; Jr sent it to Tyler Froemming and Steve Myhre Thursday at '
 '1:50 with an apology, so the three-week-old &ldquo;chase&rdquo; resets to a fresh ask in their '
 'court. Pipeline: <b>Kimberly</b> wants today 2 PM, invite unsent; <b>Stratus</b> double-booked (Tue '
 '17 yours, Wed 18 Jr&rsquo;s) with the <b>billing kickoff Wed 18, 11&ndash;12</b> stacked on '
 'Jr&rsquo;s slot; <b>GigTel</b> draft pending; <b>Threshold</b> waiting on the NDA check. <b>The Tim '
 'record is day twenty-five</b> &mdash; Tuesday&rsquo;s Izzy checkin is the next natural close. '
 '<b>Alert routing ships today</b>; the GamifyOS page + landing go-live is still unconfirmed.</p>')
i = s.index('The week&rsquo;s markers</h4>')
i = s.index('<p ', i)
j = s.index('</p>', i) + len('</p>')
s = s[:i] + markers + s[j:]

# ---------- 9. Coming up ----------
old_h4 = 'A 9.75-hour Thursday, then the week opens wide'
i = s.index(old_h4)
j = s.index('</p>', i) + len('</p>')
new_coming = ('A light Friday with one loud clock, then the Tuesday pinch</h4>\n          '
 '<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Today: PnR 8, <b>EquiStamp proposal '
 '9</b>, Dan 11, the <b>Kimberly slot at 2 if the invite goes out</b>, Review Crew 5:30. Saturday: '
 '<b>Style Bodhi! 10&ndash;1</b>. Sunday: clear. Monday Nov 16: sync 8, DW Engineering 10&ndash;2 '
 'with <b>Call Ken at noon</b> inside it, TTT 2. Tuesday Nov 17 &mdash; <b>the pinch, 7.5h</b>: '
 '<b>Izzy checkin 10</b>, <b>Stratus demo 10:40</b>, <b>GamifyOS Sync 12&ndash;1</b>, all inside DW '
 'Client 10&ndash;2. Wednesday Nov 18 &mdash; also 7.5h: Recover 9, SustAmb 9:30, <b>Jr&rsquo;s demo '
 'event 10:40</b> (cancel one), <b>billing kickoff 11&ndash;12</b>, DW 11&ndash;3, TTT 3. Thursday '
 'Nov 19: DW 8:30&ndash;12:30, Reserved 3:30, <b>Scott Van Camp 4</b>. Carried: <b>the Cathy call</b> '
 '(thirty days), <b>the CCI booking</b>, the drip and performance reports, the ATS five, the Whova '
 'trio, the Sahiti intro, the <b>Rev.io sessions ask</b>, and the <b>invoice &mdash; fifteen days '
 'past due unless the ACH cleared it</b>.</p>')
s = s[:i] + new_coming + s[j:]

# ---------- 10. Small line edits ----------
# Nortec review-queue/chase lines elsewhere keep their aging; the masthead/markers carry the reset.

# ---------- Sanity ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-13T06:13:00-06:00') == 2
assert s.count('window open') == 2
assert s.count('Good morning, Bodhi.') == 1
assert s.count('day twenty-four') == 0
assert s.count('3&ndash;1&ndash;5 by') == 0
assert s.count('Friday, November 13') == 1
assert s.count('EquiStamp') >= 3
for bad in ['hw7Mh6cK','pY3DM73R','bT5uDhjRSBk3','scottvlmft','ebccf397','5WY67Sa2',
            'PasswordReset','billcenter.net','3,082','Jose Luiz','quoter.com','doxy.me',
            'sfw-mvnn-nfd','cjk-wubx-vna','nyg-hguu-mmh','bxe-xdtp-ohs','uyt-cgnh-gtz',
            'vqd-jqoy-wsp','veu-nahg-ydy','gnj-tvnv-fyt','hag-efnz-nvc','wtj-emrp-uyn',
            '271 125 290 583 760','atscall','5359043498322','notion.com']:
    assert bad not in s, bad

open(p, 'w').write(s)
print('friday turn ok', len(s))
