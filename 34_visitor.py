class HTMLFile:
    def get_doctype_declaration(self):
        pass

    def get_head(self):
        pass

    def get_body(self):
        pass

    def accept(self, visitor):
        pass


class HTML4File(HTMLFile):
    def __init__(self, head, body, visitor):
        self._head = head
        self._body = body
        self._visitor = visitor

    def get_doctype_declaration(self):
        return ('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"\n'
                '        "http://www.w3.org/TR/html4/loose.dtd">')

    def get_head(self):
        return self._head

    def get_body(self):
        return self._body

    def accept(self, visitor):
        visitor.validate_html4_file(self)


class HTML5File(HTMLFile):
    def __init__(self, head, body, visitor):
        self._head = head
        self._body = body
        self._visitor = visitor

    def get_doctype_declaration(self):
        return '<!DOCTYPE html>'

    def get_head(self):
        return self._head

    def get_body(self):
        return self._body

    def accept(self, visitor):
        visitor.validate_html5_file(self)


class XHTMLFile(HTMLFile):
    def __init__(self, head, body, visitor):
        self._head = head
        self._body = body
        self._visitor = visitor

    def get_doctype_declaration(self):
        return ('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<!DOCTYPE html\n'
                '        PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n'
                '        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n'
                '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">')

    def get_head(self):
        return self._head

    def get_body(self):
        return self._body

    def accept(self, visitor):
        visitor.validate_xhtml_file(self)


class Visitor:
    def validate_html4_file(self, html4_file):
        pass

    def validate_html5_file(self, html5_file):
        pass

    def validate_xhtml_file(self, xhtml_file):
        pass


class HTMLFileValidator(Visitor):
    def validate_html4_file(self, html4_file):
        print("Validating HTML 4 schema with https://validator.w3.org/#validate_by_uri+with_options")

    def validate_html5_file(self, html5_file):
        print("Validating HTML 5 schema with https://validator.w3.org/#validate_by_uri+with_options")

    def validate_xhtml_file(self, xhtml_file):
        print("Validating XHTML schema with https://validator.w3.org/#validate_by_uri+with_options")


def main():
    visitor = HTMLFileValidator()

    html4_file = HTML4File('<head>\n    <title>Title</title>\n</head>','<body>\n<p>HTML4 FILE</p>\n</body>', visitor)
    html5_file = HTML5File('<head>\n    <meta charset="UTF-8">\n    <title>Title</title>\n</head>'
                           , '<body>\n<p>HTML5 FILE</p>\n</body>',  visitor)
    xhtml_file = XHTMLFile('<head>\n    <title>Title</title>\n</head>', '<body>\n<p>XHTML file</p>\n</body>', visitor)

    html4_file.accept(visitor)
    html5_file.accept(visitor)
    xhtml_file.accept(visitor)


if __name__ == '__main__':
    main()
