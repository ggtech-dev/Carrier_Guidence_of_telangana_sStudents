import { Link, useParams, useSearchParams } from 'react-router-dom'
import { useEffect, useMemo, useState } from 'react'
import { useTree, useAbroad, loadDoc, folderUrl, docUrl, ROOT_INFO } from '../data.js'
import { useLang } from '../i18n.jsx'
import { Icon, RouteLine, DocBody, SaveButton, Loading, Problem, useTitle } from '../components/ui.jsx'
import AbroadView from '../components/AbroadView.jsx'

function markTone(id) {
  if (/Govt|Jobs/.test(id)) return 'leaf'
  if (/Abroad/.test(id)) return 'sky'
  if (/Scholar|BiPC|Nursing|Doctor|Health|Pharm|Allied|Paramedical/.test(id)) return 'pink'
  return ''
}

export function Explore() {
  const { lang } = useLang()
  useTitle('Explore')
  const { data: tree, error } = useTree()
  if (error) return <Problem error={error} />
  if (!tree) return <Loading />
  return (
    <div className="page">
      <div className="pagehead"><h1>{lang === 'te' ? 'అన్నీ చూడండి' : 'Explore everything'}</h1><p>{lang === 'te' ? 'ప్రయాణంలో ఏ దశనైనా తెరవండి. ప్రతి కోర్సులో సబ్జెక్టులు, పాస్ మార్కులు, ప్రైవేట్ & ప్రభుత్వ ఉద్యోగాలు, విదేశీ ఉద్యోగాలు ఉంటాయి.' : 'Open any stage of the journey. Each course shows subjects, pass marks, private and govt jobs, and jobs abroad.'}</p></div>
      <div className="grid2" style={{ marginBottom: 18 }}>
        <Link className="tile indigo" to="/schools"><span className="t">{lang === 'te' ? '1–10 తరగతులు' : 'Class 1–10'}</span><span className="s">{lang === 'te' ? 'గురుకుల, నవోదయ, మోడల్, సైనిక్' : 'Gurukul, Navodaya, Model, Sainik'}</span></Link>
        <Link className="tile leaf" to="/colleges"><span className="t">{lang === 'te' ? 'కాలేజీలు' : 'Colleges'}</span><span className="s">{lang === 'te' ? 'జిల్లా వారీ జాబితాలు' : 'District-wise lists'}</span></Link>
      </div>
      <ul className="list">
        {tree.rootDocs.map((d) => <li key={d.id}><Link to={docUrl(d.id)}><span className="mark" /><span><span className="t">{d.title}</span><span className="s">Start here – overview of the whole guide</span></span><span className="go">{Icon.chev}</span></Link></li>)}
        {tree.roots.map((id) => (
          <li key={id}><Link to={folderUrl(id)}><span className={'mark folder ' + (ROOT_INFO[id]?.tone || '')} /><span><span className="t">{ROOT_INFO[id]?.name || tree.folders[id].name}</span><span className="s">{ROOT_INFO[id]?.hint}</span></span><span className="go">{Icon.chev}</span></Link></li>
        ))}
      </ul>
    </div>
  )
}

function useDoc(meta) {
  const [state, set] = useState({ doc: null, error: null })
  useEffect(() => {
    let alive = true
    if (!meta) return
    set({ doc: null, error: null })
    loadDoc(meta).then((doc) => alive && set({ doc, error: null }), (error) => alive && set({ doc: null, error }))
    return () => { alive = false }
  }, [meta?.id])
  return state
}

function countInside(tree, f) {
  let n = f.docs.length
  for (const c of f.folders) n += countInside(tree, tree.folders[c])
  return n
}

