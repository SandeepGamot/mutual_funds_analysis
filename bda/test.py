from bda.api_handler import ApiHandler


x = ApiHandler()

# print(x.get_historical_nav(date="01-01-2019",scheme_code="102252",full_details=False))
print(x.get_current_nav(scheme_code="131597",full_details=True))





