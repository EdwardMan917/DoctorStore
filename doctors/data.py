from doctors.models import *

def create():
    doctor_a = Doctor(
        id='93191810-7a02-4df0-a352-d2e8a146c112',
        name="陳大文", 
        address="九龍觀塘XX街1號XX大廈1A", 
        district="kwun-tong", 
        phone_number="21234567"
    )
    doctor_b = Doctor(
        id='37fcb0c2-6e31-4819-80a1-89a98d0b9b76',
        name="黃大文", 
        address="新界粉嶺XX道33號", 
        district="fanling", 
        phone_number="22234567"
    )
    doctor_c = Doctor(
        id='8332abf4-9b22-4e99-aaf9-df5dcfc3cc4b',
        name="李大文", 
        address="九龍旺角XX道3號XX中心十二樓", 
        district="mongkok", 
        phone_number="23234567"
    )
    doctor_d = Doctor(
        id='f5a98247-aea2-49df-9bcd-e3de98b8fe51',
        name="梁大文", 
        address="新界荃灣XX道100號XX商場2樓2001號舖", 
        district="tsuen-wan",
        phone_number="24234567"
    )
    doctor_e = Doctor(
        id='0316d9d5-295f-4892-9797-a316553e74d5',
        name="張大文", 
        address="香港中環XX街9號", 
        district="central", 
        phone_number="25234567"
    )
    doctor_f = Doctor(
        id='d0cd68b1-1329-45a4-93c3-410ee4815f00',
        name="林大文", 
        address="九龍觀塘XX街99號XX大廈12C", 
        district="kwun-tong", 
        phone_number="26234567"
    )
    doctor_g = Doctor(
        id='066210c7-f2e9-43f0-8ff9-4e660bcfee67',
        name="鄭大文", 
        address="香港上環XX街2號XX大廈10樓", 
        district="sheung-wan", 
        phone_number="27234567"
    )
    doctor_a.save()
    doctor_b.save()
    doctor_c.save()
    doctor_d.save()
    doctor_e.save()
    doctor_f.save()
    doctor_g.save()

    dentistry = Category(query_name="dentistry", name="牙科", doctor=doctor_a)
    pediatrics = Category(query_name="pediatrics", name="兒科", doctor=doctor_b)
    chinese_medicine = Category(query_name="chinese-medicine", name="中醫", doctor=doctor_c)
    bone_setting = Category(query_name="bone-setting", name="跌打", doctor=doctor_c)
    acupuncture = Category(query_name="acupuncture", name="針灸", doctor=doctor_c)
    psychiatric = Category(query_name="psychiatric", name="精神科", doctor=doctor_d)
    opthalmology = Category(query_name="ophthalmology", name="眼科", doctor=doctor_e)
    dermatology = Category(query_name="dermatology", name="皮膚科", doctor=doctor_f)
    dentistry.save()
    pediatrics.save()
    chinese_medicine.save()
    bone_setting.save()
    acupuncture.save()
    psychiatric.save()
    opthalmology.save()
    dermatology.save()

    Language(query_name="cantonese", name="廣東話", doctor=doctor_a).save()
    Language(query_name="english", name="英語", doctor=doctor_a).save()
    Language(query_name="cantonese", name="廣東話", doctor=doctor_b).save()
    Language(query_name="cantonese", name="廣東話", doctor=doctor_c).save()
    Language(query_name="cantonese", name="廣東話", doctor=doctor_d).save()
    Language(query_name="cantonese", name="廣東話", doctor=doctor_e).save()
    Language(query_name="cantonese", name="廣東話", doctor=doctor_f).save()
    Language(query_name="english", name="英語", doctor=doctor_f).save()

    Service(item="洗牙", price=100, remarks=None, category=dentistry, doctor=doctor_a).save()
    Service(item="診金", price=130, remarks=None, category=pediatrics, doctor=doctor_b).save()
    Service(item="診金", price=120, remarks="包兩日基本中草藥", category=chinese_medicine, doctor=doctor_c).save()
    Service(item="跌打診金", price=200, remarks="不包藥物", category=bone_setting, doctor=doctor_c).save()
    Service(item="針灸診金", price=180, remarks="不包藥物", category=acupuncture, doctor=doctor_c).save()
    Service(item="診金", price=350, remarks="包兩日基本藥物", category=psychiatric, doctor=doctor_d).save()
    Service(item="診金", price=410, remarks=None, category=opthalmology, doctor=doctor_e).save()
    Service(item="診金", price=280, remarks="不包藥物", category=dermatology, doctor=doctor_f).save()
    
    OpeningHours(doctor=doctor_a, details="星期一至五:0900-1800").save()
    OpeningHours(doctor=doctor_b, details="星期一至五:0900-1200,1500-1900;星期六:0900-1230").save()
    OpeningHours(doctor=doctor_c, details="星期一至六:0900-1900;星期日:0900-1230").save()
    OpeningHours(doctor=doctor_d, details="星期一至五:0900-1700").save()
    OpeningHours(doctor=doctor_e, details="星期一至五:0900-2000;星期六:0900-1530").save()
    OpeningHours(doctor=doctor_f, details="星期一至五:0900-1830").save()


def create_test_data():
    doctor_test_a = Doctor(
        id='b8eec005-25e7-475a-b3f9-8b5f7d8471a4',
        name="test_doctor_a", 
        address="doctor_address_a", 
        district="district_a", 
        phone_number="phone_number"
    )
    doctor_test_b = Doctor(
        id='50d00df4-3fa4-4c7d-97bc-243da5c0bc08',
        name="test_doctor_b", 
        address="doctor_address", 
        district="district_b", 
        phone_number="phone_number"
    )
    doctor_test_a.save()
    doctor_test_b.save()

    category_aa = Category(query_name="category_a", name="cat_a", doctor=doctor_test_a)
    category_ab = Category(query_name="category_b", name="cat_b", doctor=doctor_test_a)
    category_ac = Category(query_name="category_c", name="cat_c", doctor=doctor_test_a)
    category_bb = Category(query_name="category_b", name="cat_b", doctor=doctor_test_b)
    category_aa.save()
    category_ab.save()
    category_ac.save()
    category_bb.save()

    Language(query_name="language_a", name="lang_a", doctor=doctor_test_a).save()
    Language(query_name="language_b", name="lang_b", doctor=doctor_test_a).save()
    Language(query_name="language_a", name="lang_a", doctor=doctor_test_b).save()

    Service(item="service_a", price=100, remarks=None, category=category_aa, doctor=doctor_test_a).save()
    Service(item="service_b", price=500, remarks=None, category=category_ab, doctor=doctor_test_a).save()
    Service(item="service_c", price=250, remarks=None, category=category_ac, doctor=doctor_test_a).save()
    Service(item="service_b", price=250, remarks=None, category=category_bb, doctor=doctor_test_a).save()
    
    OpeningHours(doctor=doctor_test_a, details="details_a").save()
    OpeningHours(doctor=doctor_test_b, details="details_b").save()