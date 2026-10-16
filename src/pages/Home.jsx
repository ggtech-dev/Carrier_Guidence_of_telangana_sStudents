import Banners from '../components/Banners.jsx'
import { Link, useNavigate } from 'react-router-dom'
import { useState } from 'react'
import { useTree, folderUrl, docUrl, ROOT_INFO } from '../data.js'
import { Icon, useTitle, useInstall } from '../components/ui.jsx'
import { useLang } from '../i18n.jsx'
import { useAuth } from '../auth.jsx'

const I = '01_After_10th_Intermediate'
export const POPULAR = [
  [['MBBS – become a doctor', 'MBBS – డాక్టర్ అవ్వడం'], folderUrl(`${I}/BiPC/After_12th_BiPC/01_Doctor_Courses_NEET/01_MBBS_Doctor`)],
  [['B.Tech Computer Science', 'B.Tech కంప్యూటర్ సైన్స్'], folderUrl(`${I}/MPC/After_12th_MPC/01_Engineering_BTech/Engineering_Branches/01_Computer_Science_Engineering_CSE`)],
  [['Gurukul entrance (TGCET) – Class 4', 'గురుకుల ప్రవేశ పరీక్ష (TGCET) – 4వ తరగతి'], '/schools/tgcet'],
  [['Navodaya entrance (JNVST) – Class 5', 'నవోదయ ప్రవేశ పరీక్ష (JNVST) – 5వ తరగతి'], '/schools/jnvst'],
  [['B.Sc Nursing', 'B.Sc నర్సింగ్'], folderUrl(`${I}/BiPC/After_12th_BiPC/02_Nursing/03_BSc_Nursing`)],
  [['CA – Chartered Accountant', 'CA – చార్టర్డ్ అకౌంటెంట్'], folderUrl(`${I}/MEC/After_12th_MEC/01_Professional_CA_CMA_CS_ACCA_Actuary/CA_Chartered_Accountant`)],
  [['Polytechnic diploma', 'పాలిటెక్నిక్ డిప్లొమా'], folderUrl('02_After_10th_Polytechnic_Diploma')],
  [['TGPSC Group II', 'TGPSC గ్రూప్ II'], docUrl('07_After_Degree_Govt_and_Private_Jobs/01_Govt_Jobs_for_Any_Degree/03_TGPSC_Group_II')],
  [['Overseas scholarships up to ₹20 lakh', '₹20 లక్షల వరకు విదేశీ స్కాలర్‌షిప్‌లు'], docUrl('09_Scholarships_and_Student_Support/02_Telangana_Overseas_Scholarships')],
]
const GROUPS = ['MPC', 'BiPC', 'MEC', 'CEC', 'HEC']
const ROOT_TE = {
  '01_After_10th_Intermediate': ['ఇంటర్మీడియట్ (11 & 12)', 'MPC, BiPC, MEC, CEC, HEC – ప్రతి గ్రూప్ తర్వాత అన్ని డిగ్రీలు'],
  '02_After_10th_Polytechnic_Diploma': ['పాలిటెక్నిక్ డిప్లొమా', '10వ తరగతి తర్వాత 3 ఏళ్ల డిప్లొమాలు, ECET ద్వారా B.Tech'],
  '03_After_10th_ITI_Trades': ['ITI ట్రేడ్‌లు', '1–2 ఏళ్ల స్కిల్ కోర్సులు, ఉద్యోగాలు'],
  '04_After_10th_Other_Options': ['10వ తరగతి తర్వాత ఇతర దారులు', 'ఓపెన్ స్కూల్, అప్రెంటిస్‌షిప్, స్కిల్ కోర్సులు'],
  '05_After_10th_Govt_Jobs_Telangana': ['10వ తరగతి తర్వాత ప్రభుత్వ ఉద్యోగాలు', 'GDS, MTS, GD కానిస్టేబుల్, రైల్వే, అగ్నివీర్…'],
  '06_After_Inter_Govt_Jobs': ['ఇంటర్ తర్వాత ప్రభుత్వ ఉద్యోగాలు', 'పోలీస్, SSC CHSL, NDA, అగ్నివీర్…'],
  '07_After_Degree_Govt_and_Private_Jobs': ['డిగ్రీ తర్వాత ఉద్యోగాలు', 'గ్రూప్ I–IV, UPSC, బ్యాంకులు, SSC + ప్రైవేట్ రంగాలు'],
  '08_Work_and_Study_Abroad_Guide': ['విదేశాల్లో ఉద్యోగం & చదువు', 'దేశాల గైడ్‌లు, భాషా పరీక్షలు, సురక్షిత వలస'],
  '09_Scholarships_and_Student_Support': ['స్కాలర్‌షిప్‌లు & సహాయం', 'ePASS, విదేశీ స్కాలర్‌షిప్‌లు, రుణాలు, హెల్ప్‌లైన్లు'],
}
const NEW = [
  ['/schools', 'indigo', ['Class 1–10 entrance exams', '1–10 తరగతుల ప్రవేశ పరీక్షలు'], ['Gurukul (Class 4), Navodaya & Model School (Class 5), Sainik, NMMS – eligibility and dates.', 'గురుకుల (4వ తరగతి), నవోదయ & మోడల్ స్కూల్ (5వ తరగతి), సైనిక్, NMMS – అర్హత, తేదీలు.']],
  ['/colleges', 'leaf', ['Schools & colleges by district', 'జిల్లా వారీగా పాఠశాలలు & కాలేజీలు'], ['Navodaya, Gurukul, junior, engineering, medical, nursing, agriculture, polytechnic.', 'నవోదయ, గురుకుల, జూనియర్, ఇంజనీరింగ్, మెడికల్, నర్సింగ్, వ్యవసాయ, పాలిటెక్నిక్.']],
  ['/software', 'sky', ['Software courses with roadmaps', 'రోడ్‌మ్యాప్‌తో సాఫ్ట్‌వేర్ కోర్సులు'], ['Java, Python, data, DevOps, testing – months, approximate fee and jobs.', 'జావా, పైథాన్, డేటా, డెవ్‌ఆప్స్, టెస్టింగ్ – నెలలు, సుమారు ఫీజు, ఉద్యోగాలు.']],
  ['/creative', 'pink', ['Creative careers after 10th', '10వ తరగతి తర్వాత క్రియేటివ్ కెరీర్లు'], ['Video editing, photography, animation, modelling – with scam warnings.', 'వీడియో ఎడిటింగ్, ఫోటోగ్రఫీ, యానిమేషన్, మోడలింగ్ – మోసాల హెచ్చరికలతో.']],
  ['/guidance', 'indigo', ['Book personal counselling', 'వ్యక్తిగత కౌన్సెలింగ్ బుక్ చేయండి'], ['See where you fit best and request a session by email or WhatsApp.', 'మీకు ఏది సరిపోతుందో చూసి, ఈమెయిల్ / వాట్సాప్ ద్వారా సెషన్ కోరండి.']],
]

