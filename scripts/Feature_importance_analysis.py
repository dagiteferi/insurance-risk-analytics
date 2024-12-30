import shap 

def shap_for_XGBoost(xgb_model,x_test):
    #explainer for XGBoost
    explainer_xgb = shap.Explainer(xgb_model)

    # Comute SHAP values for test data
    shap_values_xgb = explainer_xgb(x_test)

    #  feature importance (summary plot)
    shap.summary_plot(shap_values_xgb, x_test, plot_type="bar")

def shap_for_random_forest(rfr_model,x_test):
   #  an explainer for Random Forest
    explainer_rf = shap.TreeExplainer(rfr_model)

    #  SHAP values
    shap_values_rf = explainer_rf.shap_values(x_test)

    # Visualize feature importance
    shap.summary_plot(shap_values_rf, x_test, plot_type="bar")

def shap_for_decision_tree(dt_model,x_test):
    #  an explainer for Decision Tree
    explainer_dt = shap.TreeExplainer(dt_model)

    #  SHAP values
    shap_values_dt = explainer_dt.shap_values(x_test)

    # Visualize feature importance
    shap.summary_plot(shap_values_dt, x_test, plot_type="bar")

def shap_for_linear_regression(lr_model, x_test):
    # Use LinearExplainer for linear regression models
    explainer_lr = shap.LinearExplainer(lr_model, x_test)
    shap_values_lr = explainer_lr(x_test)
    shap.summary_plot(shap_values_lr, x_test, plot_type="bar")
