class Property:
	def __init__(self, square_feet='', beds='', baths='', **kwargs):
		"""
		Init Property class
		"""
		self.square_feet = square_feet
		self.num_bedrooms = beds
		self.num_baths = baths

	def display(self):
		"""
		Show info about properties
		"""
		print("PROPERTY DETAILS")
		print("================")
		print("square footage: {}".format(self.square_feet))
		print("bedrooms: {}".format(self.num_bedrooms))
		print("bathrooms: {}".format(self.num_baths))
		print()

	def prompt_init():
		"""
		Input properties
		"""
		return dict(square_feet=input("Enter the square feet: "),
				beds=input("Enter number of bedrooms: "),
				baths=input("Enter number of baths: "))
	prompt_init = staticmethod(prompt_init)

def get_valid_input(input_string, valid_options):
	"""
	(str, list) -> str
	Input only valid string
	Return inputted valid string
	"""
	input_string += " ({}) ".format((", ".join(valid_options)))
	response = input(input_string)
	while response.lower() not in valid_options:
		response = input(input_string)
	return response

class Apartment:
	valid_laundries = ("coin", "ensuite", "none")
	valid_balconies = ("yes", "no", "solarium") 

	def __init__(self, balcony='', laundry='', **kwargs):
		"""
		Init Apartment, after init Property
		"""
		self.balcony = balcony
		self.laundry = laundry

	def display(self):
		"""
		Show apartment details
		"""
		print("APARTMENT DETAILS")
		print("laundry: {}".format(self.laundry))
		print("has balcony: {}".format(self.balcony))

	def prompt_init():
		"""
		Input valid apartment details, static method
		"""
		parent_init = {}
		laundry = get_valid_input(
				"What laundry facilities does "
				"the property have? ",
				Apartment.valid_laundries)
		balcony = get_valid_input(
				"Does the property have a balcony?",
				Apartment.valid_balconies)
		parent_init.update({
			"laundry": laundry,
			"balcony": balcony
		})
		return parent_init
	prompt_init = staticmethod(prompt_init)

class House:
	valid_garage = ("attached", "detached", "none")
	valid_fenced = ("yes", "no")

	def __init__(self, num_stories='',
			garage='', fenced='', **kwargs):
		"""
		Init House class, after Property class
		"""
		self.garage = garage
		self.fenced = fenced
		self.num_stories = num_stories

	def display(self):
		"""
		Show info about properties, after about house
		"""
		print("HOUSE DETAILS")
		print("# of stories: {}".format(self.num_stories))
		print("garage: {}".format(self.garage))
		print("fenced yard: {}".format(self.fenced))

	def prompt_init():
		"""
		Input valid house details, static method
		"""
		parent_init = {}
		fenced = get_valid_input("Is the yard fenced? ",
					House.valid_fenced)
		garage = get_valid_input("Is there a garage? ",
				House.valid_garage)
		num_stories = input("How many stories? ")

		parent_init.update({
			"fenced": fenced,
			"garage": garage,
			"num_stories": num_stories
		})
		return parent_init
	prompt_init = staticmethod(prompt_init)

class Purchase:
	"""
	Init purchase, (house/apartment), property
	"""
	def __init__(self, price='', taxes='', **kwargs):
		self.price = price
		self.taxes = taxes

	def display(self):
		"""
		Show purchase, (house/apartment), property
		"""
		print("PURCHASE DETAILS")
		print("selling price: {}".format(self.price))
		print("estimated taxes: {}".format(self.taxes))

	def prompt_init():
		"""
		Input valid purchase
		"""
		return dict(
			price=input("What is the selling price? "),
			taxes=input("What are the estimated taxes? "))
	prompt_init = staticmethod(prompt_init)

class Rental:
	def __init__(self, furnished='', utilities='',
			rent='', **kwargs):
		"""
		Init rental, (house/apartment), property
		"""
		self.furnished = furnished
		self.rent = rent
		self.utilities = utilities

	def display(self):
		"""
		Show purchase, (house/apartment), property
		"""
		print("RENTAL DETAILS")
		print("rent: {}".format(self.rent))
		print("estimated utilities: {}".format(self.utilities))
		print("furnished: {}".format(self.furnished))
		print("================\n")

	def prompt_init():
		"""
		Input valid rental info
		"""
		return dict(
			rent=input("What is the monthly rent? "),
			utilities=input("What are the estimated utilities? "),
			furnished = get_valid_input("Is the property furnished? ",
					("yes", "no")))
	prompt_init = staticmethod(prompt_init)

class HouseRental:
	def display(self):
		self.prop.display()
		self.house.display()
		self.rental.display()

	def __init__(self, **kwargs):
		self.prop = Property(**kwargs)
		self.house = House(**kwargs)
		self.rental = Rental(**kwargs)
		
	def prompt_init():
		"""
		Class, which connect Purchase and House classes 
		"""
		init = Property.prompt_init()
		init.update(House.prompt_init())
		init.update(Rental.prompt_init())
		return init
	prompt_init = staticmethod(prompt_init)

class ApartmentRental:
	def display(self):
		self.prop.display()
		self.apartment.display()
		self.rental.display()

	def __init__(self, **kwargs):
		self.prop = Property(**kwargs)
		self.apartment = Apartment(**kwargs)
		self.rental = Rental(**kwargs)
		
	def prompt_init():
		"""
		Class, which connect Purchase and House classes 
		"""
		init = Property.prompt_init()
		init.update(Apartment.prompt_init())
		init.update(Rental.prompt_init())
		return init
	prompt_init = staticmethod(prompt_init)

class ApartmentPurchase:
	def display(self):
		self.prop.display()
		self.apartment.display()
		self.purchase.display()

	def __init__(self, **kwargs):
		self.prop = Property(**kwargs)
		self.apartment = Apartment(**kwargs)
		self.purchase = Purchase(**kwargs)
		
#Classes WITHOUT inheritance
#Created by Roman Vey

		def prompt_init():
		"""
		Class, which connect Purchase and House classes 
		"""
		init = Property.prompt_init()
		init.update(Apartment.prompt_init())
		init.update(Purchase.prompt_init())
		return init
	prompt_init = staticmethod(prompt_init)

class HousePurchase:
	def display(self):
		self.prop.display()
		self.house.display()
		self.purchase.display()

	def __init__(self, **kwargs):
		self.prop = Property(**kwargs)
		self.house = House(**kwargs)
		self.purchase = Purchase(**kwargs)
		
	def prompt_init():
		"""
		Class, which connect Purchase and House classes 
		"""
		init = Property.prompt_init()
		init.update(House.prompt_init())
		init.update(Purchase.prompt_init())
		return init
	prompt_init = staticmethod(prompt_init)

class Agent:
	type_map = {
		("house", "rental"): HouseRental,
		("house", "purchase"): HousePurchase,
		("apartment", "rental"): ApartmentRental,
		("apartment", "purchase"): ApartmentPurchase
		}
	def __init__(self):
		"""
		Init Agent class
		"""
		self.property_list = []

	def display_properties(self):
		"""
		Display all info
		"""
		for property in self.property_list:
			property.display()

	def add_property(self):
		"""
		Add properties
		"""
		property_type = get_valid_input(
				"What type of property? ",
				("house", "apartment")).lower()
		payment_type = get_valid_input(
				"What payment type? ",
				("purchase", "rental")).lower()

		PropertyClass = self.type_map[(property_type, payment_type)]
		init_args = PropertyClass.prompt_init()
		self.property_list.append(PropertyClass(**init_args))

#a = Agent()
#a.add_property()
#a.display_properties()