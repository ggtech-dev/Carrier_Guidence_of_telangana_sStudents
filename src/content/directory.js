// School & college directory – Telangana. Only entries from published lists (sources shown per tab).
// Row: [name, town/area, district, type, extra]

const ENG_RAW = `Jayamukhi Institute of Technological Sciences|Narsampet|Warangal|Private (Autonomous)
Malla Reddy Institute of Technology and Science|Maisammaguda, Dhulapally|Medchal-Malkajgiri|Private
VNR Vignana Jyothi Institute of Engineering and Technology|Bachupally, Hyderabad|Medchal-Malkajgiri|Private (Autonomous)
Mahatma Gandhi Institute of Technology|Gandipet|Rangareddy|Private
Ellenki College of Engineering and Technology|Patancheru|Sangareddy|Private (Autonomous)
Rajiv Gandhi University of Knowledge Technologies (RGUKT Basar)|Basar|Nirmal|Government (Autonomous)
Vignana Bharathi Institute of Technology|Ghatkesar|Medchal-Malkajgiri|Private
Aurora Group of Institutions|Ghatkesar|Medchal-Malkajgiri|Private
Geethanjali College of Engineering and Technology|Cheeryal, Keesara|Medchal-Malkajgiri|Private (Autonomous)
Holy Mary Institute of Technology|Bogaram|Medchal-Malkajgiri|Private
Vignan Institute of Management and Technology for Women|Ghatkesar|Medchal-Malkajgiri|Private (Women)
Samskruti College of Engineering and Technology|Bogaram|Medchal-Malkajgiri|Private
Princeton Institute of Engineering and Technology|Ghatkesar|Medchal-Malkajgiri|Private
Anurag University / Anurag Group of Institutions|Venkatapur|Medchal-Malkajgiri|Private (Autonomous)
Sreenidhi Institute of Science and Technology|Yamnampet, Ghatkesar|Medchal-Malkajgiri|Private (Autonomous)
Kommuri Pratap Reddy Institute of Technology|Ghanpur, Ghatkesar|Medchal-Malkajgiri|Private
Nalla Malla Reddy Engineering College|Ghatkesar|Medchal-Malkajgiri|Private (Autonomous)
Megha Institute of Engineering and Technology for Women|Ghatkesar|Medchal-Malkajgiri|Private (Women)
BITS Pilani – Hyderabad Campus|Shameerpet|Medchal-Malkajgiri|Private (Deemed University)
Indian Institute of Technology Hyderabad (IIT-H)|Kandi|Sangareddy|Central Government
International Institute of Information Technology (IIIT Hyderabad)|Gachibowli|Rangareddy|Deemed University
JNTUH University College of Engineering|Kukatpally|Medchal-Malkajgiri|Government
National Institute of Technology Warangal (NIT-W)|Warangal|Hanumakonda / Warangal|Central Government
Kakatiya University College of Engineering|Warangal|Hanumakonda / Warangal|Government
University College of Engineering, Osmania University|Hyderabad|Hyderabad|Government
DVR College of Engineering and Technology|Kandi|Sangareddy|Private
Kakatiya Institute of Technology and Science|Warangal|Hanumakonda / Warangal|Private (Autonomous)
GITAM (Deemed University) Hyderabad|Rudraram|Sangareddy|Private (Deemed University)
MNR College of Engineering and Technology|Kandi|Sangareddy|Private
Chaitanya Bharathi Institute of Technology (CBIT)|Gandipet|Rangareddy|Private (Autonomous)
MLR Institute of Technology|Dundigal|Medchal-Malkajgiri|Private (Autonomous)
Sridevi Women's Engineering College|Vattinagulapally|Rangareddy|Private (Women)
Vasavi College of Engineering|Ibrahimbagh|Hyderabad|Private (Autonomous)
Bandari Srinivas Institute of Technology|Chevella|Rangareddy|Private
KG Reddy College of Engineering and Technology|Moinabad|Rangareddy|Private
Vardhaman College of Engineering|Kacharam, Shamshabad|Rangareddy|Private (Autonomous)
School of Engineering Sciences and Technology, University of Hyderabad|Gachibowli|Rangareddy|Central University
Maturi Venkata Subba Rao (MVSR) Engineering College|Nadergul|Rangareddy|Private (Autonomous)
Aurora's Technological and Research Institute|Uppal|Medchal-Malkajgiri|Private
TRR College of Engineering (Tammannagari Ramakrishna Reddy)|Inole, Patancheru|Sangareddy|Private
Bhoj Reddy Engineering College for Women|Saidabad|Hyderabad|Private (Women)
Deccan College of Engineering and Technology|Nampally|Hyderabad|Private (Minority)
G. Narayanamma Institute of Technology and Science|Shaikpet|Hyderabad|Private (Autonomous, Women)
Islamia College of Engineering and Technology|Bandlaguda|Hyderabad|Private (Minority)
Keshav Memorial Institute of Technology|Narayanguda|Hyderabad|Private
Methodist College of Engineering and Technology|Abids|Hyderabad|Private
Shadan Women's College of Engineering and Technology|Khairatabad|Hyderabad|Private (Women)
Stanley College of Engineering and Technology for Women|Abids|Hyderabad|Private (Women)
Sri Indu College of Engineering and Technology|Ibrahimpatnam|Rangareddy|Private (Autonomous)
Sri Datta College of Engineering|Ibrahimpatnam|Rangareddy|Private
Bharat Institute of Engineering and Technology|Ibrahimpatnam|Rangareddy|Private
Guru Nanak Institute of Technology|Ibrahimpatnam|Rangareddy|Private
Guru Nanak Institutions Technical Campus|Ibrahimpatnam|Rangareddy|Private (Autonomous)
Scient Institute of Technology|Ibrahimpatnam|Rangareddy|Private
Teegala Krishna Reddy Engineering College|Meerpet|Rangareddy|Private
TKR College of Engineering and Technology|Meerpet|Rangareddy|Private (Autonomous)
Mahaveer Institute of Science and Technology|Bandlaguda|Hyderabad|Private
Vaagdevi Engineering College|Bollikunta|Hanumakonda / Warangal|Private
Vaagdevi College of Engineering|Bollikunta|Hanumakonda / Warangal|Private (Autonomous)
Sumathi Reddy Institute of Technology for Women|Ananthasagar, Hasanparthy|Hanumakonda / Warangal|Private (Women)
AAR Mahaveer Engineering College|Bandlaguda|Hyderabad|Private
Muffakham Jah College of Engineering and Technology|Banjara Hills|Hyderabad|Private (Minority)
Princeton College of Engineering and Technology|Ankushapur|Medchal-Malkajgiri|Private
Shadan College of Engineering and Technology|Peerancheru|Rangareddy|Private (Minority)
Matrusri Engineering College|Saidabad|Hyderabad|Private
CVR College of Engineering|Mangalpally, Ibrahimpatnam|Rangareddy|Private (Autonomous)
Nawab Shah Alam Khan College of Engineering and Technology|Malakpet|Hyderabad|Private (Minority)
Sreyas Institute of Engineering and Technology|Bandlaguda|Hyderabad|Private
JNTUH University College of Engineering Sultanpur|Sultanpur|Sangareddy|Government
Vidya Jyothi Institute of Technology|Aziznagar, Moinabad|Rangareddy|Private (Autonomous)
Abhinav Hi-Tech College of Engineering|Moinabad|Rangareddy|Private
Joginpally B.R. Engineering College|Moinabad|Rangareddy|Private
JB Institute of Engineering and Technology|Moinabad|Rangareddy|Private (Autonomous)
Siddhartha Institute of Technology and Sciences|Ibrahimpatnam|Rangareddy|Private
Lords Institute of Engineering and Technology|Himayath Sagar|Rangareddy|Private (Autonomous, Minority)
AVN Institute of Engineering and Technology|Ibrahimpatnam|Rangareddy|Private
Visvesvaraya College of Engineering and Technology|Ibrahimpatnam|Rangareddy|Private
Gokaraju Rangaraju Institute of Engineering and Technology (GRIET)|Bachupally|Medchal-Malkajgiri|Private (Autonomous)
St. Martin's Engineering College|Dhulapally|Medchal-Malkajgiri|Private (Autonomous)
CMR Engineering College|Kandlakoya|Medchal-Malkajgiri|Private (Autonomous)
CMR Technical Campus|Kandlakoya|Medchal-Malkajgiri|Private (Autonomous)
Malla Reddy Engineering College|Maisammaguda|Medchal-Malkajgiri|Private (Autonomous)
Hyderabad Institute of Technology and Management|Gowdavelly|Medchal-Malkajgiri|Private
CMR Institute of Technology|Kandlakoya|Medchal-Malkajgiri|Private (Autonomous)
CMR College of Engineering and Technology|Kandlakoya|Medchal-Malkajgiri|Private (Autonomous)
Sphoorthy Engineering College|Nadergul|Rangareddy|Private
Institute of Aeronautical Engineering|Dundigal|Medchal-Malkajgiri|Private (Autonomous)
JNTUH University College of Engineering Jagtial|Nachupally|Jagtial|Government
JNTUH University College of Engineering Manthani|Manthani|Peddapalli|Government`

