#!/usr/bin/env python3
# Sunday Oct 18 date turn (weekend: handled inside the 8:07 AM light pass).
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
rep('day forty-one', 'day forty-two', 3)                  # #799
rx(r'day forty(?!-)', 'day forty-one', 3)                 # Eric x2 + Izzy trio
rep('thirty-seventh day double-approved', 'thirty-eighth day double-approved', 1)
rep('thirty-nine full days ago', 'forty full days ago', 1)
rep('day thirty-eight of billed Logs', 'day thirty-nine of billed Logs', 1)
rep('day thirty-two', 'day thirty-three', 4)              # JDs
rep('fifteen days', 'sixteen days', 5)                    # Emilio
rep('Fifteen days', 'Sixteen days', 1)                    # Emilio pill
rep('three days past', 'four days past', 6)               # ProGraphix
rep('Three days past due', 'Four days past due', 1)       # ProGraphix pill
rep('Day thirty-three on Eric Bramini', 'Day thirty-four on Eric Bramini', 1)
rep('night thirty-three', 'night thirty-four', 2)         # Nick
rep('thirty-five days past', 'thirty-six days past', 2)   # billing/RevIO
rep('twenty-six days unsent', 'twenty-seven days unsent', 1)
rep('forty-seven days past', 'forty-eight days past', 2)  # retirement
rep('em-roadmap at 51 days', 'em-roadmap at 52 days', 1)
rep('day eleven in drafts', 'day twelve in drafts', 1)    # lmathwig Oct 6 draft
rep('Iris, day six', 'Iris, day seven', 1)
rep('Ages as of Oct 17', 'Ages as of Oct 18', 1)

def chip1(m): return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
s, c1 = re.subn(r'(class="chip old">)(\d+)(d</span>)', chip1, s)
s, c2 = re.subn(r'(class="chip old">)(\d+)(d &mdash;)', chip1, s)
assert c1 + c2 == 5, f"chip bumps: {c1}+{c2}"

# ---------- A. stamps / masthead ----------
rep('2026-10-17T22:07:00-05:00', '2026-10-18T08:07:00-05:00', 2)
rep('<b>Brief compiled</b> Sat 8:08 AM &middot; data checked Sat 10:07 PM CT',
    '<b>Brief compiled</b> Sun 8:07 AM &middot; data checked Sun 8:07 AM CT')
rep('Saturday, October 17 &middot; 2026', 'Sunday, October 18 &middot; 2026')
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>')

# ---------- B. sub rewrite (ages written POST-BUMP) ----------
assert s.count('<p class="sub">') == 1
rx(r'<p class="sub">.*?</p>',
   '''<p class="sub">Saturday was the workshop and it ran clean: prep at noon, the <b>AI Employee Workshop 1&ndash;4</b>, breakdown to 4:30 at Gevity &mdash; and the line barely interrupted, closing at <b>one failure (8:16 PM) and one success</b>, the lightest day since the streak began. The carried sends didn&rsquo;t move over the weekend: <b>ProGraphix is four days past the submit-by date</b> (reply deleted, Cathy&rsquo;s follow-up unanswered), the <b>Laura recap + per-account export re-request</b> is still unsent with Monday&rsquo;s 62-account reconciliation riding on it, and the Emilio recap is at <b>sixteen days</b>. Sunday opened to the morning rhythm &mdash; Digests at 7:00, then <b>a needs-attention at 7:46, a failure at 7:55 and a handled call at 8:07 AM</b>. Today is <b>the nature day</b>: nothing scheduled, nothing owed before Monday. One calendar add: <b>&ldquo;Debrief AI&rdquo; Wednesday 11:30&ndash;12:30</b>, pushing Oct 21 to 7.5h. No reactions saved.</p>''')

# ---------- C. needs-decision note ----------
rep('&mdash; decide before Monday; the workshop takes the afternoon',
    '&mdash; Monday morning is the decision point; today stays in nature')

