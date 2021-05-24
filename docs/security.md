* Identifiers should not be integers, that reveals information about the data and 
  make exploration attacks simpler
  
* Passwords should be salted and use a secure algorithm, in general is good
  to request and enforce long password with alphanumeric and symbols
  
* 2FA is also an interesting feature

* Throttling may also be considered a security mechanism, because it makes a full
  data extraction in a quick manner
  
* Endpoint and action Authentication will also limit the exposure of data, so, by default, users
  should have access limited to certain endpoints and with limited capabilities
  
* HTTPs is a must

* Additional security measures
  - Access analysis, to detect callbacks out of expected hours (f.i. weekends or out-of-office-ours)
  - Ban users after a few failed attempts to authenticate
  - Ban users if the try to use an expired token several times
  - Ban users if they try to access forbidden endpoints or perform forbidden actions
    
* Architecture security measures
  - Create two layers in the system, with a public and private LAN, 
    the backend access the database(s) in the private LAN
  - Use a bastion to access certain components of the system, to prevent pyggybacking
    on connections from compromised users
  - Limit access to Office, VPN or knonw IPs
  - Since the API consumers are corporate users and partners, create a VPN to access it
    