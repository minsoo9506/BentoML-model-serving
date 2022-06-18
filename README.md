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

- `bentoml --version` = 1.0.0rc1

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
    │   ├── __init__.py
    ├── config.yml
    ├── __init__.py
    ├── process.py
    ├── save_model.py
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
  - `save_model.py`
- api 생성
  - `service.py`

### 1. Savd model

- `python src/save_model.py` 명령어를 실행하면 아래와 같은 log와 함께 모델이 저장된다.

```
2022년 06월 17일 23시 47분 50초 INFO     [cli] Using the default model signature for sklearn ({'predict': {'batchable': False}}) for model scaler.
2022년 06월 17일 23시 47분 50초 INFO     [cli] Successfully saved Model(tag="scaler:oxwx4sxojsr6vfz3", path="/home/minsoo/bentoml/models/scaler/oxwx4sxojsr6vfz3/")
2022년 06월 17일 23시 47분 51초 INFO     [cli] Using the default model signature for sklearn ({'predict': {'batchable': False}}) for model model.
2022년 06월 17일 23시 47분 51초 INFO     [cli] Successfully saved Model(tag="model:oxwx4thojsr6vfz3", path="/home/minsoo/bentoml/models/model/oxwx4thojsr6vfz3/")
```

- `entoml models list` 명령어를 실행해서 저장된 모델을 확인할 수 있다.

```
Tag                      Module           Size      Creation Time        Path
model:oxwx4thojsr6vfz3   bentoml.sklearn  1.90 KiB  2022-06-17 14:47:51  ~/bentoml/models/model/oxwx4thojs…
scaler:oxwx4sxojsr6vfz3  bentoml.sklearn  2.13 KiB  2022-06-17 14:47:50  ~/bentoml/models/scaler/oxwx4sxoj…
```

### 2. Create prediction service (api)

- `service.py`을 이용하여 api를 만들수 있다.
- `bentoml serve service.py:service --reload` 명령어를 실행하여 로컬에서 HTTP server를 시작한다.
  - `service`는 `service.py`에서 만든 service의 이름을 사용해야한다.
- `predict.py`를 이용하여 request를 날려도 되고 localhost:3000에 들어가서 직접해도 된다. (swagger ui)

### 3. Build a bento for deployment

- `bentofile.yaml` 파일을 작성한 뒤 `bentoml build` 명령어를 통해서 도시락을 만든다.
- `bentoml list`를 하면 아래처럼 도시락이 만들어짐을 확인할 수 있다.

```
 Tag                               Size       Creation Time        Path
 fraud_detection:6hugnkxpb2ts34ke  12.03 KiB  2022-06-18 14:00:02  ~/bentoml/bentos/fraud_detection/6hugnkxpb2ts34ke
```

- 위와 관련한 파일들은 `~/bentoml`에서 확인할 수 있다.
- `~/bentoml/bentos/fraud_detection/6hugnkxpb2ts34ke`로 가보면 아래와 같은 파일들이 만들어짐을 확인할 수 있다.
- 특히 Dockerfile도 만들어줘서 서버에 바로 띄울 수도 있을 것이다. (Deployment!!)

```
.
├── apis
│   └── openapi.yaml
├── bento.yaml
├── env
│   ├── conda
│   ├── docker
│   │   ├── Dockerfile
│   │   └── entrypoint.sh
│   └── python
│       ├── requirements.lock.txt
│       ├── requirements.txt
│       └── version.txt
├── models
│   └── model
│       ├── latest
│       └── oxwx4thojsr6vfz3
│           ├── model.yaml
│           └── saved_model.pkl
├── README.md
└── src
    └── src
        └── service.py
```

# Reference

- pre-commit
  - https://www.daleseo.com/pre-commit/
- bemtoML
  - https://docs.bentoml.org/en/latest/concepts/model.html
  - https://github.com/khuyentran1401/customer_segmentation/tree/bentoml_demo
  - https://zuminternet.github.io/BentoML/
