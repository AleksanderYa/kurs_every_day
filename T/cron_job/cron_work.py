from currency.models import GovBank



def hi():
    GovBank.objects.create(
        id_currency = 0,
        name_currency = None,
        value_currency = None,
        date_carrency = None
    )
    print('all dane!')