const MED_GOVT = `Osmania Medical College|Koti, Hyderabad|Hyderabad|Government|250
Gandhi Medical College|Secunderabad|Hyderabad|Government|250
Kakatiya Medical College|Warangal|Hanumakonda / Warangal|Government|250
All India Institute of Medical Sciences (AIIMS)|Bibinagar|Yadadri Bhuvanagiri|Central Government|100
ESIC Medical College|Sanathnagar, Hyderabad|Hyderabad|Central Government (ESIC)|100
Rajiv Gandhi Institute of Medical Sciences (RIMS)|Adilabad|Adilabad|Government|120
Government Medical College, Nizamabad|Nizamabad|Nizamabad|Government|120
Government Medical College, Mahabubnagar|Mahabubnagar|Mahabubnagar|Government|175
Government Medical College, Siddipet|Siddipet|Siddipet|Government|175
Government Medical College, Nalgonda|Nalgonda|Nalgonda|Government|150
Government Medical College, Suryapet|Suryapet|Suryapet|Government|150
Government Medical College, Ramagundam|Ramagundam|Peddapalli|Government|150
Government Medical College, Nagarkurnool|Nagarkurnool|Nagarkurnool|Government|150
Government Medical College, Sangareddy|Sangareddy|Sangareddy|Government|150
Government Medical College, Wanaparthy|Wanaparthy|Wanaparthy|Government|150
Government Medical College, Bhadradri Kothagudem|Kothagudem|Bhadradri Kothagudem|Government|150
Government Medical College, Mahabubabad|Mahabubabad|Mahabubabad|Government|150
Government Medical College, Jagtial|Jagtial|Jagtial|Government|150
Government Medical College, Mancherial|Mancherial|Mancherial|Government|100
Government Medical College, Jayashankar Bhupalpally|Bhupalpally|Jayashankar Bhupalpally|Government|100
Government Medical College, Rajanna Sircilla|Sircilla|Rajanna Sircilla|Government|100
Government Medical College, Nirmal|Nirmal|Nirmal|Government|100
Government Medical College, Karimnagar|Karimnagar|Karimnagar|Government|100
Government Medical College, Vikarabad|Vikarabad|Vikarabad|Government|100
Government Medical College, Khammam|Khammam|Khammam|Government|100
Government Medical College, Kamareddy|Kamareddy|Kamareddy|Government|100
Government Medical College, Kumuram Bheem Asifabad|Asifabad|Kumuram Bheem Asifabad|Government|100
Government Medical College, Jangaon|Jangaon|Jangaon|Government|100
Government Medical College, Jogulamba Gadwal|Gadwal|Jogulamba Gadwal|Government|50
Government Medical College, Mulugu|Mulugu|Mulugu|Government|50
Government Medical College, Narayanpet|Narayanpet|Narayanpet|Government|50
Government Medical College, Narsampet|Narsampet|Warangal|Government|50
Government Medical College, Quthbullapur|Quthbullapur|Medchal-Malkajgiri|Government|50
Government Medical College, Medak|Medak|Medak|Government|50
Autonomous State Medical College, Yadadri|Yadadri|Yadadri Bhuvanagiri|Government|50
Government Medical College, Maheshwaram|Maheshwaram|Rangareddy|Government|50`

