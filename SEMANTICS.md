# Table of Contents

1. [Full-Lexicon](#Full-Lexicon)
1. [Binary-Operators](#Binary-Operators)
1. [Comparions-Operators](#Comparions-Operators)
1. [Instanciation](#Instanciation)
1. [Truth-Values](#Truth-Values)
1. [Parenthesis](#Parenthesis)
1. [If-Else-Statements](#If-Else-Statements)
1. [While-Loops](#While-Loops)
1. [Lists](#Lists)
1. [Dictionaries](#Dictionaries)
1. [Functions](#Functions)
1. [Built-in-Functions](#Built-in-Functions)
1. [Import-Statements](#Import-Statements)

## <a name='Full Lexicon'>Full Lexicon</a>

| Hællang                      | Python                    |
| ---------------------------- | ------------------------- |
| plussær                      | PLUS                      |
| minusær                      | MINUS                     |
| delær                        | DIVIDE                    |
| gangær                       | MULTIPLY                  |
| mådda-med                    | MODULO                    |
| ære-samma-som                | EQUALS                    |
| hællæ                        | LPAREN                    |
| prekæs                       | RPAREN                    |
| småære-enn                   | LT                        |
| mere-enn                     | GT                        |
| er-prikk-lik                 | EQ                        |
| dersom-atter                 | IF                        |
| så                           | THEN                      |
| ente-gjør-no                 | PASS                      |
| ellers                       | ELSE                      |
| åsså-æru-ferdig              | END_OF_IF_THEN_ELSE       |
| imens                        | WHILE                     |
| ta-åsså-gjør                 | DO                        |
| åsså-gjøru-det-igjen         | END_OF_WHILE              |
| spøtt-ut                     | PRINT                     |
| klart-det                    | TRUE                      |
| ente-rekti                   | FALSE                     |
| gi-dæ                        | BREAK                     |
| en-bråtæ-beståænes-av        | START_OF_LIST             |
| å                            | LIST_ITEM_SEPARATOR       |
| å-det-var-det                | END_OF_LIST               |
| legg-te                      | PUSH                      |
| i-bråtæn                     | IN_LIST                   |
| græbb-fra                    | POP                       |
| plass-nummer                 | ARRAY_INDEX               |
| en-fungsjon                  | FUNCTION                  |
| såm-brukær                   | WITH_PARAMS               |
| såm-gjør                     | START_OF_FUNCTION         |
| åså-varn-færi                | END_OF_FUNCTION           |
| kjør                         | RUN                       |
| med                          | WITH                      |
| gi-tilbake                   | RETURN                    |
| kåmma                        | COMMA                     |
| e-orlbok-beståænes-av        | START_OF_DICT             |
| å-så-var-orlboka-færi        | END_OF_DICT               |
| betyænes                     | DICT_PAIR_SEPARATOR       |
| slå-opp                      | DICT_LOOKUP               |
| i-orlboka                    | IN_DICT                   |
| størlsen-a                   | LENGTH                    |
| fjærn                        | DICT_REMOVE               |
| hent-ut-pytonslange-funksjon | IMPORT                    |
| å-kallen-for                 | AS                        |
| i-samma-slengen              | END_OF_IMPORT             |
| dått                         | IMPORT_FUNCTION_SEPARATOR |

## <a name='Binary Operators'>Binary Operators</a>

| Hællang       | Python |
| ------------- | ------ |
| x plussær y   | x + y  |
| x minusær y   | x - y  |
| x gangær y    | x \* y |
| x delær y     | x / y  |
| x mådda-med y | x % y  |

## <a name='Comparions Operators'>Comparions Operators</a>

| Hællang          | Python |
| ---------------- | ------ |
| x småære-enn y   | x < y  |
| x mere-enn y     | x > y  |
| x er-prikk-lik y | x == y |

## <a name='Instanciation'>Instanciation</a>

| Hællang           | Python       |
| ----------------- | ------------ |
| x ære-samma-som y | x = y        |
| x kåmma y         | float("x.y") |

## <a name='Truth Values'>Truth Values</a>

| Hællang    | Python |
| ---------- | ------ |
| klart-det  | True   |
| ente-rekti | False  |

## <a name='Parenthesis'>Parenthesis</a>

| Hællang | Python |
| ------- | ------ |
| hællæ   | (      |
| prekæs  | )      |

## <a name='If Else Statements'>If Else Statements</a>

| Hællang                                               | Python                |
| ----------------------------------------------------- | --------------------- |
| dersom-atter                                          | if                    |
| så                                                    | THEN                  |
| ellers                                                | else                  |
| åsså-æru-ferdig                                       | END_OF_IF_THEN_ELSE   |
| dersom-atter ... så ... ellers så ... åsså-æru-ferdig | if ...: ... else: ... |

## <a name='While Loops'>While Loops</a>

| Hællang                                                                                          | Python                              |
| ------------------------------------------------------------------------------------------------ | ----------------------------------- |
| imens                                                                                            | while                               |
| ta-åsså-gjør                                                                                     | DO                                  |
| åsså-gjøru-det-igjen                                                                             | END_OF_WHILE                        |
| imens x småære-enn 10 ta-åsså-gjør spøtt-ut x. x ære-samma-som x plussær 1. åsså-gjøru-det-igjen | while x < 10: print(x) \n x = x + 1 |

## <a name='Lists'>Lists</a>

| Hællang                                                   | Python      |
| --------------------------------------------------------- | ----------- |
| en-bråtæ-beståænes-av                                     | [           |
| x å y                                                     | x, y        |
| å_det_var_det                                             | ]           |
| x legg-te y å-det-var-det                                 | x.append(y) |
| græbb-fra x å-det-var-det                                 | x.pop()     |
| plass-nummer i i-bråtæn x å-det-var-det                   | x[i]        |
| størlsen-a x å-det-var-det                                | len(x)      |
| endre plass-nummer i i-bråtæn x te 0 å-det-var-det        | x[i] = 0    |
| x ære-samma-som en-bråtæ-beståænes-av x å y å-det-var_det | x = [x, y]  |

## <a name='Dictionaries'>Dictionaries</a>

| Hællang                                        | Python     |
| ---------------------------------------------- | ---------- |
| e-orlbok-beståænes-av                          | {          |
| x betyænes y                                   | x: y       |
| å-så-var-orlboka-færi                          | }          |
| slå-opp key i-orlboka x å-det-var-det          | x[key]     |
| legg-te x betyænes y i-orlboka z å-det-var-det | z[x] = y   |
| fjærn key i-orlboka x å-det-var-det            | x.del(key) |

## <a name='Functions'>Functions</a>

| Hællang                                                                       | Python               |
| ----------------------------------------------------------------------------- | -------------------- |
| f ære-samma-som en-fungsjon som-gjør åså-varn-færi                            | def f():             |
| f ære-samma-som en-fungsjon som-brukær a å b som-gjør åså-varn-færi           | def f(a,b):          |
| gi-tilbake x                                                                  | return x             |
| åså-varn-færi                                                                 | END_OF_FUNCTION      |
| f ære-samma-som en-fungsjon som-brukær a å b som-gjør return a åså-varn-færi, | def f(a,b): return a |
| kjør f med 1 å 2 å-det-var-det                                                | f(1,2)               |

## <a name='Built in Functions'>Built in Functions</a>

| Hællang           | Python           |
| ----------------- | ---------------- |
| spøtt-ut x        | print(x)         |
| spøtt-ut-uten-n x | print(x, end='') |
| gi-dæ             | break            |
| ente-gjør-no      | pass             |

## <a name='Import Statements'>Import Statements</a>

| Hællang                                                                | Python               |
| ---------------------------------------------------------------------- | -------------------- |
| hent-ut-pytonslange-funksjon "math" å-kallen-for matte i-samma-slengen | import math as matte |
| kjør matte dått sin med π/2 å-det-var-det                              | math.sin(π/2)        |
