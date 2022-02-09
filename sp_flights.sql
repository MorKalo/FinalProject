CREATE or replace function sp_get_airline_by_username
(_username text)
returns TABLE(id bigint, name character varying, country_id bigint,
			 user_id bigint)
language plpgsql AS
	$$
		BEGIN
			return QUERY
			select a.id, a.name, a.country_id,
			a.user_id from airline_companies a
			join users u on a.user_id = u.id
			where u.username = _username;
		end;
	$$;

|||

CREATE or replace function sp_get_customer_by_username
(_username text)
returns TABLE(id bigint, first_name character varying, last_name character varying,
			 address character varying, phone_number character varying,
			 credit_card_no character varying, user_id bigint)
language plpgsql AS
	$$
		BEGIN
			return QUERY
			select c.id, c.first_name, c.last_name,
			c.address, c.phone_number, c.credit_card_no,
			c.user_id from customers c
			join users u on c.user_id = u.id
			where u.username = _username;
		end;
	$$;

--select * from sp_get_customer_by_username('Nanos')
|||
CREATE or replace function sp_get_user_by_username
(_username text)
returns TABLE(id bigint, username character varying, password character varying,
			  email character varying, user_role int)
language plpgsql AS
	$$
		BEGIN
			return QUERY
			select u.id, u.username, u.password,
			u.email, u.user_role from users u
			where u.username = _username;
		end;
	$$;

--select * from sp_get_user_by_username('turkish')
|||

CREATE or replace function sp_get_flights_by_airline_id
(_airline_id bigint)
returns TABLE(id bigint, airline_Company_Id bigint,
			  origin_Country_id bigint,
			  destination_Country_id bigint,
			  departure_Time timestamp,
			  landing_Time timestamp,
			  remaining_tickets int)
language plpgsql AS
	$$
		BEGIN
			return QUERY
			select f.id, f.airline_Company_Id,
			f.origin_Country_id, f.destination_Country_id,
			f.departure_Time, f.landing_Time,
			f.remaining_Tickets from flights f
			where f.airline_Company_Id = _airline_id;
		end;
	$$;

--select * from sp_get_flights_by_airline_id(2) need to check
|||

CREATE or replace function sp_get_tickets_by_customer_id
(_customer_id bigint)
returns TABLE(id bigint, flight_id bigint,
			  customer_id bigint)
language plpgsql AS
	$$
		BEGIN
			return QUERY
			select t.id, t.flight_id, t.customer_id
			from tickets t where t.customer_id = _customer_id;
		end;
	$$;

--select * from sp_get_tickets_by_customer_id(1)

|||

CREATE or replace function sp_get_arrival_flights
(_country_id int)
returns TABLE(id bigint, airline_Company_Id bigint, origin_Country_id bigint, destination_Country_id bigint, departure_Time timestamp,
			 landing_Time timestamp, remaining_Tickets int)
language plpgsql AS
	$$
		BEGIN
			return QUERY
			select * from flights where (now() AT TIME ZONE 'UTC' + interval '14 hours') > flights.landing_time and flights.destination_country_id = _country_id;
		end;
	$$;


|||

CREATE or replace function sp_get_departure_flights
(_country_id int)
returns TABLE(id bigint, airline_Company_Id bigint, origin_Country_id bigint, destination_Country_id bigint, departure_Time timestamp,
			 landing_Time timestamp, remaining_Tickets int)
language plpgsql AS
	$$
		BEGIN
			return QUERY
			select * from flights where (now() AT TIME ZONE 'UTC' + interval '14 hours') > flights.departure_time and flights.origin_country_id = _country_id;
		end;
	$$;

|||

CREATE or replace function sp_get_flights_by_parameters
(_origin_Country_id int, _destination_Country_id int, _date date)
returns TABLE(id bigint, airline_Company_Id bigint, origin_Country_id bigint, destination_Country_id bigint, departure_Time timestamp,
			 landing_Time timestamp, remaining_Tickets int)
language plpgsql AS
	$$
		BEGIN
			return QUERY
			select * from flights where date(flights.departure_time) = _date and flights.origin_Country_id = _origin_Country_id
			and flights.destination_Country_id = _destination_Country_id;
		end;
	$$;