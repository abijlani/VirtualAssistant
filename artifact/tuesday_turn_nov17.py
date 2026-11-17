# Tuesday Nov 17, 2026 day-turn (full morning pass, fired 12:12 UTC = 6:12 AM CT)
# Day facts: Monday closed 4-3-2 (nine events; 6:59a f, 7:16a f, 7:17a NA, ~7:20/7:24a s,
#   6:57p f, 7:35p NA, 7:39p f, 9:14p NA). Tuesday opens 0-2-0 (NAs 4:55, 5:15 AM, both in
#   new NA thread 1a1e72504b357fcb, now 4 msgs; failure thread 16; success 12).
# Calendar: Tue = Izzy 10-10:30, Stratus demo 10:40-11:40, DW Client 10-2, Iris training 1-2,
#   TTT 2-3, email webinar 4-5  => 8.5h (m 3.5 / f 5) - only day over the 8h line.
#   Wed billing-kickoff event GONE from calendar; Wed Stratus demo still on => Wed 7.5 unchanged.
#   Fri gains Gevity pizza party 12:30 + Friendsgiving 5-8 => 5h personal. Sat trail cleanup 2.5p.
#   Sun Pilates + red-light 2p. Mon 23: sync 0.75 + DW 4 + TTT 1 = 5.75.
# Monday news: Illia parting-ways decision, Vitaly Belsky interview, pricing session,
#   Crexendo NDA countersigning, Threshold $250+$250 counter, Nortec nudge, Laura reply sent,
#   Izzy walk-through sent, Exit Code $3,000 due Fri Nov 20.
# Hazards: 'day seventy-one' before bare 'day seventy' regex; 'thirty-three days now' is FROZEN.
import re

p = 'page-template.html'
s = open(p).read()

def rep(old, new, n):
    global s
    c = s.count(old)
    assert c == n, f"count {c}!={n} for {old[:80]!r}"
    s = s.replace(old, new)

# ---- 1. ages (highest first) ----
rep('day seventy-one', 'day seventy-two', 3)
assert len(re.findall(r'day seventy(?!-)', s)) == 3
s = re.sub(r'day seventy(?!-)', 'day seventy-one', s)
rep('night sixty-three', 'night sixty-four', 2)
rep('day sixty-two', 'day sixty-three', 1)
rep('sixty-five days past', 'sixty-six days past', 4)
rep('fifty-five days past', 'fifty-six days past', 1)
rep('day thirty-six', 'day thirty-seven', 1)
rep('Thirty-three days past', 'Thirty-four days past', 2)
rep('thirty-three days past', 'thirty-four days past', 2)
rep('(thirty-three days)', '(thirty-four days)', 2)
rep('day twenty-eight', 'day twenty-nine', 5)
rep('Day twenty-eight', 'Day twenty-nine', 1)
rep('91 days', '92 days', 1)
rep('Ages as of Nov 16', 'Ages as of Nov 17', 1)
rep('eighteen days past due', 'nineteen days past due', 2)
rep('is twelve days old', 'is thirteen days old', 1)

# ---- 2. stamps / eyebrow / greeting / brief line ----
rep('2026-11-16T21:07:00-06:00', '2026-11-17T06:12:00-06:00', 2)
rep('Monday, November 16', 'Tuesday, November 17', 1)
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>', 1)
rep('<b>Brief compiled</b> Mon 6:13 AM &middot; data checked Mon 9:07 PM CT',
    '<b>Brief compiled</b> Tue 6:12 AM &middot; data checked Tue 6:12 AM CT', 1)

