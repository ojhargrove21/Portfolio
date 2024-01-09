import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from csv import writer
from dash import Dash,html,dash_table,dcc,callback,Output,Input
import plotly.express as px
import plotly.graph_objects as go
import webbrowser
def updateData():
    tickers = pd.read_csv('Data/tickers.csv')['ticker']
    for tick in tickers:
        print(tick)
        try:
            info = yf.Ticker(tick).history(period="1Y")

            info.to_csv(f'History/{tick}History.csv', sep=",")
        except:
            print("not found")
def plotData(PerGain,focus,focusList,ticker):
    fig, ax= plt.subplots()
    tickers = pd.read_csv('Data/tickers.csv')['ticker']
    data = pd.read_csv(f'History/{ticker}History.csv')
    data['Close']=((data['Close'].shift(30)-data['Close'])/data['Close'])*100#percent gain coversion
    ax.plot(data['Date'],data['Close'],label = "%change")
    ax.plot(data['Date'],data['Close'].rolling(10).sum()/10,label='56D MA')#30 day moving average
    ax.plot(data['Date'],data['Close']+0.5*(data['Close'].rolling(10).std()),label='56D max')#30 day moving average
    ax.plot(data['Date'],data['Close']-0.5*(data['Close'].rolling(10).std()),label='56D min')#30 day moving average

##dp1
    #(data['Close'].rolling(10).max()-0.5*(data['Close'].rolling(365).std()))-(data['Close'].rolling(10).min()+0.5*(data['Close'].rolling(365).std()))


    # ax.plot(data['Date'],data['Close'].rolling(30).sum()/30,label='30D MA')#30 day moving average

    # ax.plot(data['Date'],(data['Close'].rolling(200).sum()/200)-2*(data['Close'].rolling(200).std()),label = '-200D 2SD')
    # ax.plot(data['Date'],(data['Close'].rolling(200).sum()/200)+2*(data['Close'].rolling(200).std()),label = '+200D 2SD')
    # ax.plot(data['Date'],(data['Close'].rolling(200).sum()/200)-(data['Close'].rolling(200).std()),label = '-200D 1SD')
    # ax.plot(data['Date'],(data['Close'].rolling(200).sum()/200)+(data['Close'].rolling(200).std()),label = '+200D 1SD')

    # for tick in tickers:
    #
    #     trans = 1
    #     data = pd.read_csv(f'History/{tick}History.csv')
    #     if(PerGain):
    #         data['Close']=((data['Close']-data['Close'].loc[0])/data['Close'].loc[0])*100
    #
    #     if(focus):
    #         if(tick not in focusList):
    #             trans = 0.3
    #     ax.plot(data['Date'],data['Close'],label=tick,alpha = trans)
    ax.legend()
    plt.title(ticker)
    plt.ylabel("total % Change")
    plt.xlabel("SD diff")
    #     print(tick)
    plt.show()
# 183.087204
def addTicker(ticker):
    with open('Data/tickers.csv', 'a') as tickers:
        writer_obj = writer(tickers)
        writer_obj.writerow([ticker])
        tickers.close()
def removeTicker(ticker):
    tickers = pd.read_csv('Data/tickers.csv')['ticker']

    with open('Data/tickers.csv', 'w',newline='') as file:
        writer_obj = writer(file)
        writer_obj.writerow(['ticker'])
        for tick in tickers:
            if(tick!=ticker):
                writer_obj.writerow([tick])
        file.close()

# addTicker('VYGR')
# updateData()
# plotData(True,True,['QQQ','SPY','NVDA'],'UIS')
app = Dash(__name__)
df = pd.read_csv('History/AAPLHistory.csv')
df['Close']=((df['Close']-df['Close'].loc[0])/df['Close'].loc[0])*100
df=df.assign(SDP=None)
df['SDP'] = df['Close']+(df['Close'].rolling(200).std())

percentARR=[0.07,0.05,0.07,0.06,0.05,0.05,0.07,0.08,0.16,0.11,0.23]

