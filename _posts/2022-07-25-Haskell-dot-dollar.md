---
type: post
title: Haskell dot&dollar Operators
subtitle: `.` and `$`
thumbnail-img: ""
share-img: /assets/img/path.jpg
tags: [Haskell, Funtional-Programming]
---

## `.` and `$`

The `$` operator is for avoiding parentheses. Anything appearing after it will take precedence over anything that comes before.

For example, let's say you've got a line that reads:

```haskell
putStrLn (show (1 + 1))
```

If you want to get rid of those parentheses, any of the following lines would also do the same thing:

```haskell
putStrLn (show $ 1 + 1)
putStrLn $ show (1 + 1)
putStrLn $ show $ 1 + 1
```

The primary purpose of the . operator is not to avoid parentheses, but to chain functions. It lets you tie the output of whatever appears on the right to the input of whatever appears on the left. This usually also results in fewer parentheses, but works differently.

Going back to the same example:

```haskell
putStrLn (show (1 + 1))
```

* `(1 + 1)` doesn't have an input, and therefore cannot be used with the `.` operator.
* `show` can take an `Int` and return a `String`.
* `putStrLn` can take a `String` and return an `IO ()`.

You can chain `show` to `putStrLn` like this:

```haskell
(putStrLn . show) (1 + 1)
```

If that's too many parentheses for your liking, get rid of them with the $ operator:

```haskell
putStrLn . show $ 1 + 1
```