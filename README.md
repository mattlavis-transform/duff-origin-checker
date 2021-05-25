# get duff search references and origins

## Implementation steps

- Create and activate a virtual environment, e.g.

  `python3 -m venv venv/`
  `source venv/bin/activate`

- Environment variable settings

  - DATABASE_UK=postgres connection string

- Install necessary Python modules 

  - autopep8==1.5.7
  - lxml==4.6.3
  - psycopg2==2.8.6
  - pycodestyle==2.7.0
  - python-dotenv==0.17.1
  - toml==0.10.2

  via `pip3 install -r requirements.txt`

## Usage

### To get duff search references:
`python3 get_duff_refs.py`

### To get duff origins:
`python3 get_origins.py`
