import json
from aiohttp import web
# local
from core import query_string_parser as qsp
import find_similar_tracks.business as business


async def handler(app, raw_params):
  # parse the parameters
  params = qsp.validate(
    raw_params,
    {
      'families': qsp.Parser(qsp.Type.STRING_LIST),
      'minmatched': qsp.Parser(qsp.Type.NATURAL_NUMBER, 4),
      'maxinsert': qsp.Parser(qsp.Type.WHOLE_NUMBER, 5),
    }
  )
  # process the request
  return await business.searchMicroSyntenyTracks(
    app['r_engine'],
    app['rpc'],
    params['families'],
    params['minmatched'],
    params['maxinsert']
  )


method = 'POST'
path = '/micro/find-similar-tracks'#?families&minmatched&maxinsert
async def webHandler(request):
  try:
    params = await request.json()
    response = await handler(request.app, params)
    return web.Response(text=json.dumps(response), status=200)
  except Exception as e:
    response_obj = {'status' : 'failed', 'reason': str(e)}
    return web.Response(text=json.dumps(response_obj), status=500)


route = method, path, handler, webHandler
