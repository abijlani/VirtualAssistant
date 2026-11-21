council = None  # Saturday Nov 21 weekend day turn (light-tick day turn; no full-pass brief)
import re
P = 'page-template.html'
s = open(P).read()

def rep(old, new, n):
    global s
    c = s.count(old)
    assert c == n, ('REP COUNT', old[:70], c, n)
    s = s.replace(old, new)

# ---------- 1. ages, highest first ----------
rep('day seventy-five', 'day seventy-six', 3)
rep('day seventy-four', 'day seventy-five', 3)
rep('night sixty-seven', 'night sixty-eight', 2)
rep('day sixty-six', 'day sixty-seven', 1)
rep('sixty-nine days past', 'seventy days past', 4)
rep('fifty-nine days past', 'sixty days past', 1)
s2 = re.subn(r'day forty(?!-)', 'day forty-one', s)
assert s2[1] == 2, s2[1]
s = s2[0]
rep('Thirty-seven days past', 'Thirty-eight days past', 2)
rep('thirty-seven days past', 'thirty-eight days past', 2)
rep('(thirty-seven days)', '(thirty-eight days)', 2)
rep('day thirty-two', 'day thirty-three', 4)
rep('Day thirty-two', 'Day thirty-three', 2)
rep('95 days', '96 days', 1)
rep('Ages as of Nov 20', 'Ages as of Nov 21', 1)
rep('twenty-two days past due', 'twenty-three days past due', 3)
rep('is sixteen days old', 'is seventeen days old', 3)

# ---------- 2. stamps / eyebrow / brief line ----------
rep('2026-11-20T21:07:00-06:00', '2026-11-21T07:07:00-06:00', 2)
rep('Friday, November 20', 'Saturday, November 21', 1)
rep('<b>Brief compiled</b> Fri 6:11 AM &middot; data checked Fri 9:07 PM CT',
    '<b>Brief compiled</b> Fri 6:11 AM &middot; data checked Sat 7:07 AM CT', 1)

# ---------- 3. masthead splice ----------
i = s.index('Friday is a light one')
j = s.index('No reactions saved.</p>')
new_masthead = (
 'Saturday is for the neighborhood: the <b>Lady Bird trail cleanup runs 9:30&ndash;12</b> with the '
 'picnic after, and <b>Friendsgiving at Ashlyn&rsquo;s is 5&ndash;8</b>. One piece of business is '
 'worth two minutes before the weekend takes over: <b>the $3,000 Exit Code ACH to Valera bounced '
 'Friday at 4:41 PM</b> &mdash; the invoice came due Friday, so the payment needs a re-send. '
 'Friday otherwise ended well: <b>Stratus signed</b> and Jr sent Alex Penichet the onboarding '
 'form, <b>Nortec ran its onboarding end to end</b> with the final one-line config step delivered, '
 '<b>Nicole Berry&rsquo;s reseller call ran at 1:30</b>, and Jordan&rsquo;s Test Suite fix held. '
 'Still open going into the holiday week: the <b>Kimberly note is eight days old</b>, <b>four '
 'drafts sit unsent</b> (the Tim draft is seventeen days old, the record now at day thirty-three), '
 'and the <b>$5,000 invoice is twenty-three days past due</b> unless the ACH cleared it. '
)
s = s[:i] + new_masthead + s[j:]

# ---------- 4. ledger: close Friday, open Saturday ----------
rep('and <b>failures at 6:54 and 7:47</b> &mdash; the tenth straight evening with events &mdash; <b>5&ndash;1&ndash;1 by 9:07, window open</b>.',
    'and <b>failures at 6:54 and 7:47</b> &mdash; the tenth straight evening with events &mdash; then a <b>late failure between 9 PM and midnight</b>. <b>Friday closes 6&ndash;1&ndash;1</b> &mdash; eight events, verified Saturday morning with trash included. The overnight into Saturday was restless: a <b>success at 1:02 AM</b>, a <b>failure at 1:23</b> and an overnight <b>needs-attention</b>, then another <b>needs-attention at 6:54 AM</b> &mdash; <b>1&ndash;2&ndash;1 by 7:07, window open</b>.', 1)

