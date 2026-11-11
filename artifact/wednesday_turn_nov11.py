# Wednesday Nov 11, 2026 full-pass day turn (fired 6:13 AM CT).
# Day facts: Tuesday closed 5-2-3 (success 9:21 PM after last tick) - fourth straight
# evening-burst day; Monday 10-5-3 record tie stands. LeVarr/IRIS reply SENT Tue 5:06 PM,
# Laura answered 5:27 "I will make the invite" - handoff question resolved. Drafts now
# THREE (Tim day 23, Affiliated Tech, GigTel). New fronts: Kimberly Ragsdale
# (Breastfeeding Success) wants Fri 2 PM discovery invite w/ Taylor (Bodhi to send);
# Shades and Son (Shelby) waits on Kyle's code. Eelco closing PR #992 (icon not text);
# #991/#996 took main merges. New Thu event: Chat with Tash 4:45-5 -> Thu 8.75h.
# Chart rolls Wed Nov 11 - Tue Nov 17; Pitch and Run Fri 8-9 AM personal now on calendar.
# Hazards: 'day thirty' x2 - only the Iris one bumps ('Iris, day thirty'); the Sep-8
# 'hit day thirty' is frozen. 'window open' count includes one 'window opened' - keep 2.
import re

p = 'page-template.html'
s = open(p).read()

def rep(old, new, n):
    global s
    c = s.count(old)
    assert c == n, (old[:60], c, n)
    s = s.replace(old, new)

def splice(a, b, new, keep_end=True):
    """Replace from start of a to end of b (inclusive both) with new."""
    global s
    i = s.index(a)
    j = s.index(b, i) + len(b)
    s = s[:i] + new + s[j:]

# ---------- 1. Global age bumps (highest first) ----------
rep('day sixty-five', 'day sixty-six', 3)      # 799
rep('day sixty-four', 'day sixty-five', 3)     # Eric / iz-dms trio
rep('night fifty-seven', 'night fifty-eight', 2)
rep('day fifty-six;', 'day fifty-seven;', 1)
rep('fifty-nine days past', 'sixty days past', 4)
rep('forty-nine days past', 'fifty days past', 1)
rep('Iris, day thirty', 'Iris, day thirty-one', 1)
rep('twenty-seven days past', 'twenty-eight days past', 2)
rep('Twenty-seven', 'Twenty-eight', 2)
rep('(twenty-seven days)', '(twenty-eight days)', 4)
rep('day twenty-two', 'day twenty-three', 7)   # Tim record
rep('85 days', '86 days', 1)                   # hr-nda
rep('Ages as of Nov 10', 'Ages as of Nov 11', 1)
rep('twelve days past due', 'thirteen days past due', 2)
rep('is six days old', 'is seven days old', 1)

# ---------- 2. Stamps / header / greeting ----------
rep('2026-11-10T21:07:00-06:00', '2026-11-11T06:13:00-06:00', 2)
rep('<b>Brief compiled</b> Tue 6:13 AM &middot; data checked Tue 9:07 PM CT',
    '<b>Brief compiled</b> Wed 6:13 AM &middot; data checked Wed 6:13 AM CT', 1)
rep('Tuesday, November 10', 'Wednesday, November 11', 1)
rep('Good evening, Bodhi.', 'Good morning, Bodhi.', 1)

# ---------- 3. Masthead ----------
masthead = (
 'Wednesday is the day the week has been bracing for: <b>GamifyOS Sync at 11 sits inside DW Project '
 'Engineering 11&ndash;3</b> &mdash; an <b>8.5-hour day, over the line, with the GamifyOS page and '
 'community landing due live today</b>. The morning runs Recover 9, Sustainable Ambition 9:30, then '
 '<b>Ellie &times; Caroline &times; Taylor at 10:30</b> &mdash; Taylor in the room right before her own '
 '11:00 sync. Yesterday moved real pieces: <b>your IRIS reply went out at 5:06 and Laura answered at '
 '5:27 &mdash; she is making the invite</b>, so the sales-handoff question is answered and the meeting '
 'is hers to schedule. <b>Three drafts still wait on Send</b>: Tim (day twenty-three), Affiliated Tech, '
 'GigTel. Two new fronts from Tuesday&rsquo;s off-calendar meetings: <b>Kimberly Ragsdale '
 '(Breastfeeding Success, a ~$4,500 starter scope discussed) wants a Friday 2 PM discovery call with '
 'Taylor &mdash; the invite is yours to send</b>; and <b>Shades and Son</b> waits on Kyle&rsquo;s site '
 'code (about a day out) before you wire Shelby&rsquo;s ChatGPT to Search Console. <b>Stratus is still '
 'silent</b> on the reschedule &mdash; Joseph Hymbaugh is back today. <b>Nortec still waits on Steve '
 'Myhre</b>, silent two days. Eelco is closing <b>PR #992</b> (icon, not text) and his '
 '<b>changes-requested review on #1121</b> still waits. Tuesday closed <b>5&ndash;2&ndash;3</b> &mdash; '
 'the fourth straight evening-burst day. Pick up Ladybug at 5. No reactions saved.</p>')
