const fs = require('fs');
const frag = fs.readFileSync('command-center.html', 'utf8');

// exactly what the page's script does
function j(v){return JSON.stringify(v).replace(/</g,'\\u003c').replace(/>/g,'\\u003e')
  .replace(/\u2028/g,'\\u2028').replace(/\u2029/g,'\\u2029');}
const tState = "__CC"+"_STATE__", tTemplate = "__CC"+"_TEMPLATE__";

const m = frag.match(/^  var PAGE_TEMPLATE = (".*");$/m);
if(!m) { console.error('FAIL: could not read PAGE_TEMPLATE'); process.exit(1); }
const PAGE_TEMPLATE = JSON.parse(m[1]);

function publish(state){
  return PAGE_TEMPLATE.replace(tState, ()=>j(state)).replace(tTemplate, ()=>j(PAGE_TEMPLATE));
}

let fail = 0;
const ok = (c,msg) => { console.log((c?'  ok  ':'  FAIL')+'  '+msg); if(!c) fail++; };

// 1. the embedded template is a complete document
ok(PAGE_TEMPLATE.startsWith('<!doctype html>'), 'embedded template is a full document');
ok(PAGE_TEMPLATE.includes('</html>'), 'embedded template closes </html>');

// 2. a save produces a valid full document
const s1 = {v:1,updated:'2026-08-21T22:00:00.000Z',
  proposals:{p1:'rejected',p4:'deferred'}, tasks:{'hr-nda':'done','iz-oracle':'waiting'},
  notes:{checkinChoice:'no-time', week:'Friday is always long </script> & that is fine'}};
const out1 = publish(s1);
ok(out1.startsWith('<!doctype html>'), 'saved page starts with doctype');
// The placeholders MUST still exist inside the embedded template string —
// that is what lets the next save work. What must not remain is an unfilled
// slot in the live markup, so check everything except that one line.
const liveMarkup = out1.replace(/^  var PAGE_TEMPLATE = ".*";$/m, '');
ok(!liveMarkup.includes(tState) && !liveMarkup.includes(tTemplate),
   'no unfilled placeholder in the live markup');
ok(out1.includes(tState) && out1.includes(tTemplate),
   'placeholders preserved inside the embedded template (next save works)');

// 3. the state island round-trips, including hostile text
const island = out1.match(/<script id="cc-state" type="application\/json">(.*?)<\/script>/s);
ok(!!island, 'state island present');
const parsed = JSON.parse(island[1].replace(/\\u003c/g,'<').replace(/\\u003e/g,'>'));
ok(JSON.stringify(parsed)===JSON.stringify(s1), 'state survives a save byte-for-byte');
ok(parsed.notes.week.includes('</script>'), 'a </script> typed in a note does not break out');

// 4. size stability — the killer bug would be the template nesting itself
const out2 = publish({...s1, updated:'2026-08-21T23:00:00.000Z'});
ok(Math.abs(out1.length-out2.length) < 50, `size stable across saves (${out1.length} vs ${out2.length})`);

// 5. the saved page can itself save again, identically
const m2 = out1.match(/^  var PAGE_TEMPLATE = (".*");$/m);
ok(!!m2, 'saved page still carries its template');
ok(JSON.parse(m2[1])===PAGE_TEMPLATE, 'template is identical after a save (no drift)');

console.log(fail? `\n${fail} CHECK(S) FAILED` : '\nall round-trip checks passed');
process.exit(fail?1:0);
