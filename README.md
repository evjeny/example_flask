# example_flask
Flask app template

## Установка зависимостей

Установка зависимостей:

```bash
conda env create -f environment.yml
```

Активация среды:

```bash
conda activate example_flask
```

Экспорт среды:

```bash
./export_env.sh
```

Запуск скрипта `super_useful_script.py` без активации среды (например, на сервере):

```bash
conda run -n example_flask python super_useful_script.py
```

## Запуск сервера

```bash
conda activate example_flask
./run.sh
```

## Запуск тестового запроса

```bash
./run_example_request.sh
```
