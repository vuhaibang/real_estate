from scrapy.item import Item, Field

class RealEstateItem(Item):
	price = Field()
	title = Field()
	contact = Field()
	name_contact = Field()
	detail = Field()
	area = Field()
	address = Field()
	number_bed_room = Field()