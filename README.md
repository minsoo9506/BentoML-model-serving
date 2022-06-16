# Project 목적

- BentoML 사용해보기

# 과정 정리

## pyenv, virtualenv

- `pyenv`를 이용하여 `BentoMLModelServing`라는 이름의 가상환경 생성
- python은 3.9.13 버전 이용

```bash
pyenv virtualenv 3.9.13 BentoMLModelServing
```

## pre-commit

- `pip install pre-commit`으로 pre-commit을 설치하고 commit할 때, 자동으로 실행하고 싶은 작업들을 설치한다. (아래것들)
  - flake8 (format), flake8 (lint), isort (import format), interrogate (docstring)
  - mypy도 추가하고 싶었는데 에러가 발생해서 일단 제외했다.
- `.pre-commit-config.yaml` 파일을 작성한다.
- `pre-commit install`으로 commit할 때마다 작업들이 자동으로 실행되도록 한다.
  - git hook에 등록하는 과정이다.
  - git은 특정 상황에 특정 스크립트를 실행할 수 있도록 hook이라는 기능을 지원한다. `./git/hooks`에 들어가보면 예시 파일들이 있다.

## data

- kaggle의 fraud detection data를 이용해보자
  - 친숙하고 간단하기 때문

## BentoML

```
.
├── data
│   ├── test.csv
│   ├── train.csv
│   └── valid.csv
├── pyproject.toml
├── README.md
├── requirements.txt
└── src
    ├── bentoml_app.py
    ├── config
    │   ├── core.py
    │   └── __init__.py
    ├── config.yml
    ├── __init__.py
    ├── process.py
    ├── run.py
    ├── service.py
    └── train.py
```

- 먼저 프로젝트에서 필요한 config들을 정리한다.
  - `config.yml`, `config/core.py`
- data 전처리와 관련한 과정을 만든다.
  - `process.py`
- 모델 훈련과 관련한 과정을 만든다.
  - `train.py`
- 전처리와 모델훈련을 진행하고 bentoML을 이용하여 이들을 저장한다.
  - `run.py`
- 서비스
  - `service.py`

# Reference

- pre-commit
  - https://www.daleseo.com/pre-commit/
- bemtoML
  - https://docs.bentoml.org/en/latest/concepts/model.html
  - https://github.com/khuyentran1401/customer_segmentation/tree/bentoml_demo
