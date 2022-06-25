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

Firstly, `go get github.com/bradfitz/gomemcache/mamcache`.

### set

```golang
var (
    server = "127.0.0.1:11211"
)

func main(){
    var err error
    m := mamcache.New(server)
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
```

// To be finished