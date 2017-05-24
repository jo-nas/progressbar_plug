# OpenHTF Progressbar Plug
[![Build Status](https://travis-ci.org/jo-nas/progressbar_plug.svg?branch=master)](https://travis-ci.org/jo-nas/progressbar_plug) [![Coverage Status](https://coveralls.io/repos/github/jo-nas/progressbar_plug/badge.svg?branch=master)](https://coveralls.io/github/jo-nas/progressbar_plug?branch=master)


In this package you will find a plug for the Open Hardware Test Framwork.

## Usage


## Installation
1. install the plug  
```bash
git clone https://github.com/jo-nas/progressbar_plug.git
python setup.py install
```

2. Clone OpenHTF
```bash
git clone https://github.com/google/openhtf.git
cp -R openhtf/openhtf/output/web_gui/src/ frontend/
rm -rf openhtf
cd frontend
npm install  # or yarn install
```

2. install all web stuff  
You shoot copy everything in the web folder into the frontend src folder of the openhtf package.
```bash
cp -R progressbar_plug/web/* frontend/app/
```

3. 
This line should be copied after the prompt component in the station.html file.
```html
...
</prompt>
<progressbar [progressbar]="tests[testUID].plugs.plug_states"></progressbar>
...
```

The next line should be placed in the station.ts file.
```javascript
...
import {Prompt} from './station.prompt';
import {ProgressBar} from './station.progressbar';
...
```

The directives array should be extend with "ProgressBar"
```javascript
...
directives: [StationHeader, Prompt, ProgressBar, TestHeader, PhaseListing, Logs, Metadata],
...
```

4. compile the frontend
Than compile the fontend folder.
```bash
npm run build # or yarn run build
```

5. Serve OpenHTF
```bash
python -m openhtf.output.web_gui --custom_frontend=frontend/dist/
```

## Requirements
for the frontend
- [node](https://nodejs.org/en/): Node.js JavaScript runtime ✨🐢🚀✨

for the progressbar_plug
- [tqdm](https://github.com/tqdm/tqdm): A fast, extensible progress bar for Python and CLI.
- [OpenHTF](https://github.com/google/openhtf): The open-source hardware testing framework.


## Authors
*progressbar_plug* was written by *[Jonas Steinkamp](https://jonas.steinka.mp) <jonas@steinka.mp>*.
