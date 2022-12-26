#define Objects for all entities present in client APISetu

class StateObject: 
    state_id : int
    state_name: str
    
class DistrictObject: 
    state_id : int
    district_id : int
    district_name: str

class CenterObject: 
    state_id : int
    name: str
    address: str
    state_name: str
    district_name: str
    pincode: str
    _from: str
    to: str

class SessionObject:
    session_id: int
    date: str
    available_capacity: int
    min_age_limit: int
    vaccine: str
    slots: list

