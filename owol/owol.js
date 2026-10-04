(()=>{
const LS={get(k,d){try{const v=localStorage.getItem('owol:'+k);return v==null?d:JSON.parse(v)}catch(e){return d}},set(k,v){try{localStorage.setItem('owol:'+k,JSON.stringify(v))}catch(e){}}};
// 들어온 길: ?from= 은 세션 동안 기억하고 주소창에서는 지운다(공유될 때 꼬리표가 따라가지 않게)
let from='';try{const u=new URL(location.href);const f=(u.searchParams.get('from')||'').replace(/[^a-z0-9_-]/gi,'').slice(0,20);if(f){sessionStorage.setItem('owol:from',f);u.searchParams.delete('from');history.replaceState(null,'',u.pathname+u.search+u.hash)}from=sessionStorage.getItem('owol:from')||''}catch(e){}
const local=/^(localhost|127\.|0\.0\.0\.0|\[::1\])/.test(location.hostname)||location.protocol==='file:';
const hit=(p)=>{if(local)return;const q='/hit?s=owol&p='+encodeURIComponent(p+(from?'?from='+from:''))+'&r='+encodeURIComponent(document.referrer||'');try{navigator.sendBeacon?navigator.sendBeacon(q):fetch(q,{method:'POST',keepalive:true})}catch(e){}};
const ev=(n)=>hit('/owol/e/'+n);
// N일차는 오늘 날짜로(한국 시간). 정적 페이지라 빌드한 날에 멈추지 않게
try{const dn=Math.floor((Date.now()+324e5-Date.parse('2026-09-08'))/864e5)+1;if(dn>0)document.querySelectorAll('.dayn').forEach(e=>e.textContent=dn)}catch(e){}
hit(location.pathname);
document.addEventListener('click',(e)=>{const t=e.target.closest('[data-ev]');if(t)ev(t.dataset.ev)});
let tt;const toast=(m)=>{let el=document.querySelector('.toast');if(!el){el=document.createElement('div');el.className='toast';el.setAttribute('role','status');document.body.appendChild(el)}el.textContent=m;el.classList.add('on');clearTimeout(tt);tt=setTimeout(()=>el.classList.remove('on'),1600)};
const days=[...document.querySelectorAll('.day')];if(!days.length)return;
// 체크한 날
const fin=LS.get('fin',[]);const paint=()=>{days.forEach(d=>d.classList.toggle('fin',fin.includes(+d.dataset.n)));document.querySelectorAll('.pn').forEach(p=>p.textContent=fin.length)};
const open=(d,on)=>{d.classList.toggle('open',on);d.querySelector('.dh').setAttribute('aria-expanded',on)};
days.forEach(d=>{d.querySelector('.dh').onclick=()=>{const on=!d.classList.contains('open');open(d,on);if(on)ev('open-'+d.dataset.n)};
d.querySelector('.done').onclick=()=>{const n=+d.dataset.n;const i=fin.indexOf(n);if(i<0){fin.push(n);ev('done-'+n);open(d,false);const nx=days.find(x=>!fin.includes(+x.dataset.n));if(nx){open(nx,true);setTimeout(()=>nx.scrollIntoView({behavior:'smooth',block:'start'}),60)}else toast('7일 끝. 이제 한 사람에게 보여 주세요')}else fin.splice(i,1);LS.set('fin',fin);paint()}});
paint();
const target=location.hash.match(/^#day(\d)$/);const first=target?days[+target[1]-1]:days.find(x=>!fin.includes(+x.dataset.n));if(first)open(first,true);
// 확인 칸
const chk=LS.get('chk',{});document.querySelectorAll('[data-chk]').forEach(c=>{c.checked=!!chk[c.dataset.chk];c.onchange=()=>{chk[c.dataset.chk]=c.checked;LS.set('chk',chk)}});
// 세 칸 → 프롬프트
const vals=LS.get('three',{});const fill=()=>{const three=[vals.who,vals.what,vals.now].map(s=>(s||'').trim()).filter(Boolean);
document.querySelectorAll('[data-fill=three]').forEach(s=>{s.textContent=three.length?three.join(' / '):'위에서 채운 세 칸';s.classList.toggle('empty',!three.length)});
document.querySelectorAll('[data-fill=what]').forEach(s=>{const w=(vals.what||'').trim();s.textContent=w||'무엇';s.classList.toggle('empty',!w)})};
document.querySelectorAll('[data-in]').forEach(i=>{i.value=vals[i.dataset.in]||'';i.oninput=()=>{vals[i.dataset.in]=i.value;LS.set('three',vals);fill()};i.onchange=()=>{if(i.value.trim())ev('three-'+i.dataset.in)}});fill();
// 눌러서 고르는 칸
const picks=LS.get('picks',{});const pp=()=>{document.querySelectorAll('.pick').forEach(s=>{const o=JSON.parse(s.dataset.opts);s.textContent=o[(picks[s.dataset.key]||0)%o.length]});const w=(picks['웹|앱']||0)%2;document.querySelectorAll('[data-seg]').forEach(b=>b.classList.toggle('on',+b.dataset.seg===w))};
document.querySelectorAll('.pick').forEach(s=>s.onclick=()=>{picks[s.dataset.key]=(picks[s.dataset.key]||0)+1;LS.set('picks',picks);pp()});
document.querySelectorAll('[data-seg]').forEach(b=>b.onclick=()=>{picks['웹|앱']=+b.dataset.seg;LS.set('picks',picks);pp();ev('fork-'+(b.dataset.seg==='0'?'web':'app'))});pp();
// 복사
const copy=async(t)=>{try{await navigator.clipboard.writeText(t);return true}catch(e){const a=document.createElement('textarea');a.value=t;a.setAttribute('readonly','');a.style.position='fixed';a.style.opacity='0';document.body.appendChild(a);a.select();let ok=false;try{ok=document.execCommand('copy')}catch(_){}a.remove();return ok}};
document.querySelectorAll('.cp').forEach(b=>b.addEventListener('click',async()=>{const ok=await copy(b.closest('.pr').querySelector('pre').innerText);b.textContent=ok?'복사했어요':'길게 눌러 복사';b.classList.toggle('ok',ok);setTimeout(()=>{b.textContent='복사';b.classList.remove('ok')},1600)}));
})();