# Wednesday Nov 18 full-pass day turn.
# Facts: Tuesday closed 4-2-1 (seven events; 7:11 PM failure found in the morning
# 16h trash sweep). Wednesday opens 1-0-0 via a NEW sender -
# notifications@voxtell.smartkonnect.app (5:41 AM) - first cutover evidence; alert
# queries now cover both senders. Calendar: Bodhi DECLINED Jr's 10:40 Stratus
# re-demo, deleted Wed TTT, added Call White Fences 10:30-10:45, Iris Onboarding
# 3-4 stands (LeVarr accepted). Thursday gained GigTel walkthrough 2-3 (Tanner).
# Week rolls Wed 18 - Tue 24; Tue 24 stacks to 8h flat. Threshold closed Tuesday
# on usage-only; Nortec revived (Steve: "send them to me"); Tim record hits day
# thirty; Kimberly note five days; Exit Code $3,000 due Friday; invoice twenty
# days past due. Hazards: ledger holds full history (anchor on current tail only);
# frozen strings 'hit day thirty' and 'thirty-three days now' stay; chart scale 14
# (1h = 7.142857%).
import re
P = 'page-template.html'
s = open(P).read()

def rep(old, new, n):
    global s
    c = s.count(old)
    assert c == n, f'{old[:60]!r}: expected {n}, found {c}'
    s = s.replace(old, new)

def splice(start_anchor, end_anchor, new_text, keep_end=True):
    global s
    i = s.index(start_anchor)
    j = s.index(end_anchor, i)
    s = s[:i] + new_text + (end_anchor if keep_end else '') + s[j + len(end_anchor):] if False else s
    # (not used generically; explicit splices below)

# ---------- 1. global age bumps (highest first) ----------
rep('day seventy-two', 'day seventy-three', 3)
rep('day seventy-one', 'day seventy-two', 3)
rep('night sixty-four', 'night sixty-five', 2)
rep('day sixty-three', 'day sixty-four', 1)
rep('sixty-six days past', 'sixty-seven days past', 4)
rep('fifty-six days past', 'fifty-seven days past', 1)
rep('day thirty-seven', 'day thirty-eight', 1)
rep('Thirty-four days past', 'Thirty-five days past', 2)
rep('thirty-four days past', 'thirty-five days past', 2)
rep('(thirty-four days)', '(thirty-five days)', 2)
rep('day twenty-nine', 'day thirty', 7)
rep('Day twenty-nine', 'Day thirty', 1)
rep('92 days', '93 days', 1)
rep('Ages as of Nov 17', 'Ages as of Nov 18', 1)
rep('nineteen days past due', 'twenty days past due', 3)
rep('is thirteen days old', 'is fourteen days old', 1)

# ---------- 2. stamps / eyebrow / greeting / brief line ----------
rep('2026-11-17T21:07:00-06:00', '2026-11-18T06:11:00-06:00', 2)
rep('<b>Brief compiled</b> Tue 6:12 AM', '<b>Brief compiled</b> Wed 6:11 AM', 1)
rep('data checked Tue 9:07 PM CT', 'data checked Wed 6:11 AM CT', 1)
rep('Tuesday, November 17', 'Wednesday, November 18', 1)
rep('Good evening, Bodhi.', 'Good morning, Bodhi.', 1)

