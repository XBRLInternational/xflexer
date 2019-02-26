#!/usr/bin/python

from pygments import highlight
from pygments.lexer import RegexLexer, bygroups, words, using
from pygments.token import *
from pygments.lexers.webmisc import XQueryLexer
import re


class XFLexer(RegexLexer):
    name = "xf"
    aliases = ['xf']
    filenames = ['*.xf']
    flags = re.DOTALL

    tokens = {
        'root': [
            (r'\(:.*?:\)', Comment.Multiline),
            (r'\s+', Text),
            (r'((?:test|return|evaluation-count|fallback)\s*)({)', bygroups(Keyword, Punctuation), 'XQuery'),
            (words((    
                'namespace', 'default-language', 'unsatisfied-severity', 'assertion', 'unsatisfied-message',
                'variable', 'test', 'function', 'as',
                'concept-name', 'concept-data-type', 'non-strict', 'entity-scheme',
                'explicit-dimension', 'member', 'typed-dimension','bind-as-sequence',
                'required', 'parameter', 'precondition',
                'linkrole', 'arcrole', 'axis',
            ), suffix=r'(?![-a-zA-Z_0-9:])'), Keyword),
            (r'\(\s*[A-Za-z]{2}(?:-[A-Za-z]{2})?\s*\)', Name),
            (r'"([^"]|\\.)*"', Literal.String.Double),
            (r'[-0-9][0-9]*(?:\.[0-9]*)?', Literal.Number),
            (r'=', Punctuation),
            (r'[;{}()]', Punctuation),
            (r'(\$)([A-Za-z_][-_A-Za-z0-9.]*)', bygroups(Name.Variable, Name)),
            (r'[A-Za-z_][-:_A-Za-z0-9.]*', Name),
            #(r'(namespace\s+)(\w+)(\s*=\s*)("[^"]+"\s*)(;)', bygroups(Keyword, Name, Operator, Literal.String.Double, Keyword)),
            #(r'\b(assertion-set|assertion|parameter)(\s+\S+\s*)({)', bygroups(Keyword.Declaration,Name.Label,Keyword)),
        ],
        'XQuery': [
            (r'}\s*', Punctuation, '#pop'),
            (r'("[^"]*"|\'[^\']*\'|\(:.*?:\)|[^\'"}])+', using(XQueryLexer))
        ],

    }

