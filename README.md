## Synopsis
`rsi1751` is a means for a human to transmit binary data by typing on a keyboard.  Its concept is ripped off from [RFC 1751](https://tools.ietf.org/rfc/rfc1751.txt), and if you send enough data this way you're bound to get [RSI](https://en.wikipedia.org/wiki/Repetitive_strain_injury).  Hence the punny name.

## Motivation
If this idea sounds familiar, it's because this is exactly how uuencode,
base64, base85 and friends work.

### ...Why would a human send data this way?
Surprisingly often, I find myself needing to transfer files to and from an
old computer that does not support networking or any sensible type of mass
storage device.

### Why not base64?
Sure, base64 is more space-efficient, but it's absolutely *impossible* to type.  RSI 1751 uses human-readable words that are easy to type, and it has parity error-detection to catch the inevitable brain farts and typos.

### Why not just type hex digits?
That's too slow, painful and error-prone even for me.

## Example

### Encoding itself

````
$ python2 rsi1751.py --b2h < rsi1751.py
````

becomes...

````
    1   nor sex dry lay net map put win
    2   cry sun cry all all end put sum
    3   fit neo oil put map lay dry now
    4   put car far far put map neo job
    5   net oil oil job mix oil map off
    6   map oil net put aid lay net run
````

etc.

### Decoding itself

````
$ python2 rsi1751.py --h2b
norsexdrylaynetmapputwin
crysuncryallallendputsum
fitneooilputmaplaydrynow
putcarfarfarputmapneojob
netoiloiljobmixoilmapoff
mapoilnetputaidlaynetrun
````

becomes...

````
import sys

# The top 100 three-letter wor
````

...


### How fast is it?
... Not fast.  If you're a fast typist, you can transfer files at about 1/5 the
speed of a 110 baud modem, or 1/30000 the speed of dialup.

````
>>> wpm = 100        # A fast typist types 100 words-per-minute
>>> cpm = wpm*5      # A word-unit is 5 characters.
>>> bpm = cpm/3.     # A 3-character rsi1751 word translates to one byte.
>>> bpm = bpm*(7/8.) # Parity overhead:  line is 7bytes data + 1byte parity
>>> bps = bpm/60.    # Bytes per second
>>> bps
2.4305555555555554

>>> baud = bps*8     # Bits per second
>>> baud
19.444444444444443
````

## License
This... thing... is public domain in case anyone wants it.
