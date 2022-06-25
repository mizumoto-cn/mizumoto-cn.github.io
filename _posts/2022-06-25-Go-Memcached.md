---
layout: post
title: Go & Memcached
tags: [Go]
---

## Abstract

`Memcached` is an opensource high-performance distributed in-memory caching system.

## Installation (docker-compose)

docker-compose.yml

```yml
version: '3'
services:
  memcached:
    image: memcached:1.6.14
    container_name: my_cached
    volumes:
      - ./data:/data
    ports:
      - '11211:11211'
```

Then run `docker-compose up` to install and run

## Go operations in memchached

Firstly, `go get github.com/bradfitz/gomemcache/memcache`.

### set

```golang
var (
    server = "127.0.0.1:11211"
)

func main(){
    var err error
    m := memcache.New(server)
    if m == nil {
        fmt.Printf("memcache new failed")
        return
    }

    err = m.Set(&memcache.Item{
        Key:    "car",
        Value:  []byte("blue car"),
    })

    if err != nil {
        fmt.Printf("write to memcache failed. %s", err)
        return
    }
}
```

### get

```golang
var (
  server2 = "127.0.0.1:11211"
)

func main (){
  var err error
  m := memcache.New(server2)
  if m == nil {
    fmt.Printf("memcache new failed")
    return
  }

  item, err := m.Get("car")
  if err != nil {
    fmt.Printf("read from memcache failed. %s", err)
    return
  }

  fmt.Printf("%s", item.Value)
}
```

### add

```golang
var (
  server3 = "127.0.0.1:11211"
)

func main(){
  var err error
  m := memcache.New(server3)
  if m == nil {
    fmt.Printf("memcache new failed")
    return
  }

  err = m.Add(&memcache.Item{
    Key:    "car",
    Value:  []byte("red car"),
  })

  if err != nil {
    fmt.Printf("write to memcache failed. %s", err)
    return
  }
}
```

### replace

```golang
var (
  server4 = "127.0.0.1:11211"
)

func main(){
  var err error
  m := memcache.New(server4)
  if m == nil {
    fmt.Printf("memcache new failed")
    return
  }

  err = m.Replace(&memcache.Item{
    Key:    "car",
    Value:  []byte("green car"),
  })

  if err != nil {
    fmt.Printf("write to memcache failed. %s", err)
    return
  }
}
```

### delete

```golang
if err := m.Delete("car"); err != nil {
  fmt.Printf("delete from memcache failed. %s", err)
  return
}
```

### increment

```golang
if err := m.Increment("number", 5); err != nil {
  fmt.Printf("increment from memcache failed. %s", err)
  return
}
```

### decrement

```golang
if err := m.Decrement("number", 5); err != nil {
  fmt.Printf("decrement from memcache failed. %s", err)
  return
}
```
