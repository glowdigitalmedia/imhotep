![Imhotep](https://raw.github.com/justinabrahms/imhotep/master/imhotep.png)
# Imhotep, the peaceful builder.

## What is it?
A fork of [Imhotep](https://github.com/justinabrahms/imhotep), a tool which will comment on commits coming into your
repository and check for syntactic errors and general lint warnings.

This fork adds ```--travis``` option to Imhotep, which makes it use the already cloned repo when running the lint bot post-success on Travis.

To test ```--travis``` locally:
```
export TRAVIS_BUILD_DIR='/path/to/repo'
$ imhotep --travis ...
```

It also contains a modified version of the linting tool representation (with optimized file-search), which these plugins implement:

* [Imhotep PEP8](https://github.com/glowdigitalmedia/imhotep_pep8)
* [Imhotep JSHint](https://github.com/glowdigitalmedia/imhotep_jshintdiff)

## Installation

```
pip install -e git+git://github.com/glowdigitalmedia/imhotep.git@0.1.1#egg=imhotep
```

Editable mode:

```
git clone git://github.com/glowdigitalmedia/imhotep
cd imhotep
pip install -r requirements.txt
pip install -e .
```


You'll also need to install the plugins you'd like to run:

* [Imhotep PEP8](https://github.com/glowdigitalmedia/imhotep_pep8)

```
pip install -e git+git://github.com/glowdigitalmedia/imhotep_pep8.git@0.1.1#egg=imhotep_pep8
```
Optionally put ```tox.ini``` PEP8 linter config in the repo root if you want to change linting defaults

* [Imhotep JSHint](https://github.com/glowdigitalmedia/imhotep_jshintdiff)

```
npm install jshint

pip install -e git+git://github.com/glowdigitalmedia/imhotep_jshintdiff.git@0.1.1#egg=imhotep_jshintdiff
```
Optionally put ```.jscsrc``` with JSHint config in the repo root if you want to change linting defaults

## Usage

See [Imhotep docs](https://github.com/justinabrahms/imhotep#usage).
