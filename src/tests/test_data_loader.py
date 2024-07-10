from data_loader import load_data

def test_load_data():
    df = load_data("data/winequality-red.csv")
    assert not df.empty
    assert 'fixed acidity' in df.columns
    assert 'quality' in df.columns
