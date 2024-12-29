from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error , mean_squared_error , r2_score
import xgboost as xgb

def building_model():
    lr_model = LinearRegression()#creates an instance of the LinearRegression model from
    dt_model = DecisionTreeRegressor(random_state=42)# creates an instance of the DecisionTreeRegressor model 
    rfr_model = RandomForestRegressor(random_state=42)#creates an instance of the RandomForestRegressor model
    xgb_model = xgb.XGBRegressor(random_state=42)#creates an instance of the XGBRegressor model from the xgboost library.

    return lr_model,dt_model,rfr_model,xgb_model

def define_parameter_grid_gridsearchcv(lr_model,dt_model,rfr_model,xgb_model):
    param_grid_lr = {
    'fit_intercept': [True]
    }

    param_grid_dt = {
        'max_depth': [10],
        'min_samples_split': [5]
    }

    param_grid_rf = {
        'n_estimators': [100],
        'max_depth': [10],
        'min_samples_split': [5]
    }

    param_grid_xgb = {
        'n_estimators': [100],
        'max_depth': [5],
        'learning_rate': [0.1]
    }

    lr_grid = GridSearchCV(lr_model,param_grid_lr,cv=5,scoring='r2')
    dt_grid = GridSearchCV(dt_model, param_grid_dt, cv=5, scoring='r2')
    rf_grid = GridSearchCV(rfr_model, param_grid_rf, cv=5, scoring='r2')
    xgb_grid = GridSearchCV(xgb_model, param_grid_xgb, cv=5, scoring='r2')
    return lr_grid,dt_grid,rf_grid,xgb_grid
