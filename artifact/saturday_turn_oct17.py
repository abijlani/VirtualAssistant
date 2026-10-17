#!/usr/bin/env python3
# Saturday Oct 17 date turn (weekend: handled inside the 8:08 AM light pass).
# Pattern: global age bumps FIRST (counts from the untouched template), then
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
rep('day forty', 'day forty-one', 3)                      # #799 x3
rep('thirty-sixth day double-approved', 'thirty-seventh day double-approved', 1)
rep('day thirty-nine', 'day forty', 2)                    # Eric
rep('thirty-eight full days ago', 'thirty-nine full days ago', 1)
rep('day thirty-seven of billed Logs', 'day thirty-eight of billed Logs', 1)
rep('day thirty-one', 'day thirty-two', 5)                # JDs
rep('fourteen days', 'fifteen days', 4)                   # Emilio
rep('Fourteen days', 'Fifteen days', 1)                   # Emilio pill
rep('two days past', 'three days past', 5)                # ProGraphix
rep('Two days past due', 'Three days past due', 1)        # ProGraphix pill
rep('Day thirty-two on Eric Bramini', 'Day thirty-three on Eric Bramini', 1)
rep('night thirty-two', 'night thirty-three', 2)          # Nick
rep('thirty-four days past', 'thirty-five days past', 2)  # billing/RevIO
rep('twenty-five days unsent', 'twenty-six days unsent', 1)
rep('forty-six days past', 'forty-seven days past', 2)    # retirement
rep('em-roadmap at 50 days', 'em-roadmap at 51 days', 1)
rep('day ten in drafts', 'day eleven in drafts', 1)       # lmathwig Oct 6 draft
rep('Iris, day five', 'Iris, day six', 1)
rep('Ages as of Oct 7 &middot; the Izzy DMS trio (iz-dms, iz-apis, iz-shawn) enters day thirty',
    'Ages as of Oct 17 &middot; the Izzy DMS trio (iz-dms, iz-apis, iz-shawn) is at day forty')

# chip auto-bump (+1 on every chip old)
def chip1(m): return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
s, c1 = re.subn(r'(class="chip old">)(\d+)(d</span>)', chip1, s)
s, c2 = re.subn(r'(class="chip old">)(\d+)(d &mdash;)', chip1, s)
assert c1 + c2 == 5, f"chip bumps: {c1}+{c2}"

# ---------- A. stamps / masthead ----------
rep('2026-10-16T22:07:00-05:00', '2026-10-17T08:08:00-05:00', 2)
rep('<b>Brief compiled</b> Fri 7:21 AM &middot; data checked Fri 10:07 PM CT',
    '<b>Brief compiled</b> Sat 8:08 AM &middot; data checked Sat 8:08 AM CT')
rep('Friday, October 16 &middot; 2026', 'Saturday, October 17 &middot; 2026')
rep('<h1>Good evening, Bodhi.</h1>', '<h1>Good morning, Bodhi.</h1>')

# ---------- B. sub rewrite (ages written POST-BUMP) ----------
assert s.count('<p class="sub">') == 1
rx(r'<p class="sub">.*?</p>',
   '''<p class="sub">Friday held its sends: the 10&ndash;11 audit block is behind you, but <b>the Laura recap + per-account export re-request never left</b> &mdash; no mail moved on it by this morning &mdash; and Monday&rsquo;s <b>62-account billing reconciliation</b> rides on it. <b>ProGraphix is now three days past the submit-by date</b>: the drafted reply stays deleted, the thread stayed silent through Friday, Cathy&rsquo;s follow-up unanswered. The Emilio recap reached <b>fifteen days</b> with the binding-agreement redline sitting with Jake and Matt. The line ran to pattern &mdash; four failures and two needs-attention, the evening burst ending at 7:50 &mdash; then <b>the overnight stayed quiet and Saturday opened clean</b>: a &ldquo;Call handled&rdquo; success at 6:45 AM, Daily Digests on schedule at 7:00, no failures by 8. Today is <b>the workshop</b>: prep 12&ndash;1, AI Employee Workshop 1&ndash;4, breakdown to 4:30 at Gevity, Luma page live &mdash; the morning is the only open pocket. No reactions saved.</p>''')

# ---------- C. needs-decision note ----------
rx(r'<span class="note">ProGraphix is three days past its submit-by date.*?</span>',
   '<span class="note">ProGraphix is three days past its submit-by date with the drafted reply deleted unsent &mdash; decide before Monday; the workshop takes the afternoon</span>')

# ---------- D. todaynote + sched ----------
rep('1h booked &mdash; the Iris audit block 10&ndash;11; the valve day before tomorrow&rsquo;s workshop',
    'Workshop day &mdash; 4.5h booked from noon; the morning is the only pocket')
