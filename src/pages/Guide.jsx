import { Link } from 'react-router-dom'
import { useEffect, useState } from 'react'
import { useLang } from '../i18n.jsx'
import { useTree, folderUrl, docUrl, ROOT_INFO } from '../data.js'
import { Icon, Loading, Problem, useTitle } from '../components/ui.jsx'

const I = '01_After_10th_Intermediate'
const STARTS = [
  { key: '10th', label: 'I passed 10th class', te: 'నేను 10వ తరగతి పాస్ అయ్యాను', options: [I, '02_After_10th_Polytechnic_Diploma', '03_After_10th_ITI_Trades', '04_After_10th_Other_Options', '05_After_10th_Govt_Jobs_Telangana'] },
  { key: 'inter', label: 'I am in / finished Intermediate', te: 'నేను ఇంటర్ చదువుతున్నాను / పూర్తి చేశాను', options: ['MPC', 'BiPC', 'MEC', 'CEC', 'HEC', 'Vocational_Intermediate'].map((g) => g === 'Vocational_Intermediate' ? `${I}/${g}/After_Vocational_Inter` : `${I}/${g}/After_12th_${g}`).concat('06_After_Inter_Govt_Jobs') },
  { key: 'degree', label: 'I am doing / finished a degree', te: 'నేను డిగ్రీ చదువుతున్నాను / పూర్తి చేశాను', options: ['07_After_Degree_Govt_and_Private_Jobs', '08_Work_and_Study_Abroad_Guide', '09_Scholarships_and_Student_Support'] },
  { key: 'diploma', label: 'I finished Polytechnic or ITI', te: 'నేను పాలిటెక్నిక్ లేదా ITI పూర్తి చేశాను', options: ['02_After_10th_Polytechnic_Diploma/After_Diploma', '03_After_10th_ITI_Trades', '08_Work_and_Study_Abroad_Guide'] },
]

function label(tree, id) {
  if (ROOT_INFO[id]) return ROOT_INFO[id].name
  const f = tree.folders[id]
  if (!f) return id
  if (/^After_12th_|^After_Vocational/.test(id.split('/').pop())) return `After Inter ${tree.folders[f.parent].name}`
  return f.name
}

