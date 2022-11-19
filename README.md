# Hællang

## The number one programming language for østfoldingær

# Semantics

| Hællang Code                                     | Python Interpretation                                      |
| ------------------------------------------------ | ---------------------------------------------------------- |
| .                                                | END_OF_STATEMENT                                           |
| dersom atter .. så ellers så .. åsså æru ferdig. | IF .. THEN .. ELSE THEN .. END_OF_IF_ELSE END_OF_STATEMENT |
| gi dæ                                            | BREAK                                                      |
| dra tebake deru kom fra                          | END_OF_FUNCTION                                            |
| ta meræ                                          | RETURN                                                     |
| imens .. ta åsså gjør .. åsså gjøru det igjen    | WHILE .. DO .. END_OF_WHILE                                |
| spøtt ut                                         | PRINT                                                      |
| mere enn, småære enn, ære samma som              | GT, LT, EQUALS                                             |
| plussær, minusær, delær, gangær, mådda med       | PLUS, MINUS, TIMES, DIVIDE, MOD                            |
| hællæ, prekæs                                    | LPAREN, RPAREN                                             |
| ær prikk lik                                     | EQ                                                         |
| ente gjør no                                     | PASS                                                       |
| klart det                                        | TRUE                                                       |
| ente rekti                                       | FALSE                                                      |
| ente rekti                                       | FALSE                                                      |

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