# ---------- 3. masthead ----------
i = s.index('Tuesday is the week')
j = s.index('No reactions saved.</p>')
masthead = (
    'Wednesday is kickoff day &mdash; with no kickoff time. Jr sent the updated billing '
    'pack and agenda to the SpectrumVoIP group at 1:27 Tuesday, but there is still '
    '<b>no event on your calendar</b>; the likeliest landing spot is inside Deep Work '
    '11&ndash;3 &mdash; watch the thread. The rest of today: Recover 9, Sustainable '
    'Ambition 9:30, a new 15-minute <b>Call White Fences at 10:30</b> you booked last '
    'night, and <b>Iris Onboarding 3&ndash;4</b> with LeVarr and Alex. You <b>declined '
    'Jr&rsquo;s 10:40 Stratus re-demo</b> (he hosts it solo) and dropped Wednesday TTT, '
    'so yesterday&rsquo;s duplicate-demo and onboarding collisions are both resolved. '
    'Tuesday delivered: <b>Threshold closed in a single day</b> &mdash; Jeff passed on '
    'minimums at 8:12, Jr countered usage-only at 12:42, Jeff accepted at 1:36, and the '
    'formal proposal went out at 2:29; countersignature and Chandler&rsquo;s demo access '
    'are the last steps. The <b>Stratus demo ran and they expressed interest</b>; the '
    '1 PM Iris training covered the core sales problem and prospecting; <b>Nortec woke '
    'up</b> &mdash; Steve Myhre asked for the materials and Jr sent them; and a '
    '<b>GigTel platform walkthrough is booked Thursday 2&ndash;3</b> with Tanner, which '
    'may make the week-old GigTel draft moot. Overnight, the <b>alerts started arriving '
    'from the new Smart Konnect notification service</b> &mdash; the first concrete sign '
    'the billing-platform cutover is live; the ledger now watches both senders. LiveKit '
    'reported a dashboard-only incident at 5:44 AM (calls unaffected so far). Still '
    'carrying: the <b>Kimberly note, five days old</b>; the <b>Tim record at day '
    'thirty</b> with the draft unsent; <b>Exit Code&rsquo;s $3,000 due Friday</b>; the '
    '<b>$5,000 invoice twenty days past due</b> unless the ACH cleared it; '
    'Illia&rsquo;s six reviews still unowned; and Crexendo&rsquo;s EVP intro still '
    'without a slot. Wednesday opens <b>1&ndash;0&ndash;0</b>. '
)
s = s[:i] + masthead + s[j:]

# ---------- 4. ledger: close Tuesday, open Wednesday ----------
rep('then the <b>6&ndash;9 window fired a failure at 7:02 PM</b>, the seventh straight '
    'evening &mdash; <b>3&ndash;2&ndash;1 by 9:07, window open</b>.',
    'then the <b>6&ndash;9 window fired failures at 7:02 and 7:11 PM</b> &mdash; the '
    'seventh straight evening. <b>Tuesday closes 4&ndash;2&ndash;1</b> &mdash; seven '
    'events, verified Wednesday morning with trash included. Overnight the alerts '
    '<b>switched to the new Smart Konnect notification sender</b>; its first event, a '
    '<b>failure at 5:41 AM</b>, opens the day &mdash; <b>1&ndash;0&ndash;0 by 6:11, '
    'window open</b>.', 1)

# ---------- 5. todaynote + todaysched ----------
rep('Tuesday &mdash; Izzy 10, Stratus demo 10:40 and Iris training 1&ndash;2 inside DW '
    'Client 10&ndash;2, TTT 2, webinar 4 &mdash; the week&rsquo;s heaviest day at 8.5h',
    'Wednesday &mdash; Recover 9, SustAmb 9:30, White Fences call 10:30, DW 11&ndash;3 '
    '(the billing kickoff likely lands here), Iris Onboarding 3&ndash;4 &mdash; 6.75h', 1)

i = s.index('<div class="card sched" id="todaysched">')
j = s.index('</section>', i)
sched = '''<div class="card sched" id="todaysched">
        <div class="slot free"><div class="t">6:15&ndash;9:00</div><div class="w">Open morning<small><b>Send the Kimberly note</b> (five days old), the <b>Tim draft hits day thirty</b>, and chase a time for the billing kickoff &mdash; Jr&rsquo;s pack went out yesterday with no slot attached</small></div></div>
        <div class="slot"><div class="t">9:00&ndash;9:30</div><div class="w">Recover + Shower</div></div>
        <div class="slot"><div class="t">9:30&ndash;10:30</div><div class="w">Sustainable Ambition</div></div>
        <div class="slot"><div class="t">10:30&ndash;10:45</div><div class="w">Call White Fences<small>Booked last night &mdash; 15 minutes</small></div></div>
        <div class="slot"><div class="t">11:00&ndash;3:00</div><div class="w">Deep Work: Project Engineering<small>The <b>billing kickoff</b> most likely lands inside this block &mdash; Jr&rsquo;s 10:40 Stratus re-demo runs without you (declined)</small></div></div>
        <div class="slot"><div class="t">3:00&ndash;4:00</div><div class="w">Iris Onboarding<small>LeVarr and Alex &mdash; walk through live customer examples; TTT was cleared to make room</small></div></div>
      </div>
    '''
