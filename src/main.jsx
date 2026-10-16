import { StrictMode, useEffect } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, HashRouter, Routes, Route, useLocation } from 'react-router-dom'
import { registerSW } from 'virtual:pwa-register'
import './styles.css'
import { LangProvider } from './i18n.jsx'
import { AuthProvider, useAuth } from './auth.jsx'
import { Shell } from './components/ui.jsx'
import Home from './pages/Home.jsx'
import Login from './pages/Login.jsx'
import { Explore, FolderPage, DocPage, NotFound } from './pages/Browse.jsx'
import { PathFinder, Quiz } from './pages/Guide.jsx'
import { Countries, CountryPage, Search, Saved, Install, About } from './pages/Extra.jsx'
import { Schools, SchoolExam, Colleges, Software, SoftwareCourse, Creative, CreativeCourse, Guidance, More } from './pages/New.jsx'

const HOSTED = import.meta.env.VITE_ARTIFACT === '1'
const Router = HOSTED ? HashRouter : BrowserRouter
if (!HOSTED) registerSW({ immediate: true })

function ScrollTop() {
  const { pathname } = useLocation()
  useEffect(() => { window.scrollTo(0, 0) }, [pathname])
  return null
}

function Gate() {
  const auth = useAuth()
  if (!auth.session) return <Login />
  return (
    <Shell>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/explore" element={<Explore />} />
        <Route path="/f/*" element={<FolderPage />} />
        <Route path="/d/*" element={<DocPage />} />
        <Route path="/schools" element={<Schools />} />
        <Route path="/schools/:id" element={<SchoolExam />} />
        <Route path="/colleges" element={<Colleges />} />
        <Route path="/software" element={<Software />} />
        <Route path="/software/:id" element={<SoftwareCourse />} />
        <Route path="/creative" element={<Creative />} />
        <Route path="/creative/:id" element={<CreativeCourse />} />
        <Route path="/guidance" element={<Guidance />} />
        <Route path="/more" element={<More />} />
        <Route path="/path" element={<PathFinder />} />
        <Route path="/quiz" element={<Quiz />} />
        <Route path="/countries" element={<Countries />} />
        <Route path="/countries/:code" element={<CountryPage />} />
        <Route path="/search" element={<Search />} />
        <Route path="/saved" element={<Saved />} />
        <Route path="/install" element={<Install />} />
        <Route path="/about" element={<About />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Shell>
  )
}

function App() {
  return (
    <LangProvider>
      <AuthProvider>
        <Router>
          <ScrollTop />
          <Gate />
        </Router>
      </AuthProvider>
    </LangProvider>
  )
}

createRoot(document.getElementById('root')).render(<StrictMode><App /></StrictMode>)
