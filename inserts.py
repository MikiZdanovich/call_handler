from data_service.database.models.tariff import Tariff
from data_service.database import session

# test data fro table with tariff data
def seed_test_tariff():
    lte = Tariff(band_type="LTE", price=100)
    cdma = Tariff(band_type="CDMA", price=50)
    gsm = Tariff(band_type="GSM", price=20)

    session.add(lte)
    session.add(cdma)
    session.add(gsm)

    session.commit()
    return "Tariff DB seeded"
