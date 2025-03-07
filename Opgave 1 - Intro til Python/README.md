# Intro til Python - README

# Kørsel af scriptet
Koden køres ved at trykke på Play-knappen oppe i højre hjørne, når du er inde i `Opgave 1 - Intro til Python.py` filen.

# Output
Når du kører scriptet, genereres følgende output:
1) Navne sorteret alfabetisk (A-Å), og dernæst efter længde (kortest til længest)
2) Bogstavoptælling sorteret efter hyppighed
3) Antal navne i listen (samt hvor mange af disse navne der er dubletter)
4) Gennemsnitlig navnelængde
5) Median navnelængde
6) Tre grafikker:
    a) Frekvens af bogstaver i navnelisten
    b) Bogstav sky
    c) Fordeling af navnelængder
BEMÆRK at selve dubletfjernelsen sker før videre bearbejdning af data. Så dubletter tæller ikke med i ovennævnte punkt 1-6.

# Forbehold
Af hensyn til overskueligheden og mængden af data, der skal behandles, har jeg valgt kun at tage de første 10 navne med fra `Navne_liste.txt` filen, samt at dublikere 2 af navnene. Så der forekommer 12 navne i alt. At inkludere alle navne vil naturligvis give et andet resultat, da grundlaget der arbejdes ud fra, vil være større.

# Sådan er opgaven løst
Jeg startede med at kigge på nogle YouTube videoer, for at få en basal forståelse for Python, da jeg ikke har dette. Det lykkedes mig, på baggrund af disse tutorials, at lave nogle simple print-kommandoer. Opgaven her er løst ved hjælp af ChatGPT, og min umiddelbare vurdering er at det vil tage mig en uges tid, hvis jeg skulle lave hele opgaven "fra bunden" selv.

# Eventuel viderebearbejdning af data
Hvis jeg skulle arbejde videre med denne data, kunne det også være interessant at gøre følgende:
- Lave et datarens, hvor hvert navn tjekkes for store bogstaver ud over det første bogstav (denne gøres dog overflødig af at alle navne ændres til at være med små bogstaver)
- Tjekke, om der er nogen bogstaver i alfabetet der slet ikke forekommer i nogle af navnene overhovedet
- Foruden gennemsnit og median navnelængde, kunne man også fremskaffe den korteste og den længste navnelængde
- Man kan lave et søjlediagram med hvor mange gange et navn på 3 bogstaver forekommer, et navn på 4 bogstaver, og så fremdeles
- Til sidst, og bestemt ikke mindst, så vil disse data kunne bruges til mange spændende ting, hvis de indgik i en kontekst. Er det f.eks. navne på ansatte i en virksomhed? Er det navne, der er tildelt ved fødsel et pågældende år? Og hvis man har data fra tidligere år, kan man så se nogle tendenser i disse navne der tildeles fødsel fra år til år?