# ---------- D. todaynote + sched ----------
rep('Workshop day &mdash; 4.5h booked from noon; the morning is the only pocket',
    'Nothing booked &mdash; the nature day')
rx(r'<div class="card sched" id="todaysched">.*?</div>\s*</section>',
   '''<div class="card sched" id="todaysched">
        <div class="slot free"><div class="t">All day</div><div class="w">Nothing scheduled<small>The nature day &mdash; Monday opens with Product Sync at 8:00 and the 62-account reconciliation inside Deep Work 10&ndash;2</small></div></div>
      </div>
    </section>''')

# ---------- E. Top 5 ----------
rx(r'<h4>The workshop is TODAY &mdash; prep at noon, doors at 1</h4>.*?</div></li>',
   '''<h4>Monday opens the week: Product Sync 8:00, then the 62-account reconciliation</h4>
          <p class="why">The reconciliation of the <b>62 accounts with active agreements but no live agent</b> is Monday&rsquo;s anchor, inside Deep Work (Engineering) 10&ndash;2 &mdash; and it leans on the Laura recap + per-account export re-request that still hasn&rsquo;t gone out. A Sunday-evening send sets Monday up; otherwise it&rsquo;s the first thing after the sync.</p>
          <div class="meta"><span class="pill warn">Tomorrow</span><span class="pill quiet">Deep Work 10&ndash;2</span></div>
        </div></li>''')
rep('The weekend pockets after the workshop &mdash; or Monday&rsquo;s Deep Work &mdash; are the engineering window.',
    'Sunday stays in nature; Monday&rsquo;s Deep Work (Engineering) 10&ndash;2 is the engineering window.')

# ---------- F. coming-up cards ----------
rx(r'<h4 style="font-size:14px">Today &mdash; workshop day; the morning is the pocket</h4>\s*<p[^>]*>.*?</p>',
   '''<h4 style="font-size:14px">Today &mdash; the nature day; Monday is the re-entry</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">Nothing is scheduled. Monday opens with Product Sync at 8:00, Deep Work (Engineering) 10&ndash;2 holding the <b>62-account reconciliation</b>, and Transition 2&ndash;3. The sends wait at the top of the queue: the <b>ProGraphix decision</b> (four days past), the <b>Laura recap + export re-request</b>, the Emilio recap (sixteen days).</p>''')
rep('<b>Today is the workshop</b> (prep 12&ndash;1, workshop 1&ndash;4, breakdown to 4:30 at Gevity), Luma page live; Sunday stays open &mdash; the nature day.',
    'The workshop ran Saturday 1&ndash;4 at Gevity &mdash; a clean day on the line behind it; today stays open &mdash; the nature day.')
rep('<b>Wednesday Oct 21 runs 6.5h against the 2F-15 artwork deadline</b> (FedEx&rsquo;s specs are with Jr)',
    '<b>Wednesday Oct 21 runs 7.5h against the 2F-15 artwork deadline</b> (FedEx&rsquo;s specs are with Jr) plus the new &ldquo;Debrief AI&rdquo; call 11:30&ndash;12:30')

# ---------- G. week-panel flags ----------
rx(r'<h3><span class="pill warn">Today</span> Saturday is the workshop &mdash; 4\.5h from noon; the morning is the only pocket</h3>\s*<p>.*?</p>',
   '''<h3><span class="pill warn">Today</span> Sunday is the nature day &mdash; nothing scheduled</h3>
          <p>The calendar is empty and stays that way. If anything moves, the light lifts are the sends: the <b>ProGraphix decision</b> (four days past the submit-by date &mdash; Monday morning is the call), the <b>Laura recap + per-account export re-request</b> feeding Monday&rsquo;s reconciliation, and the Emilio recap (sixteen days). Otherwise: nature.</p>''')
