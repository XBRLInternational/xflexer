# xflexer

[Pygments][pygments] syntax highlight plugin for [XF][xf] XBRL Formula grammar.

[pygments]: http://pygments.org/
[xf]: https://specifications.xbrl.org/release-history-formula-1.0-xf-grammar-wgn.html

## Installation

Install [pygments][pygments].  e.g.:

```bash
sudo pip3 install pygments
```

or 

```bash
# sudo apt-get install python3-pygments
```

You should now have the `pygmentize` command line utility (run `pygmentize -h`) to confirm.

Now install the XF plugin:

```bash
# sudo python3 setup.py install
```

XF should now appear in the list of lexers:

```console
# pygmentize -L lexer | grep  xf
* xf:
    xf (filenames *.xf)
```


