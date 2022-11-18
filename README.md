# Hællang

## The number one programming language for østfoldingær

# Semantics

| Hællang Code                                     | Python Interpretation |
| ------------------------------------------------ | --------------------- |
| dersom atter, ellers                             | if, else              |
| gi dæ                                            | break                 |
| dra tebake deru kom fra                          | end of function       |
| ta meræ                                          | return                |
| så lenge .. ta åsså gjør .. åsså gjøru det igjen | while                 |
| spøtt ut                                         | print                 |
| mere enn, småære enn, ære samma som              | >, <, =               |
| plussær, minusær, delær, gangær                  | +, -, \*, /           |
| startparangtes, endeparangtes                    | (, )                  |
| ær prikk lik                                     | ==                    |
| ente gjør no                                     | pass                  |
| klart det                                        | true                  |
| ente rekti                                       | false                 |

##### Example Code

```python
x ære samma som 4.
# x = 4
dersom atter x er mere enn 2
så spøtt ut x ellers så
ente gjør no åsså æru ferdig.
# if x > 2
# then print(x)
# else pass
# end of if-then-else
```

<statement> :=
| <statement><statement>
| dersom atter <expression> så <statement> ellers så <statement> åsså æru ferdig.
| <variable> ære samma som <expression>.
| gi dæ.
| så lenge <expression> ta åsså gjør <statement> åsså gjøru det igjen.
| spøtt utt <expression>.
| ente gjør no.

<expression> :=
| <expression> ær prikk lik <expression>
| <expression> mere enn <expression>
| <expression> småære enn <expression>
| <expression> plussær <expression>
| <expression> minusær <expression>
| <expression> delær <expression>
| <expression> gangær <expression>
| hællæ <expression> prekæs
| <number>
| <bool>

<number> := -[0-9]+

<bool> :=
| klart det
| ente rekti

<variable> := [a-z A-Z][a-z a-z 0-9 _]\*
