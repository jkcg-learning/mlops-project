import pandera as pa
from pandera import Column, DataFrameSchema, Check

data_schema = DataFrameSchema({
    "fixed acidity": Column(pa.Float, Check.greater_than_or_equal_to(0)),
    "volatile acidity": Column(pa.Float, Check.greater_than_or_equal_to(0)),
    "citric acid": Column(pa.Float, Check.greater_than_or_equal_to(0)),
    "residual sugar": Column(pa.Float, Check.greater_than_or_equal_to(0)),
    "chlorides": Column(pa.Float, Check.greater_than_or_equal_to(0)),
    "free sulfur dioxide": Column(pa.Float, Check.greater_than_or_equal_to(0)),
    "total sulfur dioxide": Column(pa.Float, Check.greater_than_or_equal_to(0)),
    "density": Column(pa.Float, Check.greater_than_or_equal_to(0)),
    "pH": Column(pa.Float, Check.greater_than_or_equal_to(0)),
    "sulphates": Column(pa.Float, Check.greater_than_or_equal_to(0)),
    "alcohol": Column(pa.Float, Check.greater_than_or_equal_to(0)),
    "quality": Column(pa.Int, Check.in_range(0, 10)),
})
