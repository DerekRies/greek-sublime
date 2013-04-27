import sublime, sublime_plugin, re

def enum(**enums):
    return type('Enum', (), enums)

Syntax = enum(JAVASCRIPT="Packages/JavaScript/JavaScript.tmLanguage",
              PYTHON="Packages/Python/Python.tmLanguage")

class ExpandMathCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        source_language = self.view.settings().get('syntax')

        line = self.view.line(self.view.sel()[0])
        content = self.view.substr(line)
        print(content)
        output = content

        if source_language == Syntax.JAVASCRIPT:
            print("its javascript")
        elif source_language == Syntax.PYTHON:
            print("its python")
            output = re.sub(r'(\d+)\!', r'math.factorial(\1)', content)
        else:
            print(self.view.settings().get('syntax'))
        self.view.replace(edit, line, output)
