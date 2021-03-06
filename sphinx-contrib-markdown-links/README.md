# Sphinx Contrib - Markdown Symlinks

This small Python file enables you to create a symbolic link to markdown pages
outside your docs directory and have links still work. This is useful if you
have things like the
[`CONTRIBUTING.md`](https://blog.github.com/2012-09-17-contributing-guidelines/)
or
[`CODE_OF_CONDUCT.md`](https://blog.github.com/2012-09-17-contributing-guidelines/)
in your repository that you also want to appear in your Sphinx documentation.

As the Markdown documents will have links relative to the source code root,
rather than the place they are now linked too, this code will fixes these paths
up.

The code also makes relative links between two Markdown documents found inside
the Sphinx documentation work even if there relative positions are now totally
different.

# Install

You can install it either via;
```shell
pip install -e "git+https://github.com/mithro/sphinx-contrib-mithro#egg=sphinx-contrib-markdown-links&subdirectory=sphinx-contrib-markdown-links"
```

Or add the following to your `requirements.txt`
```
-e git+https://github.com/mithro/sphinx-contrib-mithro#egg=sphinx-contrib-markdown-links&subdirectory=sphinx-contrib-markdown-links
```

# Set Up

```python

# Add Markdown support by following the recommonmark install instructions.
# https://recommonmark.readthedocs.io/en/latest/#getting-started

from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']

# Replace the `AutoStructify` app.add_transform with the following;
from markdown_links import MarkdownLinks
def setup(app):
    MarkdownLinks.find_links()
    app.add_config_value(
        'recommonmark_config', {
            'github_code_repo': 'https://github.com/<youruser>/<yourrepo>',
        }, True)
    app.add_transform(MarkdownLinks)
```

When running, the build should output something like the following now;
```json
{'code2docs': {'BUILDING.md': 'vtr/build_vtr.md',
               'CONTRIBUTING.md': 'vtr/dev/guidelines.md',
               'README.developers.md': 'vtr/dev/index.md'},
 'docs2code': {'vtr/build_vtr.md': 'BUILDING.md',
               'vtr/dev/guidelines.md': 'CONTRIBUTING.md',
               'vtr/dev/index.md': 'README.developers.md'}}
```

# License

This extension is available under your choice of;

 * [ISC License](COPYING) ([see also](https://creativecommons.org/publicdomain/zero/1.0/legalcode))
 * [CC0 1.0 Universal](COPYING.alt.md) ([see also](https://creativecommons.org/publicdomain/zero/1.0/legalcode))