const MED_PVT = `Mamata Medical College|Khammam|Khammam|Private|200
SVS Medical College|Mahabubnagar|Mahabubnagar|Private|150
Kamineni Institute of Medical Sciences|Narketpally|Nalgonda|Private|200
MediCiti Institute of Medical Sciences|Ghanpur, Medchal|Medchal-Malkajgiri|Private|150
Prathima Institute of Medical Sciences|Karimnagar|Karimnagar|Private|250
MNR Medical College|Sangareddy|Sangareddy|Private|150
Chalmeda Anand Rao Institute of Medical Sciences|Karimnagar|Karimnagar|Private|200
Bhaskar Medical College|Yenkapally, Moinabad|Rangareddy|Private|150
Apollo Institute of Medical Sciences|Jubilee Hills, Hyderabad|Hyderabad|Private|150
Kamineni Academy of Medical Sciences|LB Nagar, Hyderabad|Rangareddy|Private|150
Mahavir Institute of Medical Sciences|Vikarabad|Vikarabad|Private|200
RVM Institute of Medical Sciences|Mulugu (Siddipet)|Siddipet|Private|250
Mamata Academy of Medical Sciences|Bachupally|Medchal-Malkajgiri|Private|150
Patnam Mahender Reddy Institute of Medical Sciences|Chevella|Rangareddy|Private|200
Surabhi Institute of Medical Sciences|Siddipet|Siddipet|Private|200
Maheshwara Medical College|Isnapur, Patancheru|Sangareddy|Private|150
TRR Institute of Medical Sciences|Patancheru|Sangareddy|Private|150
Arundathi Institute of Medical Sciences|Dundigal|Medchal-Malkajgiri|Private|150
CMR Institute of Medical Sciences|Kandlakoya|Medchal-Malkajgiri|Private|250
Father Colombo Institute of Medical Sciences|Warangal|Hanumakonda / Warangal|Private|150
Neelima Institute of Medical Sciences|Ghatkesar|Medchal-Malkajgiri|Private|200
Prathima Relief Institute of Medical Sciences|Hanumakonda|Hanumakonda / Warangal|Private|150
Nova Institute of Medical Sciences|Rangareddy|Rangareddy|Private|250
Deccan College of Medical Sciences|Kanchanbagh, Hyderabad|Hyderabad|Private (Minority)|150
Shadan Institute of Medical Sciences|Peerancheru|Rangareddy|Private (Minority)|150
Dr VRK Women's Medical College|Aziznagar|Rangareddy|Private (Minority, Women)|100
Ayaan Institute of Medical Sciences|Moinabad|Rangareddy|Private (Minority)|150
Malla Reddy Institute of Medical Sciences|Suraram|Medchal-Malkajgiri|Private (Deemed)|200
Malla Reddy Medical College for Women|Suraram|Medchal-Malkajgiri|Private (Deemed, Women)|200`