# ---------- 5. todaynote + todaysched ----------
rep('Friday &mdash; Pitch and Run 8&ndash;9, Gevity pizza 12:30&ndash;1:30, Nicole Berry 1:30&ndash;2 &mdash; 2.5h',
    'Saturday &mdash; Lady Bird trail cleanup 9:30&ndash;12, Friendsgiving at Ashlyn&rsquo;s 5&ndash;8 &mdash; 5.5h', 1)
a = s.index('<div class="card sched" id="todaysched">')
b = s.index('</section>', a)
new_sched = ('<div class="card sched" id="todaysched">\n'
 '        <div class="slot free"><div class="t">7:00&ndash;9:30</div><div class="w">Open morning<small><b>Re-send the Exit Code payment</b> (the ACH bounced Friday at 4:41); the <b>Kimberly note</b> (eight days) travels fine on a Saturday</small></div></div>\n'
 '        <div class="slot"><div class="t">9:30&ndash;12:00</div><div class="w">Lady Bird Lake Trail Clean Up &amp; Picnic<small>Swedish Hill pastries and coffee after the cleanup</small></div></div>\n'
 '        <div class="slot free"><div class="t">12:00&ndash;5:00</div><div class="w">Open afternoon<small>Nothing scheduled &mdash; the weekend is the plan</small></div></div>\n'
 '        <div class="slot"><div class="t">5:00&ndash;8:00</div><div class="w">Friendsgiving at Ashlyn&rsquo;s<small>Moved from Friday &mdash; the week ends with people</small></div></div>\n'
 '      </div>\n    ')
s = s[:a] + new_sched + s[b:]

# ---------- 6. chart roll Sat 21 - Fri 27 ----------
a = s.index('<div class="plot" id="plot">')
b = s.index('<div class="xaxis"', a)
def bar(tot, pct, segs):
    inner = ''.join('<div class="seg %s" style="height:%s%%"></div>' % (k, v) for k, v in segs)
    return ('          <div class="bar"><div class="tot" style="bottom:calc(%s%% + 6px)">%s</div>\n'
            '            %s</div>\n' % (pct, tot, inner))
new_plot = ('<div class="plot" id="plot">\n'
 '          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>\n'
 + bar('5.5', '39.29', [('p', '39.29')])
 + bar('2', '14.29', [('p', '14.29')])
 + bar('6.75', '48.21', [('m', '12.5'), ('f', '35.71')])
 + bar('8', '57.14', [('m', '21.43'), ('f', '35.71')])
 + bar('6.5', '46.43', [('m', '7.14'), ('f', '35.71'), ('p', '3.57')])
 + bar('5.5', '39.29', [('m', '7.14'), ('f', '32.14')])
 + bar('0', '0', [])
 + '        </div>\n        ')
s = s[:a] + new_plot + s[b:]
rep('<div><b>Fri</b>20</div><div><b>Sat</b>21</div>\n          <div><b>Sun</b>22</div><div><b>Mon</b>23</div><div><b>Tue</b>24</div><div><b>Wed</b>25</div><div><b>Thu</b>26</div>',
    '<div><b>Sat</b>21</div><div><b>Sun</b>22</div>\n          <div><b>Mon</b>23</div><div><b>Tue</b>24</div><div><b>Wed</b>25</div><div><b>Thu</b>26</div><div><b>Fri</b>27</div>', 1)
rep('Fri Nov 20 &ndash; Thu Nov 26', 'Sat Nov 21 &ndash; Fri Nov 27', 1)

