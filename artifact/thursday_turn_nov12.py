# Thursday Nov 12, 2026 full-pass day turn (fired 6:13 AM CT).
# Day facts: Wednesday closed 1-3-1 (NAs 7:12/10:09 AM + 6:35 PM, success 7:43 PM,
# single late failure 10:36 PM) - lightest weekday on the ledger; the four-day
# evening-burst pattern broke (no 6-9 PM failures). Thursday is now 9.75h: NEW
# "Finish Honor's proposal" 9-10 block (from latentworks calendar) + DW 10-2 +
# Scott 2 + Reserved 3:30 + Tash 4:45 + Friendsgiving 6-9 (bring a dessert).
# Stratus demo DUPLICATED: Bodhi's event Tue Nov 17 10:40 (Penichet+Weakland
# accepted, Carlos Melo added) AND Jr's Wed Nov 18 10:40 (Hymbaugh+Weakland
# accepted) - consolidate. Kimberly invite STILL unsent, slot wanted Fri 2 PM,
# she briefs Lauren+Janet Thursday AM. Drafts still three (Tim day 24).
# Wednesday meetings: GamifyOS sync -> Phase 1 proposal (perf/visibility
# dashboard) + Discord channel norms; Ellie x Caroline x Taylor -> Dec 11
# half-day event at Jevity, GamifyOS drafts curriculum for Caroline.
# Personal-reflection Granola note (7:31 PM) deliberately kept OFF the page.
# Chart rolls Thu Nov 12 - Wed Nov 18. Hazards: bump sixty-six before
# sixty-five; '(twenty-eight days)' now x2; new Meet code hag-efnz-nvc must
# not surface.
import re

p = 'page-template.html'
s = open(p).read()

def rep(old, new, n):
    global s
    c = s.count(old)
    assert c == n, (old[:60], c, n)
    s = s.replace(old, new)

# ---------- 1. Global age bumps (highest first) ----------
rep('day sixty-six', 'day sixty-seven', 3)
rep('day sixty-five', 'day sixty-six', 3)
rep('night fifty-eight', 'night fifty-nine', 2)
rep('day fifty-seven;', 'day fifty-eight;', 1)
rep('sixty days past', 'sixty-one days past', 4)
rep('fifty days past', 'fifty-one days past', 1)
rep('day thirty-one', 'day thirty-two', 1)
rep('twenty-eight days past', 'twenty-nine days past', 2)
rep('Twenty-eight', 'Twenty-nine', 2)
rep('(twenty-eight days)', '(twenty-nine days)', 2)
rep('day twenty-three', 'day twenty-four', 5)
rep('Day twenty-three &mdash; one click closes it', 'Day twenty-four &mdash; one click closes it', 1)
rep('86 days', '87 days', 1)
rep('Ages as of Nov 11', 'Ages as of Nov 12', 1)
rep('thirteen days past due', 'fourteen days past due', 2)
rep('is seven days old', 'is eight days old', 1)

# ---------- 2. Stamps / header / greeting ----------
rep('2026-11-11T21:07:00-06:00', '2026-11-12T06:13:00-06:00', 2)
rep('<b>Brief compiled</b> Wed 6:13 AM &middot; data checked Wed 9:07 PM CT',
    '<b>Brief compiled</b> Thu 6:13 AM &middot; data checked Thu 6:13 AM CT', 1)
rep('Wednesday, November 11', 'Thursday, November 12', 1)
rep('Good evening, Bodhi.', 'Good morning, Bodhi.', 1)

