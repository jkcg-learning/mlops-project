import pytest
import pandas as pd
from preprocess import preprocess_data
from data_models import WineQuality

@pytest.fixture
def raw_data():
    return [
        WineQuality(
            fixed_acidity=7.4,
            volatile_acidity=0.7,
            citric_acid=0.0,
            residual_sugar=1.9,
            chlorides=0.076,
            free_sulfur_dioxide=11.0,
            total_sulfur_dioxide=34.0,
            density=0.9978,
            pH=3.51,
            sulphates=0.56,
            alcohol=9.4,
            quality=5
        ).dict(by_alias=True)
        for _ in range(3)
    ]

def test_preprocess_data(raw_data):
    df = pd.DataFrame(raw_data)
    df = preprocess_data(df)
    assert df.isnull().sum().sum() == 0
