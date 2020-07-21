from .models.item import Item

items = [
    Item(name='Aged Brie', sell_in=10, quality=20),
    Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=20, quality=30),
    Item(name='Sulfuras, Hand of Ragnaros', sell_in=30, quality=40),
    Item(name='Conjured', sell_in=33, quality=45)
]


def getItems():
    return items


def createItem(item):
    items.append(item)


def updateItems1():
    for item in items:
        if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
            if item.quality > 0:
                if item.name != "Sulfuras, Hand of Ragnaros":
                    item.quality = item.quality - 1
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if item.name != "Aged Brie":
                if item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if item.quality > 0:
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1


def updateItems():
    for item in items:   
        if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
            if item.quality > 0 and item.name != "Sulfuras, Hand of Ragnaros":
                if item.name == "Conjured":
                    if item.quality >=4 :
                        item.sell_in = item.sell_in - 1
                    else: item.quality=0
                else:
                    if item.quality >=2 :
                        item.quality = item.quality-2
                    else: item.quality=0 
        else:
            if item.quality < 50:
                item.quality=item.quality+1
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in <= 5:
                        if item.quality <=48:
                            item.quality = item.quality+2 
                        else: item.quality=50
                    elif item.sell_in <= 10 and item.quality < 50:
                        item.quality = item.quality+1
        if item.name !="Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1


            
           