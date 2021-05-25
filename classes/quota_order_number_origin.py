from classes.master import Master

class QuotaOrderNumberOrigin(Master):
    def __init__(self, elem):
        Master.__init__(self, elem)
        a = 1
        self.sid = Master.process_null(elem.find("sid"))
        self.quota_order_number_id = Master.process_null(elem.find("quotaOrderNumberId"))
        self.validity_start_date = Master.process_null(elem.find("validityStartDate"))
        self.validity_end_date = Master.process_null(elem.find("validityEndDate"))
        
        self.geographical_area_id = Master.process_null(elem.find("geographicalArea/geographicalAreaId"))

        pass
    
    