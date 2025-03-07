# Kortfejl håndtering - README

# Introduktion
Dette script migrerer data fra en kildefil (`source_data.csv`) til en destinationsfil (`destination_data.csv`).
Scriptet håndterer en række potentielle fejl for at sikre en stabil og sikker migrering af data.

# Forudsætninger
For at køre scriptet skal du have følgende programmer og tilføjelser installeret:
- Python 3.x
- Visual Studio Code
- Python Extension i Visual Studio Code

# Kørsel af scriptet
Koden køres ved at trykke på Play-knappen oppe i højre hjørne, når du er inde i `Opgave 3 - Kortfejl håndtering` filen i Visual Studio Code.

# Output
   - Hvis scriptet lykkes, vil du se følgende besked:
     `Data migreret succesfuldt fra 'source_data.csv' til 'destination_data.csv'.`
   - Hvis scriptet fejler, vil en relevant fejlmeddelelse blive vist i terminalen. Se "Fejlhåndtering" i række 21.

# Fejlhåndtering
Scriptet håndterer følgende fejl, og vil give en advarsel i terminalen:

**Manglende kildefil**
Hvis `source_data.csv` ikke findes, gives en fejlmeddelelse.

**Tom kildefil**
Hvis kildefilen ikke indeholder data, stoppes scriptet med en fejlmeddelelse.

**Skrivebeskyttet destinationsfil**
Hvis `destination_data.csv` ikke kan skrives til, gives en fejlmeddelelse.

**CSV-formatfejl**
Hvis kildefilen har et forkert format, advares brugeren.

**Uventede fejl**
Eventuelle andre fejl fanges og udskrives i terminalen.

# Sådan er opgaven løst
Jeg har skrevet koden ved hjælp af ChatGPT, og har igennem en række testkørsler kommet frem til en kode, der opfylder kravsspecifikationen, heriblandt håndtering af de potentielle fejl, der fremgår i kravsspecifikationen.

# Udfordringer
- Dynamisk filsti i Windows: Håndtering af backslashes (`\`) i filstier krævede brug af rå strenge (`r""`).
- Fejlmeddelelser: Jeg vil sikre, at fejlmeddelelserne var brugervenlige og dækkede de vigtigste scenarier.
- Er stien dynamisk nok, så scriptet kan køres på andre computere?

# Eventuel videre-arbejdning med opgaven
Hvis jeg skulle arbejde videre med scriptet, ville jeg overveje følgende:
- **Filtrering af data** før de kopieres til destinationsfilen. F.eks. efter fornavn.
- **Øge brugervenligheden**, såfremt filen skal bruges og læses af et menneske. Her vil jeg overveje at konvertere filen til en "rigtig" Excel-fil, for at gøre den mere bruger- og læsevenlig. I denne konvertering vil jeg også overveje at lave et filter, samt formatere arket som en tabel, for at øge brugervenligheden yderligere. Derudover indeholder arket en række tomme linjer, som jeg ligeledes vil overveje at slette i scriptet.
- **Mulighed for at tilføje dato-stempel i filnavnet**, for at skabe bedre overblik. Dette vil også give den fordel, at der skabes en ny destinationsfil når scriptet atter køres, frem for at den eksisterende destinationsfil overskrives.
- **Logning af fejl** i en separat logfil, frem for blot at vise dem i terminalen.
- **Tjekke for uregelmæssigheder i dataen**. Er der uregelmæssigheder i source_data, f.eks. "forstyrrende" mellemrum, eller forkert brug af separatorer (komma)?