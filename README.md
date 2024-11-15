> https://github.com/astral-sh/uv
```sh
# uv init
uv venv --python 3.9
source .venv/bin/activate
# uv add fastapi uvicorn pydantic-settings requests
uv pip install -r pyproject.toml
python run.py 8100
# pm2 start run.py --name ig-sample-app --interpreter .venv/bin/python3 -- 8100 -i 1
# pm2 logs
```