export function FolderPage() {
  const { lang } = useLang()
  const id = decodeURIComponent(useParams()['*'] || '')
  const { data: tree, error } = useTree()
  const { data: abroad } = useAbroad()
  const [sp, setSp] = useSearchParams()
  const f = tree?.folders[id]
  const single = f && f.docs.length === 1 ? f.docs[0] : null
  const { doc, error: derr } = useDoc(single)
  const name = f ? (ROOT_INFO[id]?.name || f.name) : ''
  useTitle(name)
  const tab = sp.get('tab') === 'abroad' && f?.abroad ? 'abroad' : 'details'

  if (error) return <Problem error={error} />
  if (!tree) return <Loading />
  if (!f) return <NotFound />

  return (
    <div className="page">
      <RouteLine tree={tree} folderId={id} />
      <div className="headrow">
        <h1>{single && doc ? doc.title : name}</h1>
        <SaveButton item={{ url: folderUrl(id), title: name, kind: 'folder' }} />
      </div>
      {ROOT_INFO[id] && <p className="muted" style={{ marginTop: 8 }}>{ROOT_INFO[id].hint}</p>}

      {f.abroad && (
        <div className="tabs" role="tablist">
          <button role="tab" aria-selected={tab === 'details'} className={tab === 'details' ? 'on' : ''} onClick={() => setSp({})}>{lang === 'te' ? 'కోర్సు వివరాలు' : 'Course details'}</button>
          <button role="tab" aria-selected={tab === 'abroad'} className={tab === 'abroad' ? 'on' : ''} onClick={() => setSp({ tab: 'abroad' })}>{lang === 'te' ? 'విదేశీ ఉద్యోగాలు' : 'Jobs abroad'}</button>
        </div>
      )}

      {tab === 'abroad' ? (abroad ? <AbroadView abroad={abroad} profileKey={f.abroad} course={(single && doc?.title) || name} /> : <Loading />) : (
        <>
          {f.folders.length > 0 && (
            <>
              <h2 className="section-title" style={{ marginTop: 18 }}>{lang === 'te' ? 'ఒక ఎంపిక చేసుకోండి' : 'Choose an option'}</h2>
              <ul className="list">
                {f.folders.map((cid) => {
                  const c = tree.folders[cid]
                  const n = countInside(tree, c)
                  return <li key={cid}><Link to={folderUrl(cid)}><span className={'mark folder ' + markTone(cid)} /><span><span className="t">{c.name}</span><span className="s">{n} {n === 1 ? 'guide' : 'guides'}{c.abroad ? ' + jobs abroad' : ''}</span></span><span className="go">{Icon.chev}</span></Link></li>
                })}
              </ul>
            </>
          )}
          {single ? (
            derr ? <Problem error={derr} /> : doc ? <div style={{ marginTop: 18 }}><p className="muted">{doc.sub}</p><DocBody doc={doc} /></div> : <Loading />
          ) : f.docs.length > 0 && (
            <>
              <h2 className="section-title">{lang === 'te' ? 'ఈ విభాగంలోని గైడ్‌లు' : 'Guides in this section'}</h2>
              <ul className="list">
                {f.docs.map((d) => <li key={d.id}><Link to={docUrl(d.id)}><span className="mark" /><span><span className="t">{d.title}</span><span className="s">{d.sub}</span></span><span className="go">{Icon.chev}</span></Link></li>)}
              </ul>
            </>
          )}
          {f.abroad && <div className="callout" style={{ marginTop: 22 }}>Want to work abroad after this? <button className="chip" style={{ marginLeft: 6 }} onClick={() => { setSp({ tab: 'abroad' }); window.scrollTo(0, 0) }}>See top 10 countries</button></div>}
        </>
      )}
    </div>
  )
}

export function DocPage() {
  const id = decodeURIComponent(useParams()['*'] || '')
  const { data: tree, error } = useTree()
  const meta = useMemo(() => {
    if (!tree) return null
    const folder = id.includes('/') ? id.slice(0, id.lastIndexOf('/')) : ''
    const list = folder ? tree.folders[folder]?.docs : tree.rootDocs
    return list?.find((d) => d.id === id) || null
  }, [tree, id])
  const { doc, error: derr } = useDoc(meta)
  useTitle(doc?.title)
  if (error) return <Problem error={error} />
  if (!tree) return <Loading />
  if (!meta) return <NotFound />
  const parent = meta.folder ? tree.folders[meta.folder] : null
  return (
    <div className="page">
      {meta.folder ? <RouteLine tree={tree} folderId={meta.folder} tail={meta.file} /> : <RouteLine tree={tree} folderId="" tail={meta.file} />}
      {derr ? <Problem error={derr} /> : !doc ? <Loading /> : (
        <>
          <div className="headrow"><h1>{doc.title}</h1><SaveButton item={{ url: docUrl(id), title: doc.title, kind: 'doc' }} /></div>
          <p className="muted" style={{ marginTop: 8 }}>{doc.sub}</p>
          <div style={{ marginTop: 18 }}><DocBody doc={doc} /></div>
          {parent?.abroad && <div className="callout"><Link to={folderUrl(parent.id) + '?tab=abroad'}>See jobs abroad for {parent.name}</Link></div>}
        </>
      )}
    </div>
  )
}

export function NotFound() {
  const { lang } = useLang()
  const te = lang === 'te'
  useTitle(te ? 'పేజీ దొరకలేదు' : 'Page not found')
  return (
    <div className="page">
      <h1>{te ? 'ఈ పేజీ దొరకలేదు' : "This page isn't here"}</h1>
      <p className="muted" style={{ marginTop: 10 }}>{te ? 'లింక్ పాతది కావచ్చు లేదా తప్పుగా టైప్ అయి ఉండవచ్చు. కోర్సు కోసం వెతకండి లేదా “అన్నీ చూడండి” నుండి మొదలుపెట్టండి.' : 'The link may be old or typed wrongly. Search for the course or start from Explore.'}</p>
      <p><Link className="btn" to="/search">{te ? 'గైడ్‌లో వెతకండి' : 'Search the guide'}</Link> <Link className="btn alt" to="/explore">{te ? 'అన్నీ చూడండి' : 'Explore'}</Link></p>
    </div>
  )
}
