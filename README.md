# The Hællang Programming Language

[Creators](https://github.com/Futhark-AS/haellang/blob/main/CONTRIBUTORS.md)

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

```python
reserved = {
    'plussær':'PLUS',
    'minusær':'MINUS',
    'gangær':'TIMES',
    'delær':'DIVIDE',
    'mådda-med':'MOD',
    'ære-samma-som':'EQUALS',
    'hællæ':'LPAREN',
    'prekæs':'RPAREN',
    'småære-enn':'LT',
    'mere-enn':'GT',
    'er-prikk-lik':'EQ',
    'dersom-atter':'IF',
    'så':'THEN',
    'ente-gjør-no':'PASS',
    'ellers':'ELSE',
    'åsså-æru-ferdig':'END_OF_IF_THEN_ELSE',
    'imens':'WHILE',
    'ta-åsså-gjør':'DO',
    'åsså-gjøru-det-igjen':'END_OF_WHILE',
    'spøtt-ut':'PRINT',
    'klart-det':'TRUE',
    'ente-rekti':'FALSE',
    'gi-dæ':'BREAK',
    'en-bråtæ-beståænes-av':'START_OF_LIST',
    'å':'LIST_ITEM_SEPARATOR',
    'å-det-var-det':'END_OF_LIST',
    'legg-te':'PUSH',
    'i-bråtæn':'IN_LIST',
    'græbb-fra':'POP',
    'plass-nummer':'ARRAY_INDEX',
    'kåmma':'COMMA',
    'e-orlbok-beståænes-av':'START_OF_DICT',
    'å-så-var-orlboka-færi':'END_OF_DICT',
    'betyænes':'DICT_PAIR_SEPARATOR',
    'slå-opp':'DICT_LOOKUP',
    'i-orlboka':'IN_DICT',
    'størlsen-a':'LENGTH',
    'fjærn':'DICT_REMOVE',
}
```

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
