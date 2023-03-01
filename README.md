# tanssi-ennuste

## Setting up

### Requirements

- Python 3
- pip

### Setup

#### 1. Clone repository

```
git clone git@github.com:mohanjith/tanssi-ennuste.git
cd tanssi-ennuste
```

#### 2. Install dependencies

```
pip install -r requirements.txt
```

### Historical data

Place the historical data file in data directory named set-1.csv. File should
contain columns Place, Band, Favourite dancers %, Score %. There can be more
columns and will be ignored.

## Usage

```
python3 predict.py <place> <band> <favourite dancers %>
```