rx(r'<div class="card sched" id="todaysched">.*?</div>\s*</section>',
   '''<div class="card sched" id="todaysched">
        <div class="slot free"><div class="t">Until noon</div><div class="w">Open morning<small>ProGraphix decision &middot; the Laura recap + export re-request &middot; final workshop prep</small></div></div>
        <div class="slot"><div class="t">12:00 &ndash; 1:00</div><div class="w">AI Employee Workshop Prep<small>Gevity: Social Wellness Club</small></div></div>
        <div class="slot"><div class="t">1:00 &ndash; 4:00</div><div class="w">AI Employee Workshop<small>Gevity &middot; Luma page live</small></div></div>
        <div class="slot"><div class="t">4:00 &ndash; 4:30</div><div class="w">Workshop Breakdown</div></div>
      </div>
    </section>''')

# ---------- E. Top 5 ----------
# 1: ProGraphix — weekend framing (ages already bumped by section L)
rep('Decide this morning: submit and reply, call her directly, or accept that the conference date slips.',
    'Nothing moved Friday. Decide this weekend: submit and reply, call her first thing Monday, or accept that the conference date slips.')
# 2: audit block -> workshop TODAY
rx(r'<h4>The Iris audit block, 10&ndash;11 &mdash; your own five-point agenda</h4>.*?</div></li>',
   '''<h4>The workshop is TODAY &mdash; prep at noon, doors at 1</h4>
          <p class="why">Prep 12&ndash;1, AI Employee Workshop 1&ndash;4, breakdown to 4:30 at Gevity &mdash; the Luma page is live. Everything else moves around it: the morning is the only open pocket until Sunday.</p>
          <div class="meta"><span class="pill crit">Today 1&ndash;4</span><span class="pill quiet">Prep 12&ndash;1 &middot; Gevity</span></div>
        </div></li>''')
# 3: workshop-tomorrow -> audit follow-through sends
rx(r'<h4>The workshop is TOMORROW &mdash; today is the last pocket</h4>.*?</div></li>',
   '''<h4>The audit follow-through hasn&rsquo;t left &mdash; Laura&rsquo;s recap + per-account export re-request</h4>
          <p class="why">Friday&rsquo;s 10&ndash;11 block set the five actions, but no mail went to Laura by this morning. The recap re-requesting the per-account export (go-live, trial dates, cancel date/reason, owner, salesperson, minutes) is what keeps <b>Monday&rsquo;s 62-account reconciliation</b> honest &mdash; a weekend send beats a Monday scramble.</p>
          <div class="meta"><span class="pill warn">Unsent</span><span class="pill quiet">Monday depends on it</span></div>
        </div></li>''')
# 5: #992 timing + pocket wording
rep('(VOXAI-936: suffix transfer tools with Ring/Voicemail) last evening.',
    '(VOXAI-936: suffix transfer tools with Ring/Voicemail) Thursday evening.')
rep('The hours after the audit block are the engineering pocket.',
    'The weekend pockets after the workshop &mdash; or Monday&rsquo;s Deep Work &mdash; are the engineering window.')
rep('<span class="pill quiet">After 11</span>', '<span class="pill quiet">Weekend pocket</span>')

# ---------- F. coming-up cards ----------
rep('Your 10&ndash;11 block today carries the follow-through',
    'Friday&rsquo;s 10&ndash;11 block set the follow-through &mdash; the recap + export re-request hasn&rsquo;t gone out yet')
rx(r'<h4 style="font-size:14px">Today 10&ndash;11, otherwise open &mdash; the valve before the workshop</h4>\s*<p[^>]*>.*?</p>',
   '''<h4 style="font-size:14px">Today &mdash; workshop day; the morning is the pocket</h4>
          <p style="font-size:13px;color:var(--ink-2);margin-top:7px">Prep 12&ndash;1, workshop 1&ndash;4, breakdown to 4:30 at Gevity. The morning pocket holds the carried sends: the <b>ProGraphix decision</b> (three days past due), the <b>Laura recap + export re-request</b>, the Emilio recap (fifteen days), and the job descriptions (day thirty-two) if energy allows. Sunday stays in nature; Monday opens with the 62-account reconciliation.</p>''')
rep('<b>Saturday is the workshop</b> (prep 12&ndash;1, workshop 1&ndash;4, breakdown to 4:30), Luma page live; Sunday stays open &mdash; the nature day.',
    '<b>Today is the workshop</b> (prep 12&ndash;1, workshop 1&ndash;4, breakdown to 4:30 at Gevity), Luma page live; Sunday stays open &mdash; the nature day.')
rep('scheduled 9&ndash;9:30 inside Deep Work. UGM itself is Oct 26&ndash;30 in Austin.',
    'scheduled 9&ndash;9:30 inside Deep Work. Friday Oct 23 holds one hour &mdash; AI-Powered Marketing with Claude, 9:30&ndash;10:30. UGM itself is Oct 26&ndash;30 in Austin.')

