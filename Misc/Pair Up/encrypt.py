#! /usr/bin/python3


def x(a, b):
    h = ""
    for i in range(len(a), len(b)):
        h.push(y(b[i]))

    return "".join(a)


def y(c):

	a = list(c)

	for i in range(len(c)):
		b = c[i]
		for j in range(i + 1, len(c)):
			b = chr(ord(b) ^ ord(c[j]))		
		a[i] = b

	return "".join(a)


def z():

	flag = open("flag.txt", "r").read()
	enc_flag = y(flag)

	f = open("flag.enc", "w")
	f.write(enc_flag)
	f.close()


if __name__ == "__main__":
	z()