# ---------- 7. Today flag ----------
a = s.index('<p><b>Mercury says the $3,000 ACH to Valera didn&rsquo;t go through</b>')
b = s.index('</p>', a) + 4
new_flag = ('<p><b>Mercury flagged the $3,000 ACH to Valera at 4:41 PM Friday</b> &mdash; the Exit '
 'Code payment bounced on its due date, and nothing since shows a re-send. Two minutes fixes it, '
 'and it&rsquo;s the only business item between you and the weekend: the <b>trail cleanup is '
 '9:30&ndash;12</b> and <b>Friendsgiving at Ashlyn&rsquo;s is 5&ndash;8</b>.</p>')
s = s[:a] + new_flag + s[b:]

# ---------- 8. markers: retire the stale "today" ----------
rep('<b>Access Systems &mdash; Nicole Berry today 1:30</b>, a 500-customer reseller interested in white-labeling;',
    '<b>Access Systems &mdash; Nicole Berry&rsquo;s call ran Friday</b>, a 500-customer reseller interested in white-labeling;', 1)

# ---------- 9. coming-up ----------
rep('A light Friday into Friendsgiving weekend, then a holiday-short week',
    'Friendsgiving today, then a holiday-short week', 1)
n = s.index('Friendsgiving today, then a holiday-short week')
l = s.index('<p ', n)
m = s.index('</p>', l) + 4
new_coming = ('<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Today &mdash; 5.5h, all '
 'of it chosen: <b>Lady Bird trail cleanup 9:30&ndash;12</b>, then <b>Friendsgiving at '
 'Ashlyn&rsquo;s 5&ndash;8</b>. Sunday: Pilates 9:30 and the red-light bed. Monday Nov 23 &mdash; '
 '6.75h: sync 8, DW Engineering 10&ndash;2 with <b>the Threshold demo 1&ndash;2 inside it</b>, '
 'TTT 2. Tuesday Nov 24 &mdash; 8h, touching the line: Izzy 10, <b>ATS catch-up 10:30</b>, '
 '<b>GamifyOS Sync noon</b>, <b>Iris training 1</b> inside DW Client 10&ndash;2, TTT 2. Wednesday '
 'Nov 25 &mdash; 6.5h: Recover 9, SustAmb 9:30, DW 11&ndash;3, TTT 3. Thursday Nov 26 is '
 'Thanksgiving &mdash; 5.5h still on the calendar: DW 8:30&ndash;12:30 with <b>Scott Van Camp '
 'inside it at 10&ndash;11</b>, Reserved 3:30 &mdash; worth deciding whether that block survives '
 'the holiday. Friday Nov 27 is clear. Carried: <b>the Cathy call</b> (thirty-eight days), <b>the '
 'CCI booking</b>, the drip and performance reports, the ATS five, the Whova trio, the Sahiti '
 'intro, the <b>Rev.io sessions ask</b>, and the <b>invoice &mdash; twenty-three days past due '
 'unless the ACH cleared it</b>.</p>')
s = s[:l] + new_coming + s[m:]

# ---------- sanity ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-21T07:07:00-06:00') == 2
assert s.count('window open') == 2
assert s.count('Good morning, Bodhi.') == 1
assert s.count('No reactions saved.') == 1
assert s.count('hit day thirty') == 1
assert s.count('thirty-three days now') == 1
assert s.count('seven days old') == 0
assert s.count('Saturday, November 21') == 1
assert s.count('Sat Nov 21 &ndash; Fri Nov 27') == 1
for bad in ['ebccf397', 'atscall', '3,082', 'Jose Luiz', '5WY67Sa2', 'PasswordReset',
            'billcenter.net', 'hw7Mh6cK', 'pY3DM73R', 'bT5uDhjRSBk3', 'mm7me9zr', 'fK9Bn7og',
            'quoter.com', 'smartkonnect.app', 'jY9Li67u', 'vercel-dns', 'vee.js']:
    assert bad not in s, bad
open(P, 'w').write(s)
print('SATURDAY TURN OK', len(s))
