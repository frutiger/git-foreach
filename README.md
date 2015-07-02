##git-foreach - parallelize git commands

### SYNOPSIS

```
git-foreach [-h] [-b] [-j JOBS] PATTERN COMMAND...

positional arguments:
  PATTERN
  COMMAND

optional arguments:
  -h, --help            show this help message and exit
  -b, --bare-repos
  -j JOBS, --jobs JOBS
```

### DESCRIPTION

Run a git command across all your repos, potentially in parallel.

Given a glob PATTERN that matches one or more git directories, you can run the
same COMMAND on them.  If these directories are actually bare repositories, you
can specify `-b`.  By default, the number of parallel jobs spawned will equal
the number of logical cores, but this can be tweaked with the `-j` flag.

### INSTALLATION

Place `git-foreach.py` in your `$PATH` somewhere. Personally, I symlink it to
`~/bin/git-foreach` and have `~/bin` in my `$PATH`.

This requires either of the latest versions of Python 2 or Python 3.

### LICENSE

Copyright (C) 2015 Masud Rahman

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

