#!/usr/bin/env python3
# Monday Oct 19 FULL morning rebuild.
# Global age bumps first (counts verified against the live template), then
# structural rewrites with age-free anchors; all in memory, count-asserted, write LAST.
import re

P = 'page-template.html'
s = open(P).read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, f"rep expected {n}, found {c}: {old[:90]!r}"
    s = s.replace(old, new)

def rx(pat, new, n=1):
    global s
    s, c = re.subn(pat, new, s, flags=re.DOTALL)
    assert c == n, f"rx expected {n}, got {c}: {pat[:90]!r}"

# ---------- L. global age bumps, highest first ----------
rep('day forty-two', 'day forty-three', 3)                 # #799
rep('thirty-eighth day double-approved', 'thirty-ninth day double-approved', 1)
rep('day forty-one', 'day forty-two', 3)                   # Eric x2 + Izzy trio
rep('forty full days ago', 'forty-one full days ago', 1)
rep('day thirty-nine of billed Logs', 'day forty of billed Logs', 1)
rep('day thirty-three', 'day thirty-four', 2)              # JDs (row + chip)
rep('Day thirty-four on Eric Bramini', 'Day thirty-five on Eric Bramini', 1)
rep('sixteen days', 'seventeen days', 5)                   # Emilio
rep('Sixteen days', 'Seventeen days', 1)                   # Emilio pill
rep('four days past', 'five days past', 6)                 # ProGraphix
rep('Four days past due', 'Five days past due', 1)         # ProGraphix pill
rep('night thirty-four', 'night thirty-five', 2)           # Nick
rep('thirty-six days past', 'thirty-seven days past', 2)   # billing/RevIO
rep('twenty-seven days unsent', 'twenty-eight days unsent', 1)
rep('forty-eight days past', 'forty-nine days past', 2)    # retirement
rep('em-roadmap at 52 days', 'em-roadmap at 53 days', 1)
rep('day twelve in drafts', 'day thirteen in drafts', 1)   # lmathwig Oct 6 draft
rep('Iris, day seven', 'Iris, day eight', 1)
rep('Ages as of Oct 18', 'Ages as of Oct 19', 1)

def chip1(m): return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
s, c1 = re.subn(r'(class="chip old">)(\d+)(d</span>)', chip1, s)
s, c2 = re.subn(r'(class="chip old">)(\d+)(d &mdash;)', chip1, s)
assert c1 + c2 == 5, f"chip bumps: {c1}+{c2}"

# ---------- A. stamps / masthead ----------
rep('2026-10-18T22:07:00-05:00', '2026-10-19T07:22:00-05:00', 2)
rep('<b>Brief compiled</b> Sun 8:07 AM &middot; data checked Sun 10:07 PM CT',
    '<b>Brief compiled</b> Mon 7:22 AM &middot; data checked Mon 7:22 AM CT')
rep('Sunday, October 18 &middot; 2026', 'Monday, October 19 &middot; 2026')
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>')

# ---------- B. sub rewrite (ages written POST-BUMP) ----------
assert s.count('<p class="sub">') == 1
rx(r'<p class="sub">.*?</p>',
   '''<p class="sub">The weekend behind you: <b>Saturday&rsquo;s workshop ran clean</b> (prep at noon, 1&ndash;4 at Gevity, one lone line failure all day), then <b>Sunday answered with the spike</b> &mdash; nine failures, seven needs-attention and four successes, closed at 10:07 PM &mdash; and Monday opened with a needs-attention at 5:28 and <b>a first failure at 7:07 AM</b>. The weekend moved nothing on the sends: <b>ProGraphix is five days past the submit-by date</b> (10/23 is Friday), the <b>Laura recap + per-account export re-request</b> is still unsent with today&rsquo;s 62-account reconciliation leaning on it, and the Emilio recap is at <b>seventeen days</b>. New and <b>due today</b>: Friday&rsquo;s Oracle Lighting session with Tim ended with you owing him <b>working Make-scenario instructions by Monday</b> &mdash; the backorder-ETA lookup is rebuilt but unverified. Today runs 5.75h: Product Sync 8:00, Deep Work (Engineering) 10&ndash;2, Transition 2&ndash;3. One website note: Sunday night&rsquo;s contact-form submission was a test (&ldquo;this is a demo&rdquo;) &mdash; the form works end-to-end. No reactions saved.</p>''')

# ---------- C. needs-decision note ----------
rep('&mdash; Monday morning is the decision point; today stays in nature',
    '&mdash; the decision point is this morning: submit and reply, call Cathy, or let 10/23 go')