splice('Wednesday is the day', 'XX-NEVER-XX', '') if False else None
i = s.index('Tuesday runs on a three-stop morning:')
j = s.index('No reactions saved.</p>', i) + len('No reactions saved.</p>')
s = s[:i] + masthead + s[j:]

# ---------- 4. Ledger: close Tuesday, open Wednesday ----------
rep('then <b>an evening burst of three: 7:06, 7:22 and 8:00</b>, the twenty-eighth straight weekday '
    'evening &mdash; <b>5&ndash;2&ndash;2 by 9:07, window open</b>.',
    'then <b>an evening burst of three: 7:06, 7:22 and 8:00</b> &mdash; the twenty-eighth straight '
    'weekday evening &mdash; and a late <b>success at 9:21 PM</b> to end it. <b>Tuesday closes '
    '5&ndash;2&ndash;3</b>, ten events, verified Wednesday morning with trash included &mdash; the '
    'fourth straight day to end in an evening failure burst. The overnight into Wednesday stayed '
    'quiet &mdash; <b>0&ndash;0&ndash;0 by 6:13, window open</b>.', 1)

# ---------- 5. Today note + schedule ----------
rep('Three-stop morning &mdash; Iris Sync 9, Izzy 10, DW Client 10:30&ndash;2:30; Birds drive 4:30, haircut 5',
    'GamifyOS Sync 11 inside DW 11&ndash;3 &mdash; 8.5h, deliverables due live; Recover 9, SustAmb 9:30, '
    'Ellie 10:30, Ladybug 5', 1)

sched = '''<div class="card sched" id="todaysched">
        <div class="slot"><div class="t">9:00&ndash;9:30</div><div class="w">Recover + Shower<small>Personal &mdash; the only margin before a six-hour run</small></div></div>
        <div class="slot"><div class="t">9:30&ndash;10:30</div><div class="w">Sustainable Ambition &mdash; Gevity Movement Studio<small>Weekly gathering</small></div></div>
        <div class="slot"><div class="t">10:30&ndash;11:00</div><div class="w">Ellie &times; Caroline &times; Bodhi &times; Taylor<small>Taylor is in this room right before her own 11:00 sync &mdash; settle the GamifyOS go-live pieces here, and lock Friday 2 PM with her for the Kimberly Ragsdale discovery call</small></div></div>
        <div class="slot"><div class="t">11:00&ndash;12:00</div><div class="w">GamifyOS Sync &mdash; inside Deep Work (Project Engineering)<small>The named collision: the sync eats the first hour of the 11&ndash;3 build block on the day the page + community landing are due live</small></div></div>
        <div class="slot"><div class="t">12:00&ndash;3:00</div><div class="w">Deep Work (Project Engineering) &mdash; remainder<small>The only real build window for the GamifyOS deliverables; the three drafts (Tim, Affiliated Tech, GigTel) and the Kimberly invite fit in the cracks</small></div></div>
        <div class="slot"><div class="t">3:00&ndash;4:00</div><div class="w">Transition, Talking, Triage<small>If Stratus answers today, 4&ndash;5 is the only clean landing &mdash; everything else stacks</small></div></div>
        <div class="slot"><div class="t">5:00&ndash;5:30</div><div class="w">Pick up Ladybug<small>Personal &mdash; closes the day</small></div></div>
      </div>
    </section>'''
