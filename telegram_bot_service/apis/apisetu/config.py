HOST_URL = "https://cdn-api.co-vin.in/api/"

STATE_URL = HOST_URL + "/v2/admin/location/states"
DISTRIC_URL = HOST_URL + "/v2/admin/location/districs/{state_id}"
APPOINTMENT_BY_DIST = HOST_URL + "/v2/appointment/sessions/public/calendarByDistrict?district_id={district_id}&date={date}"
APPOINTMENT_BY_PIN = HOST_URL + "/v2/appointment/sessions/public/calendarBypin?pincode={pincode}&date={date}"