from django import forms

class StockForm(forms.Form):
    ticker = forms.CharField(label='Stock Ticker', max_length=10)
    start_date = forms.DateField(label='Start Date')
    end_date = forms.DateField(label='End Date')