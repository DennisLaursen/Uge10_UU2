# Pandasg - README

# Introduktion
Denne opgave demonstrerer brugen af Python-bibliotekerne Pandas og Matplotlib til dataanalyse og visualisering. Opgaven omhandler indlæsning af en CSV-fil med data om danske boligpriser, gruppering af data efter region og hustype samt præsentation af resultaterne i både terminalen og i diagrammer.

# Forudsætninger
For at køre koden skal du sikre, at du har Python installeret (anbefalet version Python 3.7 eller nyere) samt de nødvendige pakker:
- Pandas
- Matplotlib

# Kørsel af scriptet
Koden køres ved at trykke på Play-knappen oppe i højre hjørne, når du er inde i `Opgave 4 - Pandas` filen i Visual Studio Code.

# Output
- Indlæsning af CSV-filen og udskrivning af de første 10 rækker.
- Udføre grupperinger på region og hustype for at beregne gennemsnitlige købspriser.
- Formatere beløb med tusindseparatorer og vise dem i millioner (f.eks. "1,2 mio. kr.") i både terminaludskrifter og diagrammer.
- Generere diagrammer, der viser de aggregerede data.

# Sådan er opgaven løst
Jeg har skrevet koden ved hjælp af ChatGPT, og har igennem en række testkørsler kommet frem til en kode, der både opfylder kravsspecifikationen, samt gør outputtet mere brugervenligt. Jeg har ændrede en række labels til dansk, foruden at tilføje tusindseparatorer i beløbene.

# Udfordringer
**Dataformattering:**
En af de største udfordringer var at sikre, at numeriske værdier blev præsenteret læsevenligt i terminalen og diagrammerne. Det omfattede:
- Tilføjelse af tusindseparatorer.
- Konvertering af beløb til millioner.
- Tilpasning af decimalseparator til dansk standard (komma i stedet for punktum).
**Håndtering af blandede datatyper:**
Der opstod udfordringer med at formatere kolonner, der indeholder både tal og tekst (fx hustype), hvilket førte til fejl. Det krævede tilføjelse af betingelser, der sikrede, at formatteringsfunktionen kun blev anvendt på numeriske værdier.

# Ønsker til feedback:
Har jeg haft en fornuftig tilgang til at gøre visningen mere brugervenlig i terminalen samt i diagrammerne?

# Eventuel videre-arbejdning med opgaven
Hvis jeg skulle arbejde videre med opgaven, ville jeg implementere yderligere validering af dataene og måske tilføje interaktive elementer i diagrammerne (fx ved brug af Plotly) for at gøre analysen endnu mere brugervenlig.
Derudover indeholder `DKHousingPricesSample100k` dokumentet masser af data, man kan arbejde videre med. Eksempelvis indeholder arket data for 32 år (1992-2024), og man kunne dermed bruge denne data til at kigge på prisudviklingen over tid, evt. granuleret ud på regioner og/eller hustyper. Man kunne også kigge på om der er en sammenhæng imellem hvornår et hus er bygget, og dets pris. Er de gamle huse billigere, fordi de kræver støre vedligeholdelse? Eller er de tværtimod dyrere, fordi der er større efterspørgsel på gamle, traditionelle huse?

# Ændringer og tilpasninger
Jeg har foretaget en række ændringer og tilpasninger, som jeg her opsummerer:
- Danske betegnelser:
Jeg har oversat visse labels til dansk (fx "Fyn & øer", "Jylland", "Sjælland" for regioner og "Lejlighed", "Landejendom", "Sommerhus", "Rækkehus" for hustyper).
- Forbedret beløbsvisning:
Beløbene (purchase_price) vises med tusindseparatorer og er omregnet til millioner i diagrammerne, så de bliver nemmere at læse (fx "1,2 mio. kr." i stedet for "1200000").