// Home-page banners ("upcoming exams"). Later this list will come from PostgreSQL and an admin page.
// Fields: id, tone (ink | leaf | pink | sky | sun), art (icon key), image (optional URL – an uploaded photo replaces the art),
// tag/title/date/note {en,te}, status: 'confirmed' | 'expected', link (app route), until (YYYY-MM-DD – hidden after this day).
// Checked 16 Oct 2026. Always confirm on the official website before applying.
export const BANNERS = [
  {
    id: 'jnvst-2027', tone: 'ink', art: 'school', status: 'confirmed', link: '/schools/jnvst', until: '2026-11-28',
    tag: { en: 'Class 5 students', te: '5వ తరగతి విద్యార్థులు' },
    title: { en: 'Navodaya (JNVST) Class 6 exam', te: 'నవోదయ (JNVST) 6వ తరగతి పరీక్ష' },
    date: { en: 'Exam: 28 November 2026', te: 'పరీక్ష: 28 నవంబర్ 2026' },
    note: { en: 'Applications are closed. Download the admit card from the official site when it is released.', te: 'దరఖాస్తులు ముగిశాయి. అడ్మిట్ కార్డ్ విడుదలయ్యాక అధికారిక సైట్ నుండి డౌన్‌లోడ్ చేయండి.' },
  },
  {
    id: 'aissee-2027', tone: 'leaf', art: 'shield', status: 'expected', link: '/schools/sainik', until: '2027-01-31',
    tag: { en: 'Class 5 and Class 8 students', te: '5వ & 8వ తరగతి విద్యార్థులు' },
    title: { en: 'Sainik School entrance (AISSEE 2027)', te: 'సైనిక్ స్కూల్ ప్రవేశ పరీక్ష (AISSEE 2027)' },
    date: { en: 'Apply: Oct–Nov 2026, Exam: Jan 2027', te: 'దరఖాస్తు: అక్టో–నవం 2026, పరీక్ష: జనవరి 2027' },
    note: { en: 'For Class 6 and Class 9 admission. Watch the NTA website for the notification.', te: '6వ & 9వ తరగతి ప్రవేశానికి. నోటిఫికేషన్ కోసం NTA వెబ్‌సైట్ చూడండి.' },
  },
  {
    id: 'jee-main-2027', tone: 'sky', art: 'gear', status: 'expected', link: '/d/01_After_10th_Intermediate/MPC/After_12th_MPC/01_Engineering_BTech/Engineering_Entrance_Exams', until: '2027-01-31',
    tag: { en: 'Inter 2nd year MPC', te: 'ఇంటర్ 2వ సంవత్సరం MPC' },
    title: { en: 'JEE Main 2027 – Session 1', te: 'JEE Main 2027 – సెషన్ 1' },
    date: { en: 'Exam: 22–30 January 2027', te: 'పరీక్ష: 22–30 జనవరి 2027' },
    note: { en: 'NTA tentative dates. Registration is expected to open in October 2026.', te: 'NTA తాత్కాలిక తేదీలు. రిజిస్ట్రేషన్ అక్టోబర్ 2026లో ప్రారంభం కావచ్చు.' },
  },
  {
    id: 'tgcet-2027', tone: 'pink', art: 'book', status: 'expected', link: '/schools/tgcet', until: '2027-04-30',
    tag: { en: 'Class 4 students', te: '4వ తరగతి విద్యార్థులు' },
    title: { en: 'Gurukul entrance (TGCET 2027)', te: 'గురుకుల ప్రవేశ పరీక్ష (TGCET 2027)' },
    date: { en: 'Apply: Dec 2026 – Jan 2027', te: 'దరఖాస్తు: డిసెంబర్ 2026 – జనవరి 2027' },
    note: { en: 'Free residential schooling from Class 5. Exam usually February–April.', te: '5వ తరగతి నుండి ఉచిత రెసిడెన్షియల్ విద్య. పరీక్ష సాధారణంగా ఫిబ్రవరి–ఏప్రిల్.' },
  },
  {
    id: 'tg-ssc-2027', tone: 'sun', art: 'pen', status: 'expected', link: '/path', until: '2027-04-30',
    tag: { en: '10th class students', te: '10వ తరగతి విద్యార్థులు' },
    title: { en: 'TG SSC (10th) Public Exams 2027', te: 'TG SSC (10వ తరగతి) పబ్లిక్ పరీక్షలు 2027' },
    date: { en: 'Exams: March–April 2027', te: 'పరీక్షలు: మార్చి–ఏప్రిల్ 2027' },
    note: { en: 'Timetable expected in December 2026. Plan your next step after 10th now.', te: 'టైమ్‌టేబుల్ డిసెంబర్ 2026లో రావచ్చు. 10వ తర్వాత మీ దారిని ఇప్పుడే ప్లాన్ చేయండి.' },
  },
]
