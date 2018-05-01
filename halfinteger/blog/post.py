import re
import yaml
import markdown


class PATTERN(object):

    SEP = re.compile(r'^(-{3,})$')
    META = re.compile(r'^(\.{3,})$')


class Post(object):
    
    def __init__(self, path, **kwargs):
        self.configs = kwargs
        self.meta = {}
        
        with open(path, 'r', encoding='utf-8') as f:
            content = self.read_meta(f.read())
            self.raw = content

        if 'extensions' in kwargs:
            self.extensions = kwargs.pop('extensions')
        else:
            self.extensions = []

    def read_meta(self, text):
        text = text.lstrip()
        lines = text.splitlines()

        first_line = lines.pop(0)
        m = re.match(PATTERN.SEP, first_line.rstrip())
        if m is None:
            raise ValueError("Missing Post Meta")

        stack = []
        while lines:
            m = re.match(PATTERN.META, lines[0].rstrip())
            if m is not None:
                lines.pop(0)
                break
            stack.append(lines.pop(0))

        meta = '\n'.join(stack)
        content = '\n'.join(lines)
        self.meta = yaml.load(meta)
        if self.meta is None:
            self.meta = {}
        return content

    def render(self, text):
        if self.meta is not None and 'markdown' in self.meta:
            if 'extensions' in self.meta['markdown']:
                self.extensions.extend(self.meta['markdown']['extensions'])

        return markdown.markdown(text, extensions=self.extensions)

    @property
    def html(self):
        return self.render(self.raw)
