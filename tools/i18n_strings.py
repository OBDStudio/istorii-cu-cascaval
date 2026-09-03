# -*- coding: utf-8 -*-
"""Russian and English copy, keyed by the Romanian original.

Conventions agreed with the client:

  * The brand name stays in Latin — "Istorii cu Cașcaval" — in every language.
    The logo is a Latin wordmark and the social handles are Latin, so the brand
    reads as one identity rather than two.
  * Russian addresses the reader with formal «вы», which is what investor-facing
    copy uses; the Romanian original's informal "tu" would read as flippant to
    this audience.
  * Moldovan and Romanian place names take their standard Russian exonyms
    (Кишинёв, Унгень, Яссы) and street names are transliterated, because that is
    how a Russian speaker in Chișinău would read an address. English keeps the
    local spellings, which are the accepted English forms.
  * Personal names, social networks, e-mail, "ROI" and "break-even" pass through
    untouched in both languages.

Anything not listed here is reported by build_i18n.py as an untranslated string,
so this file is complete by construction rather than by hope.
"""

# Strings that are identical in every language and must not be flagged as
# missing: proper nouns, brand names and network names.
PASSTHROUGH = [
    'Istorii cu Cașcaval', 'ROI', 'break-even', 'Nightstar',
    'Facebook', 'Instagram', 'TikTok', 'WhatsApp',
    'business@cheesefranchise.com', '404',
    'Cristina Rusu', 'Andrei Munteanu', 'Sergiu Cebotari', 'Mihai Vieru',
    'Ana Bejan', 'Victoria Cojocaru', 'Elena Ceban', 'Ion Țurcanu',
    'Alexandru Lungu',
]

# ---------------------------------------------------------------- RUSSIAN

