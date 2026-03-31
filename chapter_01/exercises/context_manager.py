class ContextManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename)
        return self.file

    def __exit__(self, exc_type, exc, tb):
        self.file.close()
        if exc_type:
            print(f'Error: {exc} handled')
            return True


with ContextManager('file.txt') as f:
    # print(1 / 0)
    print(f.read())

# c = ContextManager('file.txt')
# f = c.__enter__()
# print(f.read())
# c.__exit__(None, None, None)
print(f.closed)
