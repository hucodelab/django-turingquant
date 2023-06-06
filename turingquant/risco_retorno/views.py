from django.shortcuts import render
from .forms import StockForm
from django.contrib import messages
import yfinance as yf
import plotly.express as px
from plotly.offline import plot
from django.shortcuts import redirect
import json
import plotly

# Create your views here.
def histograma_retorno(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            ticker = form.cleaned_data['ticker']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            df = yf.download(ticker, start=start_date, end=end_date)
            fig = px.histogram(df['Adj Close'].pct_change().dropna(), nbins=100, title='Histograma de Retornos Diários')
            
            plot_div = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

            messages.success(request, 'Histogram successfully generated.')
    else:
        plot_div = None
        form = StockForm()

    return render(request, 'histograma_retorno.html', {'form': form, 'plot_div': plot_div})