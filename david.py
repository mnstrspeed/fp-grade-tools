#!/usr/bin/python

# david.py laat je direct fouten van je studenten verbeteren door
# feedback te in-linen en dit in een fancy html-rapportje te stoppen

import sys
from os.path import join, dirname, basename

try:
    from html import escape
except ImportError:
    from cgi import escape

COMMENT_TAG = "//>"


def output_path(path):
    return join(dirname(path), 'Commentaar_bij_' + basename(path) + '.html')


def has_comment(line):
    return line.lstrip().startswith(COMMENT_TAG)


def get_comment(line):
    return line.lstrip()[len(COMMENT_TAG)+1:]


for path in sys.argv[1:]:
    print(path)
    with open(path) as input, open(output_path(path), 'w') as output:
        output.write("""\
<html>
    <head>
    </head>
    <body>
        <style type="text/css">
            ol {
                color: #eee;
                font-family: monospace;
            }
            pre {
                margin: 0;
            }
            ol .code {
                color: #000;
            }
            ol .comment {
                position: relative;
                left: -0.5em;
                padding: 0.5em;
                margin: 1em 0;
                background-color: rgb(0, 148, 255);
                color: #fff;
                font-family: sans-serif;
            }
            ol .comment:before {
                content: '';
                position: absolute;
                width: 0;
                height: 0;
                left: 0.5em;
                top: -1em;
                border: 0.5em solid;
                border-color: transparent transparent rgb(0, 148, 255)
                     transparent;
            }
        </style>
        <ol>""")

        in_comment = False
        for line in input:

            if has_comment(line):
                if not in_comment:
                    output.write('<p class="comment">')
                output.write(get_comment(line))
                in_comment = True
            else:
                if in_comment:
                    output.write('</p>')
                output.write('</li>')
                in_comment = False

            if not in_comment:
                output.write('<li>')
                output.write('<pre><code class="code">' + escape(line.rstrip('\n')) + '</code></pre>')

        output.write('</ol></body></html>')
