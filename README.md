# Komanda 40 - Akmentiņu spēle

## Papildu prasības programmatūrai

Spēles sākumā cilvēks-spēlētājs izvēlas, ar cik akmentiņiem spēle tiks uzsākta. Akmentiņu diapazons
ir no 50 līdz 70.

## Spēles apraksts

Uz galda atrodas tik daudz akmentiņu, cik izvēlējās cilvēks-spēlētājs. Katram spēlētājam spēles
sākumā ir 0 akmentiņu un 0 punktu. Spēlētāji izpilda gājienus pēc kārtas. Spēlētājs savā gājienā drīkst
paņemt sev 2 vai 3 akmentiņus. Ja pēc akmentiņu paņemšanas uz galda ir palicis pāra akmentiņu
skaits, tad pretinieka punktiem tiek pieskaitīti 2 punkti, bet ja nepāra skaits, tad spēlētāja punktu
skaitam tiek pieskaitīti 2 punkti. Spēle beidzas, kad uz galda nepaliek neviens akmentiņš. Spēlētāju
punktu skaitam tiek pieskaitīts spēlētājam esošo akmentiņu skaits. Ja spēlētāju punktu skaits ir
vienāds, tad rezultāts ir neizšķirts. Pretējā gadījumā uzvar spēlētājs, kam ir vairāk punktu.

## Programmatūrā ir jānodrošina šādas iespējas lietotājam:

- izvēlēties, kurš uzsāk spēli: lietotājs vai dators;
- izvēlēties, kuru algoritmu izmantos dators: Minimaksa algoritmu vai Alfa-beta algoritmu;
- izpildīt gājienus un redzēt izmaiņas spēles laukumā pēc gājienu (gan lietotāja, gan datora) izpildes;
- uzsākt spēli atkārtoti pēc kārtējās spēles pabeigšanas.
- Programmatūrai ir jānodrošina grafiskā lietotāja saskarne (komandrindiņas spēles netiks pieņemtas). Šajā gadījumā runa nav par sarežģītu, 3D grafisko saskarni, bet gan par vizuālu elementu tādu kā izvēlnes, pogas, teksta lauki, ikonas, saraksti, u.c. izmantošanu.

## Darba uzdevumi:

- spēles koka vai tā daļas ģenerēšana atkarībā no spēles sarežģītības un studentu komandai pieejamiem skaitļošanas resursiem;
- heiristiskā novērtējuma funkcijas izstrāde;
- Minimaksa algoritms un Alfa-beta algoritms (kas abi var būt realizēti kā Pārlūkošana uz priekšu pār n-gājieniem);
- 10 eksperimenti ar katru no algoritmiem, fiksējot datora un cilvēka uzvaru skaitu, datora apmeklēto virsotņu skaitu, datora vidējo laiku gājiena izpildei.
