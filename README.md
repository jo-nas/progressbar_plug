# OpenHTF Progressbar Plug
[![Build Status](https://travis-ci.org/jo-nas/progressbar_plug.svg?branch=master)](https://travis-ci.org/jo-nas/progressbar_plug)


In this package you will find a plug for the Open Hardware Test Framwork.

## Usage
```
git clone <repository_link>
python setup.py install
```

## Installation
To install this plug, everything in the web folder must be copied into the frontend app folder of the openhtf package.

This line should be copied after the prompt component in the station.html file.
```html
...
</prompt>
<progressbar [progressbar]="tests[testUID].plugs.plug_states"></progressbar>
...
```

```bash
python setup.py install
```

## Requirements
[tqdm](https://github.com/tqdm/tqdm): A fast, extensible progress bar for Python and CLI
[OpenHTF](https://github.com/google/openhtf): The open-source hardware testing framework.

## Licence

## Authors
*progressbar_plug* was written by *[Jonas Steinkamp](https://jonas.steinka.mp) <jonas@steinka.mp>*.
