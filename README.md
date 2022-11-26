# The Hællang Programming Language

### [Creators](https://github.com/Futhark-AS/haellang/blob/main/CONTRIBUTORS.md)

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

# [Click here for semantics](https://github.com/Futhark-AS/haellang/blob/main/SEMANTICS.md)

##### Example Code

###### example_code/torus.haellae by Simen Sandhaug

![Donut](https://s1.gifyu.com/images/c962105be7b6c749f0ab16e7f1b20d9c-_1_.gif)

###### example_code/primes.haellae by Halvor Linder Henriksen

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