# ---- 3. masthead splice ----
i = s.index('Tuesday is the week') if 'Tuesday is the week' in s else s.index('Monday opens the week with a first-thing pair')
j = s.index('No reactions saved.</p>')
new_mast = ('Tuesday is the week&rsquo;s heaviest day &mdash; <b>8.5 hours, the only day over the '
 '8-hour line</b>: Izzy checkin 10 (<b>close the Tim record &mdash; day twenty-nine</b>), the '
 '<b>Stratus demo 10:40</b> (the duplicate never resolved &mdash; Wednesday&rsquo;s 10:40 is still '
 'on the books), Deep Work Client 10&ndash;2 with <b>Iris sales training 1&ndash;2</b> (Laura and '
 'seven SpectrumVoIP reps &mdash; bring the Lakeland numbers), TTT 2, and a 4 PM email-marketing '
 'webinar. Monday moved things: <b>you decided to part ways with Illia</b> (ConnectWise delays; '
 'his six open reviews need an owner) and <b>interviewed Vitaly Belsky</b> the same afternoon, '
 'then closed the day with a pricing-strategy working session. <b>Crexendo went from first contact '
 'to a countersigned NDA in one afternoon</b> &mdash; the EVP intro-call invite is in the inbox, '
 'no calendar event yet. Jr countered Threshold at <b>$250 platform + $250 minimum credited toward '
 'usage</b>, and nudged Nortec. <b>Caroline replied on the Dec 11 workshop</b> &mdash; ball back '
 'with you and Taylor. You sent the <b>Laura reply</b> and the <b>Izzy video walk-through</b> (Tim '
 'thanked you); <b>three drafts remain</b>: Tim (day twenty-nine), Affiliated Tech, GigTel. New '
 'payable: <b>Exit Code LLC $3,000 due Friday</b>. The <b>Kimberly note is four days old</b> and '
 'the <b>$5,000 invoice nineteen days past due</b>. Overnight: two needs-attention alerts (4:55, '
 '5:15 AM) &mdash; <b>Tuesday opens 0&ndash;2&ndash;0</b>. ')
s = s[:i] + new_mast + s[j:]

# ---- 4. ledger close Monday / open Tuesday ----
rep('Monday opened with a <b>failure at 6:59 AM</b>, then a 7:16&ndash;7:24 cluster &mdash; a second failure, a needs-attention, two successes &mdash; then, after a quiet day, the <b>6&ndash;9 window fired again: a failure at 6:57 PM, a needs-attention at 7:35, a failure at 7:39</b> &mdash; the sixth evening running &mdash; <b>4&ndash;2&ndash;2 by 9:07, window open</b>.',
    'Monday opened with a <b>failure at 6:59 AM</b>, then a 7:16&ndash;7:24 cluster &mdash; a second failure, a needs-attention, two successes &mdash; then, after a quiet workday, the <b>6&ndash;9 window fired its sixth straight evening: a failure at 6:57 PM, a needs-attention at 7:35, a failure at 7:39</b>, and a late needs-attention at 9:14 closed the day. <b>Monday closes 4&ndash;3&ndash;2</b> &mdash; nine events, verified Tuesday morning with trash included. The overnight into Tuesday brought <b>needs-attention alerts at 4:55 and 5:15 AM</b> &mdash; <b>0&ndash;2&ndash;0 by 6:12, window open</b>.', 1)

# ---- 5. todaynote + todaysched ----
rep('Monday &mdash; sync 8, DW Engineering 10&ndash;2 with Call Ken at noon inside it; first thing: the Kimberly note and the Stratus consolidation',
    'Tuesday &mdash; Izzy 10, Stratus demo 10:40 and Iris training 1&ndash;2 inside DW Client 10&ndash;2, TTT 2, webinar 4 &mdash; the week&rsquo;s heaviest day at 8.5h', 1)
i = s.index('<div class="card sched" id="todaysched">')
j = s.index('</section>', i)
new_sched = '''<div class="card sched" id="todaysched">
        <div class="slot free"><div class="t">6:15&ndash;10:00</div><div class="w">Open morning<small><b>Send the Kimberly note</b> (four days old), decide <b>Wednesday&rsquo;s Stratus demo</b> (cancel it if today&rsquo;s 10:40 covers it), and pull the Lakeland numbers for the 1 PM training</small></div></div>
        <div class="slot"><div class="t">10:00&ndash;10:30</div><div class="w">Izzy Weekly Checkin<small>Tim, Adam, Jr &mdash; <b>close the Tim record (day twenty-nine)</b> and ask for the Levitt verdict</small></div></div>
        <div class="slot"><div class="t">10:40&ndash;11:40</div><div class="w">Voxtell AI Demo &mdash; Stratus<small>Joseph Hymbaugh, Edward Weakland, Alex Penichet + Jr and Carlos Melo &mdash; inside DW Client 10&ndash;2</small></div></div>
        <div class="slot"><div class="t">1:00&ndash;2:00</div><div class="w">Iris Training with Bodhi<small>Laura Mathwig + seven SpectrumVoIP reps &mdash; how to sell Iris; the Lakeland case study is the spine</small></div></div>
        <div class="slot"><div class="t">2:00&ndash;3:00</div><div class="w">Transition, Talking, Triage<small>Three drafts in one sitting: Tim (day twenty-nine), Affiliated Tech, GigTel</small></div></div>
        <div class="slot"><div class="t">4:00&ndash;5:00</div><div class="w">Email webinar<small>&ldquo;The Only 3 Emails You Need&rdquo; &mdash; optional, and the only slack in an 8.5-hour day</small></div></div>
      </div>
    '''
