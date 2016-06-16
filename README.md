# RapydScript Quickstart

## Installation

Make sure you have node installed.

```
npm install -g rapydscript-ng
```

## Compilation

Output to standard out:

```
rapydscript main.py
```

Output to file:

```
rapyidscript -o main.js main.py
```

See compilation options:

```
rapydscript compile --help
```

## Notes

- Compilation is pretty fast.
- The compiler cannot generate source maps.
- Exceptions are accurately printed to the web console, but because there are no source maps the line number refers to the generated JS source code. Since function names are preserved by default, though, if you click on the error location you can generally figure out where in your original Python source the error occurred.