RU = {
    # -- hero / meta
    'Istorii cu Cașcaval — Devină francizor':
        'Istorii cu Cașcaval — стать франчайзи',
    'Istorii cu Cașcaval este una dintre puținele francize din regiune care combină un segment premium, concurență redusă și o experiență de cumpărare greu de replicat.':
        'Istorii cu Cașcaval — одна из немногих франшиз в регионе, которая сочетает премиальный сегмент, низкую конкуренцию и покупательский опыт, который трудно повторить.',
    'Investește într-un concept premium care deja funcționează':
        'Инвестируйте в премиальный концепт, который уже работает',
    'Devină francizor': 'Стать франчайзи',
    'Ro': 'Ru',
    'Română': 'Русский',

    # -- pillars
    'Business': 'Бизнес',
    'Model operațional validat': 'Проверенная операционная модель',
    'Oportunitate': 'Возможность',
    'Piață în creștere': 'Растущий рынок',
    'Recuperare estimată în aproximativ 14 luni':
        'Окупаемость примерно за 14 месяцев',
    'Suport': 'Поддержка',
    'Suport complet de la deschidere până la scalare':
        'Полное сопровождение от открытия до масштабирования',

    # -- why
    'De ce investitorii aleg Istorii cu Cașcaval':
        'Почему инвесторы выбирают Istorii cu Cașcaval',
    'Vinzi un produs pe care oamenii îl caută deja':
        'Вы продаёте продукт, который люди уже ищут',
    'Brânzeturile premium nu sunt o modă.': 'Премиальные сыры — не мода.',
    'Sunt parte dintr-un trend de consum orientat spre calitate, experiență și produse autentice.':
        'Это часть потребительского тренда на качество, впечатления и аутентичные продукты.',
    'Clienții cumpără pentru consum zilnic, cadouri, evenimente și experiențe gastronomice.':
        'Клиенты покупают для повседневного потребления, подарков, мероприятий и гастрономических впечатлений.',
    'Asta înseamnă trafic constant și oportunități multiple de vânzare.':
        'Это означает постоянный трафик и множество возможностей для продаж.',
    'Intri într-o categorie cu concurență limitată':
        'Вы входите в категорию с ограниченной конкуренцией',
    'Toată lumea deschide cafenelele': 'Все открывают кофейни',
    'Toată lumea deschide restaurante': 'Все открывают рестораны',
    'Aici apare avantajul.': 'Здесь и появляется преимущество.',
    'Nu lupți pentru atenție într-o piață aglomerată.':
        'Вы не боретесь за внимание на переполненном рынке.',
    'Construiești o destinație.': 'Вы создаёте место притяжения.',
    'Primești un model deja optimizat':
        'Вы получаете уже оптимизированную модель',
    'Am trecut deja prin etapele costisitoare…':
        'Мы уже прошли самые затратные этапы…',
    'Alegerea sortimentului': 'Подбор ассортимента',
    'Testarea locațiilor': 'Тестирование локаций',
    'Optimizarea marjelor': 'Оптимизация маржи',
    'Negocierea furnizorilor': 'Переговоры с поставщиками',
    'Construcția proceselor operaționale': 'Построение операционных процессов',
    'Tu pornești cu experiența acumulată, nu cu încercări și greșeli':
        'Вы начинаете с накопленным опытом, а не методом проб и ошибок',
    'Continuă scrolarea': 'Продолжайте прокручивать',

    # -- numbers
    'Cifrele care contează': 'Цифры, которые имеют значение',
    'Investiții inițiale': 'Первоначальные инвестиции',
    'Investiție totală estimativă': 'Оценочная сумма инвестиций',
    '1-2 luni': '1–2 месяца',
    'Prag de rentabilitate': 'Точка безубыточности',
    'Recuperarea investiției': 'Окупаемость инвестиций',
    '~14 luni': '~14 месяцев',
    'Profit lunar estimativ': 'Ожидаемая прибыль в месяц',
    'Lunar în primul an': 'В месяц в первый год',
    'Lunar din al doilea an': 'В месяц со второго года',
    'Lunar din al treilea an': 'В месяц с третьего года',

    # -- different
    'Ce face acest concept diferit?': 'Что делает этот концепт особенным?',
    'Ce face acest concept diferit': 'Что делает этот концепт особенным',
    # "Vindem" was folded into the kicker, so the sentence now runs on into
    # the cycling gold word beneath it and repeats the verb, as the Romanian
    # does: "…мы продаём" → "открытия".
    'Nu vindem doar brânzeturi, vindem': 'Мы продаём не только сыры, мы продаём',
    'descoperire': 'открытия',
    'recomandări': 'рекомендации',
    'experiențe': 'впечатления',
    'cadouri': 'подарки',
    'povești': 'истории',
    'De aceea modelul poate genera marje mai bune decât un magazin alimentar obișnuit.':
        'Поэтому модель способна давать более высокую маржу, чем обычный продуктовый магазин.',

    # -- benefits
    'Beneficiile brandului': 'Преимущества бренда',
    'Ce primești ca partener': 'Что вы получаете как партнёр',
    'Brand construit': 'Готовый бренд',
    'Furnizori validați': 'Проверенные поставщики',
    'Produse exclusive': 'Эксклюзивные продукты',
    'Design complet al locației': 'Полный дизайн локации',
    'Training pentru echipă': 'Обучение команды',
    'Strategie de marketing': 'Маркетинговая стратегия',
    'Consultanță operațională permanentă': 'Постоянная операционная поддержка',
    'Suport pentru dezvoltare și extindere': 'Поддержка развития и расширения',
    'Beneficiul anterior': 'Предыдущее преимущество',
    'Beneficiul următor': 'Следующее преимущество',

    # -- fit
    'Este această franciză potrivită pentru tine?': 'Подходит ли вам эта франшиза?',
    'Este această franciză potrivită pentru tine': 'Подходит ли вам эта франшиза',
    'Nu, dacă': 'Нет, если',
    'Cauți profit pasiv fără implicare':
        'Вы ищете пассивный доход без вовлечённости',
    'Vrei recuperarea investiției în câteva luni':
        'Вы хотите окупить инвестиции за несколько месяцев',
    'Nu poți respecta standardele brandului':
        'Вы не готовы соблюдать стандарты бренда',
    'Da, dacă': 'Да, если',
    'Vrei un business fizic cu produs premium':
        'Вы хотите офлайн-бизнес с премиальным продуктом',
    'Ai capital de investiție de la 45.000 EUR':
        'У вас есть инвестиционный капитал от 45 000 EUR',
    'Vrei să operezi activ sau să coordonezi un manager':
        'Вы готовы управлять лично или координировать управляющего',
    'Cauți o afacere pe termen lung': 'Вы ищете бизнес на долгий срок',

    # -- team
    'Echipa noastră': 'Наша команда',
    'Echipa care dezvoltă fiecare nouă istorie':
        'Команда, которая развивает каждую новую историю',
    'În spatele fiecărui magazin de succes se află o echipă dedicată, care crede în puterea unui parteneriat construit pe încredere, profesionalism și obiective comune. La Istorii cu Cașcaval, nu oferim doar un model de afacere, ci și experiența, cunoștințele și sprijinul unei echipe care îți este alături la fiecare etapă. De la primele planuri și până la dezvoltarea continuă a afacerii, lucrăm împreună pentru ca fiecare francizat să scrie propria poveste de succes.':
        'За каждым успешным магазином стоит преданная команда, которая верит в силу партнёрства, построенного на доверии, профессионализме и общих целях. В Istorii cu Cașcaval мы предлагаем не только бизнес-модель, но и опыт, знания и поддержку команды, которая рядом с вами на каждом этапе. От первых планов до постоянного развития бизнеса мы работаем вместе, чтобы каждый франчайзи написал свою собственную историю успеха.',
    'Manager Dezvoltare Francize': 'Менеджер по развитию франшизы',
    'Director Operațional': 'Операционный директор',
    'Fondator &amp; CEO': 'Основатель и CEO',
    'Director Comercial': 'Коммерческий директор',
    'Manager Marketing': 'Менеджер по маркетингу',
    'Manager Relații cu Partenerii': 'Менеджер по работе с партнёрами',
    'Specialist Suport Francizați': 'Специалист поддержки франчайзи',
    'Director Financiar': 'Финансовый директор',
    'Manager Expansiune': 'Менеджер по расширению',

    # -- locations
    'Locațiile noastre': 'Наши локации',
    'Următoarea locație poate fi în orașul tău':
        'Следующая локация может открыться в вашем городе',
    'Astăzi suntem prezenți în Chișinău, Ungheni, Iași și Suceava.':
        'Сегодня мы представлены в Кишинёве, Унгенах, Яссах и Сучаве.',
    'Mâine putem deschide împreună în Bălți, București, Cluj-Napoca, Timișoara, Brașov, Constanța sau în alte orașe cu potențial ridicat.':
        'Завтра мы можем вместе открыться в Бельцах, Бухаресте, Клуж-Напоке, Тимишоаре, Брашове, Констанце или в других городах с высоким потенциалом.',
    'Chișinău, sect. Centru': 'Кишинёв, сект. Центру',
    'str. Alexandru cel Bun 83': 'ул. Александру чел Бун 83',
    'Luni - Duminică 09:00 - 21:00': 'Пн – Вс 09:00 – 21:00',
    'Chișinău, Centru': 'Кишинёв, Центру',
    'str. Kogălniceanu 62': 'ул. Когэлничану 62',
    'Luni - Duminică 08:00 - 21:00': 'Пн – Вс 08:00 – 21:00',
    'Suceava, Iulius Mall': 'Сучава, Iulius Mall',
    'str. Calea Unirii 22': 'ул. Каля Унирий 22',
    'Chișinău, Port Mall': 'Кишинёв, Port Mall',
    'str. Mihail Sadoveanu 42/6': 'ул. Михаил Садовяну 42/6',
    'Luni - Duminică 10:00 - 22:00': 'Пн – Вс 10:00 – 22:00',
    'Stăuceni': 'Стэучень',
    'str. Mateevici 2/1': 'ул. Матеевич 2/1',
    'România, Iași, Palas Mall': 'Румыния, Яссы, Palas Mall',
    'str. Palas 7A': 'ул. Палас 7A',
    'Ungheni': 'Унгень',
    'Iași': 'Яссы',
    'Suceava': 'Сучава',
    'Chișinău': 'Кишинёв',
    'Chișinău, Oasis Mall': 'Кишинёв, Oasis Mall',
    'str. Bogdan Voievod 1': 'ул. Богдан Воевод 1',
    'Luni - Duminică 10:00 - 21:00': 'Пн – Вс 10:00 – 21:00',
    'Chișinău, Shopping MallDova': 'Кишинёв, Shopping MallDova',
    'str. Arborilor 21': 'ул. Арборилор 21',
    'str. Vasile Lupu 3': 'ул. Василе Лупу 3',
    'Luni - Duminică 09:00 - 20:00': 'Пн – Вс 09:00 – 20:00',
    'str. Grenoble 120/10': 'ул. Гренобль 120/10',
    'Nu cumperi doar o franciză.': 'Вы покупаете не просто франшизу.',
    'Primești un model de business construit, testat și optimizat, astfel încât să poți începe cu mai multă claritate, mai puține riscuri și șanse reale de creștere.':
        'Вы получаете построенную, протестированную и оптимизированную бизнес-модель, чтобы начать с большей ясностью, меньшими рисками и реальными шансами на рост.',
    'Completează formularul și discutăm despre oportunitățile disponibile.':
        'Заполните форму, и мы обсудим доступные возможности.',
    'Harta locațiilor Istorii cu Cașcaval în Moldova și România':
        'Карта локаций Istorii cu Cașcaval в Молдове и Румынии',
    'Ungheni — 1 magazin. Vezi pe Google Maps':
        'Унгень — 1 магазин. Посмотреть на Google Maps',
    'Iași — 1 magazin. Vezi pe Google Maps':
        'Яссы — 1 магазин. Посмотреть на Google Maps',
    'Suceava — 1 magazin. Vezi pe Google Maps':
        'Сучава — 1 магазин. Посмотреть на Google Maps',
    'Chișinău — 7 magazine. Vezi pe Google Maps':
        'Кишинёв — 7 магазинов. Посмотреть на Google Maps',

    # -- footer
    'Adresa juridică': 'Юридический адрес',
    'mun. Chișinău': 'мун. Кишинёв',
    'strada Melestiu, 26/9': 'улица Мелестиу, 26/9',
    'Rețele de socializare': 'Социальные сети',
    'Programe și Cursuri': 'Программы и курсы',
    'Termeni și condiții': 'Условия использования',
    'Politica de confidențialitate': 'Политика конфиденциальности',
    'Politica de cookie': 'Политика использования cookie',
    '2026 © Drepturile rezervate de către compania ISTORII CU CASCAVAL SRL':
        '2026 © Все права защищены компанией ISTORII CU CASCAVAL SRL',
    'Design elaborat de': 'Дизайн разработан',

    # -- modal / form
    'Numele și prenumele': 'Имя и фамилия',
    'Te rugăm să îți scrii numele.': 'Пожалуйста, укажите ваше имя.',
    'Adresa electronică': 'Электронная почта',
    'Te rugăm să introduci o adresă de email validă.':
        'Пожалуйста, введите корректный адрес электронной почты.',
    'Numărul de telefon': 'Номер телефона',
    'Te rugăm să introduci un număr de telefon.':
        'Пожалуйста, введите номер телефона.',
    'Orașul': 'Город',
    'Te rugăm să introduci orașul.': 'Пожалуйста, укажите город.',
    'Transmite solicitarea': 'Отправить заявку',
    'Închide formularul': 'Закрыть форму',
    'Termenii și condițiile': 'Условиями использования',

    # -- alt text / aria
    'Istorii cu Cașcaval — pagina principală': 'Istorii cu Cașcaval — главная страница',
    'Alege limba': 'Выберите язык',
    'Derulează mai jos': 'Прокрутите вниз',
    'De ce Istorii cu Cașcaval': 'Почему Istorii cu Cașcaval',
    'Angajată tăind cașcaval în magazin': 'Сотрудница нарезает кашкавал в магазине',
    'Clienți ciocnind pahare la o degustare': 'Гости чокаются бокалами на дегустации',
    'Vânzătoare servind un client în magazin': 'Продавец обслуживает клиента в магазине',
    'Angajată aranjând produse pe raft': 'Сотрудница раскладывает продукты на полке',
    'Angajată pregătind cașcaval în magazin': 'Сотрудница готовит кашкавал в магазине',
    'Clienți la o degustare în aer liber': 'Гости на дегустации под открытым небом',

    # -- 404 / success
    'Pagina nu a fost găsită': 'Страница не найдена',
    'Pagina nu a fost găsită — Istorii cu Cașcaval':
        'Страница не найдена — Istorii cu Cașcaval',
    'Pagina principală': 'На главную',
    'Pagina căutată nu a fost găsită.': 'Запрашиваемая страница не найдена.',
    'Datele Dvs. au fost recepționate.': 'Ваши данные получены.',
    'Solicitare trimisă — Istorii cu Cașcaval': 'Заявка отправлена — Istorii cu Cașcaval',
    'În curând veți fi contactat pentru o discuție despre oportunitatea de a deveni partenerul Istorii cu cașcaval.':
        'Скоро мы свяжемся с вами, чтобы обсудить возможность стать партнёром Istorii cu Cașcaval.',
    'Solicitarea ta a fost recepționată. Te vom contacta în curând.':
        'Ваша заявка получена. Мы свяжемся с вами в ближайшее время.',

    # -- terms
    'Termeni și condiții — Istorii cu Cașcaval': 'Условия использования — Istorii cu Cașcaval',
    'Termenii și condițiile de utilizare a website-ului Istorii cu Cașcaval.':
        'Условия использования сайта Istorii cu Cașcaval.',
    'Ultima actualizare: 15 august 2026': 'Последнее обновление: 15 августа 2026 г.',
    'Bine ai venit pe website-ul Istorii cu Cașcaval. Prin accesarea și utilizarea acestui website, confirmi că ai citit, înțeles și accepți prezentele Termeni și Condiții.':
        'Добро пожаловать на сайт Istorii cu Cașcaval. Заходя на этот сайт и используя его, вы подтверждаете, что прочитали, поняли и принимаете настоящие Условия использования.',
    'Te rugăm să citești cu atenție informațiile de mai jos înainte de utilizarea website-ului sau transmiterea unei solicitări privind franciza Istorii cu Cașcaval.':
        'Пожалуйста, внимательно прочитайте приведённую ниже информацию перед использованием сайта или отправкой заявки на франшизу Istorii cu Cașcaval.',
    'Informații generale': 'Общая информация',
    'Website-ul Istorii cu Cașcaval este administrat de:':
        'Сайт Istorii cu Cașcaval администрируется:',
    'Denumirea juridică: [DENUMIREA COMPANIEI]': 'Юридическое наименование: [DENUMIREA COMPANIEI]',
    'IDNO: [IDNO]': 'IDNO: [IDNO]',
    'Sediul juridic: [ADRESA]': 'Юридический адрес: [ADRESA]',
    'E-mail: [E-MAIL]': 'E-mail: [E-MAIL]',
    'Telefon: [TELEFON]': 'Телефон: [TELEFON]',
    'În continuare, compania poate fi denumită „Istorii cu Cașcaval”, „Compania”, „noi” sau „nouă”.':
        'Далее компания может именоваться «Istorii cu Cașcaval», «Компания», «мы» или «нам».',
    'Website-ul are rolul de a prezenta brandul Istorii cu Cașcaval, activitatea companiei, produsele, locațiile existente și oportunitățile de colaborare prin sistemul de franciză.':
        'Сайт предназначен для представления бренда Istorii cu Cașcaval, деятельности компании, продукции, действующих локаций и возможностей сотрудничества по системе франчайзинга.',
    'Utilizarea website-ului': 'Использование сайта',
    'Website-ul poate fi utilizat pentru:': 'Сайт может использоваться для:',
    'informarea despre brandul Istorii cu Cașcaval;':
        'получения информации о бренде Istorii cu Cașcaval;',
    'prezentarea conceptului de franciză;': 'ознакомления с концепцией франшизы;',
    'consultarea informațiilor orientative privind investiția și modelul de business;':
        'ознакомления с ориентировочной информацией об инвестициях и бизнес-модели;',
    'identificarea locațiilor și serviciilor disponibile;':
        'поиска доступных локаций и услуг;',
    'transmiterea unei solicitări pentru obținerea mai multor informații;':
        'отправки заявки для получения дополнительной информации;',
    'inițierea unei discuții privind posibilitatea deschiderii unei francize.':
        'начала обсуждения возможности открытия франшизы.',
    'Utilizatorul se obligă să folosească website-ul într-un mod legal și să nu întreprindă acțiuni care ar putea afecta funcționarea, securitatea sau disponibilitatea acestuia.':
        'Пользователь обязуется использовать сайт законным образом и не предпринимать действий, которые могут повлиять на его работу, безопасность или доступность.',
    'Informațiile despre franciză': 'Информация о франшизе',
    'Informațiile prezentate pe website cu privire la franciza Istorii cu Cașcaval au caracter general și informativ.':
        'Информация о франшизе Istorii cu Cașcaval, представленная на сайте, носит общий и информационный характер.',
    'Transmiterea unui formular, solicitarea unei prezentări sau purtarea unor discuții cu reprezentanții companiei nu reprezintă acceptarea automată a unei persoane în rețeaua de franciză și nu creează obligația companiei de a încheia un contract de franciză.':
        'Отправка формы, запрос презентации или переговоры с представителями компании не означают автоматического принятия лица во франчайзинговую сеть и не создают для компании обязательства заключить договор франчайзинга.',
    'Fiecare solicitare poate fi analizată individual, luând în considerare criterii precum locația propusă, disponibilitatea teritorială, capacitatea investițională, compatibilitatea cu modelul de business și alte criterii stabilite de companie.':
        'Каждая заявка может рассматриваться индивидуально с учётом таких критериев, как предлагаемая локация, территориальная доступность, инвестиционные возможности, соответствие бизнес-модели и иные критерии, установленные компанией.',
    'Condițiile finale ale colaborării vor fi stabilite exclusiv prin documentele și contractul de franciză semnate de părți.':
        'Окончательные условия сотрудничества устанавливаются исключительно документами и договором франчайзинга, подписанными сторонами.',
    'Investiții și informații financiare': 'Инвестиции и финансовая информация',
    'Valorile privind investiția inițială, costurile operaționale, cifra de afaceri, perioada estimată de recuperare a investiției, marjele sau profitul prezentate pe website sunt, dacă nu este specificat expres altfel, valori orientative. Rezultatele efective ale unei francize pot varia în funcție de numeroși factori, inclusiv:':
        'Показатели первоначальных инвестиций, операционных расходов, оборота, предполагаемого срока окупаемости, маржи или прибыли, представленные на сайте, являются ориентировочными, если прямо не указано иное. Фактические результаты франшизы могут различаться в зависимости от множества факторов, в том числе:',
    'orașul și locația magazinului;': 'города и расположения магазина;',
    'traficul și profilul clienților;': 'трафика и профиля клиентов;',
    'nivelul investiției;': 'объёма инвестиций;',
    'costurile de chirie și personal;': 'расходов на аренду и персонал;',
    'managementul afacerii;': 'управления бизнесом;',
    'condițiile economice și concurența locală;':
        'экономических условий и местной конкуренции;',
    'sezonalitatea;': 'сезонности;',
    'performanța echipei și implicarea francizatului.':
        'работы команды и вовлечённости франчайзи.',
    'Istorii cu Cașcaval nu garantează un anumit nivel al vânzărilor, veniturilor sau profitului.':
        'Istorii cu Cașcaval не гарантирует определённого уровня продаж, выручки или прибыли.',
    'Orice proiecție financiară trebuie analizată individual înainte de luarea unei decizii de investiție.':
        'Любые финансовые прогнозы должны анализироваться индивидуально до принятия инвестиционного решения.',
    'Solicitarea unei francize': 'Заявка на франшизу',
    'Persoanele interesate pot transmite o solicitare prin intermediul formularului disponibil pe website. Prin completarea formularului, utilizatorul declară că informațiile furnizate sunt corecte și actuale. După primirea solicitării, echipa Istorii cu Cașcaval poate contacta persoana interesată pentru:':
        'Заинтересованные лица могут отправить заявку через форму, доступную на сайте. Заполняя форму, пользователь подтверждает, что предоставленные сведения верны и актуальны. После получения заявки команда Istorii cu Cașcaval может связаться с заинтересованным лицом для:',
    'o discuție inițială;': 'первичного обсуждения;',
    'prezentarea conceptului;': 'презентации концепции;',
    'analiza orașului sau a locației propuse;':
        'анализа предлагаемого города или локации;',
    'prezentarea modelului de colaborare;': 'представления модели сотрудничества;',
    'stabilirea următoarelor etape ale procesului.':
        'определения дальнейших этапов процесса.',
    'Compania își rezervă dreptul de a accepta sau refuza continuarea procesului de selecție a unui potențial francizat.':
        'Компания оставляет за собой право принять или отклонить продолжение процесса отбора потенциального франчайзи.',
    'Produse și informații prezentate': 'Продукция и представленная информация',
    'Fotografiile, descrierile, sortimentele și alte informații despre produsele Istorii cu Cașcaval sunt prezentate în scop informativ. Disponibilitatea produselor poate varia în funcție de locație, sezon, furnizori și stocurile existente. Imaginile utilizate pe website pot avea caracter ilustrativ, iar aspectul produselor poate prezenta diferențe față de imaginile afișate.':
        'Фотографии, описания, ассортимент и иная информация о продукции Istorii cu Cașcaval представлены в информационных целях. Наличие продукции может различаться в зависимости от локации, сезона, поставщиков и имеющихся запасов. Изображения на сайте могут носить иллюстративный характер, а внешний вид продукции может отличаться от показанного.',
    'Proprietate intelectuală': 'Интеллектуальная собственность',
    'Conținutul website-ului, inclusiv, fără a se limita la:':
        'Содержимое сайта, включая, помимо прочего:',
    'denumirea Istorii cu Cașcaval;': 'наименование Istorii cu Cașcaval;',
    'logo-ul și elementele de identitate vizuală;':
        'логотип и элементы визуальной идентичности;',
    'texte;': 'тексты;',
    'fotografii și materiale video;': 'фотографии и видеоматериалы;',
    'elemente grafice;': 'графические элементы;',
    'designul website-ului;': 'дизайн сайта;',
    'materiale de prezentare;': 'презентационные материалы;',
    'concepte și materiale comerciale;': 'концепции и коммерческие материалы;',
    'este protejat de legislația aplicabilă privind drepturile de autor, mărcile și proprietatea intelectuală. Copierea, reproducerea, distribuirea, modificarea sau utilizarea comercială a acestor materiale fără acordul prealabil al titularului drepturilor este interzisă.':
        'защищено применимым законодательством об авторском праве, товарных знаках и интеллектуальной собственности. Копирование, воспроизведение, распространение, изменение или коммерческое использование этих материалов без предварительного согласия правообладателя запрещено.',
    'Marca Istorii cu Cașcaval': 'Товарный знак Istorii cu Cașcaval',
    'Accesarea website-ului sau transmiterea unei solicitări de franciză nu oferă utilizatorului niciun drept de utilizare a denumirii, logo-ului, identității vizuale sau altor elemente aparținând brandului Istorii cu Cașcaval. Dreptul de utilizare a mărcii de către un francizat va fi acordat numai în condițiile stabilite prin contractul de franciză.':
        'Посещение сайта или отправка заявки на франшизу не даёт пользователю никаких прав на использование наименования, логотипа, визуальной идентичности или иных элементов, принадлежащих бренду Istorii cu Cașcaval. Право использования товарного знака предоставляется франчайзи только на условиях, установленных договором франчайзинга.',
    'Limitarea răspunderii': 'Ограничение ответственности',
    'Depunem eforturi pentru ca informațiile publicate pe website să fie actuale și corecte. Cu toate acestea, pot exista erori, omisiuni sau informații care necesită actualizare. Compania își rezervă dreptul de a modifica informațiile privind produsele, locațiile, conceptul de franciză, investițiile orientative și condițiile de colaborare fără obligația unei notificări prealabile, în limitele permise de lege. Deciziile de investiție nu trebuie luate exclusiv pe baza informațiilor generale publicate pe website.':
        'Мы прилагаем усилия, чтобы информация на сайте была актуальной и корректной. Тем не менее возможны ошибки, упущения или сведения, требующие обновления. Компания оставляет за собой право изменять информацию о продукции, локациях, концепции франшизы, ориентировочных инвестициях и условиях сотрудничества без обязательства предварительного уведомления, в пределах, допускаемых законом. Инвестиционные решения не должны приниматься исключительно на основании общей информации, опубликованной на сайте.',
    'Protecția datelor cu caracter personal': 'Защита персональных данных',
    'Datele transmise prin formularele website-ului pot include numele, numărul de telefon, adresa de e-mail, localitatea și alte informații necesare pentru procesarea solicitării. Aceste date vor fi utilizate pentru comunicarea cu persoana interesată, analiza solicitării și, după caz, desfășurarea procesului de selecție pentru franciză. Mai multe informații despre modul în care sunt colectate și utilizate datele personale sunt disponibile în secțiunile de mai jos din prezentul document.':
        'Данные, передаваемые через формы сайта, могут включать имя, номер телефона, адрес электронной почты, населённый пункт и иные сведения, необходимые для обработки заявки. Эти данные используются для связи с заинтересованным лицом, рассмотрения заявки и, при необходимости, проведения отбора франчайзи. Дополнительная информация о том, как собираются и используются персональные данные, приведена в разделах ниже настоящего документа.',
    'Cookie-uri': 'Файлы cookie',
    'Website-ul poate utiliza cookie-uri și tehnologii similare pentru funcționarea corectă a paginilor, analizarea traficului și îmbunătățirea experienței utilizatorilor. Informații suplimentare sunt disponibile în prezentul document.':
        'Сайт может использовать файлы cookie и аналогичные технологии для корректной работы страниц, анализа трафика и улучшения пользовательского опыта. Дополнительная информация приведена в настоящем документе.',
    'Link-uri către website-uri externe': 'Ссылки на внешние сайты',
    'Website-ul poate conține link-uri către platforme sau website-uri administrate de terți. Istorii cu Cașcaval nu controlează și nu își asumă responsabilitatea pentru conținutul, disponibilitatea, securitatea sau politicile acestor website-uri externe.':
        'Сайт может содержать ссылки на платформы или сайты, управляемые третьими лицами. Istorii cu Cașcaval не контролирует и не несёт ответственности за содержание, доступность, безопасность или политику таких внешних сайтов.',
    'Disponibilitatea website-ului': 'Доступность сайта',
    'Nu garantăm funcționarea permanentă și fără întreruperi a website-ului. Accesul poate fi temporar suspendat pentru mentenanță, actualizări, probleme tehnice sau din alte motive independente de companie.':
        'Мы не гарантируем постоянную и бесперебойную работу сайта. Доступ может быть временно приостановлен для обслуживания, обновлений, по техническим причинам или иным обстоятельствам, не зависящим от компании.',
    'Modificarea Termenilor și Condițiilor': 'Изменение Условий использования',
    'Istorii cu Cașcaval își rezervă dreptul de a actualiza prezentele Termeni și Condiții atunci când este necesar. Versiunea actualizată va fi publicată pe această pagină, împreună cu data ultimei actualizări. Continuarea utilizării website-ului după publicarea modificărilor presupune aplicarea versiunii în vigoare a Termenilor și Condițiilor.':
        'Istorii cu Cașcaval оставляет за собой право обновлять настоящие Условия использования при необходимости. Обновлённая версия публикуется на этой странице с указанием даты последнего обновления. Продолжение использования сайта после публикации изменений означает применение действующей редакции Условий использования.',
    'Legislația aplicabilă': 'Применимое законодательство',
    'Prezentele Termeni și Condiții sunt guvernate de legislația Republicii Moldova, în măsura în care aceasta este aplicabilă companiei și serviciilor prezentate. Eventualele neînțelegeri vor fi soluționate, în primul rând, pe cale amiabilă, iar atunci când acest lucru nu este posibil, de către autoritățile sau instanțele competente conform legislației aplicabile.':
        'Настоящие Условия использования регулируются законодательством Республики Молдова в той мере, в какой оно применимо к компании и представленным услугам. Возможные разногласия разрешаются в первую очередь путём переговоров, а если это невозможно — компетентными органами или судами в соответствии с применимым законодательством.',
    'Contact': 'Контакты',
    'Pentru întrebări referitoare la website, franciză sau prezentele Termeni și Condiții, ne poți contacta la:':
        'По вопросам, касающимся сайта, франшизы или настоящих Условий использования, вы можете связаться с нами:',
    'Adresă: [ADRESA]': 'Адрес: [ADRESA]',
}

