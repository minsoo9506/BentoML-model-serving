- BentoML을 사용해보기

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
  - mypy도 추가하고 싶었는데 에러가 발생해서 이단 제외했다.
- `.pre-commit-config.yaml` 파일을 작성한다.
- `pre-commit install`으로 commit할 때마다 작업들이 실행되도록 한다.

# Reference

- pre-commit
  - https://www.daleseo.com/pre-commit/
- bemtoML
  - https://github.com/khuyentran1401/customer_segmentation/tree/bentoml_demo
