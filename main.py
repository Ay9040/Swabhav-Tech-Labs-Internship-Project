from flask import Flask, render_template, redirect, request
import tfb
app = Flask(__name__)

message = ""


@app.route("/", methods=["GET"])
def adminRegister():
    global message
    return render_template("register.html", message=message, venues=getAllVenues(), events=getAllEvents(), exhibitors=getAllExhibitors(),
                           stalls=getAllStalls(), visitors=getAllVisitors(), bookings=getAllBookings(), transactions=getAllTransactions())


def getAllVenues():
    venues = tfb.getVenues()
    return venues


def getAllStalls():
    stalls = tfb.getStalls()
    return stalls


def getAllEvents():
    events = tfb.getEvents()
    return events


def getAllVisitors():
    visitors = tfb.getVisitors()
    return visitors


def getAllExhibitors():
    exhibitors = tfb.getExhibitors()
    return exhibitors


def getAllBookings():
    bookings = tfb.getBookings()
    return bookings


def getAllTransactions():
    transactions = tfb.getTransactions()
    return transactions


def getAllIndustries():
    industries = tfb.getIndustries()
    return industries

def getAllMegaConsumers():
    megaconsumers = tfb.megaconsumer()
    return megaconsumers


@app.route('/updateVenue', methods=['POST'])
def updateVenue():
    city = request.form['venueCity']
    address = request.form['venueAddress']
    country = request.form['venueCountry']
    state = request.form['venueState']
    country_id = tfb.countryId(country)
    state_id = tfb.stateId(state, country_id)
    venue_id = request.form['modifyVenue'][0]
    tfb.updateVenue(venue_id, address, city, state_id, country_id)
    return redirect('/')


@app.route("/addVenue", methods=["POST"])
def addVenue():
    city = request.form['venueCity']
    address = request.form['venueAddress']
    country = request.form['venueCountry']
    state = request.form['venueState']
    country_id = tfb.countryId(country)
    state_id = tfb.stateId(state, country_id)
    tfb.addVenue(address, city, state_id, country_id)
    return render_template("register.html", message="Venue Added Successfully", venues=getAllVenues(), events=getAllEvents(), exhibitors=getAllExhibitors(),
                           stalls=getAllStalls(), visitors=getAllVisitors(), bookings=getAllBookings(), transactions=getAllTransactions())


@app.route("/deleteVenue", methods=["POST"])
def deleteVenue():
    venue_id = request.form['deleteVenue'][0]
    tfb.delById("Venue", venue_id)
    return redirect("/")


@app.route("/deleteStall", methods=["POST"])
def deleteStall():
    stall_id = request.form['deleteStall'][0]
    tfb.delById("Stall", stall_id)
    return redirect("/")


@app.route("/deleteEvent", methods=["POST"])
def deleteEvent():
    event_id = request.form['deleteEvent'][0]
    tfb.delById("eventtable", event_id)
    return redirect("/")


@app.route("/deleteBooking", methods=["POST"])
def deleteBooking():
    booking_exhibitor = request.form['deleteBookingExhibitor']
    booking_event = request.form['deleteBookingEvent']
    booking_stall = request.form['deleteBookingStall']
    tfb.deleteBooking(booking_exhibitor, booking_event, booking_stall)
    return redirect("/")


@app.route("/deleteExhibitor", methods=["POST"])
def deleteExhibitor():
    exhibitor_id = request.form['deleteExhibitor'][0]
    tfb.delById("exhibitor", exhibitor_id)
    return redirect("/")


@app.route("/updateStall", methods=['POST'])
def updateStall():
    stall_id = request.form['modifyStall'][0]
    stall_no = request.form['stallNo']
    price = request.form['stallPrice']
    stall_size = request.form['stallSize']
    event_name = request.form['stallEvent']
    event_id = tfb.eventID(event_name)
    tfb.updateStall(stall_id, stall_no, price, stall_size, event_id)
    return redirect('/')