# Inline-markup sentences. Word order differs between languages, so these are
# swapped as whole HTML fragments rather than node by node.
RU_BLOCKS = {
    'Asta <strong>creează loialitate</strong> și <strong>valoare</strong> mai mare per client.':
        'Это <strong>формирует лояльность</strong> и повышает <strong>ценность</strong> каждого клиента.',
    'Considerăm că ești de-acord cu <a href="termeni-si-conditii.html">Termenii și condițiile</a> accesând butonul “Devină francizor”':
        'Нажимая кнопку «Стать франчайзи», вы соглашаетесь с <a href="terms.html">Условиями использования</a>',
}


# ---------------------------------------------------------------- ENGLISH

EN = {
    'Istorii cu Cașcaval — Devină francizor': 'Istorii cu Cașcaval — Become a Franchisee',
    'Istorii cu Cașcaval este una dintre puținele francize din regiune care combină un segment premium, concurență redusă și o experiență de cumpărare greu de replicat.':
        'Istorii cu Cașcaval is one of the few franchises in the region that combines a premium segment, low competition and a shopping experience that is hard to replicate.',
    'Investește într-un concept premium care deja funcționează':
        'Invest in a premium concept that already works',
    'Devină francizor': 'Become a franchisee',
    'Ro': 'En',
    'Română': 'English',

    'Business': 'Business',
    'Model operațional validat': 'A proven operating model',
    'Oportunitate': 'Opportunity',
    'Piață în creștere': 'A growing market',
    'Recuperare estimată în aproximativ 14 luni':
        'Estimated payback in about 14 months',
    'Suport': 'Support',
    'Suport complet de la deschidere până la scalare':
        'Full support from opening to scaling',

    'De ce investitorii aleg Istorii cu Cașcaval':
        'Why investors choose Istorii cu Cașcaval',
    'Vinzi un produs pe care oamenii îl caută deja':
        'You sell a product people are already looking for',
    'Brânzeturile premium nu sunt o modă.': 'Premium cheese is not a fad.',
    'Sunt parte dintr-un trend de consum orientat spre calitate, experiență și produse autentice.':
        'It is part of a consumer shift towards quality, experience and authentic products.',
    'Clienții cumpără pentru consum zilnic, cadouri, evenimente și experiențe gastronomice.':
        'Customers buy for everyday eating, gifts, events and food experiences.',
    'Asta înseamnă trafic constant și oportunități multiple de vânzare.':
        'That means steady footfall and many different reasons to buy.',
    'Intri într-o categorie cu concurență limitată':
        'You enter a category with limited competition',
    'Toată lumea deschide cafenelele': 'Everyone is opening coffee shops',
    'Toată lumea deschide restaurante': 'Everyone is opening restaurants',
    'Aici apare avantajul.': 'That is where the advantage is.',
    'Nu lupți pentru atenție într-o piață aglomerată.':
        'You are not fighting for attention in a crowded market.',
    'Construiești o destinație.': 'You are building a destination.',
    'Primești un model deja optimizat': 'You get a model that is already optimised',
    'Am trecut deja prin etapele costisitoare…':
        'We have already been through the expensive stages…',
    'Alegerea sortimentului': 'Choosing the range',
    'Testarea locațiilor': 'Testing locations',
    'Optimizarea marjelor': 'Optimising margins',
    'Negocierea furnizorilor': 'Negotiating with suppliers',
    'Construcția proceselor operaționale': 'Building the operating processes',
    'Tu pornești cu experiența acumulată, nu cu încercări și greșeli':
        'You start with the experience already gained, not with trial and error',
    'Continuă scrolarea': 'Keep scrolling',

    'Cifrele care contează': 'The numbers that matter',
    'Investiții inițiale': 'Initial investment',
    'Investiție totală estimativă': 'Estimated total investment',
    '1-2 luni': '1–2 months',
    'Prag de rentabilitate': 'Break-even point',
    'Recuperarea investiției': 'Return on investment',
    '~14 luni': '~14 months',
    'Profit lunar estimativ': 'Estimated monthly profit',
    'Lunar în primul an': 'Per month in year one',
    'Lunar din al doilea an': 'Per month from year two',
    'Lunar din al treilea an': 'Per month from year three',

    'Ce face acest concept diferit?': 'What makes this concept different?',
    'Ce face acest concept diferit': 'What makes this concept different',
    'Nu vindem doar brânzeturi, vindem': 'We do not just sell cheese, we sell',
    'descoperire': 'discovery',
    'recomandări': 'recommendations',
    'experiențe': 'experiences',
    'cadouri': 'gifts',
    'povești': 'stories',
    'De aceea modelul poate genera marje mai bune decât un magazin alimentar obișnuit.':
        'That is why the model can deliver better margins than an ordinary food shop.',

    'Beneficiile brandului': 'Brand benefits',
    'Ce primești ca partener': 'What you get as a partner',
    'Brand construit': 'An established brand',
    'Furnizori validați': 'Vetted suppliers',
    'Produse exclusive': 'Exclusive products',
    'Design complet al locației': 'Complete store design',
    'Training pentru echipă': 'Team training',
    'Strategie de marketing': 'Marketing strategy',
    'Consultanță operațională permanentă': 'Ongoing operational guidance',
    'Suport pentru dezvoltare și extindere': 'Support for growth and expansion',
    'Beneficiul anterior': 'Previous benefit',
    'Beneficiul următor': 'Next benefit',

    'Este această franciză potrivită pentru tine?': 'Is this franchise right for you?',
    'Este această franciză potrivită pentru tine': 'Is this franchise right for you',
    'Nu, dacă': 'No, if',
    'Cauți profit pasiv fără implicare':
        'You are looking for passive income with no involvement',
    'Vrei recuperarea investiției în câteva luni':
        'You expect to recover your investment within a few months',
    'Nu poți respecta standardele brandului':
        'You cannot commit to the brand standards',
    'Da, dacă': 'Yes, if',
    'Vrei un business fizic cu produs premium':
        'You want a bricks-and-mortar business with a premium product',
    'Ai capital de investiție de la 45.000 EUR':
        'You have investment capital from EUR 45,000',
    'Vrei să operezi activ sau să coordonezi un manager':
        'You want to run it yourself or oversee a manager',
    'Cauți o afacere pe termen lung': 'You are looking for a long-term business',

    'Echipa noastră': 'Our team',
    'Echipa care dezvoltă fiecare nouă istorie':
        'The team behind every new story',
    'În spatele fiecărui magazin de succes se află o echipă dedicată, care crede în puterea unui parteneriat construit pe încredere, profesionalism și obiective comune. La Istorii cu Cașcaval, nu oferim doar un model de afacere, ci și experiența, cunoștințele și sprijinul unei echipe care îți este alături la fiecare etapă. De la primele planuri și până la dezvoltarea continuă a afacerii, lucrăm împreună pentru ca fiecare francizat să scrie propria poveste de succes.':
        'Behind every successful store is a dedicated team that believes in the power of a partnership built on trust, professionalism and shared goals. At Istorii cu Cașcaval we offer not only a business model, but the experience, knowledge and support of a team that stays with you at every stage. From the first plans through to the continued growth of the business, we work together so that every franchisee writes their own success story.',
    'Manager Dezvoltare Francize': 'Franchise Development Manager',
    'Director Operațional': 'Operations Director',
    'Fondator &amp; CEO': 'Founder &amp; CEO',
    'Director Comercial': 'Commercial Director',
    'Manager Marketing': 'Marketing Manager',
    'Manager Relații cu Partenerii': 'Partner Relations Manager',
    'Specialist Suport Francizați': 'Franchisee Support Specialist',
    'Director Financiar': 'Finance Director',
    'Manager Expansiune': 'Expansion Manager',

    'Locațiile noastre': 'Our locations',
    'Următoarea locație poate fi în orașul tău':
        'The next location could be in your city',
    'Astăzi suntem prezenți în Chișinău, Ungheni, Iași și Suceava.':
        'Today we are present in Chișinău, Ungheni, Iași and Suceava.',
    'Mâine putem deschide împreună în Bălți, București, Cluj-Napoca, Timișoara, Brașov, Constanța sau în alte orașe cu potențial ridicat.':
        'Tomorrow we could open together in Bălți, Bucharest, Cluj-Napoca, Timișoara, Brașov, Constanța or other cities with strong potential.',
    'Chișinău, sect. Centru': 'Chișinău, Centru district',
    'str. Alexandru cel Bun 83': '83 Alexandru cel Bun St.',
    'Luni - Duminică 09:00 - 21:00': 'Monday – Sunday 09:00 – 21:00',
    'Chișinău, Centru': 'Chișinău, Centru',
    'str. Kogălniceanu 62': '62 Kogălniceanu St.',
    'Luni - Duminică 08:00 - 21:00': 'Monday – Sunday 08:00 – 21:00',
    'Suceava, Iulius Mall': 'Suceava, Iulius Mall',
    'str. Calea Unirii 22': '22 Calea Unirii St.',
    'Chișinău, Port Mall': 'Chișinău, Port Mall',
    'str. Mihail Sadoveanu 42/6': '42/6 Mihail Sadoveanu St.',
    'Luni - Duminică 10:00 - 22:00': 'Monday – Sunday 10:00 – 22:00',
    'Stăuceni': 'Stăuceni',
    'str. Mateevici 2/1': '2/1 Mateevici St.',
    'România, Iași, Palas Mall': 'Romania, Iași, Palas Mall',
    'str. Palas 7A': '7A Palas St.',
    'Ungheni': 'Ungheni',
    'Iași': 'Iași',
    'Suceava': 'Suceava',
    'Chișinău': 'Chișinău',
    'Chișinău, Oasis Mall': 'Chișinău, Oasis Mall',
    'str. Bogdan Voievod 1': '1 Bogdan Voievod St.',
    'Luni - Duminică 10:00 - 21:00': 'Monday – Sunday 10:00 – 21:00',
    'Chișinău, Shopping MallDova': 'Chișinău, Shopping MallDova',
    'str. Arborilor 21': '21 Arborilor St.',
    'str. Vasile Lupu 3': '3 Vasile Lupu St.',
    'Luni - Duminică 09:00 - 20:00': 'Monday – Sunday 09:00 – 20:00',
    'str. Grenoble 120/10': '120/10 Grenoble St.',
    'Nu cumperi doar o franciză.': 'You are not just buying a franchise.',
    'Primești un model de business construit, testat și optimizat, astfel încât să poți începe cu mai multă claritate, mai puține riscuri și șanse reale de creștere.':
        'You get a business model that is built, tested and optimised, so you can start with more clarity, less risk and a real chance of growth.',
    'Completează formularul și discutăm despre oportunitățile disponibile.':
        'Fill in the form and we will talk through the opportunities available.',
    'Harta locațiilor Istorii cu Cașcaval în Moldova și România':
        'Map of Istorii cu Cașcaval locations in Moldova and Romania',
    'Ungheni — 1 magazin. Vezi pe Google Maps':
        'Ungheni — 1 store. View on Google Maps',
    'Iași — 1 magazin. Vezi pe Google Maps': 'Iași — 1 store. View on Google Maps',
    'Suceava — 1 magazin. Vezi pe Google Maps':
        'Suceava — 1 store. View on Google Maps',
    'Chișinău — 7 magazine. Vezi pe Google Maps':
        'Chișinău — 7 stores. View on Google Maps',

    'Adresa juridică': 'Registered address',
    'mun. Chișinău': 'Chișinău',
    'strada Melestiu, 26/9': '26/9 Melestiu Street',
    'Rețele de socializare': 'Social media',
    'Programe și Cursuri': 'Programmes and Courses',
    'Termeni și condiții': 'Terms and conditions',
    'Politica de confidențialitate': 'Privacy policy',
    'Politica de cookie': 'Cookie policy',
    '2026 © Drepturile rezervate de către compania ISTORII CU CASCAVAL SRL':
        '2026 © All rights reserved by ISTORII CU CASCAVAL SRL',
    'Design elaborat de': 'Design by',

    'Numele și prenumele': 'Full name',
    'Te rugăm să îți scrii numele.': 'Please enter your name.',
    'Adresa electronică': 'Email address',
    'Te rugăm să introduci o adresă de email validă.':
        'Please enter a valid email address.',
    'Numărul de telefon': 'Phone number',
    'Te rugăm să introduci un număr de telefon.': 'Please enter a phone number.',
    'Orașul': 'City',
    'Te rugăm să introduci orașul.': 'Please enter your city.',
    'Transmite solicitarea': 'Send request',
    'Închide formularul': 'Close the form',
    'Termenii și condițiile': 'Terms and Conditions',

    'Istorii cu Cașcaval — pagina principală': 'Istorii cu Cașcaval — home page',
    'Alege limba': 'Choose language',
    'Derulează mai jos': 'Scroll down',
    'De ce Istorii cu Cașcaval': 'Why Istorii cu Cașcaval',
    'Angajată tăind cașcaval în magazin': 'A shop assistant slicing cheese in store',
    'Clienți ciocnind pahare la o degustare': 'Guests raising glasses at a tasting',
    'Vânzătoare servind un client în magazin': 'A shop assistant serving a customer',
    'Angajată aranjând produse pe raft': 'A shop assistant arranging products on a shelf',
    'Angajată pregătind cașcaval în magazin': 'A shop assistant preparing cheese in store',
    'Clienți la o degustare în aer liber': 'Guests at an open-air tasting',

    'Pagina nu a fost găsită': 'Page not found',
    'Pagina nu a fost găsită — Istorii cu Cașcaval':
        'Page not found — Istorii cu Cașcaval',
    'Pagina principală': 'Back to home',
    'Pagina căutată nu a fost găsită.': 'The page you were looking for was not found.',
    'Datele Dvs. au fost recepționate.': 'We have received your details.',
    'Solicitare trimisă — Istorii cu Cașcaval':
        'Request sent — Istorii cu Cașcaval',
    'În curând veți fi contactat pentru o discuție despre oportunitatea de a deveni partenerul Istorii cu cașcaval.':
        'We will be in touch shortly to discuss the opportunity of becoming an Istorii cu Cașcaval partner.',
    'Solicitarea ta a fost recepționată. Te vom contacta în curând.':
        'Your request has been received. We will contact you shortly.',

    'Termeni și condiții — Istorii cu Cașcaval':
        'Terms and conditions — Istorii cu Cașcaval',
    'Termenii și condițiile de utilizare a website-ului Istorii cu Cașcaval.':
        'The terms and conditions for using the Istorii cu Cașcaval website.',
    'Ultima actualizare: 15 august 2026': 'Last updated: 15 August 2026',
    'Bine ai venit pe website-ul Istorii cu Cașcaval. Prin accesarea și utilizarea acestui website, confirmi că ai citit, înțeles și accepți prezentele Termeni și Condiții.':
        'Welcome to the Istorii cu Cașcaval website. By accessing and using this website, you confirm that you have read, understood and accept these Terms and Conditions.',
    'Te rugăm să citești cu atenție informațiile de mai jos înainte de utilizarea website-ului sau transmiterea unei solicitări privind franciza Istorii cu Cașcaval.':
        'Please read the information below carefully before using the website or submitting an enquiry about the Istorii cu Cașcaval franchise.',
    'Informații generale': 'General information',
    'Website-ul Istorii cu Cașcaval este administrat de:':
        'The Istorii cu Cașcaval website is operated by:',
    'Denumirea juridică: [DENUMIREA COMPANIEI]': 'Legal name: [DENUMIREA COMPANIEI]',
    'IDNO: [IDNO]': 'IDNO: [IDNO]',
    'Sediul juridic: [ADRESA]': 'Registered office: [ADRESA]',
    'E-mail: [E-MAIL]': 'Email: [E-MAIL]',
    'Telefon: [TELEFON]': 'Phone: [TELEFON]',
    'În continuare, compania poate fi denumită „Istorii cu Cașcaval”, „Compania”, „noi” sau „nouă”.':
        'The company may hereafter be referred to as “Istorii cu Cașcaval”, “the Company”, “we” or “us”.',
    'Website-ul are rolul de a prezenta brandul Istorii cu Cașcaval, activitatea companiei, produsele, locațiile existente și oportunitățile de colaborare prin sistemul de franciză.':
        'The website exists to present the Istorii cu Cașcaval brand, the company’s activity, its products, its existing locations and the opportunities to work together through the franchise system.',
    'Utilizarea website-ului': 'Use of the website',
    'Website-ul poate fi utilizat pentru:': 'The website may be used to:',
    'informarea despre brandul Istorii cu Cașcaval;':
        'learn about the Istorii cu Cașcaval brand;',
    'prezentarea conceptului de franciză;': 'review the franchise concept;',
    'consultarea informațiilor orientative privind investiția și modelul de business;':
        'consult indicative information about the investment and the business model;',
    'identificarea locațiilor și serviciilor disponibile;':
        'find available locations and services;',
    'transmiterea unei solicitări pentru obținerea mai multor informații;':
        'submit a request for further information;',
    'inițierea unei discuții privind posibilitatea deschiderii unei francize.':
        'start a conversation about opening a franchise.',
    'Utilizatorul se obligă să folosească website-ul într-un mod legal și să nu întreprindă acțiuni care ar putea afecta funcționarea, securitatea sau disponibilitatea acestuia.':
        'Users undertake to use the website lawfully and not to take any action that could affect its operation, security or availability.',
    'Informațiile despre franciză': 'Franchise information',
    'Informațiile prezentate pe website cu privire la franciza Istorii cu Cașcaval au caracter general și informativ.':
        'The information presented on the website about the Istorii cu Cașcaval franchise is general and for information purposes only.',
    'Transmiterea unui formular, solicitarea unei prezentări sau purtarea unor discuții cu reprezentanții companiei nu reprezintă acceptarea automată a unei persoane în rețeaua de franciză și nu creează obligația companiei de a încheia un contract de franciză.':
        'Submitting a form, requesting a presentation or holding discussions with company representatives does not constitute automatic acceptance into the franchise network, nor does it oblige the company to enter into a franchise agreement.',
    'Fiecare solicitare poate fi analizată individual, luând în considerare criterii precum locația propusă, disponibilitatea teritorială, capacitatea investițională, compatibilitatea cu modelul de business și alte criterii stabilite de companie.':
        'Each enquiry may be assessed individually, taking into account criteria such as the proposed location, territorial availability, investment capacity, fit with the business model and other criteria set by the company.',
    'Condițiile finale ale colaborării vor fi stabilite exclusiv prin documentele și contractul de franciză semnate de părți.':
        'The final terms of any collaboration will be established solely through the documents and the franchise agreement signed by the parties.',
    'Investiții și informații financiare': 'Investment and financial information',
    'Valorile privind investiția inițială, costurile operaționale, cifra de afaceri, perioada estimată de recuperare a investiției, marjele sau profitul prezentate pe website sunt, dacă nu este specificat expres altfel, valori orientative. Rezultatele efective ale unei francize pot varia în funcție de numeroși factori, inclusiv:':
        'Figures for initial investment, operating costs, turnover, estimated payback period, margins or profit shown on the website are indicative unless expressly stated otherwise. Actual franchise results may vary depending on many factors, including:',
    'orașul și locația magazinului;': 'the city and the store location;',
    'traficul și profilul clienților;': 'footfall and customer profile;',
    'nivelul investiției;': 'the level of investment;',
    'costurile de chirie și personal;': 'rent and staffing costs;',
    'managementul afacerii;': 'business management;',
    'condițiile economice și concurența locală;':
        'economic conditions and local competition;',
    'sezonalitatea;': 'seasonality;',
    'performanța echipei și implicarea francizatului.':
        'team performance and the franchisee’s involvement.',
    'Istorii cu Cașcaval nu garantează un anumit nivel al vânzărilor, veniturilor sau profitului.':
        'Istorii cu Cașcaval does not guarantee any particular level of sales, revenue or profit.',
    'Orice proiecție financiară trebuie analizată individual înainte de luarea unei decizii de investiție.':
        'Any financial projection should be assessed individually before an investment decision is made.',
    'Solicitarea unei francize': 'Applying for a franchise',
    'Persoanele interesate pot transmite o solicitare prin intermediul formularului disponibil pe website. Prin completarea formularului, utilizatorul declară că informațiile furnizate sunt corecte și actuale. După primirea solicitării, echipa Istorii cu Cașcaval poate contacta persoana interesată pentru:':
        'Interested parties may submit an enquiry through the form available on the website. By completing the form, the user confirms that the information provided is accurate and current. Once the enquiry is received, the Istorii cu Cașcaval team may make contact to arrange:',
    'o discuție inițială;': 'an initial conversation;',
    'prezentarea conceptului;': 'a presentation of the concept;',
    'analiza orașului sau a locației propuse;':
        'an assessment of the proposed city or location;',
    'prezentarea modelului de colaborare;': 'a presentation of the partnership model;',
    'stabilirea următoarelor etape ale procesului.':
        'agreement on the next steps in the process.',
    'Compania își rezervă dreptul de a accepta sau refuza continuarea procesului de selecție a unui potențial francizat.':
        'The company reserves the right to accept or decline to continue the selection process with a prospective franchisee.',
    'Produse și informații prezentate': 'Products and information shown',
    'Fotografiile, descrierile, sortimentele și alte informații despre produsele Istorii cu Cașcaval sunt prezentate în scop informativ. Disponibilitatea produselor poate varia în funcție de locație, sezon, furnizori și stocurile existente. Imaginile utilizate pe website pot avea caracter ilustrativ, iar aspectul produselor poate prezenta diferențe față de imaginile afișate.':
        'Photographs, descriptions, product ranges and other information about Istorii cu Cașcaval products are provided for information purposes. Product availability may vary by location, season, supplier and current stock. Images used on the website may be illustrative, and products may differ in appearance from the images shown.',
    'Proprietate intelectuală': 'Intellectual property',
    'Conținutul website-ului, inclusiv, fără a se limita la:':
        'The content of the website, including but not limited to:',
    'denumirea Istorii cu Cașcaval;': 'the Istorii cu Cașcaval name;',
    'logo-ul și elementele de identitate vizuală;':
        'the logo and visual identity elements;',
    'texte;': 'text;',
    'fotografii și materiale video;': 'photographs and video material;',
    'elemente grafice;': 'graphic elements;',
    'designul website-ului;': 'the website design;',
    'materiale de prezentare;': 'presentation materials;',
    'concepte și materiale comerciale;': 'commercial concepts and materials;',
    'este protejat de legislația aplicabilă privind drepturile de autor, mărcile și proprietatea intelectuală. Copierea, reproducerea, distribuirea, modificarea sau utilizarea comercială a acestor materiale fără acordul prealabil al titularului drepturilor este interzisă.':
        'is protected by applicable copyright, trade mark and intellectual property law. Copying, reproducing, distributing, modifying or commercially exploiting this material without the prior consent of the rights holder is prohibited.',
    'Marca Istorii cu Cașcaval': 'The Istorii cu Cașcaval trade mark',
    'Accesarea website-ului sau transmiterea unei solicitări de franciză nu oferă utilizatorului niciun drept de utilizare a denumirii, logo-ului, identității vizuale sau altor elemente aparținând brandului Istorii cu Cașcaval. Dreptul de utilizare a mărcii de către un francizat va fi acordat numai în condițiile stabilite prin contractul de franciză.':
        'Accessing the website or submitting a franchise enquiry grants the user no right to use the name, logo, visual identity or any other element belonging to the Istorii cu Cașcaval brand. The right to use the trade mark is granted to a franchisee only on the terms set out in the franchise agreement.',
    'Limitarea răspunderii': 'Limitation of liability',
    'Depunem eforturi pentru ca informațiile publicate pe website să fie actuale și corecte. Cu toate acestea, pot exista erori, omisiuni sau informații care necesită actualizare. Compania își rezervă dreptul de a modifica informațiile privind produsele, locațiile, conceptul de franciză, investițiile orientative și condițiile de colaborare fără obligația unei notificări prealabile, în limitele permise de lege. Deciziile de investiție nu trebuie luate exclusiv pe baza informațiilor generale publicate pe website.':
        'We make every effort to keep the information published on the website current and accurate. Nevertheless, errors, omissions or information requiring updating may occur. The company reserves the right to change information about products, locations, the franchise concept, indicative investment figures and terms of collaboration without prior notice, to the extent permitted by law. Investment decisions should not be made solely on the basis of the general information published on the website.',
    'Protecția datelor cu caracter personal': 'Protection of personal data',
    'Datele transmise prin formularele website-ului pot include numele, numărul de telefon, adresa de e-mail, localitatea și alte informații necesare pentru procesarea solicitării. Aceste date vor fi utilizate pentru comunicarea cu persoana interesată, analiza solicitării și, după caz, desfășurarea procesului de selecție pentru franciză. Mai multe informații despre modul în care sunt colectate și utilizate datele personale sunt disponibile în secțiunile de mai jos din prezentul document.':
        'Data submitted through the website’s forms may include name, phone number, email address, town or city and other information needed to process the enquiry. This data is used to communicate with the interested party, assess the enquiry and, where applicable, carry out the franchise selection process. Further information on how personal data is collected and used is set out in the sections below.',
    'Cookie-uri': 'Cookies',
    'Website-ul poate utiliza cookie-uri și tehnologii similare pentru funcționarea corectă a paginilor, analizarea traficului și îmbunătățirea experienței utilizatorilor. Informații suplimentare sunt disponibile în prezentul document.':
        'The website may use cookies and similar technologies so that pages work correctly, to analyse traffic and to improve the user experience. Further information is provided in this document.',
    'Link-uri către website-uri externe': 'Links to external websites',
    'Website-ul poate conține link-uri către platforme sau website-uri administrate de terți. Istorii cu Cașcaval nu controlează și nu își asumă responsabilitatea pentru conținutul, disponibilitatea, securitatea sau politicile acestor website-uri externe.':
        'The website may contain links to platforms or websites operated by third parties. Istorii cu Cașcaval does not control and accepts no responsibility for the content, availability, security or policies of those external websites.',
    'Disponibilitatea website-ului': 'Website availability',
    'Nu garantăm funcționarea permanentă și fără întreruperi a website-ului. Accesul poate fi temporar suspendat pentru mentenanță, actualizări, probleme tehnice sau din alte motive independente de companie.':
        'We do not guarantee that the website will operate continuously or without interruption. Access may be temporarily suspended for maintenance, updates, technical issues or other reasons outside the company’s control.',
    'Modificarea Termenilor și Condițiilor': 'Changes to these Terms and Conditions',
    'Istorii cu Cașcaval își rezervă dreptul de a actualiza prezentele Termeni și Condiții atunci când este necesar. Versiunea actualizată va fi publicată pe această pagină, împreună cu data ultimei actualizări. Continuarea utilizării website-ului după publicarea modificărilor presupune aplicarea versiunii în vigoare a Termenilor și Condițiilor.':
        'Istorii cu Cașcaval reserves the right to update these Terms and Conditions where necessary. The updated version will be published on this page together with the date it was last revised. Continuing to use the website after changes are published means the version then in force applies.',
    'Legislația aplicabilă': 'Governing law',
    'Prezentele Termeni și Condiții sunt guvernate de legislația Republicii Moldova, în măsura în care aceasta este aplicabilă companiei și serviciilor prezentate. Eventualele neînțelegeri vor fi soluționate, în primul rând, pe cale amiabilă, iar atunci când acest lucru nu este posibil, de către autoritățile sau instanțele competente conform legislației aplicabile.':
        'These Terms and Conditions are governed by the law of the Republic of Moldova, to the extent it applies to the company and the services presented. Any disagreement will first be addressed amicably and, where that is not possible, by the competent authorities or courts under the applicable law.',
    'Contact': 'Contact',
    'Pentru întrebări referitoare la website, franciză sau prezentele Termeni și Condiții, ne poți contacta la:':
        'For questions about the website, the franchise or these Terms and Conditions, you can reach us at:',
    'Adresă: [ADRESA]': 'Address: [ADRESA]',
}

