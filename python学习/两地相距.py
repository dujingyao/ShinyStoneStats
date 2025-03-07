coefficients = model_pipeline.named_steps['regressor'].coef_
feature_names = preprocessor.transformers_[0][1].get_feature_names_out(categorical_cols).tolist() + numerical_cols
coef_df = pd.DataFrame({'特征': feature_names, '系数': coefficients})
print(coef_df)