export function PathFinder() {
  const { lang } = useLang()
  const te = lang === 'te'
  useTitle('Find my path')
  const { data: tree, error } = useTree()
  const [start, setStart] = useState(null)
  const [stack, setStack] = useState([])
  if (error) return <Problem error={error} />
  if (!tree) return <Loading />

  const cur = stack[stack.length - 1]
  const curF = cur ? tree.folders[cur] : null
  const choices = !start ? null : !cur ? start.options : curF.folders
  const reset = () => { setStart(null); setStack([]) }

  return (
    <div className="page">
      <div className="pagehead"><h1>{te ? 'నా దారి కనుగొనండి' : 'Find my path'}</h1><p>{te ? 'ఒక్కో దశకు సమాధానం ఇవ్వండి. మీరు ఎంచుకున్న కొద్దీ మీ దారి పెరుగుతుంది – ఎప్పుడైనా వివరాలు తెరవండి.' : 'Answer one step at a time. Your route grows as you choose – open the details whenever you like.'}</p></div>

      <div className="journey" style={{ marginTop: 6 }}>
        <div className="stop big"><h3>{start ? (te ? start.te : start.label) : (te ? 'మీరు ఇప్పుడు ఎక్కడ ఉన్నారు?' : 'Where are you now?')}</h3></div>
        {stack.map((id, i) => (
          <div className="stop" key={id}>
            <h3><button className="chip" onClick={() => setStack(stack.slice(0, i + 1))}>{label(tree, id)}</button></h3>
          </div>
        ))}
      </div>

      {!start && (
        <div className="choices">
          {STARTS.map((s) => <button key={s.key} className="choice" onClick={() => setStart(s)}>{te ? s.te : s.label}</button>)}
          <Link className="choice" to="/schools" style={{ textDecoration: 'none', color: 'inherit' }}>{te ? 'నేను 1–10 తరగతుల్లో ఉన్నాను (గురుకుల, నవోదయ పరీక్షలు)' : 'I am in Class 1–10 (Gurukul, Navodaya exams)'}</Link>
          <Link className="choice" to="/quiz" style={{ textDecoration: 'none', color: 'inherit' }}>{te ? '10వ తరగతి తర్వాత ఏ గ్రూప్ తీసుకోవాలో తెలియదు – సహాయం చేయండి' : "I don't know which group to take after 10th – help me choose"}</Link>
        </div>
      )}

      {start && choices && choices.length > 0 && (
        <>
          <h2 className="section-title" style={{ marginTop: 12 }}>{cur ? (te ? 'తర్వాత ఎంచుకోండి' : 'Next, choose') : (te ? 'మీరు చూడాలనుకున్నది ఎంచుకోండి' : 'Choose what you want to explore')}</h2>
          <div className="choices">
            {choices.filter((id) => tree.folders[id]).map((id) => {
              const f = tree.folders[id]
              return <button key={id} className="choice" onClick={() => setStack([...stack, id])}><b>{label(tree, id)}</b>{f.abroad ? <span className="muted"> – includes jobs abroad</span> : ''}{f.folders.length ? <span className="muted"> – {f.folders.length} {f.folders.length === 1 ? 'option' : 'options'}</span> : ''}</button>
            })}
          </div>
        </>
      )}

      {curF && (
        <div className="panel" style={{ marginTop: 14 }}>
          <h3 style={{ marginBottom: 6 }}>{label(tree, cur)}</h3>
          <p className="muted" style={{ margin: '0 0 12px' }}>{curF.folders.length ? 'You can keep choosing above, or open this stage now.' : 'This is a course or job page – open it for full details.'}</p>
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: 10 }}>
            <Link className="btn" to={folderUrl(cur)}>{te ? 'వివరాలు తెరవండి' : 'Open details'}</Link>
            {curF.abroad && <Link className="btn alt" to={folderUrl(cur) + '?tab=abroad'}>Jobs abroad</Link>}
            {curF.docs.length > 1 && curF.docs.slice(0, 2).map((d) => <Link key={d.id} className="btn alt" to={docUrl(d.id)}>{d.file}</Link>)}
          </div>
        </div>
      )}
      {start && <p style={{ marginTop: 18 }}><button className="btn alt" onClick={() => (stack.length ? setStack(stack.slice(0, -1)) : reset())}>{te ? 'ఒక అడుగు వెనక్కి' : 'Go back one step'}</button> <button className="btn alt" onClick={reset}>{te ? 'మళ్లీ మొదలుపెట్టండి' : 'Start again'}</button></p>}
    </div>
  )
}