EN_BLOCKS = {
    'Asta <strong>creează loialitate</strong> și <strong>valoare</strong> mai mare per client.':
        'This <strong>builds loyalty</strong> and greater <strong>value</strong> per customer.',
    'Considerăm că ești de-acord cu <a href="termeni-si-conditii.html">Termenii și condițiile</a> accesând butonul “Devină francizor”':
        'By pressing “Become a franchisee” you agree to our <a href="terms.html">Terms and Conditions</a>',
}


# --------------------------------------------------------------- locales

LOCALES = {
    'ru': {'dir': 'ru', 'lang': 'ru', 'label': 'Ru', 'name': 'Русский',
           'table': RU, 'blocks': RU_BLOCKS, 'menu_label': 'Выберите язык'},
    'en': {'dir': 'en', 'lang': 'en', 'label': 'En', 'name': 'English',
           'table': EN, 'blocks': EN_BLOCKS, 'menu_label': 'Choose language'},
}

# The Romanian original, for the switcher and the hreflang set.
BASE = {'dir': '', 'lang': 'ro', 'label': 'Ro', 'name': 'Română',
        'menu_label': 'Alege limba'}

# Page filenames per locale. The terms page gets a neutral slug outside
# Romanian so a Russian URL does not carry a Romanian word.
PAGES = {
    'index.html': {'ro': 'index.html', 'ru': 'index.html', 'en': 'index.html'},
    'termeni-si-conditii.html': {'ro': 'termeni-si-conditii.html',
                                 'ru': 'terms.html', 'en': 'terms.html'},
    'politica-de-confidentialitate.html': {'ro': 'politica-de-confidentialitate.html',
                                           'ru': 'privacy.html', 'en': 'privacy.html'},
    'politica-de-cookies.html': {'ro': 'politica-de-cookies.html',
                                 'ru': 'cookies.html', 'en': 'cookies.html'},
    '404.html': {'ro': '404.html', 'ru': '404.html', 'en': '404.html'},
    'success.html': {'ro': 'success.html', 'ru': 'success.html',
                     'en': 'success.html'},
}