const NURSING = `NIMS College of Nursing|Punjagutta, Hyderabad|Hyderabad|Government
Apollo School and College of Nursing|Hyderabad|Hyderabad|Private
Balaji Institute of Nursing|Warangal|Hanumakonda / Warangal|Private
College of Nursing, Muslim Maternity and Children's Hospital|Hyderabad|Hyderabad|Private
College of Nursing, Chalmeda Anand Rao Institute of Medical Sciences|Karimnagar|Karimnagar|Private
Deepthi College of Nursing|Nalgonda|Nalgonda|Private
Eashwari Bai Memorial College of Nursing|Secunderabad|Hyderabad|Private
Global Kasturba College of Nursing|Hyderabad|Hyderabad|Private
Holy Mary College of Nursing|Hyderabad|Medchal-Malkajgiri|Private
Indo American College of Nursing|Hyderabad|Hyderabad|Private
Jesus Mary Joseph College and School of Nursing|Hyderabad|Hyderabad|Private
Kalanjali College of Nursing|Hyderabad|Hyderabad|Private
Kamineni Institute of Medical Sciences – College of Nursing|Narketpally|Nalgonda|Private
Mahila Dakshata Samithi Bansilal Malani College of Nursing|Hyderabad|Hyderabad|Private
Malla Reddy College of Nursing|Hyderabad|Medchal-Malkajgiri|Private
Mamata College of Nursing|Khammam|Khammam|Private
Maruthi Paramedical Academy College of Nursing|Khammam|Khammam|Private
MediCiti School of Nursing|Medchal|Medchal-Malkajgiri|Private
MNR College of Nursing|Sangareddy|Sangareddy|Private
Mother Krishna Bai College of Nursing|Hyderabad|Hyderabad|Private
Mother Theresa College of Nursing|Hyderabad|Hyderabad|Private
Owaisi College of Nursing|Hyderabad|Hyderabad|Private (Minority)
Pioneer College of Nursing|Hyderabad|Hyderabad|Private
Princess Durru Shehvar College of Nursing|Hyderabad|Hyderabad|Private
Santosh College of Nursing|Karimnagar|Karimnagar|Private
Shadan School of Nursing|Hyderabad|Hyderabad|Private
Sri Surya College of Nursing|Hyderabad|Hyderabad|Private
St Ann's College of Nursing|Hanamkonda|Hanumakonda / Warangal|Private
Surabhi College of Nursing|Siddipet|Siddipet|Private
SVS College of Nursing|Mahabubnagar|Mahabubnagar|Private
Tirumala Medical Academy|Nizamabad|Nizamabad|Private
Vijaya Health Care Academic Society's College of Nursing|Keesara|Medchal-Malkajgiri|Private
Vijay Marie College of Nursing|Hyderabad|Hyderabad|Private
Yashoda College of Nursing|Hyderabad|Hyderabad|Private`

