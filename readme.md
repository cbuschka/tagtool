# tagtool - python script to manipulate git tags

## Usage

### Get last tag of format (vX.X.X)
tagtool last

### Get next tag
* v1.0.9 -> v1.0.10
```
tagtool next
```
same as:
```
tagtool nextPatch
```

* v1.9.1 -> v.1.10.0
```
tagtool nextMinor
```

* v1.9.18 -> v2.0.0
```
tagtool nextMajor
```

## License
Copyright (c) 2018 by [Cornelius Buschka](https://github.com/cbuschka).

[MIT](./license.txt)

