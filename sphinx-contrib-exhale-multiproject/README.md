# Sphinx Contrib - Exhale Multiproject

This extension monkey patches exhale to support multiple doxygen projects at
one time.

This is useful if you want to import multiple sets of third party documentation
or have multiple separate code bases as part of your repo.

# Install

You can install it either via;
```shell
pip install -e "git+https://github.com/mithro/sphinx-contrib-mithro#egg=sphinx-contrib-exhale-multiproject&subdirectory=sphinx-contrib-exhale-multiproject"
```

Or add the following to your `requirements.txt`
```
-e git+https://github.com/mithro/sphinx-contrib-mithro#egg=sphinx-contrib-exhale-multiproject&subdirectory=sphinx-contrib-exhale-multiproject
```

# Set Up

```python
import exhale_multiproject_monkeypatch

# Set up multiple projects in Breathe
breathe_projects = {
    "firmware":     "_doxygen/firmware/xml",
    "edid-decode":  "_doxygen/edid-decode/xml",
    "libuip":       "_doxygen/libuip/xml",
}
breathe_default_project = "firmware"

breathe_projects_source = {
    "firmware":     "../firmware",
    "edid-decode":  "../third_party/edid-decode",
    "libuip":       "../third_party/libuip",
}

# Setup the Exhale extension
exhale_args = {
    'verboseBuild': True,

    "rootFileTitle":        "Unknown",
    "containmentFolder":    "unknown",

    # These arguments are required
    "rootFileName":          "root.rst",
    "doxygenStripFromPath":  "../",
    # Suggested optional arguments
    "createTreeView":        True,
    # TIP: if using the sphinx-bootstrap-theme, you need
    # "treeViewIsBootstrap": True,
    "exhaleExecutesDoxygen": True,
    #"exhaleUseDoxyfile":     True,
    "exhaleDoxygenStdin":    """
EXCLUDE     = ../doc */__pycache__
""",
}

# Set the project specific configurations. They will override the values in
# `exhale_args` for that project run.
exhale_projects_args = {
    "firmware": {
        "exhaleDoxygenStdin":   "INPUT = ../firmware"+exhale_args["exhaleDoxygenStdin"],
        "containmentFolder":    "firmware-api",
        "rootFileTitle":        "Firmware",
    },
    # Third Party Project Includes
    "edid-decode": {
        "exhaleDoxygenStdin":   "INPUT = ../third_party/edid-decode"+exhale_args["exhaleDoxygenStdin"],
        "containmentFolder":    "third_party-edid-decode-api",
        "rootFileTitle":        "edid-decode",
    },
    "libuip": {
        "exhaleDoxygenStdin":   "INPUT = ../third_party/libuip"+exhale_args["exhaleDoxygenStdin"],
        "containmentFolder":    "third_party-libuip-api",
        "rootFileTitle":        "libuip",
    },
}
```

# License

This extension is available under your choice of;

 * [ISC License](COPYING) ([see also](https://creativecommons.org/publicdomain/zero/1.0/legalcode))
 * [CC0 1.0 Universal](COPYING.alt.md) ([see also](https://creativecommons.org/publicdomain/zero/1.0/legalcode))