# ---------- D. todaynote + sched ----------
rep('Nothing booked &mdash; the nature day',
    '5.75h &mdash; Product Sync 8:00, Deep Work (Engineering) 10&ndash;2, Transition 2&ndash;3')
rx(r'<div class="card sched" id="todaysched">.*?</div>\s*</section>',
   '''<div class="card sched" id="todaysched">
        <div class="slot"><div class="t">8:00 &ndash; 8:45</div><div class="w">Weekly Product Sync<small>with Jr &middot; Google Meet</small></div></div>
        <div class="slot"><div class="t">10:00 &ndash; 2:00</div><div class="w">Deep Work (Engineering)<small>the 62-account reconciliation &middot; the Oracle Make-scenario instructions for Tim (due today) &middot; then the #992 / #996 / #997 reviews</small></div></div>
        <div class="slot"><div class="t">2:00 &ndash; 3:00</div><div class="w">Transition, Talking, Triage<small>the sends: Laura recap + export re-request &middot; Emilio recap &middot; the ProGraphix reply</small></div></div>
      </div>
    </section>''')

# ---------- E. Top 5 ----------
rep('Nothing moved Friday. Decide this weekend: submit and reply, call her first thing Monday, or accept that the conference date slips.',
    'Nothing moved all weekend. This morning is the decision: submit and reply, call Cathy, or accept that the conference date slips &mdash; 10/23 is Friday.')
rep('<span class="pill warn">Tomorrow</span>', '<span class="pill warn">Today 10&ndash;2</span>')
rep('A Sunday-evening send sets Monday up; otherwise it&rsquo;s the first thing after the sync.',
    'The Laura send never left, so open the block with the recap + re-request, then run the reconciliation from the funnel report already in hand.')
rx(r'<h4>The audit follow-through hasn&rsquo;t left &mdash; Laura&rsquo;s recap \+ per-account export re-request</h4>.*?</div></li>',
   '''<h4>Due today: the Oracle Lighting Make-scenario instructions to Tim</h4>
          <p class="why">Friday&rsquo;s troubleshooting session ended with the backorder-ETA lookup rebuilt but unverified &mdash; the aggregator&rsquo;s renamed columns were blanking the output, and the sheet URL must be the /export CSV, not /edit. You promised Tim working instructions by today: export the blueprint, rebuild with correct column mappings, verify end-to-end, and queue the YouTube link sheet for his team to maintain.</p>
          <div class="meta"><span class="pill crit">Promised Monday</span><span class="pill quiet">Deep Work 10&ndash;2</span></div>
        </div></li>''')
rep('Sunday stays in nature; Monday&rsquo;s Deep Work (Engineering) 10&ndash;2 is the engineering window.',
    'Deep Work (Engineering) 10&ndash;2 is the window &mdash; bugbot swept #992, #996 and #997 this morning; the reviews still wait on you.')
rep('<span class="pill quiet">Weekend pocket</span>', '<span class="pill quiet">Deep Work 10&ndash;2</span>')

# ---------- F. coming-up cards ----------
rx(r'<h4 style="font-size:14px">Today &mdash; the nature day; Monday is the re-entry</h4>\s*<p[^>]*>.*?</p>',
   '''<h4 style="font-size:14px">Today &mdash; re-entry: sync at 8, two deliverables inside Deep Work</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">Product Sync 8&ndash;8:45 (Jr confirmed). Deep Work (Engineering) 10&ndash;2 carries the <b>62-account reconciliation</b>, the <b>Oracle Make-scenario instructions promised to Tim today</b>, and the PR reviews (#992, #996, #997 &mdash; bugbot swept all three this morning). Transition 2&ndash;3 is the send window: the Laura recap + export re-request, the Emilio recap (seventeen days), the ProGraphix reply.</p>''')
rep('The workshop ran Saturday 1&ndash;4 at Gevity &mdash; a clean day on the line behind it; today stays open &mdash; the nature day.',
    'The workshop ran Saturday clean; Sunday brought the line&rsquo;s weekly spike (nine failures, seven needs-attention).')
rep('Next week: Monday 5.75h', 'This week: today 5.75h')

# ---------- G. week-panel flags ----------
rx(r'<h3><span class="pill warn">Today</span> Sunday is the nature day &mdash; nothing scheduled</h3>\s*<p>.*?</p>',
   '''<h3><span class="pill warn">Today</span> Monday runs 5.75h &mdash; sync at 8, Deep Work 10&ndash;2 with two deliverables inside</h3>
          <p>The <b>62-account reconciliation</b> and the <b>Oracle Make-scenario instructions promised to Tim today</b> both live in Deep Work (Engineering) 10&ndash;2. Before the block: the <b>ProGraphix decision</b> (five days past the submit-by date &mdash; 10/23 is Friday). Transition 2&ndash;3 takes the sends: the Laura recap + per-account export re-request feeding the reconciliation, and the Emilio recap (seventeen days).</p>''')
