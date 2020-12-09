# Changelog

### 08.12.2020

- Travic-ci integration

### 04.12.2020

- Added an example of working with pytest

- Smoke-test command line

```
pytest -v -m smoke --alluredir=alluredir
```

- All test's run command

```
pytest -v --alluredir=alluredir
```

- To view results

```
allure serve ./alluredir
```

### Sample test suite

[Interactive test results](https://kzamotin.gitlab.io/-/pysample/-/jobs/899795060/artifacts/public/index.html)

![](https://travis-ci.org/kzamotin/pysample.svg?branch=main&status=passed)

[![pipeline status](https://gitlab.com/kzamotin/pysample/badges/main/pipeline.svg)](https://gitlab.com/kzamotin/pysample/-/commits/main)

![coverage report](https://gitlab.com/kzamotin/pysample/badges/main/coverage.svg)](https://gitlab.com/kzamotin/pysample/-/commits/main)
