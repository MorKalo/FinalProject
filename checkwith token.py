#AirlineFacade
airli=AirLineFacade(LoginToken(id=2, name='turkish', role=1))
mork=AirlineCompany(id=2, name='kkkkkkk' )
airli.update_airline(mork)
______________________________________________________________
********Customer Facade*********

#cust=CustomerFacade(LoginToken(id=2, name='shlomi', role=2))
#cust.print_token()

#annas=AnonymusFacade()
#annas.login(username='Nanos', password='324')

cust=CustomerFacade(LoginToken(id=1, name='shlomi', role=2))
shlomi=Customer(last_name='shlomki', phone_number='0376526284')
#cust.update_customer(shlomi)
tick=Ticket(flight_id=2, customer_id=1)
#cust.add_ticket(tick)
#cust.remove_ticket(1)
cust.get_my_tickets()

#airli=AirLineFacade(LoginToken(id=2, name='turkish', role=1))
#mork=AirlineCompany(id=2, name='kkkkkkk' )
#airli.update_airline(mork)