# ---------- 3. Masthead ----------
masthead = (
 'Thursday is the heaviest day of the week &mdash; <b>9.75 hours</b>: a new <b>Finish Honor&rsquo;s '
 'proposal block at 9</b> (from your Latent Works calendar), DW Project Engineering 10&ndash;2, '
 '<b>Scott Van Camp at 2</b>, Reserved 3:30, <b>Chat with Tash at 4:45</b>, then <b>Friendsgiving '
 '6&ndash;9</b> &mdash; bring a dessert. The clock item: <b>the Kimberly Ragsdale discovery invite is '
 'still unsent and the slot she wants is tomorrow 2 PM</b> &mdash; she briefs Lauren and Janet this '
 'morning, so send it before the 9 AM block. <b>The Stratus demo now exists twice</b>: your event '
 '<b>Tuesday Nov 17, 10:40</b> (Alex Penichet and Edward Weakland accepted, Carlos Melo added) and '
 'Jr&rsquo;s <b>Wednesday Nov 18, 10:40</b> (Joseph Hymbaugh and Weakland accepted) &mdash; one demo, '
 'two invites; pick one and cancel the other. <b>Three drafts still wait on Send</b>: Tim (day '
 'twenty-four), Affiliated Tech, GigTel. Yesterday moved pieces: <b>Michael Wheelock got vendor-portal '
 'access</b> on Environmental Pest at your 3:10 reply, <b>Laparkan is moving with Jr</b>, '
 '<b>Threshold came back warm</b>, and the GamifyOS sync produced its next step &mdash; <b>the Phase 1 '
 'proposal</b> (performance/visibility dashboard) plus Discord-channel norms to socialize. The Ellie '
 '&times; Caroline &times; Taylor meeting set a <b>December 11 half-day event at Jevity</b> &mdash; '
 'GamifyOS drafts the curriculum for Caroline. The <b>GamifyOS page + landing were due live '
 'yesterday</b> &mdash; no confirmation either way, worth a check. <b>Per-location alert routing is '
 'due to production by tomorrow</b>. Wednesday closed <b>1&ndash;3&ndash;1</b> &mdash; the lightest '
 'weekday recorded, and the evening-burst pattern broke. No reactions saved.</p>')
i = s.index('Wednesday is the day the week has been bracing for:')
j = s.index('No reactions saved.</p>', i) + len('No reactions saved.</p>')
s = s[:i] + masthead + s[j:]

# ---------- 4. Ledger: close Wednesday, open Thursday ----------
rep('then a third at <b>6:35 PM</b> and a <b>success at 7:43 PM</b> &mdash; <b>0&ndash;3&ndash;1 by '
    '9:07, window open</b>: no failures yet, and the evening window has produced only the softer '
    'review class and a handled call so far.',
    'then a third at <b>6:35 PM</b>, a <b>success at 7:43 PM</b>, and the day&rsquo;s only failure '
    'late, at <b>10:36 PM</b>. <b>Wednesday closes 1&ndash;3&ndash;1</b>, five events, verified '
    'Thursday morning with trash included &mdash; the lightest weekday on the ledger, and the '
    '<b>four-day evening-burst pattern broke</b>: no failures at all in the 6&ndash;9 window. The '
    'overnight into Thursday stayed quiet &mdash; <b>0&ndash;0&ndash;0 by 6:13, window open</b>.', 1)

# ---------- 5. Today note + schedule ----------
rep('GamifyOS Sync 11 inside DW 11&ndash;3 &mdash; 8.5h, deliverables due live; Recover 9, SustAmb 9:30, '
    'Ellie 10:30, Ladybug 5',
    'Heaviest day of the week &mdash; 9.75h: Honor proposal 9, DW 10&ndash;2, Scott 2, Tash 4:45, '
    'Friendsgiving 6&ndash;9', 1)

sched = '''<div class="card sched" id="todaysched">
        <div class="slot"><div class="t">9:00&ndash;10:00</div><div class="w">Finish Honor&rsquo;s proposal<small>New block from your Latent Works calendar &mdash; and the natural moment to <b>send the Kimberly invite for tomorrow 2 PM</b> before the day swallows it</small></div></div>
        <div class="slot"><div class="t">10:00&ndash;2:00</div><div class="w">Deep Work (Project Engineering)<small>The three drafts (Tim day twenty-four, Affiliated Tech, GigTel), the GamifyOS Phase 1 proposal, the Stratus duplicate to consolidate, PR #1121 fixes, the Rev.io review read</small></div></div>
        <div class="slot"><div class="t">2:00&ndash;3:00</div><div class="w">Call with Scott Van Camp<small>Recurring</small></div></div>
        <div class="slot"><div class="t">3:30&ndash;4:00</div><div class="w">Reserved<small>Overflow &mdash; whatever the 10&ndash;2 block did not finish</small></div></div>
        <div class="slot"><div class="t">4:45&ndash;5:00</div><div class="w">Chat with Tash<small>Fifteen minutes, your event</small></div></div>
        <div class="slot"><div class="t">6:00&ndash;9:00</div><div class="w">Friendsgiving Social &mdash; Gevity Club<small>Dinner, live jazz, tree ceremony &mdash; <b>bring a dessert to share</b></small></div></div>
      </div>
    </section>'''