rx(r'<h3><span class="pill warn">This week</span> A steady week into the 2F-15 and booth deadlines &mdash; Wednesday picks up a debrief</h3>\s*<p>.*?</p>',
   '''<h3><span class="pill warn">This week</span> A steady week into the 2F-15 and booth deadlines &mdash; Wednesday&rsquo;s debrief now has an agenda</h3>
          <p>Today 5.75h opens with Product Sync at 8:00 and carries the <b>62-account billing reconciliation</b> plus the Oracle instructions; Tuesday 6.5h has the Izzy check-in at 10:00 and Iris Training 1&ndash;2; <b>Wednesday Oct 21 runs 7.5h</b> &mdash; the 2F-15 artwork deadline (FedEx&rsquo;s specs with Jr) plus the <b>&ldquo;Debrief AI&rdquo; call 11:30&ndash;12:30</b>, whose posted agenda includes the website, the workshop review, preferred partners, and a direct ask: what you built for Ashlyn, when, and what you charged; Thursday Oct 22 6.5h with the Netsapiens booth bill 9&ndash;9:30 and Scott at 4; Friday Oct 23 holds one hour &mdash; AI-Powered Marketing with Claude 9:30&ndash;10:30. <b>UGM starts Monday Oct 26 in Austin.</b></p>''')

# ---------- H. chart ----------
rep('Sun Oct 18 &ndash; Sat Oct 24 &middot;', 'Mon Oct 19 &ndash; Sun Oct 25 &middot;')
rx(r'(<div class="cap8" style="bottom:57\.14%"><span>8h sustainable load</span></div>\n).*?(\n        </div>\n        <div class="xaxis")',
   r'''\g<1>          <div class="bar"><div class="tot" style="bottom:calc(41.07% + 6px)">5.75</div>
            <div class="seg m" style="height:5.36%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(53.57% + 6px)">7.5</div>
            <div class="seg m" style="height:14.29%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:3.57%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(7.14% + 6px)">1</div>
            <div class="seg m" style="height:7.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\g<2>''')
rep('''<div><b>Sun</b>18</div><div><b>Mon</b>19</div>
          <div><b>Tue</b>20</div><div><b>Wed</b>21</div><div><b>Thu</b>22</div><div><b>Fri</b>23</div><div><b>Sat</b>24</div>''',
    '''<div><b>Mon</b>19</div><div><b>Tue</b>20</div>
          <div><b>Wed</b>21</div><div><b>Thu</b>22</div><div><b>Fri</b>23</div><div><b>Sat</b>24</div><div><b>Sun</b>25</div>''')

# ---------- I. table rows ----------
rep('<td class="tid">Carried</td>', '<td class="tid">Today 2&ndash;3</td>')
rep('&mdash; none of the three moved Friday', '&mdash; none of the three moved all weekend')
rep('<td class="tid">This weekend</td>', '<td class="tid">This week</td>')
rep('<td class="tid">Weekend pocket</td>', '<td class="tid">Today 10&ndash;2</td>')

# ---------- J. ledger: Monday opener ----------
rep('the heaviest day since last Sunday&rsquo;s fourteen &mdash; and <b>the window closed with nothing after 8:37</b> &mdash; verified at 10:07 PM, trash included.',
    'the heaviest day since last Sunday&rsquo;s fourteen &mdash; and <b>the window closed with nothing after 8:37</b> &mdash; verified at 10:07 PM, trash included. The overnight into Monday was not fully quiet: <b>a &ldquo;Call needs attention&rdquo; at 5:28 AM</b>, then the Daily Digests on schedule at 7:00 and <b>a first failure at 7:07 AM</b> &mdash; one failure and one needs-attention by 7:30, window open.')

# ---------- N. sanity ----------
assert s.count('__CC_STATE__') == 1
assert s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59, s.count('data-react-task="')
assert s.count('class="bar"') == 7, s.count('class="bar"')
assert s.count('2026-10-19T07:22:00-05:00') == 2
assert s.count('window open') == 2
assert 'four days past' not in s
assert 'sixteen days' not in s
assert 'Good evening' not in s
assert 'Weekend pocket' not in s

open(P, 'w').write(s)
print('monday full OK, len', len(s))
