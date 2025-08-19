from base.models import Navbar
async def navbar(request,id=None):

  data = await Navbar.filter(parent_id=None).values()

  for item in data:
    item['children'] = await Navbar.filter(
      parent_id=item['id']
    ).values()

  return data

def jaja_list(request,id=None):
  return {"orale":"orale que loco"}

async def calando(request):
  return {
    'ready':True
  }
