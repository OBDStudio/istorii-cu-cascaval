# -*- coding: utf-8 -*-
"""Generate termeni-si-conditii.html from the copy drafted in the Figma file.

    python tools/build_terms.py
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pages import shell, SITE, stagger  # noqa: E402


def p(text):
    return '      <p>%s</p>' % text


def ul(items):
    return '      <ul>\n' + '\n'.join('        <li>%s</li>' % i for i in items) + '\n      </ul>'


def section(title, *blocks):
    return ('    <section>\n      <h2>%s</h2>\n' % title) + '\n'.join(blocks) + '\n    </section>'


SECTIONS = [
    section(
        'Informații generale',
        p('Website-ul Istorii cu Cașcaval este administrat de:'),
        ul([
            'Denumirea juridică: [DENUMIREA COMPANIEI]',
            'IDNO: [IDNO]',
            'Sediul juridic: [ADRESA]',
            'E-mail: [E-MAIL]',
            'Telefon: [TELEFON]',
        ]),
        p('În continuare, compania poate fi denumită „Istorii cu Cașcaval”, „Compania”, „noi” sau „nouă”.'),
        p('Website-ul are rolul de a prezenta brandul Istorii cu Cașcaval, activitatea companiei, produsele, '
          'locațiile existente și oportunitățile de colaborare prin sistemul de franciză.'),
    ),
    section(
        'Utilizarea website-ului',
        p('Website-ul poate fi utilizat pentru:'),
        ul([
            'informarea despre brandul Istorii cu Cașcaval;',
            'prezentarea conceptului de franciză;',
            'consultarea informațiilor orientative privind investiția și modelul de business;',
            'identificarea locațiilor și serviciilor disponibile;',
            'transmiterea unei solicitări pentru obținerea mai multor informații;',
            'inițierea unei discuții privind posibilitatea deschiderii unei francize.',
        ]),
        p('Utilizatorul se obligă să folosească website-ul într-un mod legal și să nu întreprindă acțiuni care '
          'ar putea afecta funcționarea, securitatea sau disponibilitatea acestuia.'),
    ),
    section(
        'Informațiile despre franciză',
        p('Informațiile prezentate pe website cu privire la franciza Istorii cu Cașcaval au caracter general și informativ.'),
        p('Transmiterea unui formular, solicitarea unei prezentări sau purtarea unor discuții cu reprezentanții '
          'companiei nu reprezintă acceptarea automată a unei persoane în rețeaua de franciză și nu creează '
          'obligația companiei de a încheia un contract de franciză.'),
        p('Fiecare solicitare poate fi analizată individual, luând în considerare criterii precum locația propusă, '
          'disponibilitatea teritorială, capacitatea investițională, compatibilitatea cu modelul de business și '
          'alte criterii stabilite de companie.'),
        p('Condițiile finale ale colaborării vor fi stabilite exclusiv prin documentele și contractul de franciză '
          'semnate de părți.'),
    ),
    section(
        'Investiții și informații financiare',
        p('Valorile privind investiția inițială, costurile operaționale, cifra de afaceri, perioada estimată de '
          'recuperare a investiției, marjele sau profitul prezentate pe website sunt, dacă nu este specificat '
          'expres altfel, valori orientative. Rezultatele efective ale unei francize pot varia în funcție de '
          'numeroși factori, inclusiv:'),
        ul([
            'orașul și locația magazinului;',
            'traficul și profilul clienților;',
            'nivelul investiției;',
            'costurile de chirie și personal;',
            'managementul afacerii;',
            'condițiile economice și concurența locală;',
            'sezonalitatea;',
            'performanța echipei și implicarea francizatului.',
        ]),
        p('Istorii cu Cașcaval nu garantează un anumit nivel al vânzărilor, veniturilor sau profitului.'),
        p('Orice proiecție financiară trebuie analizată individual înainte de luarea unei decizii de investiție.'),
    ),
    section(
        'Solicitarea unei francize',
        p('Persoanele interesate pot transmite o solicitare prin intermediul formularului disponibil pe website. '
          'Prin completarea formularului, utilizatorul declară că informațiile furnizate sunt corecte și actuale. '
          'După primirea solicitării, echipa Istorii cu Cașcaval poate contacta persoana interesată pentru:'),
        ul([
            'o discuție inițială;',
            'prezentarea conceptului;',
            'analiza orașului sau a locației propuse;',
            'prezentarea modelului de colaborare;',
            'stabilirea următoarelor etape ale procesului.',
        ]),
        p('Compania își rezervă dreptul de a accepta sau refuza continuarea procesului de selecție a unui '
          'potențial francizat.'),
    ),
    section(
        'Produse și informații prezentate',
        p('Fotografiile, descrierile, sortimentele și alte informații despre produsele Istorii cu Cașcaval sunt '
          'prezentate în scop informativ. Disponibilitatea produselor poate varia în funcție de locație, sezon, '
          'furnizori și stocurile existente. Imaginile utilizate pe website pot avea caracter ilustrativ, iar '
          'aspectul produselor poate prezenta diferențe față de imaginile afișate.'),
    ),
    section(
        'Proprietate intelectuală',
        p('Conținutul website-ului, inclusiv, fără a se limita la:'),
        ul([
            'denumirea Istorii cu Cașcaval;',
            'logo-ul și elementele de identitate vizuală;',
            'texte;',
            'fotografii și materiale video;',
            'elemente grafice;',
            'designul website-ului;',
            'materiale de prezentare;',
            'concepte și materiale comerciale;',
        ]),
        p('este protejat de legislația aplicabilă privind drepturile de autor, mărcile și proprietatea '
          'intelectuală. Copierea, reproducerea, distribuirea, modificarea sau utilizarea comercială a acestor '
          'materiale fără acordul prealabil al titularului drepturilor este interzisă.'),
    ),
    section(
        'Marca Istorii cu Cașcaval',
        p('Accesarea website-ului sau transmiterea unei solicitări de franciză nu oferă utilizatorului niciun '
          'drept de utilizare a denumirii, logo-ului, identității vizuale sau altor elemente aparținând brandului '
          'Istorii cu Cașcaval. Dreptul de utilizare a mărcii de către un francizat va fi acordat numai în '
          'condițiile stabilite prin contractul de franciză.'),
    ),
    section(
        'Limitarea răspunderii',
        p('Depunem eforturi pentru ca informațiile publicate pe website să fie actuale și corecte. Cu toate '
          'acestea, pot exista erori, omisiuni sau informații care necesită actualizare. Compania își rezervă '
          'dreptul de a modifica informațiile privind produsele, locațiile, conceptul de franciză, investițiile '
          'orientative și condițiile de colaborare fără obligația unei notificări prealabile, în limitele permise '
          'de lege. Deciziile de investiție nu trebuie luate exclusiv pe baza informațiilor generale publicate pe '
          'website.'),
    ),
    section(
        'Protecția datelor cu caracter personal',
        p('Datele transmise prin formularele website-ului pot include numele, numărul de telefon, adresa de '
          'e-mail, localitatea și alte informații necesare pentru procesarea solicitării. Aceste date vor fi '
          'utilizate pentru comunicarea cu persoana interesată, analiza solicitării și, după caz, desfășurarea '
          'procesului de selecție pentru franciză. Mai multe informații despre modul în care sunt colectate și '
          'utilizate datele personale sunt disponibile în '
          'secțiunile de mai jos din prezentul document.'),
    ),
    section(
        'Cookie-uri',
        p('Website-ul poate utiliza cookie-uri și tehnologii similare pentru funcționarea corectă a paginilor, '
          'analizarea traficului și îmbunătățirea experienței utilizatorilor. Informații suplimentare sunt '
          'disponibile în prezentul document.'),
    ),
    section(
        'Link-uri către website-uri externe',
        p('Website-ul poate conține link-uri către platforme sau website-uri administrate de terți. Istorii cu '
          'Cașcaval nu controlează și nu își asumă responsabilitatea pentru conținutul, disponibilitatea, '
          'securitatea sau politicile acestor website-uri externe.'),
    ),
    section(
        'Disponibilitatea website-ului',
        p('Nu garantăm funcționarea permanentă și fără întreruperi a website-ului. Accesul poate fi temporar '
          'suspendat pentru mentenanță, actualizări, probleme tehnice sau din alte motive independente de companie.'),
    ),
    section(
        'Modificarea Termenilor și Condițiilor',
        p('Istorii cu Cașcaval își rezervă dreptul de a actualiza prezentele Termeni și Condiții atunci când este '
          'necesar. Versiunea actualizată va fi publicată pe această pagină, împreună cu data ultimei actualizări. '
          'Continuarea utilizării website-ului după publicarea modificărilor presupune aplicarea versiunii în '
          'vigoare a Termenilor și Condițiilor.'),
    ),
    section(
        'Legislația aplicabilă',
        p('Prezentele Termeni și Condiții sunt guvernate de legislația Republicii Moldova, în măsura în care '
          'aceasta este aplicabilă companiei și serviciilor prezentate. Eventualele neînțelegeri vor fi '
          'soluționate, în primul rând, pe cale amiabilă, iar atunci când acest lucru nu este posibil, de către '
          'autoritățile sau instanțele competente conform legislației aplicabile.'),
    ),
    section(
        'Contact',
        p('Pentru întrebări referitoare la website, franciză sau prezentele Termeni și Condiții, ne poți contacta la:'),
        ul([
            'Istorii cu Cașcaval',
            'E-mail: [E-MAIL]',
            'Telefon: [TELEFON]',
            'Adresă: [ADRESA]',
        ]),
    ),
]

BODY = '''    <div class="doc">
    ''' + stagger('Termeni și condiții', 'h1', 'doc__title') + '''
    <p class="doc__updated">Ultima actualizare: 15 august 2026</p>
    <p class="doc__lede">Bine ai venit pe website-ul Istorii cu Cașcaval. Prin accesarea și utilizarea acestui website, confirmi că ai citit, înțeles și accepți prezentele Termeni și Condiții.<br>Te rugăm să citești cu atenție informațiile de mai jos înainte de utilizarea website-ului sau transmiterea unei solicitări privind franciza Istorii cu Cașcaval.</p>

''' + '\n\n'.join(SECTIONS) + '''
    </div>'''

io.open(os.path.join(SITE, 'termeni-si-conditii.html'), 'w', encoding='utf-8').write(
    shell('Termeni și condiții — Istorii cu Cașcaval',
          'Termenii și condițiile de utilizare a website-ului Istorii cu Cașcaval.',
          BODY))
print('wrote termeni-si-conditii.html')