@app.route("/addStall", methods=["POST"])
def addStall():
    stall_no = request.form['stallNo']
    price = request.form['stallPrice']
    stall_size = request.form['stallSize']
    isBooked = 0
    event_name = request.form['stallEvent']
    event_id = tfb.eventID(event_name)
    tfb.addStall(stall_no, price, stall_size, isBooked, event_id)
    return redirect('/')


@app.route('/updateEvent', methods=['POST'])
def updateEvent():
    event_name = request.form['eventName']
    booking_start_date = request.form['eventBookingStartDate']
    start_date = request.form['eventStartDate']
    end_date = request.form['eventEndDate']
    venue = request.form['eventVenueName']
    event_id = request.form['modifyEvent'][0]
    tfb.updateEvent(event_id, event_name, booking_start_date,
                    start_date, end_date, str(venue)[0])
    return redirect('/')


@app.route("/addEvent", methods=["POST"])
def addEvent():
    event_name = request.form['eventName']
    booking_start_date = request.form['eventBookingStartDate']
    start_date = request.form['eventStartDate']
    end_date = request.form['eventEndDate']
    venue = request.form['eventVenueName']
    tfb.addEvent(event_name, booking_start_date,
                 start_date, end_date, str(venue)[0])
    return redirect('/')


@app.route('/updateVisitor', methods=['POST'])
def updateVisitor():
    first_name = request.form['visitorFirstName']
    last_name = request.form['visitorLastName']
    address = request.form['visitorAddress']
    pincode = request.form['visitorPIN']
    mobile_no = request.form['visitorMobile']
    emailid = request.form['visitorEmail']
    dob = request.form['visitorBirthdate']
    gender = request.form['visitorGender']
    gender = 1 if gender == 'Male' else 0
    visitor_id = request.form['modifyVisitor'][0]
    tfb.updateVisitor(visitor_id, first_name, last_name,
                      address, pincode, mobile_no, emailid, dob, gender)
    return redirect('/')


@app.route("/addVisitor", methods=["POST"])
def addVisitor():
    first_name = request.form['visitorFirstName']
    last_name = request.form['visitorLastName']
    address = request.form['visitorAddress']
    pincode = request.form['visitorPIN']
    mobile_no = request.form['visitorMobile']
    emailid = request.form['visitorEmail']
    dob = request.form['visitorBirthdate']
    gender = request.form['visitorGender']
    gender = 1 if gender == 'Male' else 0
    tfb.addVisitor(first_name, last_name, address, pincode,
                   mobile_no, emailid, dob, gender)
    return redirect('/')


@app.route('/updateExhibitor', methods=['POST'])
def updateExhibitor():
    exhibitor_name = request.form['exhibitorName']
    email = request.form['exhibitorEmail']
    phone_no = request.form['exhibitorPhone']
    company_name = request.form['exhibitorCompanyName']
    company_description = request.form['exhibitorCompanyDescription']
    address = request.form['exhibitorAddress']
    pincode = request.form['exhibitorPIN']
    industry = request.form['exhibitorIndustry']
    country = request.form['exhibitorCountry']
    state = request.form['exhibitorState']
    country_id = tfb.countryId(country)
    state_id = tfb.stateId(state, country_id)
    industry_id = tfb.industryId(industry)
    exhibitor_id = request.form['modifyExhibitor'][0]
    tfb.updateExhibitor(exhibitor_id, exhibitor_name, email, phone_no, company_name,
                        company_description, address, pincode, industry_id, country_id, state_id)
    return redirect('/')


@app.route("/addTransaction", methods=['POST'])
def addTransaction():
    spend = request.form['transactionSpend']
    spend_date = request.form['transactionSpendDate']
    payment_method = request.form['transactionPaymentMethod']
    event = request.form['transactionEvent']
    exhibitor = request.form['transactionExhibitor']
    visitor_id = request.form['transactionVisitor'][0]
    event_id = tfb.eventID(event)
    exhibitor_id = tfb.exhibitorID(exhibitor)
    tfb.addTransaction(spend, spend_date, payment_method,
                       event_id, exhibitor_id, visitor_id)
    return redirect("/")


