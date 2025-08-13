def create(request):
  if request['method'] == 'GET':
    pass
  elif request['method'] == 'POST':
    data = request.json()

  return {"ok":"holis"}