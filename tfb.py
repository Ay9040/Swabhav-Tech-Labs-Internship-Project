import mysql.connector as mysql

try:
    con = mysql.connect(user='root',password='root',host='127.0.0.1',database='tradefairbooking')
    cursor=con.cursor()
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

    def countryId(country):
        cursor.execute("SELECT id FROM Country WHERE country_name='"+country+"';")
        country_id=cursor.fetchone()
        return country_id[0]

    def stateId(state,country_id):
        cursor.execute("SELECT id,country_id FROM State WHERE state_name='"+state+"' AND country_id="+str(country_id)+";")
        state_id=cursor.fetchone()
        return state_id[0]
    def getIds(tablename):
        cursor.execute("SELECT id FROM "+tablename)
        id_list=cursor.fetchall()
        return id_list

    def delById(tablename,i_d):
        query="DELETE FROM "+tablename+" WHERE id="+i_d+";"
        #print(query)
        cursor.execute(query)
        con.commit()
        
    def addVenue(address,city,state_id,country_id):
        #print("Enter Contact Details : \n")
        """
        vid_list=getIds('Venue')
        vid=len(vid_list)+1
        while(vid in vid_list):
            vid+=1
        """
        query="INSERT INTO Venue(address,city,state_id,country_id)VALUES('"+address+"','"+city+"',"+str(state_id)+","+str(country_id)+");"
        print(query)
        cursor.execute(query)
        con.commit()
    
        
    def updateVenue(vid,address,city,state_id,country_id):
        query="UPDATE contact SET address='"+address+"',city_name='"+city+"',state_id="+str(state_id)+"',country_id="+str(country_id)+" WHERE id="+str(vid)+";"
        #print(query)
        cursor.execute(query)
        con.commit()
    
    def addStall(stall_no,price,stall_size,isBooked,event_id):
        """
        sid_list=getIds('Stall')
        sid=len(sid_list)+1
        while(sid in sid_list):
            sid+=1
        """
        query="INSERT INTO Stall (stall_no,price,stall_size,isBooked,event_id)VALUES("+str(stall_no)+","+str(price)+","+str(stall_size)+","+str(isBooked)+","+str(event_id)+");"
        print(query)
        cursor.execute(query)
        con.commit()
        sid_list=getIds('Stall')
        stall_id=max(sid_list)
        query="INSERT INTO BookingStallMap(stall_id,event_id)VALUES("+str(stall_id)+","+str(event_id)+");"
        #print(query)
        cursor.execute(query)
        con.commit()
        
   
        
    def updateStall(sid,stall_no,price,stall_size,isBooked,event_id):
        query="UPDATE address SET stall_no="+str(stall_no)+",price="+str(price)+",stall_size="+str(stall_size)+",isBooked="+str(isBooked)+",event_id="+str(event_id)+" WHERE id="+str(sid)+";"
        cursor.execute(query)
        con.commit()

    
    def addEvent(event_name,booking_start_date,start_date,end_date,venue_id):
        """
        sid_list=getIds('Stall')
        sid=len(sid_list)+1
        while(sid in sid_list):
            sid+=1
        """
        query="INSERT INTO EventTable (event_name,booking_start_date,start_date,end_date,venue_id)VALUES('"+event_name+"',"+str(booking_start_date)+","+str(start_date)+","+str(end_date)+","+str(venue_id)+");"
        print(query)
        cursor.execute(query)
        con.commit()
        """
        query="INSERT INTO mapAddress(contact_id,adno)VALUES("+str(cid)+","+str(adno)+");"
        #print(query)
        cursor.execute(query)
        con.commit()
        """

    def eventId(event_name):
        cursor.execute("SELECT id FROM EventTable WHERE event_name='"+event_name+"';")
        event_id=cursor.fetchone()
        return event_id[0]
        
    def updateEvent(eid,event_name,booking_start_date,start_date,end_date,venue_id):
        query="UPDATE EventTable SET stall_no='"+event_name+"',price="+str(booking_start_date)+",start_date="+str(start_date)+",end_date="+str(end_date)+",venue_id="+str(venue_id)+" WHERE id="+str(eid)+";"
        cursor.execute(query)
        con.commit()

    
    def addVisitor(first_name,last_name,address,pincode,mobile_no,emailid,dob,gender):
        """
        sid_list=getIds('Stall')
        sid=len(sid_list)+1
        while(sid in sid_list):
            sid+=1
        """
        query="INSERT INTO Stall (first_name,last_name,address,pincode,mobile_no,emailid,dob,gender)VALUES('"+first_name+"','"+last_name+"','"+address+"',"+str(pincode)+","+str(mobile_no)+",'"+emailid+"',"+str(dob)+","+str(gender)+");"
        print(query)
        cursor.execute(query)
        con.commit()
        """
        query="INSERT INTO mapAddress(contact_id,adno)VALUES("+str(cid)+","+str(adno)+");"
        #print(query)
        cursor.execute(query)
        con.commit()
        """
   
        
    def updateVisitor(vis_id,first_name,last_name,address,pincode,mobile_no,emailid,dob,gender):
        query="UPDATE address SET first_name='"+first_name+"',last_name='"+last_name+"',address='"+address+"',pincode="+str(pincode)+",mobile_no="+str(mobile_no)+",emailid='"+emailid+"',dob="+str(dob)+",gender="+str(gender)+" WHERE id="+str(vis_id)+";"
        cursor.execute(query)
        con.commit()

    
    def addExhibitor(exhibitor_name,email,phone_no,company_name,company_description,address,pincode,industry_id,country_id,state_id):
        """
        sid_list=getIds('Stall')
        sid=len(sid_list)+1
        while(sid in sid_list):
            sid+=1
        """
        query="INSERT INTO Exhibitor (exibitor_name,email,phoneno,company_name,company_description,address,pincode,industry_id,country_id,state_id)VALUES('"+exhibitor_name+"','"+email+"',"+str(phone_no)+",'"+company_name+"','"+company_description+"','"+address+"',"+str(pincode)+","+str(industry_id)+","+str(country_id)+","+str(state_id)+");"
        print(query)
        cursor.execute(query)
        con.commit()
        """
        query="INSERT INTO mapAddress(contact_id,adno)VALUES("+str(cid)+","+str(adno)+");"
        #print(query)
        cursor.execute(query)
        con.commit()
        """
   
        
    def updateExhibitor(exid,exibitor_name,email,phoneno,company_name,company_description,address,pincode,industry_id,country_id,state_id):
        query="UPDATE Exhibitor SET exihibitor_name='"+exibitor_name+"',email='"+email+"',phoneno="+str(phoneno)+",company_name='"+company_name+"',company_description='"+company_description+"',address='"+address+",pincode="+str(pincode)+",industry_id="+str(industry_id)+",country_id="+str(country_id)+",state_id="+str(state_id)+" WHERE id="+str(exid)+";"
        cursor.execute(query)
        con.commit()

    
    def addBooking(booking_date,total_amount,isBooked,event_id):
        """
        sid_list=getIds('Stall')
        sid=len(sid_list)+1
        while(sid in sid_list):
            sid+=1
        """
        query="INSERT INTO Booking (booking_date,total_amount,isBooked,event_id)VALUES("+str(booking_date)+","+str(total_amount)+","+str(isBooked)+","+str(event_id)+");"
        print(query)
        cursor.execute(query)
        con.commit()
        bid_list=getIds('Booking')
        booking_id=max(bid_list)
        query="UPDATE INTO BookingStallMap SET booking_id="+str(booking_id)+"WHERE event_id="+str(event_id)+";"
        #print(query)
        cursor.execute(query)
        con.commit()
        
   
        
    def updateBooking(bid,booking_date,total_amount,isBooked,event_id):
        query="UPDATE Booking SET booking_date="+str(booking_date)+",total_amount="+str(total_amount)+",isBooked="+str(isBooked)+",event_id="+str(event_id)+" WHERE id="+str(bid)+";"
        cursor.execute(query)
        con.commit()

    
except Exception as ex:
    print(ex)
    if(con.is_connected()):
        con.close()
        print("connection closed")
    #con.close()




if __name__=="__main__" :
    print("HEY")
    if(con.is_connected()):
        con.close()
        print("connection closed")
                