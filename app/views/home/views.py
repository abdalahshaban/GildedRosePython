from flask import redirect,render_template,url_for
from .forms import CreateItem

from ...models import Item

items =[]

@create.route('/create',methods=['GET','POST'])
def create():
  print('in fun')
  """
  Handle request to /create route 
  Add an Item 
  """
  form=CreateItem()
  if form.validate_on_submit():
    item=Item(name=form.name.data,sell_in=form.sell_in.data,quality=form.quality.data)
    # Add item to array
    items.extend(item)

    # go to list view 
    return render_template('../templates/listItems.html')
  
  # load create item view
  return render_template('../templates/createItem.html',form=form,title="CreateItem")

  