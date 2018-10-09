import des
import sys


if __name__ == '__main__':
    infile = sys.argv[1]
    outfile = sys.argv[2]
    keyfile = sys.argv[3]

    keyf = open(keyfile)
    key = keyf.read()
    keyf.close()

    keys = des.create_keys(key)


    inf = open(infile)
    inbits = des.str_to_bits(inf.read())
    outbits = [des.round_runner(x, keys) for x in inbits]
    chars = des.bits_to_str(outbits)
    outf = open(outfile, 'w+')
    outf.write(chars)
    outf.close