# Projectvoorstel: Fast Fashion Footprint Checker

**Naam:** Zoë Oggel
**Studentnummer:** 13383337

## Probleemstelling

Veel consumenten hebben geen idee hoe (on)duurzaam de kledingmerken zijn waarvan ze kopen. Er is een gebrek aan toegankelijke en begrijpbare informatie over de milieu-impact van fast fashion merken. Hierdoor blijft het bewustzijn laag en maken mensen onbewust keuzes die bijdragen aan overconsumptie en vervuiling. Tegelijkertijd groeit de interesse in duurzame mode, maar ontbreekt het aan eenvoudige tools om geïnformeerde keuzes te maken.

## Verwachte gebruikers

De verwachte gebruikers zijn:
- Jongeren en jongvolwassenen die geïnteresseerd zijn in mode, maar ook bewust willen consumeren.
- Mensen die hun ecologische voetafdruk willen verkleinen.
- Studenten en consumenten die informatie zoeken over de duurzaamheid van kledingmerken.
- Iedereen die actief op zoek is naar duurzamere alternatieven voor bekende fast fashion merken.

## Setting

De app zal vooral gebruikt worden op mobiele telefoons en laptops. Gebruikers kunnen snel opzoeken hoe duurzaam een merk is, bijvoorbeeld tijdens het online winkelen of onderweg. De app wordt gebruikt in een persoonlijke setting, waarbij gebruikers zelfstandig merken opzoeken of suggesties krijgen.

## Niche

De app combineert meerdere databronnen en gebruikt een machine learning model om een score te berekenen voor elk kledingmerk. In tegenstelling tot bestaande lijsten of blogs, biedt deze tool een gepersonaliseerde inschatting gebaseerd op input van de gebruiker en externe gegevens (zoals productieketens, materiaalgebruik, reviews en transparantierapporten). De niche ligt in het feit dat de app:
- Realtime feedback geeft.
- Visuele en begrijpelijke uitleg biedt.
- De focus legt op duurzaamheid als het item bij de consument is

## Samenvatting oplossing

Deze applicatie zal consumenten helpen om duurzamere keuzes te maken binnen mode door middel van een webapp die de milieu-impact van kledingmerken inzichtelijk maakt. De gebruiker krijgt een eenvoudige interface waarin zij merken kunnen opzoeken en zien hoe deze scoren op duurzaamheid, op basis van data en machine learning. Het doel is dat de data zo veel mogelijk voorspelt of een kledingstuk lang mee zal gaan of niet, dus richt zich specifiek op duurzaamheid als het item al bij de consument is.

De specifieke input is nog afhankelijk van beschikbare informatie, maar hier is een overzicht:
- Gebruikte materialen
- Reviews over het merk/ product en of dingen snel stuk gaan en slecht in elkaar zitten
- Aantal nieuwe items per jaar

## Features

### Verplicht

- **Merkzoekfunctie**: Gebruikers kunnen een kledingmerk opzoeken. In het beginsel is dit een selectiemenu, maar als het lukt om de scraper goed te bouwen is het hopelijk een opzoekfunctie met autofill.
- **Footprint Score**: Een visuele en numerieke score gebaseerd op duurzaamheid.
- **Resultaatpagina met uitleg**: Per merk komt er een overzicht van hoe de score is opgebouwd (bijv. materiaalgebruik, CO₂-uitstoot, transport, etc.).
- **Machine learning model**: Classificeert merken op basis van diverse duurzaamheidsindicatoren.
- **Responsief design**: Werkt goed op zowel mobiel als desktop.

### Optioneel (in aflopende belangrijkheid)

- uitgebreidere merkzoekfunctie
- Suggesties voor duurzamere alternatieven
- Gebruikersaccount + favorietenlijst
- Invoeroptie voor kledingstuk (bv. "spijkerbroek H&M") en een inschatting van die specifieke aankoop
- Accessibility features
- Informatiepagina’s over fast fashion impact
- Vergelijkingsoptie: merken vergelijken


## Vereisten

### Databronnen

- [Good On You](https://directory.goodonyou.eco/) – duurzaamheidsbeoordelingen van merken *(scrapen/API afhankelijk van toegankelijkheid)*
- [Sustainable Apparel Coalition](https://apparelcoalition.org/) – Higg Index
- [Open Apparel Registry](https://openapparel.org/) – Leveranciersinformatie
- [Zalando](https://www.zalando.nl/dames-home/) - Informatie over materiaal
- [Trustpilot](https://nl.trustpilot.com) - Reviews over merken
- Gebruikersinput (zoals merk, soort kledingstuk)

### Externe componenten / bibliotheken

- Flask – Webframework
- Scikit-learn – Voor het machine learning model
- Pandas / NumPy – Dataverwerking
- Bootstrap of Tailwind – Front-end styling
- Requests / BeautifulSoup – Voor API’s of scrapen van data
- Matplotlib / Seaborn – Voor visualisaties van duurzaamheidsscores
- Beautiful soup & selenium – Voor het scrapen van de nodife informatie

## Wat wordt moeilijk?

- **Toegang tot betrouwbare en consistente data**: Veel data over duurzaamheid van merken is versnipperd of niet publiek beschikbaar.
  - Oplossing: Beginnen met een kleine subset van merken met goed toegankelijke data (bijv. van Good On You).
- **Gebalanceerde en eerlijke score creëren**: Machine learning model moet transparant en uitlegbaar zijn.
  - Oplossing: Het gebruiken van interpreteerbare modellen zoals decision trees en geef duidelijke uitleg bij resultaten.



