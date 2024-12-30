import shap 

def shap_for_XGBoost(xgb_model,x_test):
    # Create an explainer for XGBoost
    explainer_xgb = shap.Explainer(xgb_model)

    # Compute SHAP values for test data
    shap_values_xgb = explainer_xgb(x_test)

    # Visualize feature importance (summary plot)
    shap.summary_plot(shap_values_xgb, x_test, plot_type="bar")