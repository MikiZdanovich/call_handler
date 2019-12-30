from data_service.database.models.tariff import Tariff
from data_service.database import session


LTE = Tariff(band_type="LTE", price=100)
CDMA = Tariff(band_type="CDMA", price=50)
GSM = Tariff(band_type="GSM", price=20)

session.add(LTE)
session.add(CDMA)
session.add(GSM)

session.commit()