symbols = '$¢£¥€¤'

# build list using traditional way
codes = []
for symbol in symbols:
    codes.append(symbol)
print(codes)

# build list using listcomps
codes = [symbol for symbol in symbols]
print(codes)


x = 'ABC'
codes = [ord(x) for x in x]
print(x)
print(codes)
codes = [last := ord(c) for c in x]
print(last)
# print(c)  # NameError: c not defined

beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

