# Table of Contents

1. [Full-Lexicon](#Full-Lexicon)
1. [Binary-Operators](#Binary-Operators)
1. [Comparions-Operators](#Comparions-Operators)
1. [Instanciation](#Instanciation)
1. [Truth-Values](#Truth-Values)
1. [Parenthesis](#Parenthesis)
1. [Functions](#Functions)
1. [If-Else-Statements](#If-Else-Statements)
1. [While-Loops](#While-Loops)
1. [Lists](#Lists)
1. [Dictionaries](#Dictionaries)

## <a name='Full Lexicon'>Full Lexicon</a>

| Hællang               | Python              |
| --------------------- | ------------------- |
| plussær               | PLUS                |
| minusær               | MINUS               |
| delær                 | DIVIDE              |
| gangær                | MULTIPLY            |
| mådda-med             | MODULO              |
| ære-samma-som         | EQUALS              |
| hællæ                 | LPAREN              |
| prekæs                | RPAREN              |
| småære-enn            | LT                  |
| mere-enn              | GT                  |
| er-prikk-lik          | EQ                  |
| dersom-atter          | IF                  |
| så                    | THEN                |
| ellers                | ELSE                |
| åsså-æru-ferdig       | END_OF_IF_THEN_ELSE |
| ente-gjør-no          | PASS                |
| imens                 | WHILE               |
| ta-åsså-gjør          | DO                  |
| åsså-gjøru-det-igjen  | END_OF_WHILE        |
| spøtt-ut              | PRINT               |
| klart-det             | TRUE                |
| ente-rekti            | FALSE               |
| gi-dæ                 | BREAK               |
| en-bråtæ-beståænes-av | START_OF_LIST       |
| å                     | LIST_ITEM_SEPARATOR |
| å-det-var-det         | END_OF_LIST         |
| legg-te               | APPEND              |
| i-bråtæn              | IN_LIST             |
| størlsen-a            | LENGTH              |
| græbb-fra             | POP                 |
| plass-nummer          | ARRAY_INDEX         |
| kåmma                 | COMMA               |
| e-orlbok-beståænes-av | START_OF_DICT       |
| å-så-var-orlboka-færi | END_OF_DICT         |
| betyænes              | KEY_VALUE_SEPARATOR |
| slå-opp               | DICT_LOOKUP         |
| i-orlboka             | IN_DICT             |
| fjærn                 | DICT_REMOVE         |

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

## <a name='Functions'>Functions</a>

| Hællang      | Python   |
| ------------ | -------- |
| spøtt-ut x   | print(x) |
| gi-dæ        | break    |
| ente-gjør-no | pass     |

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
| å-det-var-det                                             | ]           |
| x legg-te y                                               | x.append(y) |
| græbb-fra x                                               | x.pop()     |
| plass-nummer i i-bråtæn x                                 | x[i]        |
| størlsen-a x                                              | len(x)      |
| x ære-samma-som en-bråtæ-beståænes-av x å y å_det_var_det | x = [x, y]  |

## <a name='Dictionaries'>Dictionaries</a>

| Hællang                 | Python     |
| ----------------------- | ---------- |
| e-orlbok-beståænes-av   | {          |
| x betyænes y            | x: y       |
| å-så-var-orlboka-færi   | }          |
| slå-opp key i-orlboka x | x[key]     |
| fjærn key i-orlboka x   | x.del(key) |
