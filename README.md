# PyTypus

### Funcional Types Tools For Python.

![Python CI](https://github.com/sammyrulez/pytypus/workflows/Python%20CI/badge.svg)

A library to enable a partial functional programming experince in Python.
Heavily inspired by [Scala Cats](https://typelevel.org/cats/) and [fp-ts](https://gcanti.github.io/fp-ts/).

# Data Structure


## OptionT

`OptionT[T]` is a light wrapper on an `Optional`. Speaking technically, it is a monad for `Optional`, but you don’t need to know what that means for it to be useful. OptionT can be more convenient to work with than using Optional directly since you can  safetly run functions on it withouc checking for `None` values. Integrates some of the python object protocol.

```

    f = option.some("string") # f is a OptionT[string]
    mapped_f = f.map(lambda s: len(s)) # mapped_f is

```

## Either

In day-to-day programming, it is fairly common to find ourselves writing functions that can fail. For instance, querying a service may result in a connection issue, or some unexpected JSON response. To communicate these errors it has become common practice to throw exceptions. This pattern has a long istroy of braeaking the flow of your code and since *"explicit is bettar than implicit"*, how then do we communicate an error? By making it explicit in the data type we return.

```
    def parse(x:string) -> Either[String,List[String]]:
        ...

```

## Validated

## State

## Chain

## Kleisli

# Functional Syntax helpers

## Curry

## Const

## Pattern matcher







