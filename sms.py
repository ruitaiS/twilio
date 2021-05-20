from twilio.rest import Client 
 
account_sid = 'ACdfbb3dda18012f353c95fac77d01670d' 
auth_token = 'b28e5134a923bc3104fd2ebd7a656a21' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG61ae0c3f2db5cc660b70c583e5a6f90f', 
                              body='hi',      
                              to='+12039709198' 
                          ) 
 
print(message.sid)