s = s[:i] + sched + s[j:]

# ---------- 6. chart roll Wed 18 - Tue 24 ----------
i = s.index('<div class="plot" id="plot">')
j = s.index('<div class="xaxis"')
plot = '''<div class="plot" id="plot">
          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>
          <div class="bar"><div class="tot" style="bottom:calc(48.21% + 6px)">6.75</div>
            <div class="seg m" style="height:16.07%"></div><div class="seg f" style="height:28.57%"></div><div class="seg p" style="height:3.57%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(53.57% + 6px)">7.5</div>
            <div class="seg m" style="height:21.43%"></div><div class="seg f" style="height:32.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(35.71% + 6px)">5</div>
            <div class="seg p" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(17.86% + 6px)">2.5</div>
            <div class="seg p" style="height:17.86%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(14.29% + 6px)">2</div>
            <div class="seg p" style="height:14.29%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(41.07% + 6px)">5.75</div>
            <div class="seg m" style="height:5.36%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(57.14% + 6px)">8</div>
            <div class="seg m" style="height:21.43%"></div><div class="seg f" style="height:35.71%"></div></div>
        </div>
        '''
s = s[:i] + plot + s[j:]

rep('''<div><b>Tue</b>17</div><div><b>Wed</b>18</div>
          <div><b>Thu</b>19</div><div><b>Fri</b>20</div><div><b>Sat</b>21</div><div><b>Sun</b>22</div><div><b>Mon</b>23</div>''',
    '''<div><b>Wed</b>18</div><div><b>Thu</b>19</div>
          <div><b>Fri</b>20</div><div><b>Sat</b>21</div><div><b>Sun</b>22</div><div><b>Mon</b>23</div><div><b>Tue</b>24</div>''', 1)

rep('Tue Nov 17 &ndash; Mon Nov 23', 'Wed Nov 18 &ndash; Tue Nov 24', 1)

# ---------- 7. Today flag ----------
pill = '<span class="pill warn">Today</span>'
i = s.index(pill) + len(pill)
j = s.index('</p>', i) + 4
flag = (
    ' Kickoff day without a kickoff time &mdash; and the Tim record hits day thirty</h3>\n'
    '          <p>The <b>billing kickoff is supposed to happen today</b>: Jr&rsquo;s pack '
    'and agenda went to nine people Tuesday at 1:27, but there is <b>no calendar event '
    'and no time</b> &mdash; a one-line nudge in the open morning pins it before it '
    'collides with Deep Work. <b>Kimberly Ragsdale&rsquo;s ask is five days old</b> '
    '&mdash; own the miss in one line, propose two concrete times, lock Taylor in. '
    '<b>The Tim record hits day thirty today</b> and the draft reply has sat for '
    'fourteen days &mdash; send it or kill it. And overnight the <b>alerts started '
    'arriving from the Smart Konnect notification service</b> &mdash; the cutover '
    'you&rsquo;ve been waiting on is visibly live; worth two minutes to confirm the '
    'routing is complete, not split across systems.</p>'
)
s = s[:i] + flag + s[j:]

