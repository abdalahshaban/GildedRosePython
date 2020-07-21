from flask import redirect,render_template,url_for
from .forms import CreateItem
from . import home
from ...models.item import Item

# @home.route('/')
# def home():
#     return render_template('home/index.html',len = len(items),items=items)

@home.route('/create',methods=['GET','POST'])
def create():

  form=CreateItem()
  if form.validate_on_submit():
    item=Item(name=form.name.data,sell_in=form.sell_in.data,quality=form.quality.data)
    # Add item to array
    items.extend(item)

    # go to list view 
    return render_template(url_for('createItem.html'))

  # load create item view
  return render_template('home/createItem.html',form=form,title="CreateItem")

  