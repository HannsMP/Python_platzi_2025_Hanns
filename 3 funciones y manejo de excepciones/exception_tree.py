def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

print_exception_hierarchy(Exception)

#   Exception
#       ArithmeticError
#           FloatingPointError
#           OverflowError
#           ZeroDivisionError
#       AssertionError
#       AttributeError
#       BufferError
#       EOFError
#       ImportError
#           ModuleNotFoundError
#           ZipImportError
#       LookupError
#           IndexError
#           KeyError
#           CodecRegistryError
#       MemoryError
#       NameError
#           UnboundLocalError
#       OSError
#           BlockingIOError
#           ChildProcessError
#           ConnectionError
#               BrokenPipeError
#               ConnectionAbortedError
#               ConnectionRefusedError
#               ConnectionResetError
#           FileExistsError
#           FileNotFoundError
#           InterruptedError
#           IsADirectoryError
#           NotADirectoryError
#           PermissionError
#           ProcessLookupError
#           TimeoutError
#           UnsupportedOperation
#       ReferenceError
#       RuntimeError
#           NotImplementedError
#           RecursionError
#           _DeadlockError
#       StopAsyncIteration
#       StopIteration
#       SyntaxError
#           IndentationError
#               TabError
#       SystemError
#           CodecRegistryError
#       TypeError
#       ValueError
#           UnicodeError
#               UnicodeDecodeError
#               UnicodeEncodeError
#               UnicodeTranslateError
#           UnsupportedOperation
#       Warning
#           BytesWarning
#           DeprecationWarning
#           EncodingWarning
#           FutureWarning
#           ImportWarning
#           PendingDeprecationWarning
#           ResourceWarning
#           RuntimeWarning
#           SyntaxWarning
#           UnicodeWarning
#           UserWarning
#       ExceptionGroup