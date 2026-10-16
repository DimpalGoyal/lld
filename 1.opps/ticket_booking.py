class Movie:
    def __init__(self, movie_name:str, total_seats:int, ticket_price:int):
        self.movie_name = movie_name
        self.total_seats = total_seats 
        self.ticket_price = ticket_price 
        self.booked_seats = 0
    
    def book_tickets(self, seats:int):
        print("\n") 
        if seats > self.total_seats - self.booked_seats:
            print("not enough seats available")
        else:
            self.booked_seats += seats
            self.total_seats -= seats
            print(f"{seats} are booked!!!")
            print(f"total price is: {self.booked_seats * self.ticket_price}")

    
    def show_status(self):
        print("\ncurrently showing:")
        print(f"movie name: {self.movie_name}")
        print(f"available seats: {self.total_seats}")
        print(f"ticket price: {self.ticket_price}")
    
    
m1 = Movie("hello",10,100)
m1.show_status()
m1.book_tickets(30)
m1.show_status()