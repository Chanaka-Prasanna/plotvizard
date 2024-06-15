from plotvizard.data_processing import load_data, filter_data
from plotvizard.plotting import scatter_plot
from plotvizard.interactivity import create_dash_app

# Load data
df = load_data('data/sample_data.csv')

# Example 1: Create a scatter plot using matplotlib/seaborn
scatter_plot(df, x_col='A', y_col='B')

# Example 2: Filter data and create a Dash app
filtered_df = filter_data(df, column='A', value=3)  # Replace with an existing column and value
print(filtered_df)

app = create_dash_app(filtered_df)
app.run_server(debug=True)

