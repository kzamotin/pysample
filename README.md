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

![Status](https://github.com/kzamotin/pysample/raw/main/allure_report.png)
![](https://travis-ci.org/kzamotin/pysample.svg?branch=main&status=passed)
