# PyTypus

### Funcional Types Tools For Python.

A library to enable a partial functional programming experince in Python.
Heavily inspired by [Scala Cats and](https://typelevel.org/cats/)[fp-ts](https://gcanti.github.io/fp-ts/).

## OptionT

`OptionT[T]` is a light wrapper on an `Optional`. Speaking technically, it is a monad for `Optional`, but you don’t need to know what that means for it to be useful. OptionT can be more convenient to work with than using Optional directly since you can  safetly run functions on it withouc checking for `None` values. Integrates some of the python object protocol.

```

    f = option.some("string") # f is a OptionT[string]
    mapped_f = f.map(lambda s: len(s)) # mapped_f is

```