const AGRI = `College of Agriculture (PJTSAU)|Rajendranagar|Rangareddy|Government|B.Sc (Hons) Agriculture
Agricultural College (PJTSAU)|Aswaraopet|Bhadradri Kothagudem|Government|B.Sc (Hons) Agriculture
Agricultural College (PJTSAU)|Jagtial|Jagtial|Government|B.Sc (Hons) Agriculture
Agricultural College (PJTSAU)|Palem|Nagarkurnool|Government|B.Sc (Hons) Agriculture
Agricultural College (PJTSAU)|Warangal|Hanumakonda / Warangal|Government|B.Sc (Hons) Agriculture
BJR Agricultural College (PJTSAU)|Sircilla|Rajanna Sircilla|Government|B.Sc (Hons) Agriculture
Agricultural College (PJTSAU)|Adilabad|Adilabad|Government|B.Sc (Hons) Agriculture
Agricultural College (PJTSAU)|Tornala|Siddipet|Government|B.Sc (Hons) Agriculture
College of Agricultural Engineering (PJTSAU)|Kandi|Sangareddy|Government|B.Tech Agricultural Engineering
College of Food Science and Technology (PJTSAU)|Rudrur|Nizamabad|Government|B.Tech Food Technology
College of Community Science (PJTSAU)|Saifabad|Hyderabad|Government|B.Sc (Hons) Community Science
College of Horticulture (SKLTGHU)|Mojerla|Wanaparthy|Government|B.Sc (Hons) Horticulture
College of Horticulture (SKLTGHU)|Rajendranagar|Rangareddy|Government|B.Sc (Hons) Horticulture
College of Veterinary Science (PVNRTVU)|Rajendranagar|Rangareddy|Government|BVSc & AH
College of Veterinary Science (PVNRTVU)|Korutla|Jagtial|Government|BVSc & AH
College of Veterinary Science (PVNRTVU)|Mamnoor|Hanumakonda / Warangal|Government|BVSc & AH
College of Dairy Technology (PVNRTVU)|Kamareddy|Kamareddy|Government|B.Tech Dairy Technology
College of Fishery Science (PVNRTVU)|Pebbair|Wanaparthy|Government|B.F.Sc`

const POLY = `J.N. Government Polytechnic|Ramanthapur|Hyderabad|Government
Government Institute of Electronics|Secunderabad|Hyderabad|Government
Q.Q. Government Polytechnic|Chandulal Baradari|Hyderabad|Government
Government Polytechnic for Women|Secunderabad|Hyderabad|Government (Women)
Government Polytechnic|Warangal|Hanumakonda / Warangal|Government
Government Polytechnic|Karimnagar|Karimnagar|Government
Government Polytechnic|Nizamabad|Nizamabad|Government
Government Polytechnic|Kothagudem|Bhadradri Kothagudem|Government
Government Polytechnic|Mahabubnagar|Mahabubnagar|Government`

const NAV = `JNV Karimnagar|Choppadandi|Karimnagar|Central Government|Running
JNV Nalgonda|Chalakurthy|Nalgonda|Central Government|Running
JNV Kamareddy (old Nizamabad)|Nizamsagar|Kamareddy|Central Government|Running
JNV Khammam|Palair|Khammam|Central Government|Running
JNV Kumuram Bheem Asifabad (old Adilabad)|Sirpur Kagaznagar|Kumuram Bheem Asifabad|Central Government|Running
JNV Rangareddy|Gachibowli (HCU campus)|Rangareddy|Central Government|Running
JNV Siddipet (old Medak)|Wargal|Siddipet|Central Government|Running
JNV Warangal|Mamnoor|Hanumakonda / Warangal|Central Government|Running
JNV Nagarkurnool (old Mahabubnagar)|Vattem|Nagarkurnool|Central Government|Running
JNV Jagtial|Temporary campus|Jagtial|Central Government|New (approved Dec 2024)
JNV Nizamabad|Temporary campus|Nizamabad|Central Government|New (approved Dec 2024)
JNV Bhadradri Kothagudem|Temporary campus|Bhadradri Kothagudem|Central Government|New (approved Dec 2024)
JNV Medchal-Malkajgiri|Temporary campus|Medchal-Malkajgiri|Central Government|New (approved Dec 2024)
JNV Mahabubnagar|Temporary campus|Mahabubnagar|Central Government|New (approved Dec 2024)
JNV Sangareddy|Temporary campus|Sangareddy|Central Government|New (approved Dec 2024)
JNV Suryapet|Temporary campus|Suryapet|Central Government|New (approved Dec 2024)`

