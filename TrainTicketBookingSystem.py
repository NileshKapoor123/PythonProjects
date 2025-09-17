class Train:

    def __init__( self, trainNumber, destination, seatsAvailable ):

        self.trainNumber = trainNumber
        self.destination = destination
        self.seatsAvailable = seatsAvailable
        self.passengers = [ ]

    def bookTicket( self, name ):

        if self.seatsAvailable > 0:

            self.passengers.append( name )
            self.seatsAvailable -= 1

            print( f"Ticket has been booked for: { name } on train: { self.trainNumber } going to: { self.destination } " )

        else:

            print( "No seats available" )


    def cancelTicket( self, name ):

        if name in self.passengers:

            self.passengers.remove(name)
            self.seatsAvailable += 1

            print( f"The ticket for { name } has been cancelled" )

        else:

            print( f" The ticket for { name } does not exist" )

    def showTicketBooking( self, name ):

        if name in self.passengers:
            print( f"There is a ticket for { name } on train: { self.trainNumber } going to: { self.destination } " )

        else:
            print( f"The ticket for { name } does not exist" )

    def showPassengers( self ):

        if self.passengers:

            print( f"Passengers: { self.passengers } " )

        else:

            print( "No passengers have been booked on yet " )


if __name__ == "__main__":

    train = Train( "100", "Edinburgh", 1000 )

    while True:
        print( "Welcome to the Ticket Booking System! \nWhat would you like to do?" )
        print( "1. Book Tickets" )
        print( "2. Cancel Tickets" )
        print( "3. Show Passengers" )
        print( "4. Show Ticket Booking" )
        print( "5. exit " )
        choice = int( input( "Enter your choice: " ) )

        if choice == 1:
            name = input( "Enter your name: " )
            train.bookTicket( name )

        elif choice == 2:
            name = input( "Enter your name: " )
            train.cancelTicket ( name )

        elif choice == 3:
            train.showPassengers( )

        elif choice == 4:
            name = input( "Enter your name: " )
            train.showTicketBooking( name )

        elif choice == 5:
            print( "Thank you for your time!" )
            break

        else:
            print( "Invalid choice, please retry: \n" )