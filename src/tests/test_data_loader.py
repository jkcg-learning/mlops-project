from data_loader import load_data

def test_load_data():
    df = load_data("data/winequality-red.csv")
    assert df.empty is False