export default function Home() {
  const { t, lang } = useLang()
  const x = lang === 'te' ? 1 : 0
  useTitle('')
  const { data: tree } = useTree()
  const auth = useAuth()
  const nav = useNavigate()
  const [q, setQ] = useState('')
  const inst = useInstall()
  const nCourses = tree ? Object.values(tree.folders).filter((f) => f.abroad).length : null
  const hello = auth?.session && !auth.session.guest ? (x ? `నమస్తే, ${auth.session.name}` : `Hello, ${auth.session.name}`) : null

  return (
    <div className="page">
      <Banners />
      <section className="hero">
        {hello && <p className="hello">{hello}</p>}
        <h1>{t('heroTitle')}</h1>
        <p className="lead">{t('heroLead')}</p>
        <form className="searchbox" role="search" onSubmit={(e) => { e.preventDefault(); nav(`/search?q=${encodeURIComponent(q)}`) }}>
          {Icon.search}
          <input value={q} onChange={(e) => setQ(e.target.value)} placeholder={t('searchPh')} aria-label={t('search')} />
          <button className="btn" type="submit">{t('search')}</button>
        </form>
        {tree && <p className="statsrow"><span><b>8</b> {x ? 'పాఠశాల ప్రవేశ పరీక్షలు' : 'school entrance exams'}</span><span><b>247</b> {x ? 'పాఠశాలలు & కాలేజీలు' : 'schools & colleges listed'}</span><span><b>{nCourses}</b> {x ? 'కోర్సులకు విదేశీ ఉద్యోగాలు' : 'courses with abroad jobs'}</span><span><b>{x ? 'ఆఫ్‌లైన్' : 'Works offline'}</b></span></p>}
      </section>

      <section className="mapline" aria-labelledby="journey-h">
        <h2 id="journey-h">{t('journey')}</h2>
        <div className="journey">
          <div className="stop big">
            <h3>{t('stopSchool')}</h3>
            <div className="branches">
              <Link className="chip" to="/schools/tgcet">{x ? 'గురుకుల – 4వ తరగతి' : 'Gurukul – Class 4'}</Link>
              <Link className="chip" to="/schools/jnvst">{x ? 'నవోదయ – 5వ తరగతి' : 'Navodaya – Class 5'}</Link>
              <Link className="chip" to="/schools/model">{x ? 'మోడల్ స్కూల్' : 'Model School'}</Link>
              <Link className="chip" to="/schools/sainik">{x ? 'సైనిక్ స్కూల్' : 'Sainik School'}</Link>
              <Link className="chip" to="/schools/nmms">NMMS</Link>
            </div>
          </div>
          <div className="stop">
            <h3>{t('stop10')}</h3>
            <div className="branches">
              <Link className="chip" to={folderUrl(I)}>{x ? 'ఇంటర్మీడియట్' : 'Intermediate'}</Link>
              <Link className="chip" to={folderUrl('02_After_10th_Polytechnic_Diploma')}>{x ? 'పాలిటెక్నిక్' : 'Polytechnic'}</Link>
              <Link className="chip" to={folderUrl('03_After_10th_ITI_Trades')}>ITI</Link>
              <Link className="chip" to="/creative">{x ? 'క్రియేటివ్ కోర్సులు' : 'Creative courses'}</Link>
              <Link className="chip" to={folderUrl('05_After_10th_Govt_Jobs_Telangana')}>{x ? 'ఇప్పుడే ప్రభుత్వ ఉద్యోగాలు' : 'Govt jobs now'}</Link>
            </div>
          </div>
          <div className="stop">
            <h3>{t('stopInter')}</h3>
            <div className="branches">
              {GROUPS.map((g) => <Link key={g} className="chip" to={folderUrl(`${I}/${g}/After_12th_${g}`)}>{g}</Link>)}
              <Link className="chip" to={folderUrl(`${I}/Vocational_Intermediate`)}>{x ? 'వొకేషనల్' : 'Vocational'}</Link>
            </div>
          </div>
          <div className="stop">
            <h3>{t('stopDegree')}</h3>
            <div className="branches">
              <Link className="chip" to={folderUrl(`${I}/MPC/After_12th_MPC/01_Engineering_BTech`)}>{x ? 'ఇంజనీరింగ్' : 'Engineering'}</Link>
              <Link className="chip" to={folderUrl(`${I}/BiPC/After_12th_BiPC/01_Doctor_Courses_NEET`)}>{x ? 'డాక్టర్ కోర్సులు' : 'Doctor courses'}</Link>
              <Link className="chip" to="/colleges?tab=engineering">{x ? 'కాలేజీలు' : 'Colleges'}</Link>
              <Link className="chip" to="/software">{x ? 'సాఫ్ట్‌వేర్ కోర్సులు' : 'Software courses'}</Link>
            </div>
          </div>
          <div className="stop">
            <h3>{t('stopJob')}</h3>
            <div className="branches">
              <Link className="chip" to={folderUrl('07_After_Degree_Govt_and_Private_Jobs')}>{x ? 'ప్రభుత్వ & ప్రైవేట్ ఉద్యోగాలు' : 'Govt & private jobs'}</Link>
              <Link className="chip" to="/countries">{t('abroad')}</Link>
              <Link className="chip" to={folderUrl('09_Scholarships_and_Student_Support')}>{x ? 'స్కాలర్‌షిప్‌లు' : 'Scholarships'}</Link>
            </div>
          </div>
        </div>
      </section>

      <h2 className="section-title">{t('newFeatures')}</h2>
      <div className="grid2">
        {NEW.map(([to, tone, title, sub]) => <Link key={to} className={'tile ' + tone} to={to}><span className="t">{title[x]}</span><span className="s">{sub[x]}</span></Link>)}
      </div>

      <h2 className="section-title">{t('notSure')}</h2>
      <div className="grid2">
        <Link className="tile indigo" to="/path"><span className="t">{t('findPath')}</span><span className="s">{t('findPathSub')}</span></Link>
        <Link className="tile pink" to="/quiz"><span className="t">{t('quizTitle')}</span><span className="s">{t('quizSub')}</span></Link>
      </div>

      <h2 className="section-title">{t('popular')}</h2>
      <ul className="list">
        {POPULAR.map(([title, url]) => <li key={url}><Link to={url}><span className="mark" /><span className="t">{title[x]}</span><span className="go">{Icon.chev}</span></Link></li>)}
      </ul>

      <h2 className="section-title">{t('everything')}</h2>
      <div className="grid2">
        {Object.entries(ROOT_INFO).map(([id, r]) => (
          <Link key={id} className={'tile ' + r.tone} to={folderUrl(id)}><span className="t">{x ? ROOT_TE[id][0] : r.name}</span><span className="s">{x ? ROOT_TE[id][1] : r.hint}</span></Link>
        ))}
      </div>

      {!inst.standalone && (
        <div className="install">
          <p>{t('keepPhone')}</p>
          {inst.canPrompt ? <button className="btn yellow" onClick={inst.prompt}>{t('installApp')}</button> : <Link className="btn yellow" to="/install">{t('howInstall')}</Link>}
        </div>
      )}
      <p className="footer-note">{t('footerNote')}</p>
    </div>
  )
}