const SPORTS = `Telangana State Sports School|Hakimpet, Shamirpet mandal|Medchal-Malkajgiri|Government|Classes 4–12
Regional Sports School|Indira Priyadarshini Stadium|Adilabad|Government|Classes 4–10
Regional Sports School|Dr B.R. Ambedkar Stadium|Karimnagar|Government|Classes 4–10`

const parse = (s) => s.trim().split('\n').map((l) => l.split('|').map((x) => x.trim()))

// tab definitions – name/intro are { en, te }
export const DIRECTORY = [
  { id: 'navodaya', name: { en: 'Navodaya schools', te: 'నవోదయ పాఠశాలలు' }, rows: parse(NAV), cols: ['school', 'place', 'district', 'type', 'status'],
    intro: { en: 'Free CBSE residential schools (Class 6–12), one per district. Entrance in Class 5 (JNVST).', te: 'ఉచిత CBSE రెసిడెన్షియల్ పాఠశాలలు (6–12), జిల్లాకు ఒకటి. 5వ తరగతిలో ప్రవేశ పరీక్ష (JNVST).' },
    source: 'NVS / Wikipedia list; new schools per Union Cabinet approval (Dec 2024)', official: 'navodaya.gov.in' },
  { id: 'residential', name: { en: 'Residential (Gurukul) schools', te: 'గురుకుల పాఠశాలలు' }, rows: [
      ['Telangana Social Welfare Residential Educational Institutions Society (TGSWREIS)', 'All districts', 'All districts', 'Government', 'About 230+ schools'],
      ['Telangana Tribal Welfare Residential Educational Institutions Society (TGTWREIS)', 'All districts', 'All districts', 'Government', 'About 85+ schools'],
      ['Mahatma Jyotiba Phule BC Welfare Residential Educational Institutions Society (MJPTBCWREIS)', 'All districts', 'All districts', 'Government', 'About 140+ schools'],
      ['Telangana Residential Educational Institutions Society (TGREIS)', 'All districts', 'All districts', 'Government', 'About 35 schools'],
      ['Telangana Minorities Residential Educational Institutions Society (TMREIS)', 'All districts', 'All districts', 'Government', 'Minority residential schools'],
      ['Kasturba Gandhi Balika Vidyalayas (KGBV) – girls', 'Most mandals', 'All districts', 'Government', 'No entrance; apply at KGBV / MEO'],
      ['Telangana Model Schools', 'Mandal level', 'All districts', 'Government', 'English medium; entrance MSAT'],
      ...parse(SPORTS),
    ], cols: ['school', 'place', 'district', 'type', 'notes'],
    intro: { en: 'About 500 free Gurukul schools through four societies (entrance TGCET in Class 4), plus KGBV, Model and Sports schools. Each society website lists its schools district-wise.', te: 'నాలుగు సొసైటీల ద్వారా సుమారు 500 ఉచిత గురుకుల పాఠశాలలు (4వ తరగతిలో TGCET), అదనంగా KGBV, మోడల్, స్పోర్ట్స్ స్కూల్స్. ప్రతి సొసైటీ వెబ్‌సైట్‌లో జిల్లా వారీగా పాఠశాలల జాబితా ఉంది.' },
    source: 'TGCET notification (school counts are approximate)', official: 'tgcet.cgg.gov.in, tgswreis.telangana.gov.in, tgtwreis.telangana.gov.in, mjptbcwreis.telangana.gov.in' },
  { id: 'private', name: { en: 'Private & all schools', te: 'ప్రైవేట్ & అన్ని పాఠశాలలు' }, rows: [], cols: [],
    intro: { en: 'Telangana has tens of thousands of schools. The official UDISE+ portal lists every recognised school (government and private) by district, mandal and village with board, medium and facilities.', te: 'తెలంగాణలో వేల సంఖ్యలో పాఠశాలలు ఉన్నాయి. అధికారిక UDISE+ పోర్టల్‌లో ప్రతి గుర్తింపు పొందిన పాఠశాల (ప్రభుత్వ, ప్రైవేట్) జిల్లా, మండలం, గ్రామం వారీగా బోర్డు, మాధ్యమం, సౌకర్యాలతో ఉంటుంది.' },
    how: [{ en: 'Open udiseplus.gov.in and choose "Know your school" / school search', te: 'udiseplus.gov.in తెరిచి "Know your school" / స్కూల్ సెర్చ్ ఎంచుకోండి' },
          { en: 'Select State: Telangana, then your district and mandal (block)', te: 'రాష్ట్రం: తెలంగాణ ఎంచుకుని, తర్వాత మీ జిల్లా, మండలం (బ్లాక్) ఎంచుకోండి' },
          { en: 'Check that the school is recognised before paying any admission fee', te: 'అడ్మిషన్ ఫీజు చెల్లించే ముందు పాఠశాలకు గుర్తింపు ఉందో లేదో చూడండి' }],
    source: 'Ministry of Education – UDISE+', official: 'udiseplus.gov.in, schooledu.telangana.gov.in' },
  { id: 'junior', name: { en: 'Junior colleges (Intermediate)', te: 'జూనియర్ కాలేజీలు (ఇంటర్)' }, rows: [
      ['Telangana Residential Junior Colleges (TGRJC)', '35 colleges', 'All districts', 'Government (residential)', 'Entrance TGRJC CET'],
      ['Gurukul junior colleges (SC, ST, BC, Minority societies)', 'Across Telangana', 'All districts', 'Government (residential)', 'Through society admissions'],
      ['Government Junior Colleges', 'Most mandal headquarters', 'All districts', 'Government', 'Free; direct admission after 10th'],
      ['Telangana Model School junior colleges', 'Mandal level', 'All districts', 'Government', 'English medium'],
      ['KGBV junior colleges (girls)', 'Many mandals', 'All districts', 'Government', 'For girls'],
      ['Private and aided junior colleges', 'Across Telangana', 'All districts', 'Private / Aided', 'Check TGBIE affiliation'],
    ], cols: ['school', 'place', 'district', 'type', 'notes'],
    intro: { en: 'Thousands of junior colleges are affiliated to TGBIE. Use the official list to find colleges in your district and mandal, and always check affiliation before joining.', te: 'వేల జూనియర్ కాలేజీలు TGBIEకి అనుబంధంగా ఉన్నాయి. మీ జిల్లా, మండలంలోని కాలేజీలను అధికారిక జాబితాలో చూడండి; చేరే ముందు అనుబంధాన్ని తప్పకుండా తనిఖీ చేయండి.' },
    source: 'TGBIE / TGRJC', official: 'tgbie.cgg.gov.in, tgrjc.cgg.gov.in' },
  { id: 'engineering', name: { en: 'Engineering colleges', te: 'ఇంజనీరింగ్ కాలేజీలు' }, rows: parse(ENG_RAW), cols: ['college', 'place', 'district', 'type'],
    intro: { en: 'Major engineering colleges and universities. Admission through TG EAPCET, JEE Main (NIT) or JEE Advanced (IIT). The full counselling list with every college code is on the TG EAPCET site.', te: 'ప్రధాన ఇంజనీరింగ్ కాలేజీలు, విశ్వవిద్యాలయాలు. TG EAPCET, JEE మెయిన్ (NIT) లేదా JEE అడ్వాన్స్‌డ్ (IIT) ద్వారా ప్రవేశం. ప్రతి కాలేజీ కోడ్‌తో పూర్తి జాబితా TG EAPCET వెబ్‌సైట్‌లో ఉంది.' },
    source: 'Wikipedia list of engineering colleges in Telangana (selected); TGCHE for the full list', official: 'tgeapcet.nic.in, tgche.ac.in' },
  { id: 'medical', name: { en: 'Medical colleges (MBBS)', te: 'మెడికల్ కాలేజీలు (MBBS)' }, rows: [...parse(MED_GOVT), ...parse(MED_PVT)], cols: ['college', 'place', 'district', 'type', 'seats'],
    intro: { en: '36 government and central medical colleges (about 4,290 MBBS seats) and 29 private colleges. Admission only through NEET-UG and KNRUHS / MCC counselling.', te: '36 ప్రభుత్వ, కేంద్ర మెడికల్ కాలేజీలు (సుమారు 4,290 MBBS సీట్లు), 29 ప్రైవేట్ కాలేజీలు. NEET-UG, KNRUHS / MCC కౌన్సెలింగ్ ద్వారానే ప్రవేశం.' },
    source: 'Govt colleges & seats: PW (Physics Wallah) list; private: MBBS Council list – seats change yearly, confirm in the KNRUHS seat matrix', official: 'knruhs.telangana.gov.in, mcc.nic.in' },
  { id: 'nursing', name: { en: 'Nursing colleges', te: 'నర్సింగ్ కాలేజీలు' }, rows: parse(NURSING), cols: ['college', 'place', 'district', 'type'],
    intro: { en: 'B.Sc Nursing admission is through TG EAPCET (BiPC) and KNRUHS counselling. Government nursing colleges are attached to government medical colleges – see the KNRUHS seat matrix for the latest list.', te: 'B.Sc నర్సింగ్ ప్రవేశం TG EAPCET (BiPC), KNRUHS కౌన్సెలింగ్ ద్వారా. ప్రభుత్వ నర్సింగ్ కాలేజీలు ప్రభుత్వ మెడికల్ కాలేజీలకు అనుబంధంగా ఉంటాయి – తాజా జాబితాకు KNRUHS సీట్ మ్యాట్రిక్స్ చూడండి.' },
    source: 'Careers360 B.Sc Nursing list (private) + NIMS', official: 'knruhs.telangana.gov.in' },
  { id: 'agri', name: { en: 'Agriculture, Veterinary & allied', te: 'వ్యవసాయ, పశువైద్య & అనుబంధ' }, rows: parse(AGRI), cols: ['college', 'place', 'district', 'type', 'course'],
    intro: { en: 'Government colleges of PJTSAU (agriculture), SKLTGHU (horticulture) and PVNRTVU (veterinary, dairy, fisheries). Admission through TG EAPCET (Agriculture & Pharmacy stream).', te: 'PJTSAU (వ్యవసాయం), SKLTGHU (ఉద్యానవనం), PVNRTVU (పశువైద్యం, డెయిరీ, మత్స్య) ప్రభుత్వ కాలేజీలు. TG EAPCET (అగ్రికల్చర్ & ఫార్మసీ) ద్వారా ప్రవేశం.' },
    source: 'PJTSAU (Wikipedia), SKLTGHU (Wikipedia), PVNRTVU official site', official: 'pjtsau.edu.in, skltghu.ac.in, pvnrtvu.ac.in' },
  { id: 'polytechnic', name: { en: 'Government polytechnics', te: 'ప్రభుత్వ పాలిటెక్నిక్‌లు' }, rows: parse(POLY), cols: ['college', 'place', 'district', 'type'],
    intro: { en: 'Major government polytechnics. More than 130 government and private polytechnics take TG POLYCET – the full list with codes is on the POLYCET counselling site.', te: 'ప్రధాన ప్రభుత్వ పాలిటెక్నిక్‌లు. 130కి పైగా ప్రభుత్వ, ప్రైవేట్ పాలిటెక్నిక్‌లు TG POLYCET ద్వారా ప్రవేశం ఇస్తాయి – కోడ్‌లతో పూర్తి జాబితా POLYCET కౌన్సెలింగ్ సైట్‌లో ఉంది.' },
    source: 'TG POLYCET participating colleges (IndCareer list, government only)', official: 'tgpolycet.nic.in, sbtet.telangana.gov.in' },
]

export const COL_LABEL = {
  school: { en: 'School / society', te: 'పాఠశాల / సొసైటీ' }, college: { en: 'College', te: 'కాలేజీ' }, place: { en: 'Town / area', te: 'పట్టణం / ప్రాంతం' },
  district: { en: 'District', te: 'జిల్లా' }, type: { en: 'Type', te: 'రకం' }, status: { en: 'Status', te: 'స్థితి' }, notes: { en: 'Notes', te: 'వివరాలు' },
  seats: { en: 'MBBS seats', te: 'MBBS సీట్లు' }, course: { en: 'Course', te: 'కోర్సు' },
}
