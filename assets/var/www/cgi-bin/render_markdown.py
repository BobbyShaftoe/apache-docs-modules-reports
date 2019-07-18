#!/opt/py37/bin/python

import os
import mistune


def main(os_args):
    """
    Main function
    :param os_args:
    :rtype: str
    """
    print("Content-type: text/html\n")
    print(HEADER)
    print("\n")
    print("<body>\n")
    query_string = os_args['QUERY_STRING']

    markdown_file = query_string.split('=')[1]

    markdown = mistune.Markdown()

    with open(markdown_file) as m:
        markdown_body = m.read()

    print(markdown(markdown_body))
    print("</body>")


HEADER = """
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" 
      integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<style>
body { margin-left: 12px; }
.h1, h1 {
    font-size: 2rem;
}
.h2, h2 {
    font-size: 1.5rem;
}
.h3, h3 {
    font-size: 1.3rem;
}
.h4, h4 {
    font-size: 1.1rem;
}
.h5, h5 {
    font-size: .9rem;
}
.h6, h6 {
    font-size: .7rem;
}
p { margin-left: 0.5em; }
pre { margin-left: 1em; }}
</style>
</head>
"""

if __name__ == '__main__':
    main(os.environ)