app.layout = html.Div([
    dcc.Dropdown(options=['AAPL','AMZN','AVGO','COST','GOOG','GOOGL','META','MSFT','NVDA','TSLA','QQQ','SPY','Portfolio'], value='AAPL',id='class_select',className='class_select',style={'width':'30%'}),
    dcc.Checklist(style={'width':'20%','height':'10%','position':'absolute','left':'0%','top':'20%'},inline=True,id='traces',options=[
        {'label':'30D MA','value':'30D_MA'},
        {'label':'30D SD','value':'30D_SD'},
        {'label':'200D MA','value':'200D_MA'},
        {'label':'200D SD','value':'200D_SD'},
        {'label':'30D min','value':'30D_min'},
        {'label':'30D max','value':'30D_max'},


    ]),
    dcc.Input(id='AAPL%',style={'width':'15%','position':'absolute','left':'15%','top':'2%'},placeholder='% holdings in AAPL',value=percentARR[0]),
    dcc.Input(id='AMZN%',style={'width':'15%','position':'absolute','left':'30%','top':'2%'},placeholder='% holdings in AMZN',value=percentARR[1]),
    dcc.Input(id='AVGO%',style={'width':'15%','position':'absolute','left':'45%','top':'2%'},placeholder='% holdings in AVGO',value=percentARR[2]),
    dcc.Input(id='META%',style={'width':'15%','position':'absolute','left':'60%','top':'2%'},placeholder='% holdings in META',value=percentARR[6]),
    dcc.Input(id='MSFT%',style={'width':'15%','position':'absolute','left':'75%','top':'2%'},placeholder='% holdings in MSFT',value=percentARR[7]),

    dcc.Input(id='COST%',style={'width':'15%','position':'absolute','left':'15%','top':'7%'},placeholder='% holdings in COST',value=percentARR[3]),
    dcc.Input(id='GOOG%',style={'width':'15%','position':'absolute','left':'30%','top':'7%'},placeholder='% holdings in GOOG',value=percentARR[4]),
    dcc.Input(id='GOOGL%',style={'width':'15%','position':'absolute','left':'45%','top':'7%'},placeholder='% holdings in GOOGL',value=percentARR[5]),
    dcc.Input(id='NVDA%',style={'width':'15%','position':'absolute','left':'60%','top':'7%'},placeholder='% holdings in NVDA',value=percentARR[8]),
    dcc.Input(id='TSLA%',style={'width':'15%','position':'absolute','left':'75%','top':'7%'},placeholder='% holdings in TSLA',value=percentARR[9]),
    dcc.Input(id='QQQ%',style={'width':'15%','position':'absolute','left':'15%','top':'12%'},placeholder='% holdings in QQQ',value=percentARR[10]),






    dcc.Graph(figure={},id='graph-1',style={'width':'100%','position':'absolute','left':'0%','top':'30%'})
])
@callback(
    Output(component_id='graph-1',component_property='figure'),
    Input(component_id='class_select',component_property='value'),
    Input(component_id='traces',component_property='value'),
    Input(component_id='AAPL%',component_property='value'),
    Input(component_id='AMZN%',component_property='value'),
    Input(component_id='AVGO%',component_property='value'),
    Input(component_id='META%',component_property='value'),
    Input(component_id='MSFT%',component_property='value'),
    Input(component_id='COST%',component_property='value'),
    Input(component_id='GOOG%',component_property='value'),
    Input(component_id='GOOGL%',component_property='value'),
    Input(component_id='NVDA%',component_property='value'),
    Input(component_id='TSLA%',component_property='value'),
    Input(component_id='QQQ%',component_property='value')


)
def updateGraphs(col_chosen,traces,AAPL,AMZN,AVGO,META,MSFT,COST,GOOG,GOOGL,NVDA,TSLA,QQQ):





    if col_chosen != 'Portfolio':
        df = pd.read_csv(f'History/{col_chosen}History.csv')
      #convert to percent
        df['Close']=((df['Close']-df['Close'].loc[0])/df['Close'].loc[0])*100
#created new data columns

        df=df.assign(MA30D=None)
        df['MA30D'] = (df['Close'].rolling(30).sum())/30
        df=df.assign(MA200D=None)
        df['MA200D'] = (df['Close'].rolling(200).sum())/200
        df=df.assign(MAX30D=None)
        df['MAX30D'] = df['Close'].rolling(30).max()
        df=df.assign(MIN30D=None)
        df['MIN30D'] = df['Close'].rolling(30).min()

        df=df.assign(SDP=None)
        df['SDP'] = df['Close']+(df['Close'].rolling(200).std())
        df=df.assign(SDN=None)
        df['SDN'] = df['Close']-(df['Close'].rolling(200).std())
        df=df.assign(SDP2=None)

        df['SDP2'] = df['Close']+(df['Close'].rolling(30).std())
        df=df.assign(SDN2=None)
        df['SDN2'] = df['Close']-(df['Close'].rolling(30).std())
    else:
        df = pd.read_csv(f'History/AAPLHistory.csv')
        df['Close']=((df['Close']-df['Close'].loc[0])/df['Close'].loc[0])*100

        df2 = pd.read_csv(f'History/AMZNHistory.csv')
        df2['Close']=((df2['Close']-df2['Close'].loc[0])/df2['Close'].loc[0])*100
        df3=pd.read_csv(f'History/AVGOHistory.csv')
        df3['Close']=((df3['Close']-df3['Close'].loc[0])/df3['Close'].loc[0])*100
        df4=pd.read_csv(f'History/COSTHistory.csv')
        df4['Close']=((df4['Close']-df4['Close'].loc[0])/df4['Close'].loc[0])*100
        df5=pd.read_csv(f'History/GOOGHistory.csv')
        df5['Close']=((df5['Close']-df5['Close'].loc[0])/df5['Close'].loc[0])*100
        df6=pd.read_csv(f'History/GOOGLHistory.csv')
        df6['Close']=((df6['Close']-df6['Close'].loc[0])/df6['Close'].loc[0])*100
        df7=pd.read_csv(f'History/METAHistory.csv')
        df7['Close']=((df7['Close']-df7['Close'].loc[0])/df7['Close'].loc[0])*100
        df8=pd.read_csv(f'History/MSFTHistory.csv')
        df8['Close']=((df8['Close']-df8['Close'].loc[0])/df8['Close'].loc[0])*100
        df9=pd.read_csv(f'History/NVDAHistory.csv')
        df9['Close']=((df9['Close']-df9['Close'].loc[0])/df9['Close'].loc[0])*100
        df10=pd.read_csv(f'History/TSLAHistory.csv')
        df10['Close']=((df10['Close']-df10['Close'].loc[0])/df10['Close'].loc[0])*100
        df11=pd.read_csv(f'History/QQQHistory.csv')
        df11['Close']=((df11['Close']-df11['Close'].loc[0])/df11['Close'].loc[0])*100
