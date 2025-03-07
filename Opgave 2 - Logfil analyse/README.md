# Logfil Analyse - README

# Introduktion
Dette script er udviklet til automatisk at analysere en logfil, filtrere bestemte typer af logmeddelelser (ERROR og WARNING), og gemme disse i separate filer i en mappe kaldet "Rapport". Disse filer tildeles et datostempel inklusive klokkeslæt, således at flere log-analyser kan foretages uden at tidligere analyser overskrives.
Derudover kontrollerer scriptet, om optællingen af loglinjer stemmer overens med outputfilerne for at sikre dataintegritet.

# Forudsætninger
For at kunne køre scriptet, skal du have følgende programmer og tilføjelser installeret:
- Python 3.x (seneste version anbefales)
- colorama-biblioteket, som bruges til farvekodede terminalmeddelelser.
- GitHub-repository'et skal indeholde scriptfilen samt en logfil ved navn `app_log (logfil analyse) - random.txt`.

# Kørsel af scriptet
Koden køres ved at trykke på Play-knappen oppe i højre hjørne, når du er inde i `Opgave 2 - Logfil analyse` filen i Visual Studio Code.

# Output
- Efter at scriptet er kørt, vil en mappe ved navn `Rapport` automatisk blive oprettet, hvis den ikke findes.
- I denne mappe genereres to filer:
  - `ERROR_[dato_tid].txt` (indeholder alle ERROR-linjer fra logfilen)
  - `WARNING_[dato_tid].txt` (indeholder alle WARNING-linjer fra logfilen)
- I terminalen vises en besked om hvorvidt optællingen af loglinjer stemmer overens.
- Derudover optælles antallet af linjer at hhv. typen ERROR, WARNING, SUCCESS og INFO, foruden en optælling af ukendte linjer. Dette vises ligeledes i terminalen.

# Fejlhåndtering
Scriptet håndterer følgende fejl, og giver en advarsel i terminalen:

**Logfilen findes ikke**
Hvis scriptet ikke kan finde logfilen på den angivne placering.
Løsning: Sørg for at filen `app_log (logfil analyse) - random.txt` findes i scriptets mappe.

**Logfilen er åben**
Hvis logfilen allerede er åben i et andet program, kan scriptet ikke køre.
Løsning: Luk logfilen og prøv igen.

**Logfilen er tom**
Hvis logfilen ikke indeholder nogen data.
Løsning: Tjek logfilens indhold og sørg for, at den ikke er tom.

**Manglende permitter**
Hvis scriptet ikke kan oprette outputfilerne i "Rapport"-mappen.
Løsning: Sørg for, at scriptet har adgang til at skrive i den pågældende mappe.

**Optælling stemmer ikke overens**
Hvis antallet af linjer i outputfilerne ikke matcher det forventede antal.
Løsning: Tjek logfilen for uventede linjer og undersøg outputfilerne.

# Sådan er opgaven løst
Jeg har bygget koden ved hjælp af ChatGPT, og har lavet adskillige testkørsler, og bygget mere kode på for at gøre den mere robust, samt tilføjet en række nyttige funktioner. Eksempelvis tager scriptet højde for en række potentielle fejl (se linje 23-44), og jeg har indbygget en funktion, der gør, at de to rapportfiler (ERROR og WARNING) gemmes med et datostempel inkl. klokkeslæt, således at flere loganalyser kan køres uden at tidligere resultater overskrives. Via min indbyggede fejlhåndtering blev jeg også opmærksom på at der også forekommer andre typer af beskeder i loggen end ERROR og WARNING, som jeg havde overset i første omgang. Da min første optælling ikke stemte overens, blev jeg opmærksom på at der også er SUCCES og INFO typer i loggen, jeg skulle forholde mig til, hvorfor jeg også implementerede optælling af disse i koden. 

# Eventuel videre-arbejdning med opgaven
Selvom det er smart, at der laves separate filer med ERROR og WARNING typer, så er der alligevel adskillige 100 linjer at forholde sig til. Det er noget omstændigt at gennemgå, hvorfor jeg vil foreslå at arbejde videre med dette data. Det kunne gøres ved at granulere dataen yderligere, og lave et cirkeldiagram med de forskellige fejlbeskeder, der genereres i loggen. Er der nogle fejl der forekommer hyppigere end andre? Dette kunne give anledning at kigge på de fejl, brugerne hyppighst støder på, og identificere disse med det formål at rette dem. Eksempel: "ERROR Missing configuration file", hvor tit forekommer denne fejl? Er det muligt at identificere hvor denne fejl forekommer? Hvis fejlen forekommer det samme sted, kan man sætte ind med en løsning her.