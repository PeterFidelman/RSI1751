## Synopsis
`rsi1751` is a means for a human to transmit binary data by typing on a
keyboard.  Its concept is ripped off from
[RFC 1751](https://tools.ietf.org/rfc/rfc1751.txt), hence the punny name.

## Example

### Encoding itself
`$ python2 rsi1751.py --b2h < rsi1751.py`
becomes...
`    0   nor sex dry lay net map put win`
`    1   cry sun cry all all end put sum`
`    2   fit neo oil put map lay dry now`
`    3   put car far far put map neo job`
`    4   net oil oil job mix oil map off`
`    5   map oil net put aid lay net run`
etc.

### Decoding itself
`$ python2 rsi1751.py --h2b`
`norsexdrylaynetmapputwin`
`crysuncryallallendputsum`
`fitneooilputmaplaydrynow`
`putcarfarfarputmapneojob`
`netoiloiljobmixoilmapoff`
`mapoilnetputaidlaynetrun`

becomes...

`import sys`
` `
`# The top 100 three-letter wor`
...

## Motivation
If this idea sounds familiar, it's because this is exactly how uuencode,
base64, base85 and friends work.

### ...Why?
Surprisingly often, I find myself needing to transfer files to and from an
old computer that does not support networking or any sensible type of mass
storage device.

### Why not base64?
Sure, it's more efficient, but it's absolutely *impossible* to type.

### Why not just type hex digits?
That's too slow and painful even for me.

### How fast is it?
... Not fast.  If you're a fast typist, you can transfer files at about 1/5 the
speed of a 110 baud modem, or 1/30000 the speed of dialup.

``
`>>> wpm = 100        # A fast typist types 100 words-per-minute`
`>>> cpm = wpm*5      # A word-unit is 5 characters.`
`>>> bpm = cpm/3.     # A 3-character rsi1751 word translates to one byte.`
`>>> bpm = bpm*(7/8.) # Parity overhead:  line is 7bytes data + 1byte parity`
`>>> bps = bpm/60.    # Bytes per second`
`>>> bps`
`2.4305555555555554`

`>>> baud = bps*8     # Bits per second`
`>>> baud`
`19.444444444444443`

## License
This... thing... is public domain in case anyone wants it.
