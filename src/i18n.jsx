import { createContext, useContext, useEffect, useState } from 'react'

const KEY = 'cot-lang'
const read = () => { try { return localStorage.getItem(KEY) || 'en' } catch { return 'en' } }

const LangCtx = createContext({ lang: 'en', setLang: () => {} })

export function LangProvider({ children }) {
  const [lang, setLangState] = useState(read)
  const setLang = (l) => { setLangState(l); try { localStorage.setItem(KEY, l) } catch { /* ignore */ } }
  useEffect(() => { document.documentElement.lang = lang === 'te' ? 'te' : 'en-IN' }, [lang])
  return <LangCtx.Provider value={{ lang, setLang }}>{children}</LangCtx.Provider>
}

export function useLang() {
  const { lang, setLang } = useContext(LangCtx)
  const t = (key) => (DICT[key] ? DICT[key][lang] || DICT[key].en : key)
  const L = (obj) => (obj == null ? '' : typeof obj === 'string' ? obj : obj[lang] || obj.en)
  return { lang, setLang, t, L }
}

export const DICT = {
  appName: { en: 'Career of Telangana Students', te: 'తెలంగాణ విద్యార్థుల కెరీర్' },
  appName1: { en: 'Career of Telangana', te: 'తెలంగాణ విద్యార్థుల' }, appName2: { en: 'Students', te: 'కెరీర్' },
  tagline: { en: 'Your path from school to career', te: 'బడి నుండి కెరీర్ వరకు మీ దారి' },
  home: { en: 'Home', te: 'హోమ్' }, explore: { en: 'Explore', te: 'అన్నీ చూడండి' }, path: { en: 'My path', te: 'నా దారి' },
  search: { en: 'Search', te: 'వెతకండి' }, saved: { en: 'Saved', te: 'సేవ్ చేసినవి' }, more: { en: 'More', te: 'మరిన్ని' },
  schools: { en: 'Class 1–10', te: '1–10 తరగతులు' }, colleges: { en: 'Colleges', te: 'కాలేజీలు' }, software: { en: 'Software courses', te: 'సాఫ్ట్‌వేర్ కోర్సులు' },
  creative: { en: 'Creative careers', te: 'క్రియేటివ్ కెరీర్లు' }, guidance: { en: 'Book counselling', te: 'కౌన్సెలింగ్' },
  counselShort: { en: 'Counselling', te: 'కౌన్సెలింగ్' },
  abroad: { en: 'Jobs abroad', te: 'విదేశీ ఉద్యోగాలు' }, quiz: { en: 'Stream quiz', te: 'గ్రూప్ క్విజ్' }, install: { en: 'Install & share', te: 'ఇన్‌స్టాల్ & షేర్' },
  about: { en: 'About & help', te: 'సమాచారం & సహాయం' }, signOut: { en: 'Sign out', te: 'సైన్ అవుట్' }, guest: { en: 'Guest', te: 'అతిథి' },
  railNote: { en: 'Free guide for Telangana students. Always confirm dates and rules on official websites.', te: 'తెలంగాణ విద్యార్థులకు ఉచిత గైడ్. తేదీలు, నిబంధనలు అధికారిక వెబ్‌సైట్లలో తప్పక సరిచూసుకోండి.' },
  offline: { en: "You're offline – everything you opened before still works.", te: 'మీరు ఆఫ్‌లైన్‌లో ఉన్నారు – ఇంతకుముందు తెరిచినవన్నీ పనిచేస్తాయి.' },
  englishOnly: { en: '', te: 'ఈ వివరమైన గైడ్ ప్రస్తుతం ఇంగ్లీష్‌లో ఉంది. తెలుగు అనువాదం త్వరలో.' },
  salaryNote: { en: 'Salary is approximate, not guaranteed. Real pay can be lower or higher – it depends on the company, city, your skills, experience and the job market at that time. Use it only as a rough idea.', te: 'జీతం సుమారు అంచనా మాత్రమే, హామీ కాదు. అసలు జీతం దీనికంటే తక్కువ లేదా ఎక్కువ ఉండవచ్చు – కంపెనీ, నగరం, మీ నైపుణ్యాలు, అనుభవం, ఆ సమయంలో ఉద్యోగ మార్కెట్‌పై ఆధారపడి ఉంటుంది. దీనిని ఒక అంచనాగా మాత్రమే చూడండి.' },
  salaryShort: { en: 'Approximate – actual pay may be lower or higher', te: 'సుమారు – అసలు జీతం తక్కువ లేదా ఎక్కువ ఉండవచ్చు' },
  // home
  heroTitle: { en: 'Where do you go after school?', te: 'బడి తర్వాత మీ దారి ఏది?' },
  heroLead: { en: 'Every entrance exam, course, college, job and scholarship open to a Telangana student – from Class 1 to a job in India or abroad.', te: 'తెలంగాణ విద్యార్థికి అందుబాటులో ఉన్న ప్రతి ప్రవేశ పరీక్ష, కోర్సు, కాలేజీ, ఉద్యోగం, స్కాలర్‌షిప్ – 1వ తరగతి నుండి భారత్‌లో లేదా విదేశాల్లో ఉద్యోగం వరకు.' },
  searchPh: { en: 'Try “nursing UK” or “Group 2”', te: '“nursing UK” లేదా “Group 2” అని వెతకండి' },
  journey: { en: 'Your journey', te: 'మీ ప్రయాణం' },
  stopSchool: { en: 'School years (Class 1–10)', te: 'బడి రోజులు (1–10 తరగతులు)' },
  stop10: { en: '10th class pass', te: '10వ తరగతి పాస్' }, stopInter: { en: 'Intermediate – pick your group', te: 'ఇంటర్మీడియట్ – మీ గ్రూప్ ఎంచుకోండి' },
  stopDegree: { en: 'Degree, engineering, medicine', te: 'డిగ్రీ, ఇంజనీరింగ్, మెడిసిన్' }, stopJob: { en: 'Job – in Telangana, India or abroad', te: 'ఉద్యోగం – తెలంగాణ, భారత్ లేదా విదేశాల్లో' },
  newFeatures: { en: 'New in this version', te: 'ఈ వెర్షన్‌లో కొత్తవి' },
  notSure: { en: 'Not sure yet?', te: 'ఇంకా నిర్ణయించలేదా?' },
  findPath: { en: 'Find my path step by step', te: 'నా దారిని దశలవారీగా కనుగొనండి' }, findPathSub: { en: 'Tell us what you finished – we show only the options open to you.', te: 'మీరు ఏమి పూర్తి చేశారో చెప్పండి – మీకు సాధ్యమైన ఎంపికలే చూపిస్తాం.' },
  quizTitle: { en: 'Which Inter group suits me?', te: 'నాకు ఏ ఇంటర్ గ్రూప్ సరిపోతుంది?' }, quizSub: { en: '10 quick questions about what you enjoy.', te: 'మీ ఇష్టాల గురించి 10 చిన్న ప్రశ్నలు.' },
  popular: { en: 'Students often open', te: 'విద్యార్థులు తరచుగా చూసేవి' }, everything: { en: 'Everything in this guide', te: 'ఈ గైడ్‌లో అన్నీ' },
  keepPhone: { en: 'Keep this guide on your phone. Install it like an app – it opens fast and works without internet.', te: 'ఈ గైడ్‌ను మీ ఫోన్‌లో ఉంచుకోండి. యాప్‌లా ఇన్‌స్టాల్ చేయండి – త్వరగా తెరుచుకుంటుంది, ఇంటర్నెట్ లేకున్నా పనిచేస్తుంది.' },
  installApp: { en: 'Install app', te: 'యాప్ ఇన్‌స్టాల్ చేయండి' }, howInstall: { en: 'How to install', te: 'ఎలా ఇన్‌స్టాల్ చేయాలి' },
  footerNote: { en: 'Information prepared October 2026 as a guide. Fees, seats, age limits and exam patterns change every year – always confirm on the official website before applying.', te: 'అక్టోబర్ 2026 నాటి సమాచారం, మార్గదర్శకం కోసం మాత్రమే. ఫీజులు, సీట్లు, వయోపరిమితులు, పరీక్షా విధానాలు ప్రతి సంవత్సరం మారుతాయి – దరఖాస్తుకు ముందు అధికారిక వెబ్‌సైట్‌లో సరిచూసుకోండి.' },
  // common
  save: { en: 'Save', te: 'సేవ్' }, savedBtn: { en: 'Saved', te: 'సేవ్ అయింది' }, open: { en: 'Open', te: 'తెరవండి' },
  eligibility: { en: 'Who can apply', te: 'ఎవరు దరఖాస్తు చేయవచ్చు' }, pattern: { en: 'Exam / selection', te: 'పరీక్ష / ఎంపిక' }, when: { en: 'When', te: 'ఎప్పుడు' },
  website: { en: 'Official website', te: 'అధికారిక వెబ్‌సైట్' }, tips: { en: 'Tips', te: 'సూచనలు' }, entry: { en: 'Entry', te: 'ప్రవేశం' },
  confirm: { en: 'Always confirm dates, age limits and rules in the latest official notification.', te: 'తేదీలు, వయోపరిమితులు, నిబంధనలను తాజా అధికారిక నోటిఫికేషన్‌లో తప్పక సరిచూసుకోండి.' },
  district: { en: 'District', te: 'జిల్లా' }, allDistricts: { en: 'All districts', te: 'అన్ని జిల్లాలు' }, filter: { en: 'Search by name or town', te: 'పేరు లేదా పట్టణంతో వెతకండి' },
  results: { en: 'results', te: 'ఫలితాలు' }, source: { en: 'Source', te: 'ఆధారం' }, noMatch: { en: 'No match. Clear the search or choose "All districts".', te: 'ఏమీ దొరకలేదు. సెర్చ్ తొలగించండి లేదా "అన్ని జిల్లాలు" ఎంచుకోండి.' },
  howToFind: { en: 'How to find schools near you', te: 'మీ దగ్గర పాఠశాలలు ఎలా కనుగొనాలి' },
  // login
  signIn: { en: 'Sign in', te: 'సైన్ ఇన్' }, createAccount: { en: 'Create account', te: 'ఖాతా సృష్టించండి' }, username: { en: 'Username', te: 'యూజర్‌నేమ్' },
  password: { en: 'Password', te: 'పాస్‌వర్డ్' }, confirmPassword: { en: 'Confirm password', te: 'పాస్‌వర్డ్ మళ్లీ' }, fullName: { en: 'Full name', te: 'పూర్తి పేరు' },
  continueGuest: { en: 'Continue as guest', te: 'అతిథిగా కొనసాగండి' }, haveAccount: { en: 'Already have an account?', te: 'ఇప్పటికే ఖాతా ఉందా?' }, newHere: { en: 'New here?', te: 'కొత్తవారా?' },
  showPw: { en: 'Show', te: 'చూపించు' }, hidePw: { en: 'Hide', te: 'దాచు' },
  loginLead: { en: 'Career guidance for every Telangana student – entrance exams, colleges, jobs, abroad and scholarships.', te: 'ప్రతి తెలంగాణ విద్యార్థికి కెరీర్ మార్గదర్శనం – ప్రవేశ పరీక్షలు, కాలేజీలు, ఉద్యోగాలు, విదేశాలు, స్కాలర్‌షిప్‌లు.' },
  deviceNote: { en: 'Your account is saved on this device only.', te: 'మీ ఖాతా ఈ పరికరంలో మాత్రమే సేవ్ అవుతుంది.' },
  errBadLogin: { en: 'Username or password is incorrect.', te: 'యూజర్‌నేమ్ లేదా పాస్‌వర్డ్ తప్పు.' },
  errUserTaken: { en: 'That username is already used on this device. Choose another.', te: 'ఈ యూజర్‌నేమ్ ఇప్పటికే వాడుకలో ఉంది. వేరేది ఎంచుకోండి.' },
  errPwShort: { en: 'Use at least 6 characters for the password.', te: 'పాస్‌వర్డ్‌కు కనీసం 6 అక్షరాలు వాడండి.' },
  errPwMatch: { en: 'The two passwords do not match.', te: 'రెండు పాస్‌వర్డ్‌లు సరిపోలలేదు.' },
  errUser: { en: 'Username: 3–20 letters, numbers or underscore.', te: 'యూజర్‌నేమ్: 3–20 అక్షరాలు, అంకెలు లేదా అండర్‌స్కోర్.' },
  errName: { en: 'Enter your name.', te: 'మీ పేరు నమోదు చేయండి.' },
  poweredBy: { en: 'A GGTECH Software Solutions product', te: 'GGTECH సాఫ్ట్‌వేర్ సొల్యూషన్స్ ఉత్పత్తి' },
}
