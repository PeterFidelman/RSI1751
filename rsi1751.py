import sys

# The top 100 three-letter words in NGSL v1.01
words = \
["the", "and", "you", "for", "par", "not", "ion", "she", "but", "say", "all",
"one", "can", "get", "who", "see", "out", "use", "now", "new", "way", "any",
"day", "how", "may", "man", "too", "sin", "lot", "try", "own", "ask", "put",
"old", "off", "end", "why", "let", "mid", "big", "set", "run", "few", "pay",
"yes", "job", "non", "buy", "far", "car", "bad", "age", "low", "pre", "yet",
"cue", "bit", "sit", "ago", "per", "top", "win", "eye", "add", "law", "war",
"die", "cut", "eat", "boy", "act", "kid", "ray", "air", "due", "lie", "arm",
"art", "key", "bat", "ton", "son", "bed", "hit", "fit", "guy", "dye", "hip",
"tax", "gut", "aim", "sub", "red", "lab", "bus", "fin", "bar", "box", "fly",
"hot", "dog", "oil", "fun", "rub", "neo", "nor", "fix", "sea", "mix", "sex",
"leg", "lay", "dry", "gas", "net", "cry", "map", "bag", "pop", "aid", "fan",
"sun", "sum", "egg", "gun", "fee", "cup", "tie", "ice", "wed", "odd", "tea",
"row", "dad", "fat", "tip", "ear", "cat", "ban", "sad", "sky", "ill", "via",
"hat", "gap", "bet", "toy", "gay", "owe", "era", "wet", "mom", "sir", "pub",
"bid", "van", "web", "log", "god", "tap", "lip", "pen", "dig", "cap", "rid",
"mad", "joy", "pig", "pot", "cow", "bin", "ski", "pro", "raw", "rat", "two",
"six", "ten", "fax", "hey", "mum", "nod", "pet", "zoo", "bay", "pie", "pin",
"pit", "jet", "beg", "jam", "bow", "dot", "bye", "sue", "tag", "fig", "spy",
"cop", "shy", "pad", "fur", "dip", "con", "wow", "nut", "kit", "lad", "gym",
"tin", "hug", "mud", "fry", "opt", "rip", "pan", "lap", "toe", "bee", "bug",
"hop", "cab", "rap", "sew", "ash", "ink", "hut", "flu", "wit", "vet", "vow",
"fox", "rob", "jar", "dam", "jaw", "rod", "hum", "oak", "lid", "rib", "dim",
"arc", "ant", "ass", "rig", "ram", "sip", "rag", "pat", "rug", "sow", "mug",
"wax", "fog", "lag"]


def byteToWord(i):
	return words[i]

# returns byte 0..255, or 256 on unrecognized word
def wordToByte(word):
	try:
		return words.index(word)
	except ValueError:
		return 256

# bytes to english
def b2e():
	chars = "".join(sys.stdin.readlines())
	bytea = bytearray(chars)
	for b in bytea:
		print byteToWord(b),

# bytes to printout
# the format of a printout is n words plus one parity word
def b2p(wordsPerLine):
	chars = "".join(sys.stdin.readlines())
	bytea = bytearray(chars)
	lineno = 0
	colno = 0
	parity = 0

	for b in bytea:
		if colno == 0:
			print "%5d\t" % lineno,
		parity ^= b
		colno += 1
		print byteToWord(b),
		if colno == wordsPerLine:
			colno = 0
			print byteToWord(parity)
			parity = 0
			lineno += 1

# english to bytes
def e2b():
	# workaround to keep Windows from munging binary data
	# http://stackoverflow.com/a/2374443
	if sys.platform == "win32":
		import os, msvcrt
		msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)

	chars = "".join(sys.stdin.readlines())
	worda = chars.split()
	for w in worda:
		i = wordToByte(w)
		if i == 256:
			raise Exception("Bad word %s" % w)
		sys.stdout.write(chr(i))

def usage():
	print
	print "usage:  " + str(sys.argv[0]) + " [--e2b] [--b2e]"
	print "    --e2b        english to bytes"
	print "    --b2e        bytes to english"
	print "    --b2p        bytes to printout"
	print

def main():
	try:
		mode = sys.argv[1]
	except:
		mode = None

	if (mode == "--e2b"):
		e2b()
	elif (mode == "--b2e"):
		b2e()
	elif (mode == "--b2p"):
		b2p(4)
	else:
		usage()

# run main
if __name__ == "__main__":
	main()