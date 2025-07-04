from src.main import score

def test_pybowl():
    score_sheet = "-- -- -- -- -- -- -- -- -- --"
    expected_score=0

    assert score(score_sheet)== expected_score


def test_pybowl1():
    score_sheet = "1- -- -- -- -- -- -- -- -- --"
    expected_score=1

    assert score(score_sheet)== expected_score

def test_pybowl2():
    score_sheet = "11 -- -- -- -- -- -- -- -- --"
    expected_score=2

    assert score(score_sheet)== expected_score

def test_pybowl3():
    score_sheet = "19 -- -- -- -- -- -- -- -- --"
    expected_score=10

    assert score(score_sheet)== expected_score

def test_pybowl4():
    score_sheet = "11 11 11 11 11 11 11 11 11 11"
    expected_score=20

    assert score(score_sheet)== expected_score

def test_pybowl5():
    score_sheet = "1/ -- -- -- -- -- -- -- -- --"
    expected_score=10

    assert score(score_sheet)== expected_score


def test_pybowl6():
    score_sheet = "1/ 54 -- -- -- -- -- -- -- --"
    expected_score=24

    assert score(score_sheet)== expected_score

def test_pybowl7():
    score_sheet = "4/ 4- -- -- -- -- -- -- -- --"
    expected_score=18

    assert score(score_sheet)== expected_score


def test_pybowl8():
    score_sheet = "4/ 4- X -- -- -- -- -- -- --"
    expected_score=28

    assert score(score_sheet)== expected_score


def test_pybowl9():
    score_sheet = "4/ 4- X 1- -- -- -- -- -- --"
    expected_score=30

    assert score(score_sheet)== expected_score


def test_pybowl10():
    score_sheet = "4/ 4- X 14 -- -- -- -- -- --"
    expected_score=38

    assert score(score_sheet)== expected_score

def test_pybowl11():
    score_sheet = "4/ 4- X X X 1- -- -- -- --"
    expected_score=81

    assert score(score_sheet)== expected_score

def test_pybowl12():
    score_sheet = "4/ 4- X 4/ X 1- -- -- -- --"
    expected_score=70

    assert score(score_sheet)== expected_score  

def test_pybowl13():
    score_sheet = "X X X X X X X X X XXX"
    expected_score=300

    assert score(score_sheet)== expected_score  

def test_pybowl14():
    score_sheet = "6/ 7- -- -4 51 -- -/ 3- -- 9/X"
    expected_score=70

    assert score(score_sheet)== expected_score  