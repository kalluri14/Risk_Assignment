from django.db import models

class equities(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    ticker = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    start_date = models.DateTimeField()

    def __str__(self):
        return self.id

class daily_returns(models.Model):
    date = models.DateTimeField()
    returns = models.SmallIntegerField(default =5)
    equity_id = models.ForeignKey(equities, on_delete=models.CASCADE)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adj_close = models.FloatField()

    def __str__(self):
        return self.equity_id

