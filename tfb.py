import mysql.connector as mysql

try:
    con = mysql.connect(user='root', password='root',
                        host='127.0.0.1', database='tradefairbooking')
    cursor = con.cursor()
    print("Connected : "+str(con.is_connected()))
    """
    def getAll():
        query="SELECT * FROM contact INNER JOIN mapAddress on contact.contact_id=mapAddress.contact_id INNER JOIN address on mapAddress.adno=address.adno"
        if('#' in query):
            query=query.replace('#','')
            #print(query)
        cursor.execute(query)
        records=cursor.fetchall()
        return records
    """

    def getVenues():
        cursor.execute("SELECT * FROM VENUE")
        venues = cursor.fetchall()
        return venues

    def getTransactions():
        cursor.execute("SELECT m.id, first_name, last_name, exhibitor_name,spend, spend_date FROM megaconsumercard m LEFT JOIN Visitor v on m.visitor_id=v.id LEFT JOIN booking b on b.id = m.booking_id LEFT JOIN exhibitor e on b.exhibitor_id=e.id;")
        transactions = cursor.fetchall()
        return transactions

    def getStalls():
        cursor.execute(
            "SELECT s.id, stall_no, event_name from Stall s LEFT JOIN eventtable e on s.event_id = e.id")
        stalls = cursor.fetchall()
        return stalls

    def getCountries():
        cursor.execute("SELECT country_name from COUNTRY")
        countries = cursor.fetchall()
        return countries

    def getStates():
        cursor.execute("SELECT state_name from STATE")
        states = cursor.fetchall()
        return states

    def getIndustries():
        cursor.execute("SELECT industry_name from INDUSTRY")
        industries = cursor.fetchall()
        return industries

    def getBookings():
        cursor.execute("SELECT b.id,e.id,event_name,exhibitor_id,exhibitor_name,stall_no,company_name,company_description,stall_size, price  from booking b left join eventtable e on b.event_id=e.id left join exhibitor ex on b.exhibitor_id=ex.id left join bookingstallmap m on m.booking_id = b.id left join stall s on m.stall_id=s.id")
        bookings = cursor.fetchall()
        return bookings

    def getEvents():
        cursor.execute("SELECT * FROM eventtable")
        events = cursor.fetchall()
        return events

    def getVisitors():
        cursor.execute("SELECT id, first_name, last_name FROM visitor")
        visitors = cursor.fetchall()
        return visitors

    def getExhibitors():
        cursor.execute("SELECT * from exhibitor")
        exhibitors = cursor.fetchall()
        return exhibitors

    def getIndustries():
        cursor.execute("SELECT id, industry_name from industry")
        industries = cursor.fetchall()
        return industries

    def countryId(country):
        cursor.execute(
            "SELECT id FROM Country WHERE country_name='"+country+"';")
        country_id = cursor.fetchone()
        return country_id[0]

    def eventID(event):
        cursor.execute(
            "SELECT id FROM eventtable WHERE event_name='" + event + "';")
        event_id = cursor.fetchone()
        return event_id[0]

    def exhibitorID(exhibitor):
        cursor.execute(
            "SELECT id FROM exhibitor WHERE exhibitor_name='" + exhibitor + "';")
        exhibitor_id = cursor.fetchone()
        return exhibitor_id[0]

    def stallId(stall, event_id):
        cursor.execute("SELECT id FROM STALL WHERE stall_no=" +
                       str(stall) + " AND event_id=" + str(event_id) + ";")
        stall_id = cursor.fetchone()
        return stall_id[0]

    def stateId(state, country_id):
        cursor.execute("SELECT id,country_id FROM State WHERE state_name='" +
                       state+"' AND country_id="+str(country_id)+";")
        state_id = cursor.fetchone()
        return state_id[0]

    def industryId(industry):
        cursor.execute(
            "Select id FROM Industry WHERE industry_name='" + industry + "';")
        industry_id = cursor.fetchone()
        return industry_id[0]
    
    def bookedIndustries():
        query="""SELECT industry_id,industry_name,event_id,COUNT(industry_id) AS noBookings FROM industry INNER JOIN  
        (SELECT event_id,booking.id as booking_id,exhibitor_id,exhibitor_name,company_name,company_description,industry_id 
        FROM booking INNER JOIN exhibitor ON exhibitor.id=booking.exhibitor_id ) AS exhibitorBookings 
        ON industry.id=exhibitorBookings.industry_id
        GROUP BY industry_id,event_id
        ORDER BY noBookings DESC"""
        cursor.execute(query)
        industries=cursor.fetchall()
        return industries


    def getIds(tablename):
        cursor.execute("SELECT id FROM "+tablename)
        id_list = cursor.fetchall()
        return id_list

    def delById(tablename, i_d):
        query = "DELETE FROM "+tablename+" WHERE id="+i_d+";"
        # print(query)
        cursor.execute(query)
        con.commit()

    def addVenue(address, city, state_id, country_id):
        #print("Enter Contact Details : \n")
        """
        vid_list=getIds('Venue')
        vid=len(vid_list)+1
        while(vid in vid_list):
            vid+=1
        """
        query = "INSERT INTO Venue(address,city,state_id,country_id)VALUES('" + \
            address+"','"+city+"',"+str(state_id)+","+str(country_id)+");"
        print(query)
        cursor.execute(query)
        con.commit()

    def deleteBooking(exhibitor, event, stall_no):
        exhibitor_id = exhibitorID(exhibitor)
        event_id = eventID(event)
        stall_id = stallId(stall_no, event_id)
        query = "SELECT b.id FROM booking b LEFT JOIN BookingStallMap m ON b.id = m.booking_id WHERE b.exhibitor_id=" + \
            str(exhibitor_id) + " AND b.event_id=" + str(event_id) + \
            " AND m.stall_id=" + str(stall_id) + ";"
        cursor.execute(query)
        bid = cursor.fetchone()[0]
        delById("Booking", str(bid))

    def updateVenue(vid, address, city, state_id, country_id):
        query = "UPDATE venue SET address='"+address+"',city='"+city+"',state_id=" + \
            str(state_id)+",country_id=" + \
            str(country_id)+" WHERE id="+str(vid)+";"
        # print(query)
        cursor.execute(query)
        con.commit()

    def addTransaction(spend, spend_date, payment_method, event_id, exhibitor_id, visitor_id):
        query = "SELECT id from booking WHERE exhibitor_id=" + \
            str(exhibitor_id) + " AND event_id=" + str(event_id) + ";"
        cursor.execute(query)
        bid = cursor.fetchone()
        query = "INSERT INTO megaconsumercard(spend, spend_date, payment_mode, event_id, booking_id, visitor_id) VALUES(" + \
                str(spend) + ",'" + str(spend_date) + "','" + str(payment_method) + \
            "'," + str(event_id) + "," + \
            str(bid[0]) + "," + str(visitor_id) + ");"
        cursor.execute(query)
        con.commit()

    def updateTransaction(transaction_id, spend, spend_date, payment_method, event_id, exhibitor_id, visitor_id):
        query = "SELECT id from booking WHERE exhibitor_id=" + \
            str(exhibitor_id) + " AND event_id=" + str(event_id) + ";"
        cursor.execute(query)
        bid = cursor.fetchone()
        query = "UPDATE megaconsumercard SET spend=" + str(spend) + ", spend_date='" + str(spend_date) + "', payment_mode='" + str(payment_method) + "', event_id=" + \
                str(event_id) + ", booking_id=" + str(bid[0]) + ", visitor_id=" + str(
                    visitor_id) + " WHERE id=" + str(transaction_id) + ";"
        cursor.execute(query)
        con.commit()

    def addStall(stall_no, price, stall_size, isBooked, event_id):
        """
        sid_list=getIds('Stall')
        sid=len(sid_list)+1
        while(sid in sid_list):
            sid+=1
        """
        query = "INSERT INTO Stall (stall_no,price,stall_size,isBooked,event_id) VALUES("+str(
            stall_no)+","+str(price)+","+str(stall_size)+","+str(isBooked)+","+str(event_id)+");"
        print(query)
        cursor.execute(query)
        con.commit()
        #sid_list = getIds('Stall')
        #stall_id = max(sid_list)
        # query = "INSERT INTO BookingStallMap(stall_id,event_id) VALUES("+str(
        #    stall_id)+","+str(event_id)+");"
        # print(query)
        # cursor.execute(query)
        # con.commit()

    def updateStall(sid, stall_no, price, stall_size, event_id):
        query = "UPDATE Stall SET stall_no="+str(stall_no)+",price="+str(price)+",stall_size="+str(
            stall_size)+",event_id='"+str(event_id)+"' WHERE id="+str(sid)+";"
        cursor.execute(query)
        con.commit()

    def addEvent(event_name, booking_start_date, start_date, end_date, venue_id):
        """
        sid_list=getIds('Stall')
        sid=len(sid_list)+1
        while(sid in sid_list):
            sid+=1
        """
        query = "INSERT INTO EventTable (event_name,booking_start_date,start_date,end_date,venue_id)VALUES('" + \
            event_name+"','"+str(booking_start_date)+"','"+str(start_date) + \
            "','"+str(end_date)+"','"+str(venue_id)+"');"
        print(query)
        cursor.execute(query)
        con.commit()
        """
        query="INSERT INTO mapAddress(contact_id,adno)VALUES("+str(cid)+","+str(adno)+");"
        #print(query)
        cursor.execute(query)
        con.commit()
        """

    def updateEvent(event_id, event_name, booking_start_date, start_date, end_date, venue_id):
        query = "UPDATE EventTable SET event_name='" + str(event_name) + "',booking_start_date='"+str(booking_start_date)+"', start_date='"+str(
            start_date)+"', end_date='"+str(end_date)+"', venue_id="+str(venue_id)+" WHERE id='"+str(event_id)+"';"
        cursor.execute(query)
        con.commit()

    def addVisitor(first_name, last_name, address, pincode, mobile_no, emailid, dob, gender):
        """
        sid_list=getIds('Stall')
        sid=len(sid_list)+1
        while(sid in sid_list):
            sid+=1
        """
        query = "INSERT INTO Visitor(first_name,last_name,address,pincode,mobile_no,email_id,dob,gender) VALUES('"+first_name + \
            "','"+last_name+"','"+address+"'," + \
                str(pincode)+",'"+str(mobile_no)+"','" + \
            emailid+"','"+str(dob)+"',"+str(gender)+");"
        print(query)
        cursor.execute(query)
        con.commit()
        """
        query="INSERT INTO mapAddress(contact_id,adno)VALUES("+str(cid)+","+str(adno)+");"
        #print(query)
        cursor.execute(query)
        con.commit()
        """

    def updateVisitor(vis_id, first_name, last_name, address, pincode, mobile_no, emailid, dob, gender):
        query = "UPDATE visitor SET first_name='"+first_name+"',last_name='"+last_name+"',address='"+address+"',pincode=" + \
            str(pincode)+",mobile_no='"+str(mobile_no)+"',email_id='"+emailid + \
            "',dob='"+str(dob)+"',gender="+str(gender) + \
            " WHERE id="+str(vis_id)+";"
        cursor.execute(query)
        con.commit()

    def addExhibitor(exhibitor_name, email, phone_no, company_name, company_description, address, pincode, industry_id, country_id, state_id):
        """
        sid_list=getIds('Stall')
        sid=len(sid_list)+1
        while(sid in sid_list):
            sid+=1
        """
        query = "INSERT INTO Exhibitor(exhibitor_name,email,phoneno,company_name,company_description,address,pincode,industry_id,country_id,state_id) VALUES('"+exhibitor_name + \
            "','"+email+"','"+str(phone_no)+"','"+company_name+"','"+company_description+"','"+address + \
            "',"+str(pincode)+","+str(industry_id)+"," + \
            str(country_id)+","+str(state_id)+");"
        print(query)
        cursor.execute(query)
        con.commit()
        """
        query="INSERT INTO mapAddress(contact_id,adno)VALUES("+str(cid)+","+str(adno)+");"
        #print(query)
        cursor.execute(query)
        con.commit()
        """

    def updateExhibitor(exid, exibitor_name, email, phoneno, company_name, company_description, address, pincode, industry_id, country_id, state_id):
        query = "UPDATE Exhibitor SET exhibitor_name='"+exibitor_name+"',email='"+email+"',phoneno="+str(phoneno)+",company_name='"+company_name+"',company_description='"+company_description+"',address='"+address+"',pincode="+str(
            pincode)+",industry_id="+str(industry_id)+",country_id="+str(country_id)+",state_id="+str(state_id)+" WHERE id="+str(exid)+";"
        cursor.execute(query)
        con.commit()

    def addBooking(booking_date, event_id, exhibitor_id, stall_id):
        """
        sid_list=getIds('Stall')
        sid=len(sid_list)+1
        while(sid in sid_list):
            sid+=1
        """
        query = "SELECT price, isBooked FROM stall WHERE id=" + str(stall_id)
        cursor.execute(query)
        stall_details = cursor.fetchone()
        print(stall_details)
        if stall_details[1] == 0:
            query = "INSERT INTO Booking(booking_date,total_amount,event_id, exhibitor_id) VALUES('"+str(
                booking_date)+"',"+str(stall_details[0])+","+str(event_id)+","+str(exhibitor_id)+");"
            print(query)
            cursor.execute(query)
            con.commit()
            bid_list = getIds('Booking')
            booking_id = max(bid_list)[0]
            query = "INSERT INTO BookingStallMap(booking_id,event_id,stall_id) VALUES(" + str(
                booking_id)+","+str(event_id)+"," + str(stall_id) + ");"
            print(query)
            cursor.execute(query)
            con.commit()
            query = "UPDATE stall SET isBooked=1 WHERE id=" + \
                str(stall_id) + ";"
            print(query)
            cursor.execute(query)
            con.commit()
        else:
            return -1

    def updateBooking(bid, booking_date, event_id, exhibitor_id, stall_id):
        query = "SELECT price FROM stall WHERE id=" + str(stall_id)
        cursor.execute(query)
        total_amount = cursor.fetchone()
        query = "UPDATE Booking SET booking_date='"+str(booking_date)+"',total_amount="+str(
            total_amount[0])+", event_id="+str(event_id)+", exhibitor_id="+str(exhibitor_id)+" WHERE id="+str(bid)+";"
        cursor.execute(query)
        con.commit()
     
    def megaconsumer():
        query= """SELECT * FROM
                    (
                    SELECT Visitor.first_name AS NAME , Visitor.last_name AS SURNAME ,SUM(spend) AS TotalAmount,event_id
                    FROM Visitor INNER JOIN megaconsumercard ON Visitor.id=MegaConsumerCard.visitor_id 
                    GROUP BY visitor_id,event_id
                    ) AS VisitorTransactions
                    WHERE TotalAmount>=3000
                    ORDER BY TotalAmount"""
        cursor.execute(query)
        megaconsumerlist = cursor.fetchall()
        return megaconsumerlist
    
    def industrybuisness():
        query="""SELECT Industry.industry_name , industrySum AS BuisnessDone
                FROM Industry INNER JOIN
                (
                SELECT Exhibitor.industry_id AS industry_id,SUM(totalSum) AS industrySum
                FROM Exhibitor INNER JOIN
                (
                SELECT Booking.exhibitor_id AS exhibitor_id,SUM(TotalAmount) AS totalSum
                FROM Booking INNER JOIN 
                (SELECT MegaConsumerCard.booking_id, SUM(MegaConsumerCard.spend) AS TotalAmount
                 FROM MegaConsumerCard
                 GROUP BY booking_id
                 ) AS consumerPays ON Booking.id=consumerPays.booking_id
                 GROUP BY Booking.exhibitor_id
                 ) AS bookingConsume  ON Exhibitor.id=bookingConsume.exhibitor_id
                 GROUP BY Exhibitor.industry_id
                 ) AS exhibitionBusiness
                 ON Industry.id=exhibitionBusiness.industry_id
                 LIMIT 10;"""
        cursor.execute(query)
        topindustry=cursor.fetchall()
        return topindustry
    

    



except Exception as ex:
    print(ex)
    if(con.is_connected()):
        con.close()
        print("connection closed")
    # con.close()


if __name__ == "__main__":
    print("HEY")
    if(con.is_connected()):
        con.close()
        print("connection closed")
