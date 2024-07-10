from pydantic import BaseModel, Field, conint, confloat

class WineQuality(BaseModel):
    """Pydantic model for wine quality data validation."""

    fixed_acidity: confloat(ge=0) = Field(..., alias='fixed acidity')
    volatile_acidity: confloat(ge=0) = Field(..., alias='volatile acidity')
    citric_acid: confloat(ge=0) = Field(..., alias='citric acid')
    residual_sugar: confloat(ge=0) = Field(..., alias='residual sugar')
    chlorides: confloat(ge=0) = Field(..., alias='chlorides')
    free_sulfur_dioxide: confloat(ge=0) = Field(..., alias='free sulfur dioxide')
    total_sulfur_dioxide: confloat(ge=0) = Field(..., alias='total sulfur dioxide')
    density: confloat(ge=0) = Field(..., alias='density')
    pH: confloat(ge=0) = Field(..., alias='pH')
    sulphates: confloat(ge=0) = Field(..., alias='sulphates')
    alcohol: confloat(ge=0) = Field(..., alias='alcohol')
    quality: conint(ge=0, le=10) = Field(..., alias='quality')
