import plotly.express as px 
 
# using the tips dataset
df = px.data.tips() 
 
# plotting the violin chart
fig = px.violin(df, x="day", y="total_bill")
 
# showing the plot
fig.show()
