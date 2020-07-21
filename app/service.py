from .models.item import Item

items=[
  Item(name='Aged Brie',sell_in=1,quality=1),
  Item(name='Backstage passes to a TAFKAL80ETC concert',sell_in=2,quality=2),
  Item(name='Sulfuras, Hand of Ragnaros',sell_in=3,quality=3),
  Item(name='Conjured',sell_in=4,quality=4)
]


def getItems():
  return items

def updateItem():
  return ''