# ---------- G. week-panel flags ----------
rx(r'<h3><span class="pill warn">Today</span> Friday has one booked hour &mdash; the audit block 10&ndash;11; everything else is the valve</h3>\s*<p>.*?</p>',
   '''<h3><span class="pill warn">Today</span> Saturday is the workshop &mdash; 4.5h from noon; the morning is the only pocket</h3>
          <p>Prep 12&ndash;1, the <b>AI Employee Workshop 1&ndash;4</b>, breakdown to 4:30 at Gevity &mdash; Luma page live. Before noon: the <b>ProGraphix decision</b> (three days past the submit-by date, reply deleted unsent) and the <b>Laura recap + per-account export re-request</b> that didn&rsquo;t leave Friday. The job descriptions (day thirty-two) and the Emilio recap (fifteen days) ride the weekend.</p>''')
rx(r'<h3><span class="pill warn">This week</span> The workshop is tomorrow; next week runs steady into the 2F-15 and booth deadlines</h3>\s*<p>.*?</p>',
   '''<h3><span class="pill warn">This week</span> Workshop today, nature Sunday, then a steady week into the 2F-15 and booth deadlines</h3>
          <p>Sunday stays open &mdash; the nature day. Next week opens gentle: Monday 5.75h with Product Sync at 8:00 and the <b>62-account billing reconciliation</b>, Tuesday 6.5h with the Izzy check-in at 10:00 and Iris Training 1&ndash;2, <b>Wednesday Oct 21 runs 6.5h against the 2F-15 artwork deadline</b> (FedEx&rsquo;s specs already in Jr&rsquo;s hands), and Thursday Oct 22 6.5h with the Netsapiens booth bill scheduled 9&ndash;9:30. Friday Oct 23 holds one hour &mdash; AI-Powered Marketing with Claude 9:30&ndash;10:30. <b>UGM is the week after, Oct 26&ndash;30.</b></p>''')

# ---------- H. chart ----------
rep('Fri Oct 16 &ndash; Thu Oct 22 &middot;', 'Sat Oct 17 &ndash; Fri Oct 23 &middot;')
rx(r'(<div class="cap8" style="bottom:57\.14%"><span>8h sustainable load</span></div>\n).*?(\n        </div>\n        <div class="xaxis")',
   r'''\g<1>          <div class="bar"><div class="tot" style="bottom:calc(32.14% + 6px)">4.5</div>
            <div class="seg m" style="height:32.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(41.07% + 6px)">5.75</div>
            <div class="seg m" style="height:5.36%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
            <div class="seg m" style="height:7.14%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:3.57%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(7.14% + 6px)">1</div>
            <div class="seg m" style="height:7.14%"></div></div>\g<2>''')
rep('''<div><b>Fri</b>16</div><div><b>Sat</b>17</div>
          <div><b>Sun</b>18</div><div><b>Mon</b>19</div><div><b>Tue</b>20</div><div><b>Wed</b>21</div><div><b>Thu</b>22</div>''',
    '''<div><b>Sat</b>17</div><div><b>Sun</b>18</div>
          <div><b>Mon</b>19</div><div><b>Tue</b>20</div><div><b>Wed</b>21</div><div><b>Thu</b>22</div><div><b>Fri</b>23</div>''')

# ---------- I. already-home table rows ----------
rep('<td class="tid">Today after 11</td><td><b>The Emilio recap</b>',
    '<td class="tid">Carried from Fri</td><td><b>The Emilio recap</b>')
rep('<b>the Laura recap + per-account export re-request</b> out of the audit block',
    '<b>the Laura recap + per-account export re-request</b> &mdash; none of the three moved Friday')
rep('<td class="tid">Today</td><td><b>The three job descriptions</b>',
    '<td class="tid">This weekend</td><td><b>The three job descriptions</b>')
rep('ws-jds &rarr; ws-landing &middot; the workshop is tomorrow &mdash; today&rsquo;s open afternoon is the last pocket',
    'ws-jds &rarr; ws-landing &middot; the workshop is today &mdash; the landing page never shipped; the JDs are still owed for the hiring push itself')
rep('<td class="tid">Today after 11</td><td><b>The identification query first</b>',
    '<td class="tid">Weekend pocket</td><td><b>The identification query first</b>')

# ---------- J. ledger: Saturday opener + stale "this morning" ----------
rep('LiveKit logged another Frankfurt incident this morning',
    'LiveKit logged another Frankfurt incident Friday morning')
rep('after Thursday&rsquo;s burst, not during it.)',
    'after Thursday&rsquo;s burst, not during it.) The overnight into Saturday stayed quiet &mdash; <b>Saturday opened clean</b>: a &ldquo;Call handled&rdquo; success at 6:45 AM and the morning Daily Digests on schedule at 7:00, no failures by 8.')

# ---------- N. sanity ----------
assert s.count('__CC_STATE__') == 1
assert s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59, s.count('data-react-task="')
assert s.count('class="bar"') == 7, s.count('class="bar"')
assert s.count('2026-10-17T08:08:00-05:00') == 2
assert s.count('window open') == 1          # only the archival "window opened"
assert 'TOMORROW' not in s
assert 'two days past' not in s
assert 'fourteen days' not in s
assert 'Good evening' not in s

open(P, 'w').write(s)
print('saturday turn OK, len', len(s))
