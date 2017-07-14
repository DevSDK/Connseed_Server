# Just Server Not More



POST: /Data/PostRawData

### Parameter    
    
    device : device pk (id)
    wtr    : Wtr Value
    ppm    : PPM Value
    tmp    : Temperature Value
    hum    : Humidity Value
    lux    : Lux Value


GET: /Data/GetRawData

### Parameter
    device : device pk(id)

GET: /Data/DeviceList

    
### Require Login (USER) Information.

#### Response
    application/json; charset=utf-8
    'id', 'EUI','Battery', 'Nickname'



POST: /Login

### Parameter
    id : account id
    pw : password

#### Response 
    OK                  : status 200
    Invalid  GET Method : status 401
    IsLogined           : status 401
    Parameter Denied    : status 401
    Login InValid       : status 401
    anyexception        : status 400

