from classes.master import Master
from classes.quota_order_number_origin import QuotaOrderNumberOrigin

class QuotaOrderNumber(Master):
    def __init__(self, elem, file):
        Master.__init__(self, elem)
        self.sid = Master.process_null(elem.find("sid"))
        self.quota_order_number_id = Master.process_null(elem.find("quotaOrderNumberId"))
        self.validity_start_date = Master.process_null(elem.find("validityStartDate"))
        self.validity_end_date = Master.process_null(elem.find("validityEndDate"))
        self.file = file[7:15]
                
        self.quota_order_number_origins = []
        
        origins = elem.findall("quotaOrderNumberOrigin")
        for item in origins:
            quota_order_number_origin = QuotaOrderNumberOrigin(item)
            self.quota_order_number_origins.append(quota_order_number_origin)
            a = 1
        pass
