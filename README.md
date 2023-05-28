# pydra-petpvc

----

Pydra tasks for PETPVC.

[Pydra][pydra] is a dataflow engine which provides
a set of lightweight abstractions for DAG
construction, manipulation, and distributed execution.

[PETPVC][petpvc] is a toolbox for partial volume correction (PVC)
in positron emission tomography (PET).

## Installation

```console
pip install pydra-petpvc
```

A separate installation of PETPVC is required to use this package.
Please review the project's [homepage][petpvc] for installation instructions and licensing information.

An official conda package is available through [conda-forge][petpvc-conda]:

```console
conda install -c conda-forge petpvc
```

## Development

This project is managed with [Hatch][hatch]:

```console
pipx install hatch
```

To run the test suite:

```console
hatch run test
```

To fix linting issues:

```console
hatch run lint:fix
```

## Licensing

This project is distributed under the terms of the [Apache License, Version 2.0][license].

[hatch]: https://hatch.pypa.io/

[license]: https://spdx.org/licenses/Apache-2.0.html

[petpvc]: https://github.com/UCL/PETPVC

[petpvc-conda]: https://anaconda.org/conda-forge/petpvc

[pydra]: https://pydra.readthedocs.io/