rx(r'<h3><span class="pill warn">This week</span> Workshop today, nature Sunday, then a steady week into the 2F-15 and booth deadlines</h3>\s*<p>.*?</p>',
   '''<h3><span class="pill warn">This week</span> A steady week into the 2F-15 and booth deadlines &mdash; Wednesday picks up a debrief</h3>
          <p>Monday 5.75h opens with Product Sync at 8:00 and the <b>62-account billing reconciliation</b>, Tuesday 6.5h has the Izzy check-in at 10:00 and Iris Training 1&ndash;2, <b>Wednesday Oct 21 now runs 7.5h</b> &mdash; the 2F-15 artwork deadline (FedEx&rsquo;s specs with Jr) plus the new <b>&ldquo;Debrief AI&rdquo; call 11:30&ndash;12:30</b> landing inside the Deep Work block &mdash; and Thursday Oct 22 6.5h with the Netsapiens booth bill scheduled 9&ndash;9:30. Friday Oct 23 holds one hour &mdash; AI-Powered Marketing with Claude 9:30&ndash;10:30; Saturday stays open. <b>UGM is the week after, Oct 26&ndash;30.</b></p>''')

# ---------- H. chart ----------
rep('Sat Oct 17 &ndash; Fri Oct 23 &middot;', 'Sun Oct 18 &ndash; Sat Oct 24 &middot;')
rx(r'(<div class="cap8" style="bottom:57\.14%"><span>8h sustainable load</span></div>\n).*?(\n        </div>\n        <div class="xaxis")',
   r'''\g<1>          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(41.07% + 6px)">5.75</div>
            <div class="seg m" style="height:5.36%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(53.57% + 6px)">7.5</div>
            <div class="seg m" style="height:14.29%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:3.57%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(7.14% + 6px)">1</div>
            <div class="seg m" style="height:7.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>\g<2>''')
rep('''<div><b>Sat</b>17</div><div><b>Sun</b>18</div>
          <div><b>Mon</b>19</div><div><b>Tue</b>20</div><div><b>Wed</b>21</div><div><b>Thu</b>22</div><div><b>Fri</b>23</div>''',
    '''<div><b>Sun</b>18</div><div><b>Mon</b>19</div>
          <div><b>Tue</b>20</div><div><b>Wed</b>21</div><div><b>Thu</b>22</div><div><b>Fri</b>23</div><div><b>Sat</b>24</div>''')

# ---------- I. table rows ----------
rep('<td class="tid">Carried from Fri</td>', '<td class="tid">Carried</td>')
rep('the workshop is today &mdash; the landing page never shipped; the JDs are still owed for the hiring push itself',
    'the workshop ran Saturday &mdash; the landing page never shipped; the JDs are still owed for the hiring push itself')

# ---------- J. ledger: Sunday opener ----------
rep('and <b>the window closed with nothing after 8:16</b> &mdash; verified at 10:07 PM, trash included.',
    'and <b>the window closed with nothing after 8:16</b> &mdash; verified at 10:07 PM, trash included. The overnight into Sunday stayed quiet &mdash; Sunday opened to the morning rhythm: Daily Digests at 7:00, then <b>a &ldquo;Call needs attention&rdquo; at 7:46, a failure at 7:55 and a &ldquo;Call handled&rdquo; success at 8:07 AM</b> &mdash; one failure, one needs-attention and one success by 8, window open.')

# ---------- N. sanity ----------
assert s.count('__CC_STATE__') == 1
assert s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59, s.count('data-react-task="')
assert s.count('class="bar"') == 7, s.count('class="bar"')
assert s.count('2026-10-18T08:07:00-05:00') == 2
assert s.count('window open') == 2          # live Sunday + archival "window opened"
assert 'workshop is TODAY' not in s
assert 'three days past' not in s
assert 'fifteen days' not in s
assert 'Good evening' not in s

open(P, 'w').write(s)
print('sunday turn OK, len', len(s))