# ---------- 8. markers ----------
m = s.index('The week&rsquo;s markers</h4>')
mp = s.index('<p ', m)
pe = s.index('>', mp) + 1
j = s.index('</p>', pe)
markers = (
    'Tuesday closed <b>4&ndash;2&ndash;1</b> &mdash; seven events: overnight '
    'needs-attention at 4:55 and 5:15, a 6:44 failure, a 7:14 success, a midday failure '
    'at 12:48, then the <b>6&ndash;9 window&rsquo;s seventh straight evening</b> '
    '(failures 7:02 and 7:11). Wednesday opened <b>1&ndash;0&ndash;0</b> &mdash; and '
    'from a <b>new sender</b>: the alerts now arrive from the Smart Konnect '
    'notification service, the first concrete evidence the billing-platform cutover is '
    'live &mdash; the alert-routing question is answering itself. Pipeline: '
    '<b>Threshold accepted usage-only Tuesday</b> &mdash; proposal out at 2:29, '
    'countersignature and Chandler&rsquo;s demo access the last steps; <b>Stratus '
    'expressed interest</b> at the demo (Jr runs today&rsquo;s re-demo solo &mdash; you '
    'declined); <b>Nortec is live again</b> &mdash; Steve asked for the materials and '
    'got them; the <b>GigTel walkthrough is Thursday 2&ndash;3</b>; <b>Illia&rsquo;s '
    'six reviews still need an owner</b>; <b>Vitaly Belsky interviewed</b>; '
    '<b>Crexendo&rsquo;s NDA is countersigning</b> with the EVP intro to schedule; '
    '<b>Caroline&rsquo;s workshop reply</b> sits with you and Taylor; <b>Exit Code '
    '$3,000 is due Friday</b>; <b>Heart-Led Wellness</b> first session Thursday '
    '11&ndash;12 inside Deep Work. <b>The Tim record is day thirty</b> &mdash; '
    'Tuesday&rsquo;s checkin came and went without closing it. The GamifyOS go-live '
    'remains unconfirmed.'
)
s = s[:pe] + markers + s[j:]

# ---------- 9. coming up ----------
rep('A top-heavy Tuesday, then the week eases into Friendsgiving',
    'A kickoff Wednesday, a stacked Thursday, then Friendsgiving', 1)
c = s.index('A kickoff Wednesday, a stacked Thursday, then Friendsgiving')
cp = s.index('<p ', c)
pe = s.index('>', cp) + 1
j = s.index('</p>', pe)
coming = (
    'Today &mdash; 6.75h: Recover 9, SustAmb 9:30, <b>Call White Fences 10:30</b>, DW '
    '11&ndash;3, <b>Iris Onboarding 3&ndash;4</b> &mdash; and the <b>billing kickoff '
    'still needs a time</b>. Thursday Nov 19 &mdash; now 7.5h: DW 8:30&ndash;12:30 with '
    '<b>Heart-Led Wellness 11&ndash;12 inside it</b> (first session), the <b>GigTel '
    'walkthrough 2&ndash;3</b>, Reserved 3:30, <b>Scott Van Camp 4</b>. Friday Nov 20 '
    '&mdash; 5h, all personal: <b>Pitch and Run 8</b>, <b>Gevity pizza party 12:30</b>, '
    '<b>Friendsgiving at Ashlyn&rsquo;s 5&ndash;8</b> &mdash; and the <b>Exit Code '
    'invoice is due</b>. Saturday: <b>Lady Bird trail cleanup 9:30&ndash;12</b>. '
    'Sunday: Pilates 9:30 and the red-light bed. Monday Nov 23 &mdash; 5.75h: sync 8, '
    'DW Engineering 10&ndash;2, TTT 2. Tuesday Nov 24 &mdash; 8h, touching the line: '
    'Izzy 10, <b>ATS catch-up 10:30</b>, <b>GamifyOS Sync noon</b>, <b>Iris training '
    '1</b> inside DW Client 10&ndash;2, TTT 2. Carried: <b>the Cathy call</b> '
    '(thirty-five days), <b>the CCI booking</b>, the drip and performance reports, the '
    'ATS five, the Whova trio, the Sahiti intro, the <b>Rev.io sessions ask</b>, and '
    'the <b>invoice &mdash; twenty days past due unless the ACH cleared it</b>.'
)
s = s[:pe] + coming + s[j:]

# ---------- sanity ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-18T06:11:00-06:00') == 2
assert s.count('window open') == 2
assert s.count('Good morning, Bodhi.') == 1
assert s.count('No reactions saved.') == 1
assert s.count('day twenty-nine') == 0 and s.count('Tuesday, November 17') == 0
assert s.count('hit day thirty') == 1 and s.count('thirty-three days now') == 1
for bad in ['ebccf397', 'atscall', '3,082', 'Jose Luiz', '5WY67Sa2', 'PasswordReset',
            'billcenter.net', 'hw7Mh6cK', 'pY3DM73R', 'bT5uDhjRSBk3', 'mm7me9zr',
            'fK9Bn7og', 'quoter.com', 'smartkonnect.app']:
    assert bad not in s, bad
open(P, 'w').write(s)
print('wednesday turn OK', len(s))