// ---------------- Stream quiz (English + Telugu) ----------------
const CATS = {
  eng: { name: ['MPC – Engineering, technology & science', 'MPC – ఇంజనీరింగ్, టెక్నాలజీ & సైన్స్'], url: folderUrl(`${I}/MPC/After_12th_MPC`), about: ['Maths-based: B.Tech, B.Sc, B.Arch, pilot, defence and IT careers.', 'గణితం ఆధారంగా: B.Tech, B.Sc, B.Arch, పైలట్, డిఫెన్స్, IT కెరీర్లు.'] },
  med: { name: ['BiPC – Medicine, nursing & health', 'BiPC – మెడిసిన్, నర్సింగ్ & ఆరోగ్యం'], url: folderUrl(`${I}/BiPC/After_12th_BiPC`), about: ['Doctor, dentist, nursing, pharmacy, allied health, agriculture and veterinary careers.', 'డాక్టర్, డెంటిస్ట్, నర్సింగ్, ఫార్మసీ, అలైడ్ హెల్త్, వ్యవసాయ, పశువైద్య కెరీర్లు.'] },
  com: { name: ['MEC / CEC – Commerce, accounts & business', 'MEC / CEC – కామర్స్, అకౌంట్స్ & బిజినెస్'], url: folderUrl(`${I}/MEC/After_12th_MEC`), about: ['CA, CMA, CS, B.Com, BBA, banking and finance careers.', 'CA, CMA, CS, B.Com, BBA, బ్యాంకింగ్, ఫైనాన్స్ కెరీర్లు.'] },
  arts: { name: ['HEC – Civil services, law, teaching & media', 'HEC – సివిల్ సర్వీసెస్, లా, టీచింగ్ & మీడియా'], url: folderUrl(`${I}/HEC/After_12th_HEC`), about: ['IAS/Group I, law, teaching, journalism, social work and arts.', 'IAS/గ్రూప్ I, లా, టీచింగ్, జర్నలిజం, సోషల్ వర్క్, ఆర్ట్స్.'] },
  skill: { name: ['Polytechnic or ITI – Skills and early jobs', 'పాలిటెక్నిక్ లేదా ITI – స్కిల్స్, త్వరగా ఉద్యోగం'], url: folderUrl('02_After_10th_Polytechnic_Diploma'), about: ['Earn sooner with hands-on technical skills; you can still reach B.Tech later through ECET.', 'చేతి నైపుణ్యాలతో త్వరగా సంపాదించండి; తర్వాత ECET ద్వారా B.Tech కూడా చేయవచ్చు.'] },
}
const Q = [
  [['Which subject do you enjoy most?', 'మీకు ఏ సబ్జెక్ట్ అంటే ఎక్కువ ఇష్టం?'], [[['Maths or Physics', 'గణితం లేదా ఫిజిక్స్'], { eng: 2 }], [['Biology', 'జీవశాస్త్రం'], { med: 2 }], [['Accounts, economics or business', 'అకౌంట్స్, ఎకనామిక్స్ లేదా బిజినెస్'], { com: 2 }], [['History, civics or languages', 'చరిత్ర, పౌరశాస్త్రం లేదా భాషలు'], { arts: 2 }], [['Making or repairing things', 'వస్తువులు తయారు చేయడం / రిపేర్ చేయడం'], { skill: 2 }]]],
  [['What do you like doing in free time?', 'ఖాళీ సమయంలో ఏమి చేయడం ఇష్టం?'], [[['Using computers, apps or gadgets', 'కంప్యూటర్లు, యాప్స్, గ్యాడ్జెట్లు వాడటం'], { eng: 2 }], [['Helping people, animals or plants', 'మనుషులు, జంతువులు, మొక్కలకు సహాయం చేయడం'], { med: 2 }], [['Planning money, buying and selling', 'డబ్బు ప్లాన్ చేయడం, కొనడం–అమ్మడం'], { com: 2 }], [['Reading, debating or writing', 'చదవడం, వాదించడం, రాయడం'], { arts: 2 }], [['Fixing bikes, wiring or tools', 'బైక్‌లు, వైరింగ్, పనిముట్లతో పని'], { skill: 2 }]]],
  [['How are your Maths marks?', 'మీ గణితం మార్కులు ఎలా ఉంటాయి?'], [[['Very good', 'చాలా బాగుంటాయి'], { eng: 2, com: 1 }], [['Average', 'సగటు'], { com: 1, arts: 1, med: 1 }], [['Maths is hard for me', 'గణితం నాకు కష్టం'], { arts: 1, med: 1, skill: 1 }]]],
  [['How soon do you want to start earning?', 'ఎంత త్వరగా సంపాదించడం మొదలుపెట్టాలనుకుంటున్నారు?'], [[['Within 2–3 years', '2–3 సంవత్సరాల్లో'], { skill: 3 }], [['In 4–5 years is fine', '4–5 సంవత్సరాలైనా పర్వాలేదు'], { eng: 1, com: 1, arts: 1 }], [['I can study 6+ years for a big goal', 'పెద్ద లక్ష్యం కోసం 6+ సంవత్సరాలు చదవగలను'], { med: 2, eng: 1 }]]],
  [['Where would you like to work?', 'ఎక్కడ పని చేయాలనుకుంటున్నారు?'], [[['Hospital or lab', 'ఆసుపత్రి లేదా ల్యాబ్'], { med: 2 }], [['Office with computers', 'కంప్యూటర్లతో ఆఫీస్'], { eng: 1, com: 1 }], [['Site, factory or outdoors', 'సైట్, ఫ్యాక్టరీ లేదా బయట'], { skill: 1, eng: 1 }], [['Govt office, court or classroom', 'ప్రభుత్వ ఆఫీస్, కోర్టు లేదా తరగతి గది'], { arts: 2 }], [['My own business', 'సొంత వ్యాపారం'], { com: 2 }]]],
  [['What is your biggest strength?', 'మీ అతిపెద్ద బలం ఏమిటి?'], [[['Solving problems', 'సమస్యలు పరిష్కరించడం'], { eng: 2 }], [['Patience and caring', 'ఓర్పు, సేవా గుణం'], { med: 2 }], [['Numbers and planning', 'లెక్కలు, ప్లానింగ్'], { com: 2 }], [['Speaking and writing', 'మాట్లాడటం, రాయడం'], { arts: 2 }], [['Working with my hands', 'చేతులతో పని చేయడం'], { skill: 2 }]]],
  [['Which job title excites you most?', 'ఏ ఉద్యోగం మీకు ఎక్కువ ఉత్సాహం ఇస్తుంది?'], [[['Engineer or software developer', 'ఇంజనీర్ లేదా సాఫ్ట్‌వేర్ డెవలపర్'], { eng: 2 }], [['Doctor, nurse or pharmacist', 'డాక్టర్, నర్స్ లేదా ఫార్మసిస్ట్'], { med: 2 }], [['CA, banker or manager', 'CA, బ్యాంకర్ లేదా మేనేజర్'], { com: 2 }], [['IAS officer, lawyer, teacher or journalist', 'IAS అధికారి, లాయర్, టీచర్ లేదా జర్నలిస్ట్'], { arts: 2 }], [['Electrician, technician or mechanic', 'ఎలక్ట్రీషియన్, టెక్నీషియన్ లేదా మెకానిక్'], { skill: 2 }]]],
  [['How much can your family spend on studies?', 'చదువుపై మీ కుటుంబం ఎంత ఖర్చు చేయగలదు?'], [[['Very little – I need free or low-cost options', 'చాలా తక్కువ – ఉచిత / తక్కువ ఖర్చు ఎంపికలు కావాలి'], { skill: 2, arts: 1 }], [['Some support for a normal degree', 'సాధారణ డిగ్రీకి కొంత సపోర్ట్'], { com: 1, arts: 1, eng: 1 }], [['They can support a long or costly course', 'ఎక్కువ కాలం / ఎక్కువ ఖర్చు కోర్సుకు సపోర్ట్ చేయగలరు'], { med: 1, eng: 1 }]]],
  [['Are you comfortable with blood, injections or hospitals?', 'రక్తం, ఇంజెక్షన్లు, ఆసుపత్రులతో మీకు ఇబ్బంది లేదా?'], [[['Yes, no problem', 'అవును, ఏ ఇబ్బంది లేదు'], { med: 2 }], [['Not really', 'అంతగా కాదు'], { eng: 1, com: 1, arts: 1, skill: 1 }]]],
  [['Do you want to prepare for govt exams like Group I/II or police?', 'గ్రూప్ I/II, పోలీస్ వంటి ప్రభుత్వ పరీక్షలకు సిద్ధం కావాలనుకుంటున్నారా?'], [[['Yes, that is my dream', 'అవును, అదే నా కల'], { arts: 2 }], [['Maybe later', 'తర్వాత చూద్దాం'], { com: 1, eng: 1 }], [['I prefer private job or business', 'ప్రైవేట్ ఉద్యోగం లేదా వ్యాపారమే ఇష్టం'], { com: 1, eng: 1 }]]],
]