i = s.index('<div class="card sched" id="todaysched">')
j = s.index('</section>', i) + len('</section>')
s = s[:i] + sched + s[j:]

# ---------- 6. Chart: roll week Thu Nov 12 - Wed Nov 18 ----------
rep('Wed Nov 11 &ndash; Tue Nov 17', 'Thu Nov 12 &ndash; Wed Nov 18', 1)
plot = '''<div class="plot" id="plot">
          <div class="cap8" style="bottom:57.14%"><span>8h sustainable load</span></div>
          <div class="bar"><div class="tot" style="bottom:calc(69.64% + 6px)">9.75</div>
            <div class="seg m" style="height:37.5%"></div><div class="seg f" style="height:32.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(17.86% + 6px)">2.5</div>
            <div class="seg m" style="height:10.71%"></div><div class="seg p" style="height:7.14%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(21.43% + 6px)">3</div>
            <div class="seg p" style="height:21.43%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(0% + 6px)">0</div></div>
          <div class="bar"><div class="tot" style="bottom:calc(48.21% + 6px)">6.75</div>
            <div class="seg m" style="height:12.5%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(46.43% + 6px)">6.5</div>
            <div class="seg m" style="height:10.71%"></div><div class="seg f" style="height:35.71%"></div></div>
          <div class="bar"><div class="tot" style="bottom:calc(53.57% + 6px)">7.5</div>
            <div class="seg m" style="height:14.29%"></div><div class="seg f" style="height:35.71%"></div><div class="seg p" style="height:3.57%"></div></div>
        </div>
        '''
i = s.index('<div class="plot" id="plot">')
j = s.index('<div class="xaxis"', i)
s = s[:i] + plot + s[j:]

rep('<div><b>Wed</b>11</div><div><b>Thu</b>12</div>\n          <div><b>Fri</b>13</div><div><b>Sat</b>14</div><div><b>Sun</b>15</div><div><b>Mon</b>16</div><div><b>Tue</b>17</div>',
    '<div><b>Thu</b>12</div><div><b>Fri</b>13</div>\n          <div><b>Sat</b>14</div><div><b>Sun</b>15</div><div><b>Mon</b>16</div><div><b>Tue</b>17</div><div><b>Wed</b>18</div>', 1)

# ---------- 7. Flag 1 (Today) ----------
flag1 = ('<h3><span class="pill warn">Today</span> Nine and three-quarter hours &mdash; and one invite '
 'that cannot slip past 9 AM</h3>\n          '
 '<p><b>The Kimberly Ragsdale invite is the clock item</b>: she wants <b>tomorrow 2 PM</b> with Taylor '
 'joining, and she briefs Lauren and Janet this morning &mdash; send it at the top of the <b>9 AM '
 'Honor&rsquo;s-proposal block</b>. In DW 10&ndash;2: <b>consolidate the Stratus duplicate</b> (your '
 'Tue Nov 17 10:40 vs Jr&rsquo;s Wed Nov 18 10:40 &mdash; both partially accepted, both sit inside '
 'build blocks), the <b>three drafts</b> (Tim day twenty-four, Affiliated Tech, GigTel), the '
 '<b>GamifyOS Phase 1 proposal</b>, and <b>check the GamifyOS page + landing actually went live</b>. '
 'Per-location alert routing (RV Country, 11 assistants) is <b>due to production tomorrow</b>. The '
 'evening is spoken for: Friendsgiving 6&ndash;9, dessert in hand.</p>')
i = s.index('<h3><span class="pill warn">Today</span>')
j = s.index('</p>', i) + len('</p>')
s = s[:i] + flag1 + s[j:]

