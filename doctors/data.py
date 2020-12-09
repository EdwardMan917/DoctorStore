from doctors.models import *

def create():
    doctor_a = Doctor(
        name="陳大文", 
        address="九龍觀塘XX街1號XX大廈1A", 
        district="kwun-tong", 
        phone_number="21234567"
    )
    doctor_b = Doctor(
        name="黃大文", 
        address="新界粉嶺XX道33號", 
        district="fanling", 
        phone_number="22234567"
    )
    doctor_c = Doctor(
        name="李大文", 
        address="九龍旺角XX道3號XX中心十二樓", 
        district="mongkok", 
        phone_number="23234567"
    )
    doctor_d = Doctor(
        name="梁大文", 
        address="新界荃灣XX道100號XX商場2樓2001號舖", 
        district="tsuen-wan",
        phone_number="24234567"
    )
    doctor_e = Doctor(
        name="張大文", 
        address="香港中環XX街9號", 
        district="central", 
        phone_number="25234567"
    )
    doctor_f = Doctor(
        name="林大文", 
        address="九龍觀塘XX街99號XX大廈12C", 
        district="kwun-tong", 
        phone_number="26234567"
    )
    doctor_g = Doctor(
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

    Category(query_name="dentistry", name="牙科", doctor=doctor_a).save()
    Category(query_name="pediatrics", name="兒科", doctor=doctor_b).save()
    Category(query_name="chinese-medicine", name="中醫", doctor=doctor_c).save()
    Category(query_name="bone-setting", name="跌打", doctor=doctor_c).save()
    Category(query_name="acupuncture", name="針灸", doctor=doctor_c).save()
    Category(query_name="psychiatric", name="精神科", doctor=doctor_d).save()
    Category(query_name="ophthalmology", name="眼科", doctor=doctor_e).save()
    Category(query_name="dermatology", name="皮膚科", doctor=doctor_f).save()

    Language(query_name="cantonese", name="廣東話", doctor=doctor_a).save()
    Language(query_name="english", name="英語", doctor=doctor_a).save()
    Language(query_name="cantonese", name="廣東話", doctor=doctor_b).save()
    Language(query_name="cantonese", name="廣東話", doctor=doctor_c).save()
    Language(query_name="cantonese", name="廣東話", doctor=doctor_d).save()
    Language(query_name="cantonese", name="廣東話", doctor=doctor_e).save()
    Language(query_name="cantonese", name="廣東話", doctor=doctor_f).save()
    Language(query_name="english", name="英語", doctor=doctor_f).save()

    Service(item="洗牙", price=100, remarks=None, doctor=doctor_a).save()
    Service(item="診金", price=130, remarks=None, doctor=doctor_b).save()
    Service(item="診金", price=120, remarks="包兩日基本中草藥", doctor=doctor_c).save()
    Service(item="跌打診金", price=200, remarks="不包藥物", doctor=doctor_c).save()
    Service(item="針灸診金", price=180, remarks="不包藥物", doctor=doctor_c).save()
    Service(item="診金", price=350, remarks="包兩日基本藥物", doctor=doctor_d).save()
    Service(item="診金", price=410, remarks=None, doctor=doctor_e).save()
    Service(item="診金", price=280, remarks="不包藥物", doctor=doctor_f).save()
    
    OpeningHours(doctor=doctor_a, details="星期一至五:0900-1800").save()
    OpeningHours(doctor=doctor_b, details="星期一至五:0900-1200,1500-1900;星期六:0900-1230").save()
    OpeningHours(doctor=doctor_c, details="星期一至六:0900-1900;星期日​:0900-1230").save()
    OpeningHours(doctor=doctor_d, details="星期一至五:0900-1700").save()
    OpeningHours(doctor=doctor_e, details="星期一至五:0900-2000;星期六:0900-1530").save()
    OpeningHours(doctor=doctor_f, details="星期一至五:0900-1830").save()