@app.route("/updateTransaction", methods=['POST'])
def updateTransaction():
    transaction_id = request.form['modifyTransaction'][0]
    spend = request.form['transactionSpend']
    spend_date = request.form['transactionSpendDate']
    payment_method = request.form['transactionPaymentMethod']
    event = request.form['transactionEvent']
    exhibitor = request.form['transactionExhibitor']
    visitor_id = request.form['transactionVisitor'][0]
    event_id = tfb.eventID(event)
    exhibitor_id = tfb.exhibitorID(exhibitor)
    tfb.updateTransaction(transaction_id, spend, spend_date,
                          payment_method, event_id, exhibitor_id, visitor_id)
    return redirect('/')


@app.route("/deleteTransaction", methods=['POST'])
def deleteTransaction():
    transaction_id = request.form['deleteTransaction'][0]
    tfb.delById("megaconsumercard", transaction_id)
    return redirect("/")


@app.route("/addExhibitor", methods=["POST"])
def addExhibitor():
    exhibitor_name = request.form['exhibitorName']
    email = request.form['exhibitorEmail']
    phone_no = request.form['exhibitorPhone']
    company_name = request.form['exhibitorCompanyName']
    company_description = request.form['exhibitorCompanyDescription']
    address = request.form['exhibitorAddress']
    pincode = request.form['exhibitorPIN']
    industry = request.form['exhibitorIndustry']
    country = request.form['exhibitorCountry']
    state = request.form['exhibitorState']
    country_id = tfb.countryId(country)
    state_id = tfb.stateId(state, country_id)
    industry_id = tfb.industryId(industry)
    tfb.addExhibitor(exhibitor_name, email, phone_no, company_name,
                     company_description, address, pincode, industry_id, country_id, state_id)
    return redirect('/')


@app.route("/updateBooking", methods=['POST'])
def updateBooking():
    booking_date = request.form['bookingDate']
    event = request.form['bookingEvent']
    exhibitor = request.form['bookingExhibitor']
    stall = request.form['bookingStall']
    event_id = tfb.eventID(event)
    exhibitor_id = tfb.exhibitorID(exhibitor)
    stall_id = tfb.stallId(stall, event_id)
    booking_id = request.form['modifyBooking'][0]
    tfb.updateBooking(booking_id, booking_date,
                      event_id, exhibitor_id, stall_id)
    return redirect('/')


@app.route("/addBooking", methods=["POST"])
def addBooking():
    global message
    booking_date = request.form['bookingDate']
    event = request.form['bookingEvent']
    exhibitor = request.form['bookingExhibitor']
    stall = request.form['bookingStall']
    event_id = tfb.eventID(event)
    exhibitor_id = tfb.exhibitorID(exhibitor)
    stall_id = tfb.stallId(stall, event_id)
    if tfb.addBooking(booking_date, event_id, exhibitor_id, stall_id) == -1:
        message = "Stall already Booked"

    return redirect('/')


@app.route("/industryBooking", methods=["GET"])
def indusBook():
    return render_template('indusBook.html', venues=getAllVenues(), events=getAllEvents(), exhibitors=getAllExhibitors(),
                           stalls=getAllStalls(), visitors=getAllVisitors(), bookings=getAllBookings(), transactions=getAllTransactions(),industries=getAllIndustries())


@app.route("/megaConsumers",methods=["GET"])
def megaConsumers():
    return render_template('megaConsumer.html',events=getAllEvents(),megaConsumers=getAllMegaConsumers(),exhibitors=getAllExhibitors(),
                           stalls=getAllStalls())
                           stalls=getAllStalls(), visitors=getAllVisitors(), bookings=getAllBookings(), transactions=getAllTransactions(), industries=getAllIndustries())


@app.route('/bookingDash', methods=['GET'])
def bookingDash():
    return render_template('bookingDash.html', bookings = getAllBookings())
