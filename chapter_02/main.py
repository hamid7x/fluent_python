from collections import abc

print(issubclass(list, abc.Sequence))
print(issubclass(list, abc.MutableSequence))
print(issubclass(tuple, abc.Sequence))
print(issubclass(tuple, abc.MutableSequence))
