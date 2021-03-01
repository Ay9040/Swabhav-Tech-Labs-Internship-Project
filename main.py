from flask import Flask, render_template, redirect, request
import tfb
app = Flask(__name__)


@app.route("/", methods=["GET"])
def adminRegister():
    return render_template("register.html",message="")

@app.route("/addVenue", methods=["POST"])
def addVenue():
    city=request.form['venueCity']
    address=request.form['venueAddress']
    country=request.form['venueCountry']
    state=request.form['venueState']
    country_id=tfb.countryId(country)
    state_id=tfb.stateId(state,country_id)
    tfb.addVenue(address,city,state_id,country_id)
    return render_template("register.html",message="Venue Added Successfully")


@app.route("/addStall", methods=["POST"])
def addStall():
    stall_no=request.form['stallNo']
    price=request.form['stallPrice']
    stall_size=request.form['stallSize']
    isBooked=True
    event_name=request.form['stallEvent']
    event_id=tfb.eventId(event_name)
    tfb.addStall(stall_no,price,stall_size,isBooked,event_id)
    return render_template("register.html",message="Venue Added Successfully")


@app.route("/addEvent", methods=["POST"])
def addEvent():
    event_name=request.form['eventName']
    booking_start_date=request.form['eventBookingStartDate']
    start_date=request.form['eventStartDate']
    end_date=request.form['eventEndDate']
    venue_id=request.form['eventVenueName']
    tfb.addEvent(event_name,booking_start_date,start_date,end_date,venue_id)
    return render_template("register.html",message="Venue Added Successfully")


@app.route("/addVisitor", methods=["POST"])
def addVisitor():
    first_name=request.form['venueCity']
    last_name=request.form['venueCity']
    address=request.form['venueAddress']
    pincode=request.form['venueCountry']
    mobile_no=request.form['venueState']
    emailid=request.form['venueState']
    dob=request.form['venueState']
    gender=request.form['venueState']
    tfb.addVisitor(first_name,last_name,address,pincode,mobile_no,emailid,dob,gender)
    return render_template("register.html",message="Venue Added Successfully")


@app.route("/addExhibitor", methods=["POST"])
def addExhibitor():
    exhibitor_name=request.form['venueCity']
    email=request.form['venueAddress']
    phone_no=request.form['venueCountry']
    company_name=request.form['venueState']
    company_description=request.form['venueState']
    address=request.form['venueState']
    pincode=request.form['exhibitorPincode']
    industry_id=request.form['exhibitorPincode']
    country=request.form['venueCountry']
    state=request.form['venueState']
    country_id=tfb.countryId(country)
    state_id=tfb.stateId(state,country_id)
    tfb.addExhibitor(exhibitor_name,email,phone_no,company_name,company_description,address,pincode,industry_id,country_id,state_id)
    return render_template("register.html",message="Venue Added Successfully")

@app.route("/addBooking", methods=["POST"])
def addBooking():
    booking_date=request.form['venueCity']
    total_amount=request.form['venueAddress']
    isBooked=request.form['venueCountry']
    event_id=request.form['venueState']
    tfb.addBooking(booking_date,total_amount,isBooked,event_id)
    return render_template("register.html",message="Venue Added Successfully")