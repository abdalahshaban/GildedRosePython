from flask import redirect, render_template, url_for
from .forms import CreateItem
from . import home
from ...models.item import Item

from ...service import createItem, updateItems, getItems


@home.route('/create', methods=['GET', 'POST'])
def create():
    form = CreateItem()
    if form.validate_on_submit():
        item = Item(name=form.name.data, sell_in=form.sell_in.data,
                    quality=form.quality.data)
        # Add item to array
        createItem(item)
        # go to list view
        return redirect(url_for('home'))

    # load create item view
    return render_template('home/createItem.html', form=form, title="Create Item")


@home.route('/update', methods=['GET'])
def update():
    updateItems()
    # load create item view
    return render_template('home/index.html', len=len(getItems()), items=getItems())
