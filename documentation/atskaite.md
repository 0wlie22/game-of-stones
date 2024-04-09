<h1 style="text-align: center;">GAME OF STONES</h1>

<h2 style="text-align: center;">Pirmā praktiska darba atskaite</h2>

**Darba autori**:

- Darja Sedova
- Iļja Spirts
- Vladislavs Sidorkins
- Regnārs Slapiņš
- Daniels Kikste-Zanders

[Saite uz darba kodu](https://github.com/0wlie22/game-of-stones)

<div style="page-break-after: always;"></div>

## Spēles apraksts

Pirms spēles sākuma lietotājs izvēlas:

- sākuma akmentiņu skaitu (no 50 līdz 70)
- kurš pirmais uzsāks spēli - lietotājs vai dators
- algoritms, kuru algoritmu izmantos dators

Uz galda atrodas tik daudz akmentiņu, cik izvēlās cilvēks-spēlētājs (no 50 līdz 70).
Katram spēlētājam spēles sākumā ir 0 akmentiņu un 0 punktu.
Spēlētāji izpilda gājienus pēc kārtas. Spēlētājs savā gājienā drīkst paņemt sev 2 vai 3 akmentiņus.

**Punkti**: Ja pēc akmentiņu paņemšanas uz galda ir palicis pāra akmentiņu
skaits, tad pretinieka punktiem tiek pieskaitīti 2 punkti, bet ja nepāra skaits, tad spēlētāja punktu skaitam tiek pieskaitīti 2 punkti.

**Spēles beigu nosacījumi**: Spēle beidzas, kad uz galda nepaliek neviens akmentiņš, vai arī ir palicis tikai viens akmentiņš.

**Uzvarētājs**: Spēlētāju punktu skaitam tiek pieskaitīts spēlētājam esošo akmentiņu skaits.Ja spēlētāju punktu skaits ir vienāds, tad rezultāts ir neizšķirts. Pretējā gadījumā uzvar spēlētājs, kam ir vairāk punktu.

<div style="page-break-after: always;"></div>

## Pamatalgoritma realizācija

### Spēles koka ģenerēšana

Spēles koka ģenerēšanas funkcija tiek izmantota, lai izveidotu visus iespējamos gājienus no pašreizējā spēles stāvokļa. Tiek veikta izvēles metode, kura ņem vērā vietu un laika kompleksitātes prasības. Spēles algoritms ģenerē koku, izmantojot uz priekšu kustēšanās metodi. Ģenerēšanas beigās tiek izveidots pilns koks, kas satur visus iespējamos gājienus no dotā stāvokļa.

Datu struktūra, ko izmanto, lai glabātu spēles koku dotajā Python koda (skat. pielikums 1) ir klase `GameState`. Šī klase izmanto Python iebūvētās datu struktūras un dažas papildu funkcijas, ko nodrošina modulis `dataclasses`. Šeit ir detalizēts datu struktūras apraksts:

- `stones_left: int`: Šis lauks glabā atlikušo akmens skaitu spēlē. Tas ir vienkāršs vesels skaitlis.
- `player_turn: Literal["computer", "player"]`: Šis lauks glabā informāciju par to, kura spēlētāja kārta ir spēlēt. Tas var būt vai nu "computer" vai "player".
- `computer_points: int` un `player_points: int`: Šie lauki glabā datora un spēlētāja punktus attiecīgi.
- `computer_stones: int` un `player_stones: int`: Šie lauki glabā datora un spēlētāja paņemto akmens skaitu attiecīgi.
- `_estimation_value: int | None`: Šis lauks glabā spēles stāvokļa novērtējuma vērtību. To izmanto heuristiskajā novērtējuma funkcijā.
- `parent: "GameState | None"`: Šis lauks glabā pašreizējā spēles stāvokļa vecāku. To izmanto, lai pārvietotos atpakaļ pa spēles koku.
- `children: list["GameState"]`: Šis lauks glabā pašreizējā spēles stāvokļa bērnus. To izmanto, lai pārvietotos pa spēles koku uz leju.

Klase `GameState` ietver arī vairākas metodes, lai manipulētu ar spēles koku un pārvietotos pa to, piemēram, `generate_next_state`, `points_to_add`, `generate_state_tree`, `traversal`, `post_order_traversal`, `leaf_nodes`, `left_child`, `right_child`, kā arī metodes spēles stāvokļa ielādei un saglabāšanai.

Piemēram, ar funkcijas `generate_state_tree` palīdzību tiek ģenerēts spēles koks. Sākumā izsauc metodi `generate_next_state()`, kas ģenerē nākamo spēles stāvokli un pievieno to kā bērnu pašreizējam stāvoklim. Pēc tam, funkcija iterē cauri visiem bērniem (jeb nākamajiem spēles stāvokļiem) un katram bērnam izsauc šo pašu `generate_state_tree()` metodi. Tādējādi, šī funkcija izveido visu iespējamo spēles stāvokļu koku, sākot no pašreizējā stāvokļa.

### Heiristiskā novērtējuma funkcija

Aiz spēles koka ģenerēšanas seko heiristisko vērtējumu piešķiršana virsotnēm. Šajā darbā tika izveidotas heiristiskās funkicijas - metodes, lai novērtētu un veiktu vērtējumu katram stāvoklim spēles koka struktūrā (skat. pielikums 2.1 un 2.2)

Balstoties uz minēno koda fragmentu darba pielikumā, gan Minimax, gan AlphaBeta algoritmi realizē heiristiskās funkcijas (funkciajas _estimate_). Šīs funkcijas aprēķina novērtējumu, pamatojoties uz abu spēlētāju kopējo skaitu un punktiem konkrētajā stāvoklī. Ja datora-spēlētāja kopējais skaits pārsniedz spēlētāja kopējo skaitu, tad tiek piešķirta vērtība 1. Ja abu spēlētāju kopējie skaiti ir vienādi, tad vērtība ir 0. Savukārt, ja spēlētāja kopējais skaits pārsniedz datora-spēlētāja kopējo skaitu, tiek piešķirta vērtība -1.

Izvēle šai konkretajai heiristiskajai funkcijai tika veikta, jo tā ir vienkārša un tajā tiek ņemti vērā tikai pašreizējie kopējie skaiti un punkti. Tā ir efektīva, jo ļauj balstīties tikai uz faktiskiem rezultātiem, neiekļaujot sarežģītāku vai detalizētāku vērtējumu piemēru. Šāda vienkārša funkcija ir piemērota Minimax un AlphaBeta algoritmiem, jo tās mērķis ir salīdzināt spēles stāvokļus un izvēlēties vislabāko gājienu, balstoties uz spēlētāju rezultātiem.

### Spēles algoritma pielietojums

Pēc heiristisko vērtējumu piešķiršanu virsotnēm tiek pielietots spēles algoritms, izmantojot Minimax vai AlphaBeta metodi, lai izvēlētos optimālo gājienu spēles koka struktūrā. Algoritms meklē maksimālo vai minimālo gājienu atkarībā no datora-spēlētāja vai cilvēka-spēlētāja. Tas ir darbības posms, kurā tiek pieņemti lēmumi par turpmāko gājienu spēles koka struktūrā. Algoritms strādā, apskatot spēles stāvokļus no pašreizējā līdz beigu stāvoklim, ņemot vērā heiristiskos vērtējumus. Minimax un AlphaBeta algoritmi ļauj spēles algoritmam veikt "maksimālās" un "minimālās" vērtības izvēli spēles koka struktūrā atbilstoši pašreizējam spēlētājam.

Minimax algoritms mēģina maksimizēt datora-spēlētāja labumu un minimizēt cilvēka-spēlētāja labumu, meklējot maksimāli labus gājienus. Tas izveido spēles koka struktūru, kas saskata visus iespējamos gājienus, novērtē tos ar heiristiskajā funkcijā iegūtajiem rezultātiem un veic lēmumu, ņemot vērā maksimumu vai minimumu. AlphaBeta algoritms savukārt, ir optimizēta Minimax algoritma versija, kas pārspēj nevajadzīgi meklējumus spēles koka struktūrā. Tas veic dažus papildu pārbaudes, lai izvairītos no bezjēdzīgiem izmēģinājumiem. Algoritms meklē tikai vislabākos gājienus, kas maksimizē datora-spēlētāja labumu un minimizē cilēka-spēlētāja labumu.

### Uzvaras ceļa atrašana

Pēc spēles algoritma pielietošanas tiek meklēts uzvaras ceļš. Šajā procesā tiek apskatīti visi ceļi no saknes līdz lapām, lai atrastu un izvēlētos ceļu ar maksimālo vērtējumu. Tas ir darbības solis, kurā tiek meklēts ceļš, kas nes vislielāko ieguvumu un mērķtiecīgi virzās uz spēles uzvaru.

Uzvaras ceļa atrašanai tiek izmantots spēles koka algoritms, kura pamatā ir Minimax vai AlphaBeta metode. Katra virsotne vai stāvoklis, ko apmeklē algoritms, tiek novērtēts ar heiristiskajā funkcijā iegūtajiem rezultātiem. Pēc tam, apskatot visus ceļus no saknes līdz lapām, tiek izvēlēts ceļš ar maksimālo vērtējumu, kurš tiek marķēts kā uzvaras ceļš. Uzvaras ceļš tiek atgriezts kā rezultāts, lai to varētu izmantot spēles izvēlētajā gājienā. Tas palīdz spēlētājam veikt optimālo gājienu, kas novedīs viņu uz uzvaru spēlē.

<div style="page-break-after: always;"></div>

## Algoritmu savstārpējais salīdzinājums

Lai salīdzinātu Minimax un AlphaBeta algoritmus tika veikti 10 eksperimenti ar katru no tiem ar dažādu sākuma akmentiņu skaitu un sākuma spēlētāju. Eksperimentu rezultātus var redzēt apakšsniegtajā tabulā:

| Nr. | Stones | Algorithm  | First Player | Time per move | Nodes visited | Score | Winner   | Tree generation time | Tree estimation time |
| --- | ------ | ---------- | ------------ | ------------- | ------------- | ----- | -------- | -------------------- | -------------------- |
| 1   | 50     | Alpha-Beta | player       | 2.809e-05     | 12            | 49:48 | player   | 2.433                | 1.846                |
| 2   | 51     | Alpha-Beta | player       | 2.742e-05     | 12            | 51:50 | player   | 3.817                | 2.446                |
| 3   | 52     | Alpha-Beta | player       | 2.752e-05     | 12            | 52:50 | player   | 4.888                | 3.259                |
| 4   | 53     | Alpha-Beta | player       | 2.727e-05     | 13            | 52:52 | draw     | 6.776                | 4.316                |
| 5   | 54     | Alpha-Beta | player       | 2.782e-05     | 13            | 53:52 | player   | 8.147                | 5.752                |
| 6   | 55     | Alpha-Beta | computer     | 2.994e-05     | 14            | 52:56 | computer | 11.720               | 7.719                |
| 7   | 56     | Alpha-Beta | computer     | 3.014e-05     | 14            | 52:57 | computer | 15.727               | 10.197               |
| 8   | 57     | Alpha-Beta | computer     | 2.961e-05     | 14            | 56:57 | computer | 19.342               | 13.793               |
| 9   | 58     | Alpha-Beta | computer     | 3.806e-05     | 14            | 55:59 | computer | 28.811               | 18.858               |
| 10  | 59     | Alpha-Beta | computer     | 3.294e-05     | 14            | 57:60 | computer | 40.298               | 25.318               |

<div style="page-break-after: always;"></div>

| Nr. | Stones | Algorithm | First Player | Time per move | Nodes visited | Score | Winner   | Tree generation time | Tree estimation time |
| --- | ------ | --------- | ------------ | ------------- | ------------- | ----- | -------- | -------------------- | -------------------- |
| 1   | 50     | Minimax   | player       | 2.736e-05     | 12            | 49:48 | player   | 2.425                | 1.499                |
| 2   | 51     | Minimax   | player       | 2.698e-05     | 12            | 51:50 | player   | 3.782                | 1.998                |
| 3   | 52     | Minimax   | player       | 2.748e-05     | 12            | 52:50 | player   | 4.925                | 2.671                |
| 4   | 53     | Minimax   | player       | 2.749e-05     | 13            | 52:52 | draw     | 6.800                | 3.541                |
| 5   | 54     | Minimax   | player       | 2.742e-05     | 13            | 53:52 | player   | 8.226                | 4.721                |
| 6   | 55     | Minimax   | computer     | 3.072e-05     | 14            | 52:56 | computer | 11.713               | 6.261                |
| 7   | 56     | Minimax   | computer     | 2.989e-05     | 13            | 53:57 | computer | 15.911               | 8.431                |
| 8   | 57     | Minimax   | computer     | 3.016e-05     | 14            | 56:57 | computer | 19.034               | 11.360               |
| 9   | 58     | Minimax   | computer     | 2.965e-05     | 14            | 56:57 | computer | 28.914               | 15.024               |
| 10  | 59     | Minimax   | computer     | 3.188e-05     | 15            | 56:60 | computer | 58.109               | 21.145               |

**Secinājumi par algoritmu salīdzinājumu**:

- Abi algoritmi rada līdzīgu laika patēriņu kārtas nodošanai: tas ir apmēram 2.7 - 3.0e-05 sekundes gan AlphaBeta, gan Minimax
- Abos algoritmos mazāk kā 15 virsotnes tiek apmeklēti, lai veiktu lēmumu, kas liecina par efektīvu problemātikas risināšanu
- AlphaBeta un Minimax rezultāts spēļu iznākumā ir vienāds, balstoties arī uz to, kurš bija pirmā kārta
- Algoritmi atšķiras pēc koka ģenerēšanas laika un koka novērtēšanas laika. Vidēji AlphaBeta algoritms prasa vairāk laika gan koka ģenerēšanai, gan novērtēšanai salīdzinājumā ar Minimax algoritmu. Tas var norādīt uz to, ka AlphaBeta ir sarežģītāks un prasa vairāk resursu savu rezultātu panākšanai
- Kopumā gan Minimax, gan AlphaBeta algoritmi strādā līdzīgi šīs konkrētajās situācijās, bet AlphaBeta algoritms, šķiet, prasa nedaudz vairāk laika un resursu

<div style="page-break-after: always;"></div>

## Secinājumi

Šajā praktiskajā darbā tika izstrādāta spēle "Game of Stones", izmantojot divus algoritmus - Minimax un tā optimizēto versiju AlphaBeta. Tika paveikts plašs un detalizēts darbs, ne tikai radot un analizējot spēles koka struktūru, bet arī pielietojot un testējot šos algoritmus, lai noteiktu efektīvāko stratēģiju spēlē.

Neatkarīgi no tā, vai tika izmantots Minimax vai AlphaBeta, abu algoritmu izpilde bija efektīva, nodrošinot precīzus un savlaicīgus rezultātus. Tomēr, AlphaBeta, būdams Minimax algoritma optimizēta versija, prasīja nedaudz vairāk laika un resursu, kas liecina par tā papildu funkcionalitāti.

Kopumā šis darbs ir efektīvs paraugs, kā var izstrādāt kvalitatīvu un aizraujošu spēli, izmantojot pareizi izvēlētus algoritmus un datu struktūras. Rezultāts ir spēle, kas ne tikai sniedz lielisku spēlētāja pieredzi, bet arī stimulē loģisko domāšanu, jo katra gājiena izvēlē ir jāizvērtē tā ietekme uz galīgo uzvaras ceļu. Tādējādi, šis darbs demonstrē, ka akadēmiskās zināšanas par algoritmiem un datu struktūrām var tikt veiksmīgi pielietotas praktiskā veidā - radot aizraujošas un intelektuāli izaicinošas spēles.

<div style="page-break-after: always;"></div>

## Pielikumi

### Pielikums 1 - GameState klase

```python
class GameState:
    stones_left: int = field(hash=True)
    player_turn: Literal["computer", "player"] = field(hash=True)
    computer_points: int = field(default=0, hash=True)
    player_points: int = field(default=0, hash=True)
    computer_stones: int = field(default=0, hash=True)
    player_stones: int = field(default=0, hash=True)
    _estimation_value: int | None = field(default=None, init=False, hash=False)
    parent: "GameState | None" = field(default=None, init=False, hash=False)
    children: list["GameState"] = field(default_factory=list, init=False, hash=False)
```

### Pielikums 2.1 - Heiristiskā funkcija Minimax algoritmā

```python
    def estimate(self, root: GameState) -> None:
        for node in root.post_order_traversal():
            if node.children:
                self._estimate_node(node)
            else:
                self._estimate_leaf(node)

    def _estimate_leaf(self, node: GameState) -> None:
        computer_total = node.computer_stones + node.computer_points
        player_total = node.player_stones + node.player_points

        if computer_total > player_total:
            node.estimation_value = 1
        elif computer_total == player_total:
            node.estimation_value = 0
        else:
            node.estimation_value = -1

    def _estimate_node(self, node: GameState) -> None:
        if node.player_turn == "computer":
            node.estimation_value = max(
                child.estimation_value for child in node.children if child.estimation_value is not None
            )
        else:
            node.estimation_value = min(
                child.estimation_value for child in node.children if child.estimation_value is not None
            )
```

### Pielikums 2.2 - Heiristiskā funkcija AlphaBeta algoritmā

```python
    def estimate(
        self, root: GameState, alpha: float = -float("inf"), beta: float = float("inf")
    ) -> None:
        for node in root.post_order_traversal():
            if node.children:
                self._estimate_node(node, alpha, beta)
            else:
                self._estimate_leaf(node)

    def _estimate_leaf(self, node: GameState) -> None:
        computer_total = node.computer_stones + node.computer_points
        player_total = node.player_stones + node.player_points

        if computer_total > player_total:
            node.estimation_value = 1
        elif computer_total == player_total:
            node.estimation_value = 0
        else:
            node.estimation_value = -1

    def _estimate_node(self, node: GameState, alpha: float, beta: float) -> None:
        if node.player_turn == "computer":
            max_value = -float("inf")
            for child in node.children:
                if child.estimation_value is not None:
                    max_value = max(max_value, child.estimation_value)
                    alpha = max(alpha, max_value)
                    if beta <= alpha:
                        break
            node.estimation_value = max_value
        else:
            min_value = float("inf")
            for child in node.children:
                if child.estimation_value is not None:
                    min_value = min(min_value, child.estimation_value)
                    beta = min(beta, min_value)
                    if beta <= alpha:
                        break
            node.estimation_value = min_value
```