s = s[:i] + new_sched + s[j:]

# ---- 6. chart splice + xaxis + weeknote ----
i = s.index('<div class="plot" id="plot">')
j = s.index('<div class="xaxis"')
new_plot = '''<div class="plot" id="plot">
          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>
          <div class="bar"><div class="tot" style="bottom:calc(60.71% + 6px)">8.5</div>
            <div class="seg m" style="height:25%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(53.57% + 6px)">7.5</div>
            <div class="seg m" style="height:14.29%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:3.57%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
            <div class="seg m" style="height:14.29%"></div><div class="seg f" style="height:32.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(35.71% + 6px)">5</div>
            <div class="seg p" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(17.86% + 6px)">2.5</div>
            <div class="seg p" style="height:17.86%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(14.29% + 6px)">2</div>
            <div class="seg p" style="height:14.29%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(41.07% + 6px)">5.75</div>
            <div class="seg m" style="height:5.36%"></div><div class="seg f" style="height:35.71%"></div></div>
        </div>
        '''
s = s[:i] + new_plot + s[j:]
rep('''<div><b>Mon</b>16</div><div><b>Tue</b>17</div>
          <div><b>Wed</b>18</div><div><b>Thu</b>19</div><div><b>Fri</b>20</div><div><b>Sat</b>21</div><div><b>Sun</b>22</div>''',
    '''<div><b>Tue</b>17</div><div><b>Wed</b>18</div>
          <div><b>Thu</b>19</div><div><b>Fri</b>20</div><div><b>Sat</b>21</div><div><b>Sun</b>22</div><div><b>Mon</b>23</div>''', 1)
rep('Mon Nov 16 &ndash; Sun Nov 22', 'Tue Nov 17 &ndash; Mon Nov 23', 1)

# ---- 7. Today flag ----
i = s.index('<span class="pill warn">Today</span>')
j = s.index('</p>', i)
new_flag = ('<span class="pill warn">Today</span> An 8.5-hour Tuesday &mdash; and the Stratus duplicate fires today</h3>\n'
 '          <p><b>Both Stratus demos are still on the books</b>: today&rsquo;s 10:40 happens either way &mdash; '
 'if it lands, <b>cancel Wednesday&rsquo;s 10:40 before end of day</b> so the team isn&rsquo;t pulled in twice. '
 '<b>Kimberly Ragsdale&rsquo;s ask is four days old</b> &mdash; the reschedule note is a five-minute send in the open '
 'morning: own the miss in one line, propose two concrete times, lock Taylor in. The <b>1 PM Iris training</b> is the '
 'day&rsquo;s highest-leverage hour: eight SpectrumVoIP sellers learning how to sell your product &mdash; the Lakeland '
 'numbers (40,129 calls, 15% handled end to end) are the spine. And <b>Illia&rsquo;s six open reviews need an owner</b> '
 'now that Monday&rsquo;s parting-ways decision is made &mdash; fold them into the review queue or hand them to Eelco.')
s = s[:i] + new_flag + s[j:]