#created new data columns
        df['Close']=(df['Close']*AAPL)+(df2['Close']*AMZN)+(df3['Close']*AVGO)+(df4['Close']*COST)+(df5['Close']*GOOG)+(df6['Close']*GOOGL)+(df7['Close']*META)+(df8['Close']*MSFT)+(df9['Close']*NVDA)+(df10['Close']*TSLA)+(df11['Close']*QQQ)
        df=df.assign(MA30D=None)
        df['MA30D'] = (df['Close'].rolling(30).sum())/30
        df=df.assign(MA200D=None)
        df['MA200D'] = (df['Close'].rolling(200).sum())/200


        df=df.assign(SDP=None)
        df['SDP'] = df['Close']+(df['Close'].rolling(200).std())
        df=df.assign(SDN=None)
        df['SDN'] = df['Close']-(df['Close'].rolling(200).std())
        df=df.assign(SDP2=None)

        df['SDP2'] = df['Close']+(df['Close'].rolling(30).std())
        df=df.assign(SDN2=None)
        df['SDN2'] = df['Close']-(df['Close'].rolling(30).std())

        df=df.assign(MAX30D=None)
        df['MAX30D'] = df['Close'].rolling(30).max()
        df=df.assign(MIN30D=None)
        df['MIN30D'] = df['Close'].rolling(30).min()

    #checks for the checkbox corisponding
    fig = px.line(df,x='Date',y='Close')
    if '200D_SD' in str(traces):
        fig.add_trace(
        go.Scatter(
            x=df['Date'],
            y=df['SDP'],
            mode='lines',
            line=go.scatter.Line(color='red'),
            showlegend=True,
            text='200D SD +1',
            name='200D SD +1'
            )
        )
        fig.add_trace(
        go.Scatter(
            x=df['Date'],
            y=df['SDN'],
            mode='lines',
            line=go.scatter.Line(color='green'),
            showlegend=True,
            text='200D SD -1',
            name='200D SD -1'
            )
        )
    if '30D_SD' in str(traces):
        fig.add_trace(
        go.Scatter(
            x=df['Date'],
            y=df['SDP2'],
            mode='lines',
            line=go.scatter.Line(color='orange'),
            showlegend=True,
            text='30D SD +1',
            name='30D SD +1'
            )
        )
        fig.add_trace(
        go.Scatter(
            x=df['Date'],
            y=df['SDN2'],
            mode='lines',
            line=go.scatter.Line(color='cyan'),
            showlegend=True,
            text='30D SD -1',
            name='30D SD -1'
            )
        )
    if '30D_MA' in str(traces):
        fig.add_trace(
        go.Scatter(
            x=df['Date'],
            y=df['MA30D'],
            mode='lines',
            line=go.scatter.Line(color='black'),
            showlegend=True,
            text='30D MA',
            name='30D MA'
            )
        )
    if '200D_MA' in str(traces):
        fig.add_trace(
        go.Scatter(
            x=df['Date'],
            y=df['MA200D'],
            mode='lines',
            line=go.scatter.Line(color='gray'),
            showlegend=True,
            text='200D MA',
            name='200D MA'
            )
        )
    if '30D_max' in str(traces):
        fig.add_trace(
        go.Scatter(
            x=df['Date'],
            y=df['MAX30D'],
            mode='lines',
            line=go.scatter.Line(color='yellow'),
            showlegend=True,
            text='30D max',
            name='30D max'
            )
        )
    if '30D_min' in str(traces):
        fig.add_trace(
        go.Scatter(
            x=df['Date'],
            y=df['MIN30D'],
            mode='lines',
            line=go.scatter.Line(color='rgb(255,100,100)'),
            showlegend=True,
            text='30D min',
            name='30D min'
            )
        )


    return fig


if __name__ == '__main__':
    updateData()
    webbrowser.open_new("http://localhost:8050")
    app.run(debug=True)
