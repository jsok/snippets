from argparse import ArgumentParser
import datetime
import os
import subprocess


# The directory to store all snippets and configuration in
SNIPPET_DIR = os.path.expanduser("~/.snippets")

SNIPPET_FILE = "snippets.txt"

# The name of the configuration file
SNIPPET_CONF = ".snippets.conf"

# The name of the default snippet template
SNIPPET_TEMPLATE = ".snippets.tmpl"


class Snippets(object):
    def __init__(self, snippet_dir=SNIPPET_DIR):
        self.snippet_dir = snippet_dir

    def today(self):
        """Returns today's date as a formatted string"""
        now = datetime.datetime.now()
        return now.strftime("%Y%m%d")

    def get_template_file(self):
        template_file = os.path.join(self.snippet_dir, SNIPPET_TEMPLATE)
        if not os.path.exists(template_file):
            raise Exception("Template file '%s' does not exist" % template_file)
        return template_file

    def prepare_snippet(self):
        with open(self.get_template_file()) as f:
            tmpl = eval(f.read())

        new_snippet = tmpl.format(date=self.today())
        return new_snippet

    def get_snippets_file(self):
        snippets_file = os.path.join(self.snippet_dir, SNIPPET_FILE)


        if not os.path.exists(snippets_file):
            open(snippets_file, 'a').close()

        return snippets_file

    def append_snippet(self):
        new_snippet = self.prepare_snippet()

        with open(self.get_snippets_file(), 'a') as f:
            f.write(new_snippet)

    def open_editor(self):
        editor = os.environ['EDITOR'] or 'vim'
        subprocess.call([editor, self.get_snippets_file()])


def main():
    parser = ArgumentParser(description='Snippets')
    parser.add_argument('-a', '--add',
                        dest='action_add',
                        action='store_true',
                        help='Add a new snippet entry')

    args = parser.parse_args()


    snippets = Snippets()
    if args.action_add:
        snippets.append_snippet()

    snippets.open_editor()


if __name__ == "__main__":
    main()
