[![CI pipeline](https://github.com/PiotMik/PythonWorkshops/actions/workflows/continuous_integration.yml/badge.svg?branch=develop)](https://github.com/PiotMik/PythonWorkshops/actions/workflows/continuous_integration.yml)

# Python Workshops
Repozytorium przygotowane na warsztaty z Pythona prowadzone dla KNMF na AGH 08.05 - 29.05 2024.

Celem warsztatów jest zaprezentowanie języka programowania Python w kontekście zastosowania w matematyce finansowej.
Tematyką cyklu są symulacje i wycena opcji metodą Monte Carlo. Warsztaty podzielone są na trzy części po 1.5h, podczas których uczestnicy rozwiązywać będą praktyczne zadania używając popularnych pakietów pythona.


## 08.05.24 - Jak pracować z kodem w dużym zespole
Tematem zajęć jest przedstawienie uczestnikom w jaki sposób zespoły developerskie współpracują nad wspólnym kodem aplikacji.
Uczestnicy zaznajomią się z systemem kontroli wersji Git i operacjami wykonywanymi podczas codziennej pracy developera, oraz strategią Gitflow.
Celem warsztatów jest samodzielne usprawnienie kodu, z poprawnym użyciem kontroli wersji. 
    
> Agenda:
> - Git & GitHub
> - Strategia Gitflow
> - CLI `git` / Git VSCode extension
> - Prezentacja gitflow w praktyce
> - Samodziele ćwiczenia uczestników

> Materiały pomocnicze:
> - [Short Git tutorial](https://www.freecodecamp.org/news/learn-the-basics-of-git-in-under-10-minutes-da548267cc91/)
> - [Git cheatsheet](https://training.github.com/downloads/pl/github-git-cheat-sheet/)
> - [Gitflow](https://www.atlassian.com/pl/git/tutorials/comparing-workflows/gitflow-workflow)


## 22.05.24 - Jak uprzyjemnić sobie pracę z kodem
Tematem zajęć jest przedstawienie uczestnikom narzędzi używanych przez developerów w celu usprawnienia pracy nad kodem aplikacji. 
Uczestnicy zaznajomią się ze standardami czystego kodu w Pythonie, testami jednostkowymi, oraz narzędziami automatyzującymi te procesy (`black`, `pytest`). Dowiedzą się również w jaki sposób analizować poprawność przepływu kodu z użyciem punktów kontrolnych i debuggera.
Celem warsztatów jest samodzielne usprawnienie kodu, z wykorzystaniem narzędzi poznanych podczas warsztatów.

> Agenda:
> - Skrypty w pythonie
> - Symulacje zmiennych losowych i wizualizacje (`numpy`, `matplotlib`, `seaborn`)
> - Debugging kodu
> - Czysta składnia i jej automatyczne kontrolowanie (`PEP8`, `flake8`, `black`)
> - Testy jednostkowe (`pytest`)

> Materiały pomocnicze:
> - Good `numpy` [tutorials](https://www.w3schools.com/python/numpy/default.asp)
> - `seaborn` [further reading](https://seaborn.pydata.org/tutorial/introduction.html)
> - [`SciencePlots` theme](https://github.com/garrettj403/SciencePlots) for your thesis, research papers
> - [`PEP8` reference](https://peps.python.org/pep-0008/)
> - [`pytest` tutorial](https://blog.qalabs.pl/pytest/pytest-pierwsze-kroki/)


## 05.06.24 - Programowanie obiektowe
Tematem zajęć jest zapoznanie uczestników z konceptem programowania obiektowego w Pythonie.
Uczestnicy będą mieli okazję zobaczyć i zaimplementować koncept dziedziczenia, wyposażyć klasę w metody typu *dunder*, oraz poznać przydatne biblioteki usprawniające development OOP. 
Celem warsztatów jest rozszerzenie biblioteki o dodatkowe funkcjonalności, oraz usprawnienie kodu z wykorzystaniem poznanych technik OOP.

> Agenda:
> - Klasy i ich definicja w pythonie
> - Zmienne klasowe, atrybuty i metody
> - Dziedziczenie i polimorfizm
> - Metody dunder i dekoratory @property, @classmethod
> - `dataclass`

> Materiały pomocnicze:
> - `pydantic` [intro](https://docs.pydantic.dev/latest/)
> - OOP [tutorial](https://realpython.com/python3-object-oriented-programming/)

## 12.06.24 - Otwarcie aplikacji dla użytkowników
Tematem zajęć jest zapoznanie uczestników z architekturą REST.
Uczestnicy będą mieli okazję dowiedzieć się w jaki sposób developerzy eksponują wybrane funkcjonalności biblioteki dla użytkowników, oraz rozszerzyć REST API o funkcjonalności zaimplementowane na poprzednich warsztatach.
Celem warsztatów jest prezentacja części developmentu aplikacji dotyczącej dostarczenia do użytkowników.

> Agenda:
> - GitHub Pull Requests
> - REST architecture

> Materiały pomocnicze:
> - REST [overview](https://www.redhat.com/en/topics/api/what-is-a-rest-api)


### Authors
[Piotr Mikler <piotr.mikler1997@gmail.com>](https://github.com/PiotMik)

