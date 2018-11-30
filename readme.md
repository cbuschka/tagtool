# tagtool - python script to manipulate git tags

## Usage

### List all tags (matching vX.X.X) sorted semantically
```
tagtool list
```

### Get last tag of format (vX.X.X)
```
tagtool last
```

### Get next tag
* with incremented patch number: v1.0.9 -> v1.0.10
```
tagtool next
```
same as:
```
tagtool nextPatch
```

* with next minor version: v1.9.1 -> v.1.10.0
```
tagtool nextMinor
```

* with next major version: v1.9.18 -> v2.0.0
```
tagtool nextMajor
```

## License
Copyright (c) 2018 by [Cornelius Buschka](https://github.com/cbuschka).

[MIT](./license.txt)

