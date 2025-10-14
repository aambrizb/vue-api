from fastapi import APIRouter, Request
from globaltechia import utils
from tortoise.expressions import Q
import importlib
import os
import traceback

router = APIRouter()

@router.api_route("/api/method/{app}/{method}",methods=["GET", "POST"])
async def get_method(app,method,request: Request):

  _module   = None
  _view     = utils.getView(app,method)

  if _view:
    try:
      response = await _view(request)
      return response
    except Exception as ex:
      return {
        "status" : 404,
        "msg"    : str(ex)
      }

  return {
    "method" : request['method'],
    "app"    : app,
    "method" : method
  }
@router.api_route("/api/{app}/{view}",methods=["GET", "POST"])
async def get_view(app,view,request: Request):

  _view     = utils.getView(app, view,prefix="View")

  # Verify, if exists model.
  if not _view:
    _model = utils.getModel(app,view)
    if _model and request.method == 'POST':
      payload = await request.json()
      try:
        obj = await _model.create(**payload)
        return {
          "status" : 200,
          "id"     : obj.id,
          "msg"    : "Successfully Operation"
        }
      except Exception as ex:
        return {
          "status"    : 404,
          "msg"       : str(ex),
          "traceback" : traceback.format_exc()
        }
    else:
      _schema = await _model.schema(obj=None)
      return {
        "verbose_name" : _model.Meta.verbose_name if _model.Meta.verbose_name else view,
        "form"         : _schema,
        "messages"     : []
      }
  else:
    try:
      response = await _view(request)
      return response
    except Exception as ex:
      return {
        "status"    : 404,
        "msg"       : str(ex),
        "traceback" : traceback.format_exc()
      }

  return {
    "method" : request['method'],
    "app"    : app,
    "view"   : view
  }

@router.api_route("/api/{app}/{view}/list",methods=["GET"])
async def get_list(app,view,request: Request):

  _search   = request.query_params.get("search")
  _page     = request.query_params.get("page")

  _view     = None
  _props    = {}

  _view = utils.getView(app,f'{view}_list')

  if _view:
    return _view(request)

    # Verify, if exists model.
  else:
    _model = utils.getModel(app,view)

    if _model:

      _query    = Q()

      if _search and hasattr(_model,'Admin') \
        and hasattr(_model.Admin,'search_field') \
        and len(_model.Admin.search_field) > 0:
        for x in _model.Admin.search_field:
          _x_split = x.split(" ")
          for z in _x_split:
            _query |= Q(**{f"{x}__icontains": z})

      _list_display = getattr(_model.Admin, 'list_display',[])
      _list_hidden  = getattr(_model.Admin, 'list_hidden', [])
      _list_total   = _list_display+_list_hidden
      _methods      = [m for m in dir(_model.Admin) if callable(getattr(_model.Admin, m)) and not m.startswith("__")]
      _values       = list(set(_list_total) - set(_methods))

      data         = await _model.filter(_query).order_by('-id').values(*_values)

      # Add Custom Data
      for item_data,item_method in zip(data,_methods):
        _el = utils.dictToObj(item_data)
        item_data[item_method] = getattr(_model.Admin, item_method)(_el)

      if hasattr(_model,'Admin'):

        if hasattr(_model.Admin,'search_field') and len(_model.Admin.search_field) > 0:
          _props['search'] = True
        if hasattr(_model.Admin,'list_per_page') and getattr(_model.Admin,'list_per_page') > 0:

          list_per_page = getattr(_model.Admin,'list_per_page')

          _pagination          = utils.Pagination(data,list_per_page,_page)
          _props["pagination"] = _pagination.getProps()
          data                 = _pagination.getData()

      _base_headers      = _model._meta.fields_map
      _final_headers     = {}
      _headers           = []

      if hasattr(_model,'Admin'):
        if type(_model.Admin.list_display) == list and len(_model.Admin.list_display) > 0:

          for y in _model.Admin.list_display:
            _final_headers[y] = _base_headers[y] if y in _base_headers else None
      else:
        _final_headers = _base_headers

      _tmp = {}

      for x in _final_headers:
        if isinstance(_final_headers[x], utils.FrameField):
          _label = _final_headers[x].label if _final_headers[x].label else x
          _tmp = {
            'name'    : x,
            'label'   : _label,
            'boolean' : isinstance(_final_headers[x],utils.BooleanField)
          }
          _headers.append(_tmp)
        else:
          _headers.append({
            'name'    : x,
            'label'   : x,
            'boolean' : False
          })

      return {
        "verbose_name" : _model.Meta.verbose_name if _model.Meta.verbose_name else view,
        "props"        : _props,
        "headers"      : _headers,
        "data"         : data
      }

    else:
      return {
        'code':404,
        'msg':'Not model found.'
      }

@router.api_route("/api/{app}/{view}/{id}/delete",methods=["DELETE"])
async def delete_view(app,view,id,request: Request):

  _view = utils.getView(app,view)

  # Verify, if exists model.
  if not _view:
    _model = utils.getModel(app,view)

    if _model:
      try:
        await _model.filter(id=id).delete()
        return {
          "status" : 200,
          "id"     : id,
          "msg"    : "Successfully Operation"
        }
      except Exception as ex:
        return {
          "status" : 404,
          "msg"    : str(ex)
        }
  else:
    try:
      response = _view(request,id)
      return response
    except Exception as ex:
      return {
        "status" : 404,
        "msg"    : str(ex)
      }

  return {
    "method" : request['method'],
    "app"    : app,
    "view"   : view
  }

@router.api_route("/api/{app}/{view}/{id}",methods=["GET", "POST"])
async def edit_view(app,view,id,request: Request):

  _view = utils.getView(app,view,prefix="View")

  # Verify, if exists model.
  if not _view:
    _model = utils.getModel(app,view)

    if _model and request.method == 'POST':

      payload = await request.json()

      try:
        _updated_model = await _model.filter(id=id).update(**payload)
        return {
          "status" : 200,
          "id"     : id,
          "msg"    : "Successfully Operation"
        }
      except Exception as ex:
        print("[ERROR] ",ex)
        return {
          "status" : 404,
          "msg"    : str(ex)
        }
    else:
      _tmp = await _model.filter(id=id).last()

      return {
        "verbose_name" : _model.Meta.verbose_name if _model.Meta.verbose_name else view,
        "form"         : await _model.schema(obj=_tmp),
        "messages"     : []
      }

  else:
    try:
      response = await _view(request,id)
      return response
    except Exception as ex:
      return {
        "status" : 404,
        "msg"    : str(ex)
      }

  return {
    "method" : request['method'],
    "app"    : app,
    "view"   : view
  }
