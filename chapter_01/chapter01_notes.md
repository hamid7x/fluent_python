# Fluent Python - Chapter 1 Notes

These are my personal notes while studying Chapter 1 of *Fluent Python*.  
The goal here is to understand how Python really works under the hood, especially objects, names, and attribute lookup.

---

## 1. Everything in Python is an object

In Python, everything is an object:
- numbers
- strings
- lists
- functions
- classes

So when we write:

```python
x = 5
```

`5` is an object, and `x` is just a name pointing to it.

---

## 2. Names are just labels (binding)

A variable is not the value itself. It's just a name (label) bound to an object.

```python
count = 5
```

This means:
1. create object `5`
2. bind (attach) the name `count` to that object

So mentally:

```
count ───► 5
```

We can rebind the name:

```python
count = 10
```

Now:

```
count ───► 10
```

---

## 3. Namespaces

A namespace is basically a mapping of:

```
name → object
```

Examples:
- global namespace
- local namespace (inside functions)
- class namespace
- instance namespace

You can think of it like a dictionary.

---

## 4. Instance attributes and `__dict__`

When you create an object:

```python
obj = MiniList([1, 2, 3])
```

Python stores instance attributes inside:

```python
obj.__dict__
```

Example:

```python
obj.x = 100
```

Internally:

```python
obj.__dict__ = {"x": 100}
```

So instance attributes live inside `__dict__`.

---

## 5. Attribute lookup order

When you access an attribute:

```python
obj.x
```

Python searches in this order:

1. Instance attributes (`obj.__dict__`)
2. Class attributes (`Class.__dict__`)
3. Parent classes (MRO)
4. `__getattr__` (if defined)

If nothing is found, Python raises `AttributeError`.

---

## 6. `__getattribute__` and `__getattr__`

### `__getattribute__`
- Called for **every** attribute access
- Runs first

```python
obj.x  →  __getattribute__("x")
```

### `__getattr__`
- Called **only if** attribute is not found

```python
obj.y  →  not found  →  __getattr__("y")
```

---

## 7. Data model methods

Python allows objects to behave like built-in types by implementing special methods.

### `__len__`
Defines behavior for `len(obj)`

```python
class MiniList:
    def __len__(self):
        return len(self._data)
```

Usage:

```python
len(obj)
```

### `__getitem__`
Defines indexing and iteration behavior

```python
class MiniList:
    def __getitem__(self, key):
        return self._data[key]
```

Usage:

```python
obj[0]
obj[-1]
```

Also used internally in loops:

```python
for x in obj:
    ...
```

### `__iter__` *(optional but common)*
Used to make an object iterable:

```python
def __iter__(self):
    return iter(self._data)
```

---

## 8. Example: `MiniList`

```python
class MiniList:
    def __init__(self, data):
        self._data = data

    def __repr__(self):
        return f"MiniList({self._data})"

    def __len__(self):
        return len(self._data)

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __contains__(self, item):
        return item in self._data

    def __getattribute__(self, name):
        print(f"accessing {name}")
        return super().__getattribute__(name)

    def __getattr__(self, name):
        return f"{name} not exist"
```

---

## 9. Key ideas to remember

- Variables are just names
- Names point to objects
- Objects live in memory
- Namespaces store mappings of `names → objects`
- Attribute access follows a lookup chain
- Special methods let us customize object behavior

---

## 10. Final mental model

```
name (variable)
   ↓
namespace (mapping)
   ↓
object in memory
```

And for attributes:

```
obj.x
  ↓
instance __dict__
  ↓
class __dict__
  ↓
parent classes (MRO)
  ↓
__getattr__
```