# ---------- 8. Markers ----------
markers = ('<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Wednesday closed '
 '<b>1&ndash;3&ndash;1</b> &mdash; five events, the lightest weekday on the ledger, and <b>the '
 'four-day evening-burst pattern broke</b>: its only failure came at 10:36 PM, outside the 6&ndash;9 '
 'window that had been reliable. Pipeline: <b>Stratus is double-booked</b> &mdash; Tue 17 (yours) and '
 'Wed 18 (Jr&rsquo;s), both partially accepted &mdash; consolidate today; <b>Kimberly Ragsdale</b> '
 'wants tomorrow 2 PM and the invite is unsent; <b>Threshold</b> is warm with Jr checking the NDA; '
 '<b>GigTel</b> still has your draft pending; <b>Nortec</b> is silent via Steve Myhre, third day. '
 '<b>The Tim record is day twenty-four</b> &mdash; the next natural close is Tuesday&rsquo;s Izzy '
 'checkin. New deliverables out of Wednesday: the <b>GamifyOS Phase 1 proposal</b> and the '
 '<b>December 11 Jevity event curriculum for Caroline</b> (Dec 4 is the fallback date). '
 '<b>Per-location alert routing</b> ships to production by Friday.</p>')
i = s.index('The week&rsquo;s markers</h4>')
i = s.index('<p ', i)
j = s.index('</p>', i) + len('</p>')
s = s[:i] + markers + s[j:]

# ---------- 9. Coming up ----------
old_h4 = 'An 8.5-hour pinch today, an 8.75-hour Thursday, then the week breathes'
i = s.index(old_h4)
j = s.index('</p>', i) + len('</p>')
new_coming = ('A 9.75-hour Thursday, then the week opens wide</h4>\n          '
 '<p style="font-size:13px;color:var(--ink-2);margin-top:7px">Today: <b>Honor&rsquo;s proposal 9</b>, '
 'DW 10&ndash;2, <b>Scott Van Camp 2</b>, Tash 4:45, <b>Friendsgiving 6&ndash;9</b>. Friday: <b>Pitch '
 'and Run 8&ndash;9 AM</b>, the <b>Kimberly discovery call wants 2 PM</b> (invite unsent), Review Crew '
 'happy hour 5:30, <b>alert routing due to production</b>. Saturday: <b>Style Bodhi! 10&ndash;1</b>. '
 'Sunday: clear. Monday Nov 16: sync 8, DW Engineering 10&ndash;2 with <b>Call Ken at noon</b> inside '
 'it, TTT 2. Tuesday Nov 17: <b>Izzy checkin 10</b> and <b>the Stratus demo 10:40</b> both inside DW '
 'Client 10&ndash;2 &mdash; if your Tuesday event wins the consolidation, Tuesday is the new pinch. '
 'Wednesday Nov 18: Recover 9, SustAmb 9:30, <b>Jr&rsquo;s demo event 10:40</b>, DW 11&ndash;3, TTT 3. '
 'Carried: <b>the Cathy call</b> (twenty-nine days), <b>the CCI booking</b>, the drip and performance '
 'reports, the ATS five, the Whova trio, the Sahiti intro, the <b>Rev.io sessions ask</b>, and the '
 '<b>invoice &mdash; fourteen days past due unless the ACH cleared it</b>.</p>')
s = s[:i] + new_coming + s[j:]

# ---------- Sanity ----------
assert s.count('__CC_STATE__') == 1 and s.count('__CC_TEMPLATE__') == 1
assert s.count('data-react-task="') == 59
assert s.count('class="bar"') == 7
assert s.count('2026-11-12T06:13:00-06:00') == 2
assert s.count('window open') == 2
assert s.count('Good morning, Bodhi.') == 1
assert s.count('day twenty-three') == 0
assert s.count('0&ndash;3&ndash;1') == 0
assert s.count('Thursday, November 12') == 1
assert s.count('Honor') >= 3
for bad in ['hw7Mh6cK','pY3DM73R','bT5uDhjRSBk3','scottvlmft','ebccf397','5WY67Sa2',
            'PasswordReset','billcenter.net','3,082','Jose Luiz','quoter.com','doxy.me',
            'sfw-mvnn-nfd','cjk-wubx-vna','nyg-hguu-mmh','bxe-xdtp-ohs','uyt-cgnh-gtz',
            'vqd-jqoy-wsp','veu-nahg-ydy','gnj-tvnv-fyt','hag-efnz-nvc','271 125 290 583 760',
            'atscall','2932894139574','2365130726592','latentworks.llc']:
    assert bad not in s, bad

open(p, 'w').write(s)
print('thursday turn ok', len(s))
