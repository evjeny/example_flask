conda env export --no-builds > temp.yml && grep -v "prefix" temp.yml  > environment.yml && rm temp.yml