i = s.index('<div class="card sched" id="todaysched">')
j = s.index('</section>', i) + len('</section>')
s = s[:i] + sched + s[j:]

# ---------- 6. Chart: roll week Wed Nov 11 - Tue Nov 17 ----------
rep('Tue Nov 10 &ndash; Mon Nov 16', 'Wed Nov 11 &ndash; Tue Nov 17', 1)
plot = '''<div class="plot" id="plot">
          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>
          <div class="bar"><div class="tot" style="bottom:calc(60.71% + 6px)">8.5</div>
            <div class="seg m" style="height:17.86%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:7.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(62.5% + 6px)">8.75</div>
            <div class="seg m" style="height:30.36%"></div><div class="seg f" style="height:32.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(17.86% + 6px)">2.5</div>
            <div class="seg m" style="height:10.71%"></div><div class="seg p" style="height:7.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(21.43% + 6px)">3</div>
            <div class="seg p" style="height:21.43%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(48.21% + 6px)">6.75</div>
            <div class="seg m" style="height:12.5%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(39.29% + 6px)">5.5</div>
            <div class="seg m" style="height:3.57%"></div><div class="seg f" style="height:35.71%"></div></div>
        </div>
        '''
i = s.index('<div class="plot" id="plot">')
j = s.index('<div class="xaxis"', i)
s = s[:i] + plot + s[j:]

rep('<div><b>Tue</b>10</div><div><b>Wed</b>11</div>\n          <div><b>Thu</b>12</div><div><b>Fri</b>13</div><div><b>Sat</b>14</div><div><b>Sun</b>15</div><div><b>Mon</b>16</div>',
    '<div><b>Wed</b>11</div><div><b>Thu</b>12</div>\n          <div><b>Fri</b>13</div><div><b>Sat</b>14</div><div><b>Sun</b>15</div><div><b>Mon</b>16</div><div><b>Tue</b>17</div>', 1)

# ---------- 7. Flag 1 (Today) ----------
flag1 = ('<h3><span class="pill warn">Today</span> The GamifyOS collision is here &mdash; 8.5 hours, '
 'deliverables due live, one real build window</h3>\n          '
 '<p><b>GamifyOS Sync 11&ndash;12 sits inside DW Project Engineering 11&ndash;3</b>, so <b>12&ndash;3 '
 'is the only build window</b> on the day the <b>page and community landing are due live</b>. Use '
 '<b>Ellie &times; Caroline &times; Taylor at 10:30</b> to settle go-live state before the sync, and '
 'to <b>lock Friday 2 PM with Taylor for the Kimberly Ragsdale discovery call</b> &mdash; the invite '
 'is yours to send. <b>Three drafts wait on Send</b>: Tim (day twenty-three), Affiliated Tech, GigTel. '
 '<b>Laura&rsquo;s handoff question is answered</b> &mdash; she is making the invite. If <b>Stratus</b> '
 'replies today (Joseph Hymbaugh is back), 4&ndash;5 is the only clean slot. Eelco&rsquo;s '
 '<b>changes-requested review on PR #1121</b> still waits, and he is closing <b>#992</b> &mdash; icon, '
 'not text.</p>')
i = s.index('<h3><span class="pill warn">Today</span>')
j = s.index('</p>', i) + len('</p>')
s = s[:i] + flag1 + s[j:]

# ---------- 8. Markers ----------
markers = ('<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Tuesday closed '
 '<b>5&ndash;2&ndash;3</b> &mdash; ten events, and <b>the fourth straight day to end in an evening '
 'failure burst</b> (Saturday through Tuesday); Monday&rsquo;s <b>10&ndash;5&ndash;3 record tie</b> '
 'stands, and the 6&ndash;9 PM window is now the reliable failure zone &mdash; the root-cause look is '
 'still worth scheduling. The pipeline: <b>Nortec</b> waits on Steve Myhre (silent two days); '
 '<b>Stratus</b> owes a reschedule pick &mdash; Joseph Hymbaugh is back today; <b>GigTel</b> has the '
 'demo account live with Tanner Robinson and your draft pending; <b>Kimberly Ragsdale</b> wants '
 'Friday 2 PM &mdash; the invite is the next move. <b>Per-location alert routing</b> (RV Country, 11 '
 'assistants) is due to production by Friday. <b>The Tim record is day twenty-three</b> &mdash; no '
 'Izzy call today to force it; one Send closes it.</p>')
