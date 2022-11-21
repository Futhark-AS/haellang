# The Hællang Programming Language

![Hællang Logo](logo/Haellang_logo.png)

#### The number one programming language for østfoldingær

> # Installation

1. Create a folder for the project
2. In the terminal type `git clone https://github.com/Futhark-AS/haellang.git`
3. Move into the folder and create a virtual environment with `python -m venv venv`
4. Activate virtual environment
   - For windows: `source venv/Scripts/activate`
   - For mac: `source venv/bin/activate`
5. Install requirements `pip install -r requirements.txt`

Now you can you write a .haellae file in Hællang and run it using the command: `python haellang.py path-to-file/file.haellae`

> # Semantics

| Hællang Code                                        | Python Interpretation                                      |
| --------------------------------------------------- | ---------------------------------------------------------- |
| .                                                   | END_OF_STATEMENT                                           |
| dersom-atter .. så .. ellers så .. åsså-æru-ferdig. | IF .. THEN .. ELSE THEN .. END_OF_IF_ELSE END_OF_STATEMENT |
| gi-dæ                                               | BREAK                                                      |
| dra-tebake-deru-kom-fra                             | END_OF_FUNCTION                                            |
| ta-meræ                                             | RETURN                                                     |
| imens .. ta-åsså-gjør .. åsså-gjøru-det-igjen       | WHILE .. DO .. END_OF_WHILE                                |
| spøtt-ut                                            | PRINT                                                      |
| mere-enn, småære-enn, ære-samma-som                 | GT, LT, EQUALS                                             |
| plussær, minusær, delær, gangær, mådda-med          | PLUS, MINUS, TIMES, DIVIDE, MOD                            |
| hællæ, prekæs                                       | LPAREN, RPAREN                                             |
| ær-prikk-lik                                        | EQ                                                         |
| ente-gjør-no                                        | PASS                                                       |
| klart-det                                           | TRUE                                                       |
| ente-rekti                                          | FALSE                                                      |
| en-bråtæ-beståænes-av .. å .. å-det-var-det         | START_OF_LIST .. LIST_SEPARATOR .. END_OF_LIST             |
| legg-te .. på x                                     | x.append(..)                                               |
| græbb-fra x                                         | x.pop()                                                    |
| plass-nummer .. på x                                | x[..]                                                      |

> ##### Example Code

```
n ære samma som 2.
imens n småære enn 100 ta åsså gjør
    p ære samma som klart det.
    d ære samma som 2.
    imens d småære enn n delær 2 plussær 1 ta åsså gjør
        dersom atter
            hællæ n mådda med d prekæs er prikk lik 0
        så
            p ære samma som ente rekti.
            gi dæ.
        ellers så
            ente gjør no,
        åsså æru ferdig.
        d ære samma som d plussær 1.
    åsså gjøru det igjen.
    dersom atter
        p
    så
        spøtt ut n.
    ellers så
        ente gjør no.
    åsså æru ferdig.
    n ære samma som n plussær 1.
åsså gjøru det igjen.
```

```python
n = 2
while n < 100:
  p = True
  d = 2
  while d < n / 2 + 1:
      if (n % d) == 0:
          p = False
          break
      else:
          pass
      d = d + 1
  if p:
      print(n)
  else:
      pass
  n = n + 1
# Prints all prime numbers from 1 to 100
```
