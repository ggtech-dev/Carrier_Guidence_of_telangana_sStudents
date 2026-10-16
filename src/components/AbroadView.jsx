import { useState } from 'react'
import { Link } from 'react-router-dom'
import { Icon, SalaryNote } from './ui.jsx'

const SECTOR = { health: ['health', 'Healthcare jobs & licensing'], edu: ['edu', 'Teaching jobs'], eng: ['eng', 'Engineering registration'] }

export function CountryApps({ c, sector }) {
  const sec = SECTOR[sector]
  return (
    <>
      <h4>Job apps & websites</h4>
      <ul>{c.general.map((x) => <li key={x}>{x}</li>)}</ul>
      {sec && c[sec[0]] && <><h4>{sec[1]}</h4><ul>{c[sec[0]].map((x) => <li key={x}>{x}</li>)}</ul></>}
      <h4>Work visa</h4>
      <ul>{c.visa.map((x) => <li key={x}>{x}</li>)}</ul>
      <h4>Language & permanent stay</h4>
      <p style={{ margin: 0 }}>{c.lang}. {c.pr}</p>
      <h4>Official portal & Indian embassy</h4>
      <p style={{ margin: 0 }}>{c.official}</p><p style={{ margin: 0 }}>Indian embassy: {c.embassy}</p>
      <h4>Watch out</h4>
      <p style={{ margin: 0 }}>{c.note}</p>
    </>
  )
}

export default function AbroadView({ abroad, profileKey, course }) {
  const p = abroad.profiles[profileKey]
  const [open, setOpen] = useState(0)
  if (!p) return null
  return (
    <div className="doc">
      <p className="muted">Jobs abroad for <b>{course}</b> – profession group: {p.name}. {abroad.orderHelp}</p>
      <section>
        <h2>Top 10 countries</h2>
        <p className="muted" style={{ fontSize: '.92rem' }}>Tap a country to see job apps, visa, language and embassy.</p>
        <ol className="rank">
          {p.rows.map(([code, why, lic, sal], i) => {
            const c = abroad.countries[code]
            const isOpen = open === i
            return (
              <li key={code}>
                <button onClick={() => setOpen(isOpen ? -1 : i)} aria-expanded={isOpen}>
                  <span className="n">{i + 1}</span>
                  <span><span className="c">{c.name}</span><span className="w">{why}</span><span className="w"><b>Licence / exam:</b> {lic}</span></span>
                  <span className="sal">{sal}</span>
                </button>
                {isOpen && <div className="more"><CountryApps c={c} sector={p.sector} /><p style={{ marginTop: 10 }}><Link to={`/countries/${code}`}>Full country guide</Link></p></div>}
              </li>
            )
          })}
        </ol>
        <SalaryNote />
      </section>
      {p.portals.length > 0 && <section><h2>Apps useful in every country</h2><ul>{p.portals.map((x) => <li key={x}>{x}</li>)}</ul></section>}
      <section><h2>Exams & certificates you will need</h2><ul>{p.exams.map((x) => <li key={x}>{x}</li>)}</ul></section>
      <section><h2>Step-by-step plan</h2><ol style={{ paddingLeft: '1.3em' }}>{p.steps.map((x) => <li key={x}>{x}</li>)}</ol></section>
      {p.tips.length > 0 && <section><h2>Important notes</h2><ul>{p.tips.map((x) => <li key={x}>{x}</li>)}</ul></section>}
      <section>
        <h2>Stay safe</h2>
        <div className="callout"><ul style={{ margin: 0 }}>{abroad.safety.map((x) => <li key={x}>{x}</li>)}</ul></div>
      </section>
      <section>
        <h2>Before you go</h2>
        <ul>
          <li>Documents: passport, certificates + marks memos, attestation/apostille, experience letters, police clearance, language test score.</li>
          <li>Credential checks: DataFlow (Gulf health), WES/ICAS (Canada), WES/ECE (USA), UK ENIC, anabin/ZAB (Germany).</li>
          <li>Salaries are approximate only (Oct 2026) – actual pay may be lower or higher. Gulf salaries are usually tax-free with housing; Western salaries are before tax.</li>
        </ul>
        <ul><li><Link to="/f/08_Work_and_Study_Abroad_Guide">Open the full Work & study abroad guide</Link></li><li><Link to="/f/09_Scholarships_and_Student_Support">Scholarships for study abroad</Link></li></ul>
      </section>
    </div>
  )
}

export { Icon }
