from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error , mean_squared_error , r2_score
import xgboost as xgb

def building_model():
    lr_model = LinearRegression()
    dt_model = DecisionTreeRegressor(random_state=42)
    rfr_model = RandomForestRegressor(random_state=42)
    xgb_model = xgb.XGBRegressor(random_state=42)

    return lr_model,dt_model,rfr_model,xgb_model
