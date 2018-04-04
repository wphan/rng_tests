## Test Results
We ran the tests by executing ```run_all_tests.py``` in the top level directory.


| OS            | P-score       | Duration (seconds)  |
| ------------- |---------------| -----|
| **Cumulative Sum**
| Linux (WSL)    | 0.0 |58.79|
| Linux (Ubuntu) | 0.0 |58.56|
| Windows        | 0.0 |59.46|
| **Frequency Monobit**
| Linux (WSL)    | 0.64 |20.42|
| Linux (Ubuntu) | 0.17 |20.19|
| Windows        | 0.69 |20.311|
| **Random Excursions**
| Linux (WSL)    | [0.8952597254694096, 0.5137191951857011, 0.7880062562046076, 0.7237093349672239, 0.8274726830394723, 0.129714117718572, 0.21464819069110885, 0.3924802434178003] |20.42|
| Linux (Ubuntu) | [0.6881938939836805, 0.9215963353826954, 0.7433622291401368, 0.21017852517108035, 0.6857571223835579, 0.6370661425299113, 0.7669670375554871, 0.29333764462070266] |20.19|
| Windows        | [0.23427963499731055, 0.9531722959453167, 0.3821753924485052, 0.36642356345457294, 0.4195409656886766, 0.534170114754244, 0.40032445002315825, 0.7605811694952002] |20.311|
| **Runs**
| Linux (WSL)    | 0.12 |55.82|
| Linux (Ubuntu) | 0.90 |55.98|
| Windows        | 0.35 |56.011|
| **Spectral (Discrete Fourier Transform)**
| Linux (WSL)    | 0.58 |43.69|
| Linux (Ubuntu) | 0.49 |39.94|
| Windows        | 0.48 |94.14|


### Randomness conditions:
| Test            | Condition
| ------------- |---------------|
| Cumulative Sum | p-score approaches 0 as randomness increases |
| Frequency Monobit | random if p-score >= 0.01 |
| Random Excursions | random if all 8 p-scores >= 0.01 |
| Runs | random if p-score >= 0.01 |
| Spectral | random if p-score >= 0.01 |


## Install dependencies
```
# create virtualenvironment
virtualenv venv

# activate venv (POSIX)
source venv/bin/activate

# activate venv (Windows)
source venv/scripts/activate

# install deps
pip install -r requirements.txt
```

## Usage
```
# run single test
cd rng_tests
python monobit.py

# run everything
python run_all_tests.py
```
