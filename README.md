# nw_scale-distances
Converts/scales distances in newick trees

## Author
Jason Kwong (@kwongjc)

## Dependencies
* Python 3.x

## Usage
```
$ nw_scale-distances.py --h
usage: 
  nw_scale-distances.py [OPTIONS] newick.tree

Converts/scales distances in Newick trees

positional arguments:
  nwtree          newick tree file

optional arguments:
  -h, --help      show this help message and exit
  --days          output distances in days (for timed phylogeny)
  --years         output distances in years (for timed phylogeny)
  --factor FLOAT  output distances multiplied by this scale factor
  --version       show program's version number and exit
```

## Examples
**To convert distance values in a timed phylogeny (e.g. from BEAST) from days to years:**
```
$ nw_scale-distances.py --years newick.tree
```
**To scale distance values to a factor of 10%:**
```
$ nw_scale-distances.py --factor 0.1 newick.tree
```

## Bugs

Please submit via the [GitHub issues page](https://github.com/kwongj/nw_scale-distances/issues).  

## Software Licence

[GPLv3](https://github.com/kwongj/nw_scale-distances/blob/master/LICENSE)