i = s.index('The week&rsquo;s markers</h4>')
i = s.index('<p ', i)
j = s.index('</p>', i) + len('</p>')
s = s[:i] + markers + s[j:]

# ---------- 9. Coming up ----------
coming = ('A three-stop Tuesday, then back-to-back 8.5-hour days')
new_h4 = 'An 8.5-hour pinch today, an 8.75-hour Thursday, then the week breathes'
i = s.index(coming)
j = s.index('</p>', i) + len('</p>')
new_coming = (new_h4 + '</h4>\n          '
 '<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Today: <b>GamifyOS Sync 11&ndash;12 '
 'inside DW 11&ndash;3</b>, the page + landing due live, Ladybug 5. Thursday Nov 12 &mdash; '
 '<b>8.75h</b>: DW 10&ndash;2, <b>Scott Van Camp 2</b>, Reserved 3:30, <b>Chat with Tash 4:45</b> '
 '(new), <b>Friendsgiving 6&ndash;9 PM</b>. Friday: <b>Pitch and Run 8&ndash;9 AM</b>, the '
 '<b>Kimberly discovery call wants 2 PM</b> (invite unsent), Review Crew happy hour 5:30. Saturday: '
 '<b>Style Bodhi! 10&ndash;1</b>. Monday Nov 16: sync 8, DW Engineering 10&ndash;2 with <b>Call Ken '
 'at noon</b> inside it, TTT 2. Tuesday Nov 17: <b>Izzy checkin 10</b> inside DW Client 10&ndash;2 '
 '&mdash; the natural close for the Tim record if it survives that long. Carried: <b>the Cathy '
 'call</b> (twenty-eight days), <b>the CCI booking</b>, the drip and performance reports, the ATS '
 'five, the Whova trio, the Sahiti intro, and the <b>invoice &mdash; thirteen days past due unless '
 'the ACH cleared it</b>.</p>')
assert s[i-4:i] != '</h4', 'anchor sanity'
s = s[:i] + new_coming + s[j:]

# ---------- 10. Small line edits ----------
rep('#886, #991, #992, <b>#799 at day sixty-six</b>',
    '#886, #991, #996, <b>#799 at day sixty-six</b>', 1)
rep('<b>PR #992 (VOXAI-936, Ring/Voicemail transfer labels) requested your review</b> last evening.',
    '<b>PR #992 (VOXAI-936, Ring/Voicemail transfer labels) is being closed by Eelco</b> &mdash; not '
    'the right implementation, he wants an icon instead of text; <b>#996 (copyable tool IDs)</b> is '
    'open in its place.', 1)
rep('Send it Monday, first thing.', 'Send it today, first thing.', 1)
rep('One Send this morning and Tuesday&rsquo;s Izzy check-in arrives with it done.',
    'One Send this morning closes it &mdash; Tuesday&rsquo;s check-in came and went without it.', 1)
rep('Day eighteen &mdash; one click closes it', 'Day twenty-three &mdash; one click closes it', 1)

# ---------- Sanity ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-11T06:13:00-06:00') == 2
assert s.count('window open') == 2        # ledger + 'window opened'
assert s.count('Good morning, Bodhi.') == 1
assert s.count('day twenty-two') == 0
assert s.count('twenty-seven days') == 0
assert s.count('5&ndash;2&ndash;2') == 0
assert s.count('Four drafts') == 0
assert s.count('5&ndash;2&ndash;3') >= 2
for bad in ['hw7Mh6cK','pY3DM73R','bT5uDhjRSBk3','scottvlmft','ebccf397','5WY67Sa2',
            'PasswordReset','billcenter.net','3,082','Jose Luiz','quoter.com','doxy.me',
            'sfw-mvnn-nfd','cjk-wubx-nva','cjk-wubx-vna','nyg-hguu-mmh','bxe-xdtp-ohs',
            'uyt-cgnh-gtz','vqd-jqoy-wsp','veu-nahg-ydy','gnj-tvnv-fyt','271 125 290 583 760',
            'atscall','2629588395566','4043841245241','9914961465124']:
    assert bad not in s, bad

open(p, 'w').write(s)
print('wednesday turn ok', len(s))