# ---- 8. markers (index-based) ----
i = s.index('The week&rsquo;s markers</h4>')
i = s.index('<p ', i)
k = s.index('>', i) + 1
j = s.index('</p>', i)
new_markers = ('Monday closed <b>4&ndash;3&ndash;2</b> &mdash; nine events: the 6:59 AM failure, a 7:16&ndash;7:24 '
 'cluster, a quiet workday, then the <b>6&ndash;9 window&rsquo;s sixth straight evening</b> (failure 6:57, '
 'needs-attention 7:35, failure 7:39) and a late 9:14 needs-attention. Tuesday opened <b>0&ndash;2&ndash;0 '
 'overnight</b> (4:55, 5:15 AM). Record Sunday &mdash; <b>12&ndash;3&ndash;10</b> &mdash; still deserves its two '
 'minutes: worth asking what ran. Pipeline: <b>the Illia transition was decided Monday</b> (six open reviews need an '
 'owner) and <b>Vitaly Belsky interviewed</b>; <b>Crexendo&rsquo;s NDA is countersigning</b> with the EVP intro call '
 'to schedule; <b>Threshold</b> waits on Jeff&rsquo;s answer to the $250+$250 counter; <b>Nortec</b> was nudged '
 'Monday; <b>Caroline&rsquo;s workshop reply</b> sits with you and Taylor; <b>Exit Code $3,000 is due Friday</b>; '
 '<b>Heart-Led Wellness</b> first session Thursday 11&ndash;12 inside Deep Work. <b>The Tim record is day '
 'twenty-nine</b> &mdash; today&rsquo;s Izzy checkin closes it. The <b>Wednesday billing-kickoff event is off the '
 'calendar</b> &mdash; ask Eelco whether it moved. Alert routing and the GamifyOS go-live both remain unconfirmed.')
s = s[:k] + new_markers + s[j:]

# ---- 9. coming-up ----
rep('A steady Monday, a demo-day Tuesday, a stacked Wednesday',
    'A top-heavy Tuesday, then the week eases into Friendsgiving', 1)
i = s.index('A top-heavy Tuesday, then the week eases into Friendsgiving</h4>')
i = s.index('<p ', i)
k = s.index('>', i) + 1
j = s.index('</p>', i)
new_coming = ('Today &mdash; 8.5h, the only day over the 8-hour line: Izzy 10, <b>Stratus demo 10:40</b>, '
 '<b>Iris training 1&ndash;2</b>, TTT 2, webinar 4 &mdash; and the <b>Kimberly note</b> first thing. '
 'Wednesday Nov 18 &mdash; 7.5h: Recover 9, SustAmb 9:30, <b>the second Stratus demo 10:40</b> (cancel it today if '
 'the first lands), DW 11&ndash;3, TTT 3 &mdash; <b>the billing-kickoff event is off the calendar</b>. '
 'Thursday Nov 19 &mdash; 6.5h: DW 8:30&ndash;12:30 with <b>Heart-Led Wellness 11&ndash;12 inside it</b> (first '
 'session), Reserved 3:30, <b>Scott Van Camp 4</b>. Friday Nov 20 &mdash; 5h, all personal: <b>Pitch and Run 8</b>, '
 '<b>Gevity pizza party 12:30</b>, <b>Friendsgiving at Ashlyn&rsquo;s 5&ndash;8</b> &mdash; and the <b>Exit Code '
 'invoice is due</b>. Saturday: <b>Lady Bird trail cleanup 9:30&ndash;12</b>. Sunday: Pilates 9:30 and the red-light '
 'bed. Monday Nov 23 &mdash; 5.75h: sync 8, DW Engineering 10&ndash;2, TTT 2. Next Tuesday 24 stacks: Izzy 10, '
 '<b>ATS catch-up 10:30</b>, <b>GamifyOS Sync noon</b>, <b>Iris training 1</b>. Carried: <b>the Cathy call</b> '
 '(thirty-four days), <b>the CCI booking</b>, the drip and performance reports, the ATS five, the Whova trio, the '
 'Sahiti intro, the <b>Rev.io sessions ask</b>, and the <b>invoice &mdash; nineteen days past due unless the ACH '
 'cleared it</b>.')
s = s[:k] + new_coming + s[j:]

# ---- sanity ----
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-17T06:12:00-06:00') == 2
assert s.count('window open') == 2
assert s.count('Good morning, Bodhi') == 1
assert s.count('Tuesday, November 17') == 1
for bad in ['ebccf397','atscall','3,082','Jose Luiz','5WY67Sa2','PasswordReset','billcenter.net',
            'hw7Mh6cK','pY3DM73R','bT5uDhjRSBk3','mm7me9zr','fK9Bn7og','546 498 863','278 630 569',
            '243 621','ya0kgCefr7z5t0EvFx']:
    assert bad not in s, bad
open(p, 'w').write(s)
print('tuesday turn ok', len(s))
