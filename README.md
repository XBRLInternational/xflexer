# xflexer

[Pygments][pygments] syntax highlight plugin for [XF][xf] XBRL Formula grammar.

[pygments]: http://pygments.org/
[xf]: https://specifications.xbrl.org/release-history-formula-1.0-xf-grammar-wgn.html

## Installation

Install pygments.  e.g.:

``` 
   sudo pip3 install pygments
```

or 

```
   sudo apt-get install python3-pygments
```

You should now have the `pygmentize` command line utility (run `pygmentize -h`) to confirm.

Now install the XF plugin:

```
   sudo python3 setup.py install
```

XF should now appear in the list of lexers:

```
pygmentize -L lexer | grep  xf
* xf:
    xf (filenames *.xf)
```


