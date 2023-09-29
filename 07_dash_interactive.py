import pandas as pd
import dash
import dash_html_components as html 
import dash_core_components as dcc 
from dash.dependencies import Input, Output 
import plotly.express as px 

# Transform space x launch data into pandas dataframe
spacex_df = pd.read_csv('spacex_launch_dash.csv') 
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create dash application
app = dash.Dash(__name__)

# Create application layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
                                        
                                        # TASK 1: Add a dropdown list to enable Launch Site slection
                                        # Default select value is for ALL sites
                                        dcc.Dropdown(id='site-dropdown',
                                        options=[
                                            {'label': 'All Sites', 'value': 'All Sites'},
                                            {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                                            {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                            {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}],
                                        placeholder='Select a Launch Site Here',
                                        value='All Sites',
                                        searchable=True),
                                        html.Br(), 

                                        # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                        # Show the Success vs. Failed counts for the chosen site
                                        html.Div(dcc.Graph(id='success-pie-chart')),
                                        html.Br(),

                                        # TASK 3: Add a slider to select payload range
                                        dcc.RangeSlider(id='payload-slider',
                                        min=0,
                                        max=10000,
                                        step=1000,
                                        marks={i: '{}'.format(i) for i in range(0, 10001, 1000)},
                                        value=[min_payload, max_payload]),

                                        # TASK 4: Add a scatter plot to show the coorelation between payload mass and launch success
                                        html.Div(dcc.Graph(id='success-payload-scatter-chart'))
                                        ])

# Callback functions for for dropdown functions

# TASK 2: 'site-dropdown' as input, 'success-pie-chart' as output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
                Input(component_id='site-dropdown', component_property='value'))

def get_pie_chart(launch_site):
        if launch_site == 'All Sites':
            fig = px.pie(values=spacex_df.groupby('Launch Site')['class'].mean(),
                            names=spacex_df.groupby('Launch Site')['Launch Site'].first(),
                            title='Success Launches by Site')
        else: 
            fig = px.pie(values=spacex_df[spacex_df['Launch Site'] == str(launch_site)]['class'].value_counts(normalize=True),
                                            names=spacex_df['class'].unique(),
                                            title='Success Launches for Site {}'.format(launch_site))
        return(fig) 

# TASK 4: 'site-dropdown' and 'payload-slider' as inputs; 'success-payload-scatter-chart' as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
                [Input(component_id='site-dropdown', component_property='value'),
                 Input(component_id='payload-slider', component_property='value')])

def get_payload_chart(launch_site, payload_mass):
        if launch_site == 'All Sites':
            fig = px.scatter(spacex_df[spacex_df['Payload Mass (kg)'].between(payload_mass[0], payload_mass[1])],
                                x='Payload Mass (kg)',
                                y='class',
                                color='Booster Version Category',
                                hover_data=['Launch Site'],
                                title='Correlation Between Payload Mass and Success Launches for All Sites')
        else: 
            df = spacex_df[spacex_df['Launch Site'] == str(launch_site)]
            fig = px.scatter(df[df['Paylaod Mass (kg)'].between(payload_mass[0], payload_mass[1])],
                                x='Payload Mass (kg)',
                                y='class',
                                color='Booster Version Category',
                                hover_data=['Launch Site'],
                                title='Correlation Between Payload Mass and Success Launches for Site {}'.format(launch_site))
        return(fig)

# Launch the application
if __name__ == '__main__':
    app.run_server()                                           