export function Quiz() {
  const { lang, t } = useLang()
  const x = lang === 'te' ? 1 : 0
  useTitle(t('quiz'))
  const [ans, setAns] = useState([])
  const i = ans.length
  const done = i === Q.length
  const score = { eng: 0, med: 0, com: 0, arts: 0, skill: 0 }
  ans.forEach((a, qi) => Object.entries(Q[qi][1][a][1]).forEach(([k, v]) => { score[k] += v }))
  const max = Math.max(1, ...Object.values(score))
  const ranked = Object.entries(score).sort((a, b) => b[1] - a[1])
  useEffect(() => { if (done) { try { localStorage.setItem('cot-quiz', JSON.stringify(ranked.map(([k]) => k))) } catch { /* ignore */ } } }, [done])

  return (
    <div className="page">
      <div className="pagehead"><h1>{t('quizTitle')}</h1><p>{x ? 'పది చిన్న ప్రశ్నలు. తప్పు సమాధానాలు ఉండవు – మీకు నిజమైనది ఎంచుకోండి.' : 'Ten quick questions. There are no wrong answers – choose what is true for you.'}</p></div>
      {!done ? (
        <>
          <div className="progress" aria-label={`Question ${i + 1} of ${Q.length}`}><i style={{ width: `${(i / Q.length) * 100}%` }} /></div>
          <p className="muted">{x ? `ప్రశ్న ${i + 1} / ${Q.length}` : `Question ${i + 1} of ${Q.length}`}</p>
          <h2>{Q[i][0][x]}</h2>
          <div className="choices">{Q[i][1].map(([lbl], k) => <button key={lbl[0]} className="choice" onClick={() => setAns([...ans, k])}>{lbl[x]}</button>)}</div>
          {i > 0 && <button className="btn alt" onClick={() => setAns(ans.slice(0, -1))}>{x ? 'ముందు ప్రశ్న' : 'Previous question'}</button>}
        </>
      ) : (
        <>
          <h2 style={{ marginBottom: 12 }}>{x ? 'మీకు బాగా సరిపోయేవి' : 'Your best matches'}</h2>
          {ranked.map(([k, v], n) => (
            <div className="result" key={k} style={n > 1 ? { opacity: .8 } : null}>
              <h3>{CATS[k].name[x]}</h3>
              <div className="bar"><i style={{ width: `${(v / max) * 100}%` }} /></div>
              <p className="muted" style={{ margin: '0 0 8px' }}>{CATS[k].about[x]}</p>
              {n < 2 && <Link className="btn" to={CATS[k].url}>{x ? 'కోర్సులు, ఉద్యోగాలు చూడండి' : 'See courses and jobs'}</Link>}
            </div>
          ))}
          <div className="callout">{x ? 'ఈ క్విజ్ ఒక ప్రారంభం మాత్రమే. నిర్ణయించే ముందు తల్లిదండ్రులు, టీచర్లు, ఆ రంగంలో పనిచేసేవారితో మాట్లాడండి.' : 'This quiz is only a starting point. Talk to your parents, teachers and someone working in the field before deciding.'}</div>
          <p style={{ marginTop: 14 }}><Link className="btn" to="/guidance">{t('guidance')}</Link> <button className="btn alt" onClick={() => setAns([])}>{x ? 'క్విజ్ మళ్లీ రాయండి' : 'Take the quiz again'}</button></p>
        </>
      )}
    </div>
  )
}

export { Icon }
